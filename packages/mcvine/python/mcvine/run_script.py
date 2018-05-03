#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, sys

def mpi_run(script, workdir, ncount, nodes, buffer_size=int(1e6), overwrite_datafiles=False):
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
    return

def run1(script, workdir, ncount, buffer_size=int(1e6), overwrite_datafiles=False):
    """run a mcvine simulation script on one node. The script must define the instrument.

Parameters:

* script: path to instrument script
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
    import imp
    m = imp.load_source('mcvinesim', script)
    assert hasattr(m, 'instrument')
    instrument = m.instrument
    ncount = int(ncount)
    workdir = os.path.abspath(workdir)
    ppsd = os.path.join(workdir, 'post-processing-scripts')
    if not os.path.exists(ppsd): os.makedirs(ppsd)
    
    N = (ncount-1)//buffer_size+1
    remained = ncount
    for i in range(N):
        n = min(remained, buffer_size)
        instrument.simulate(n, outputdir=workdir, overwrite_datafiles=overwrite_datafiles, iteration_no=i, post_processing_scripts_dir=ppsd)
        remained -= n
        continue
    assert remained == 0
    for comp in instrument.components:
        comp.create_pps()
        continue
    from mcni import run_ppsd
    run_ppsd(ppsd)
    return


import click
@click.command()
@click.argument("script")
@click.option("--workdir", default="output", help="work directory")
@click.option("--ncount", default=int(1e6), help="neutron count")
@click.option("--overwrite_datafiles", default=False, help="overwrite datafiles", is_flag=True)
@click.option("--buffer_size", default=int(1e6), help="neutron buffer size")
def main(script, workdir, ncount, buffer_size=int(1e6), overwrite_datafiles=False):
    run1(script, workdir, ncount, buffer_size, overwrite_datafiles)
    return

if __name__ == '__main__': main()
