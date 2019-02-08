.. _kernel_E_Q:

Analytical E(Q)
^^^^^^^^^^^^^^^

This kernel scatters neutrons according to a
:math:`S(|\vec{Q}|,E)=S(|\vec{Q}|) \delta(E-E(|\vec{Q}|))` input.
Both :math:`S(|\vec{Q}|)` and :math:`E(|\vec{Q}|)`
are analytical functions.

Parameters: 

- Qmin: Minimum momentum transfer
- Qmax: Minimum momentum transfer
- E_Q: E(Q) expression. for example: 30+5*sin(Q)
- S_Q: S(Q) expression. for example: 1

Example::

  <E_Q_Kernel 
     E_Q="30+5*sin(Q)" 
     S_Q="1" 
     Qmin="0./angstrom"
     Qmax="10./angstrom"
     />
  
