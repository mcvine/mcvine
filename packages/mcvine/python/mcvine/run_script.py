#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, sys, yaml
from mcni import run_ppsd, run_ppsd_in_parallel

def run_mpi(script, workdir, ncount, nodes, buffer_size=int(1e6), overwrite_datafiles=False, **kwds):
    """run a mcvine simulation script on one node. The script must define the instrument.
Parameters:

* script: path to instrument script
* workdir: working dir
* ncount: neutron count
* nodes:  number of MPI nodes
* buffer_size: buffer size (optional)

An example script:

  # script myinstrument.py
  import mcvine
  instrument = mcvine.instrument()
  # add source
  source = mcvine.components.sources.Source_simple('source')
  instrument.append(source, position=(0,0,0))
  # add monitor
  monitor = mcvine.components.monitors.E_monitor('monitor', filename='IE.dat')
  instrument.append(monitor, position=(0,0,1))
  # end of script

"""
    _check_workdir(workdir, overwrite_datafiles)
    ncount = int(ncount); buffer_size = int(buffer_size)    
    assert buffer_size>0
    if ncount < 100:
        nodes = 1; buffer_size = ncount
    else:
        max_buffer_size = ncount//nodes//5
        min_buffer_size = 20
    buffer_size = min(max_buffer_size, buffer_size)
    buffer_size = max(min_buffer_size, buffer_size)
    overwrite_datafiles = '--overwrite_datafiles' if overwrite_datafiles else ''
    if kwds:
        kwds_file = 'mcvine_run_script_kwds.yml'
        with open(kwds_file, 'w') as outfile:
            yaml.dump(kwds, outfile, default_flow_style=False)
    cmd = 'python -m "mcvine.run_script" {script} --workdir {workdir} --ncount {ncount} {overwrite_datafiles} --buffer_size {buffer_size}'
    cmd = cmd.format(script=script, workdir=workdir, ncount=ncount, overwrite_datafiles=overwrite_datafiles, buffer_size=buffer_size)
    cmd += ' --mpi-mode=worker'
    if kwds:
        cmd += ' --additional-kargs=%s' % kwds_file
    cmd = "mpirun -np {} ".format(nodes) + cmd
    if os.system(cmd):
        raise RuntimeError("%s failed" % cmd)
    ppsd = os.path.join(workdir, 'post-processing-scripts')
    run_ppsd_in_parallel(ppsd, nodes)
    return


def run1_mpi(script, workdir, ncount, **kwds):
    "run a script on one MPI node. this is called 'worker' mode"
    # find out how many neutrons 
    from mcni.components.ParallelComponent import ParallelComponent
    pc = ParallelComponent()
    from mcni.pyre_support.Instrument import getPartitions
    partitions = getPartitions(ncount, pc.mpi.size)
    ncount1 = partitions[pc.mpi.rank]
    kwds.update(mpiSize=pc.mpi.size, mpiRank=pc.mpi.rank, run_pps=False)
    run1(script, workdir, ncount1, **kwds)
    return


def run1(script, workdir, ncount, buffer_size=int(1e6), overwrite_datafiles=False, run_pps=True, **kwds):
    """run a mcvine simulation script on one node. The script must define the instrument.

Parameters:

* script: path to instrument script. the script must either create an instrument or provide a method to do so
* workdir: working dir
* ncount: neutron count
* buffer_size: buffer size (optional)

An example script:

  # script myinstrument.py
  import mcvine
  instrument = mcvine.instrument()
  # add source
  source = mcvine.components.sources.Source_simple('source')
  instrument.append(source, position=(0,0,0))
  # add monitor
  monitor = mcvine.components.monitors.E_monitor('monitor', filename='IE.dat')
  instrument.append(monitor, position=(0,0,1))
  # end of script

"""
    _check_workdir(workdir, overwrite_datafiles)
    import imp
    m = imp.load_source('mcvinesim', script)
    assert hasattr(m, 'instrument')
    instrument = m.instrument
    from mcni.Instrument import Instrument
    if not isinstance(instrument, Instrument):
        assert callable(instrument) # has to be a  method that creates instrument
        instrument = instrument(**_getRelevantKwds(instrument, kwds))
    ncount = int(ncount)
    workdir = os.path.abspath(workdir)
    ppsd = os.path.join(workdir, 'post-processing-scripts')
    from mcni.components.ParallelComponent import ParallelComponent
    pc = ParallelComponent()
    if pc.mpi.size and pc.mpi.rank==0:
        if not os.path.exists(ppsd): os.makedirs(ppsd)
    
    N = (ncount-1)//buffer_size+1
    remained = ncount
    for i in range(N):
        n = min(remained, buffer_size)
        instrument.simulate(n, outputdir=workdir, overwrite_datafiles=overwrite_datafiles, iteration_no=i, post_processing_scripts_dir=ppsd, **kwds)
        remained -= n
        continue
    assert remained == 0
    for comp in instrument.components:
        if not hasattr(comp, 'create_pps'):
            import warnings
            warnings.warn('Developer: %s does not implement method "create_pps"' % comp)
            continue
        comp.create_pps()
        continue
    if run_pps:
        run_ppsd(ppsd)
    return


def _getRelevantKwds(method, kwds):
    """return kwd args for the given method, and remove them from the given kwds"""
    import inspect
    argspec = inspect.getargspec(method)
    d = dict()
    for a in argspec.args:
        if a in kwds:
            d[a] = kwds[a]
            del kwds[a]
    return d


def _check_workdir(workdir, overwrite_datafiles):
    if os.path.exists(workdir):
        if overwrite_datafiles:
            import shutil; shutil.rmtree(workdir)
        else:
            raise IOError("%s exists. set overwrite_datafiles=True to overwrite" % workdir)
    return

import click
@click.command()
@click.argument("script")
@click.option("--workdir", default="output", help="work directory")
@click.option("--ncount", default=int(1e6), help="neutron count")
@click.option("--overwrite_datafiles", default=False, help="overwrite datafiles", is_flag=True)
@click.option("--buffer_size", default=int(1e6), help="neutron buffer size")
@click.option("--mpi-mode", default=None)
@click.option("--nodes", default=1)
@click.option("--run-pps", default=False, help="run post-processing script. only valid for None mpi mode",
              is_flag=True)
@click.option("--additional-kargs", default=None, help='addiontal kwd args in a yaml file')
def main(
        script, workdir, ncount,
        buffer_size=int(1e6), overwrite_datafiles=False, mpi_mode=None, nodes=1, run_pps=False,
        additional_kargs = None,
):
    if additional_kargs:
        kwds = yaml.load(open(additional_kargs))
    else:
        kwds = dict()
    if mpi_mode == 'worker':
        run1_mpi(
            script, workdir, ncount,
            buffer_size=buffer_size, overwrite_datafiles=overwrite_datafiles, **kwds)
    elif mpi_mode == 'server':
        run_mpi(
            script, workdir, ncount, nodes, buffer_size,
            overwrite_datafiles=overwrite_datafiles, **kwds)
    else:
        run1(script, workdir, ncount, buffer_size, overwrite_datafiles, run_pps=run_pps, **kwds)
    return

if __name__ == '__main__': main()
