#!/usr/bin/env python


from . import mcvine, click

@mcvine.command()
@click.option(
    "--workdir", default="mcvine-test-work",
    help="work directory"
)
def test(workdir):
    """
    run mcvine tests.

    It requires cmake and all mcvine dependencies.
    It is assumed that the tests are installed under
    $MCVINE_DIR/share/mcvine/tests.
    The tests will run at a separate work directory.
    """

    import os, sys, psutil, subprocess as sp
    if os.path.exists(workdir):
        raise RuntimeError("%s already exists")
    os.makedirs(workdir)
    os.chdir(workdir)

    from mcvine.deployment_info import mcvinedir
    testsdir = os.path.join(mcvinedir, 'share', 'mcvine', 'tests')

    cores = psutil.cpu_count() - 1
    if cores < 1: cores = 1

    cmd = '''cmake %s && env CTEST_OUTPUT_ON_FAILURE=1 make test ARGS="-j%s"''' % (testsdir, cores)
    sp.check_call(cmd, shell=True)
    return
