#!/usr/bin/env python

import os, numpy as np, shutil
import mcvine.run_script as mrs


import click
@click.command()
@click.option(
    "--ncount", type=float, default=1e4,
    help='neutron count'
)
@click.option("--nodes", type=int, default=1)
@click.option("--debug/--no-debug", default=False)
@click.option("--sample-type", default='mcvine')
def main(ncount, nodes, debug, sample_type):
    if debug:
        ncount = min(50, ncount)
    outdir = 'out-{}-n{:g}-nodes{}{}'.format(sample_type, ncount, nodes, '-debug' if debug else '')
    if os.path.exists(outdir): shutil.rmtree(outdir)
    mrs.run_mpi(
        'instr.py',
        outdir, int(ncount),
        nodes=nodes, overwrite_datafiles=True,
        debug=debug, sample=sample_type
    )
    return

if __name__ == '__main__': main()
