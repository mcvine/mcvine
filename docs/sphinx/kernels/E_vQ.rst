.. _kernel_E_vQ:

Analytical :math:`E(\vec{Q})`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This kernel scatters neutrons according to a
:math:`S(\vec{Q},E)=S(\vec{Q}) \delta(E-E(\vec{Q}))` input.
Both :math:`S(\vec{Q})` and :math:`E(\vec{Q})`
are analytical functions.

Parameters: 

- Emax: maximum energy transfer
- E_Q: E(Q) expression. for example: 20 + 5 * sin(Qx+Qy+Qz)
- S_Q: S(Q) expression. for example: 1

Example::

  <E_vQ_Kernel 
     E_Q="20 + 5 * sin(Qx+Qy+Qz)"
     S_Q="1" 
     Emax="30*meV"
     />

The expression uses the `function parser for C++ <http://warp.povusers.org/FunctionParser/fparser.html>`_ format. It is quite flexible and can be quite complex.
It can even support
discontinous dispersion surface. 
Here is an example::

  E_Q="pi:=3.1415926535897932; twopi:=2*pi; a:=7; b:=5; c:=5.5; beta:=96/180.*pi;  h:=a*Qz/twopi; k:=b*Qx/twopi; l:=c*(cos(beta)*Qz+sin(beta)*Qy)/twopi; lmod2:=l%2; lmod2p:=if(lmod2 < 0, lmod2+2, lmod2); cospih2:=cos(h/2*pi)^2; cospil2:=cos(l/2*pi)^2; cospik2:=cos(k*pi)^2; dkmod1:=abs(k-int(k)); (40^2*(1-cospih2*cospik2) + 60^2*(1-cospil2*cospik2))^(1./2)*exp(-dkmod1*0.15) + if(lmod2p>0.5 & lmod2p<1.5, 13.5, 0)"

