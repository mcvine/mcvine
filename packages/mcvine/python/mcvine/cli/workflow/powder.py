# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, stat, click

from . import workflow

@workflow.command()
@click.option("--instrument", default='ARCS')
@click.option("--sample", default='V')
@click.option("--workdir", default="")
def powder(instrument, sample, workdir):
    workdir = workdir or "mcvine-workflow-powder-%s-%s" % (instrument, sample)
    # copy from template
    from mcvine import resources
    template = os.path.join(resources.instrument(instrument), 'workflows', 'powder')
    import shutil
    shutil.copytree(template, workdir)
    # create "beam" subdir
    beam = os.path.join(workdir, 'beam')
    os.makedirs(beam)
    # add script to run beam
    create_beam_run_script(beam)
    # copy sampleassembly template
    sampleargs = sample.split('/')
    if len(sampleargs) > 3:
        raise ValueError('Wrong sample input %s. Examples: %s' % (sample, sample_examples))
    template = resources.sample(*sampleargs)
    if not os.path.exists(template):
        raise RuntimeError("Sample template for %r does not exist" % sample)
    shutil.copytree(template, os.path.join(workdir, 'sampleassembly'))
    return


sample_examples = '"V", "V/300K", or "V/300K/plate"'


def create_beam_run_script(workdir):
    name = "run.sh"
    content = """#!/usr/bin/env bash

mcvine instruments arcs beam --keep-in-cache --use-cache E=100 --ncount=1e8

"""
    path = os.path.join(workdir, name)
    open(path, 'wt').write(content)
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC)
    return


# End of file 
