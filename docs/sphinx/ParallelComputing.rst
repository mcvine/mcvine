.. _ParallelComputing:

Parallel computing
==================

Requirements
------------
mpi implementation.



Advanced topics
---------------
Set environment variable "MCVINE_MPI_BINDING" to choose mpi binding.

Choices:
* pyre
* mpi4py

Test whether pyre mpi is available::

 $ mpirun -n 2 python -c "import mpi; print mpi.world().rank"

If it prints out "0" and "1" (in any order), pyre mpi is good.


Test whether mpi4py is available::

 $ mpirun -n 2 python -c "from mpi4py import MPI; print MPI.COMM_WORLD.Get_size()"

If it prints out "0" and "1" (in any order), pyre mpi is good.


Use slurm
---------

Set environment variable "MCVINE_MPI_LAUNCHER" to "slurm".

Default launcher is "mpich2".

