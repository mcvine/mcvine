Known problems
==============


multiphonon S(Q,E) may fail at low temperature
----------------------------------------------

This calculation involves computation of factors like exp(E/kBT) and
could diverge if E is too large compare to kBT. 
It fails when, for example, when input DOS has an energy range 
up to 50meV, and temperature is 3 Kelvin, and multiphonon
S(Q,E) spectrum is calculated up to 10th order.



multiphonon S(Q,E) may fail if phonon DOS has too many data points
------------------------------------------------------------------

Less than 1000 data points should be fine.
Otherwise, may be out of memory.

