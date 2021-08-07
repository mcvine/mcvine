#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

#
import os

ENVVAR_MPI_LAUNCHER = "MCVINE_MPI_LAUNCHER"
mpi_launcher_choice = os.environ.get(ENVVAR_MPI_LAUNCHER, 'mpirun')
def build_launch_cmd(nodes, cmd):
    if mpi_launcher_choice == 'mpirun':
        cmd = "mpirun -np {} {}".format(nodes, cmd)
    elif mpi_launcher_choice == 'slurm':
        cmd = "srun -n {} {}".format(nodes, cmd)
    elif mpi_launcher_choice == 'serial':
        pass
    else:
        raise NotImplementedError("launcher {}".format(mpi_launcher_choice))
    return cmd

ENVVAR_BINDING_NAME = 'MCVINE_MPI_BINDING'
if mpi_launcher_choice == 'serial':
    # if running in serial mode, no point to find a mpi binding
    os.environ[ENVVAR_BINDING_NAME] = 'NONE'
mpi_binding_choice = os.environ.get(ENVVAR_BINDING_NAME)

# End of file
