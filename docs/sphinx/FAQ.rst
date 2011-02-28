.. _faq:

Frequently Asked Questions
==========================

How do I ...
------------

... Use a mcstas component that I wrote myself?
    An automatic tools is available to wrap a mcstas component to a mcvine component.
    Please take a look at :ref:`user-defined-mcstas-components`.

... Check whether parallel mcvine simulation is available for my system?
    Run the following command::

      $ mpirun -np 2 python -c "import mpi; print mpi.world().rank"

    If you see two number "0" and "1" (random sequence), parallel mcvine is available.

... Get help on the instrument simulation application I have created?
    Say if your application is mysimapp.py, you can do::

      $ mysimapp.py -h

    to see what this app is about, and the available options. 
    For help on common simulation application options, please refer 
    to :ref:`fundamentals-instrument`; for a tutorial, see
    :ref:`create-sim-app`.

... What does the intensities at monitors mean?
    Please refer to :ref:`fundamentals-simulated-intensities`
