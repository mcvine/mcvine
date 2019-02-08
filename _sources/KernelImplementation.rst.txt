.. _kernel-implementation:

Kernel implementation
=====================

Basics
------
Kernel represents a kind of scattering mechanism for a homogeneous
neutron scatterer.

Mainly we are concerned with two methods for the scattering kernel:

* scattering_coefficient(neutron)
* S(neutron)

The method scattering_coefficient(neutron) can be computed as
:math:`\sigma / v_0`, where :math:`\sigma` is the total cross section
of a unit cell and :math:`v_0` is the unit cell volume,
if the material is crystalline.

The method S(neutron) resembles the dynamic structure factor
:math:`S({\bold Q}, E)`.
In this method, we need to choose a scattering direction and 
its speed, and adjust the probability of the neutron
according to the dynamic structure factor.
It is useful to remember that the dynamic structure factor
is concerned with the orientation and energy distribution
of the scattered neutrons, while the total amount of scattering
is determined by the cross section, which is already taken
care of by the scattering_coefficient method.
Another useful fact is when the scattering is isotropic,
:math:`S({\bold Q})=1`.
The method S(neutron) is more complicated than just
computing :math:`S({\bold Q}, E)`, however.
It involves Monte Carlo selection and the random variables
are usually not simply :math:`\bold Q` and :math:`E`.

In the following, typical implementations for some 
kernels are documented. 


Isotropic kernel
----------------
Isotropic kernel can be useful for testing purpose.
And it could be a good approximation for incoherent 
scattering at low temperature.

The implementation is easy: just generate
randomly and uniformly neutrons in all :math:`4\pi`
solid angle.



S(Q,E) kernel
-------------
This kernel works with scalar Q instead of :math:`\bold Q`
vector, meaning it is most useful for powder studies.

Start from the definition of dynamic structure factor:

.. math:: 
   \frac{d^2 \sigma}{d\Omega dE_f} =
   \frac{\sigma}{4\pi} 
   \frac{k_f}{k_i}
   N S(Q,E)

The integrated scattering intensity for a chosen :math:`Q`
and :math:`E` is at a cone, or we can write

.. math::
   \frac{\sigma}{4\pi} 
   d\Omega
   \frac{k_f}{k_i}
   N S(Q,E)
   =
   \frac{\sigma}{4\pi} 
   2\pi \sin\theta d\theta
   \frac{k_f}{k_i}
   N S(Q,E)
   
Observe

.. math::
   k_i^2 + k_f^2 - 2 k_i k_f \cos\theta = Q^2

and hence,

.. math::
   k_i k_f \sin\theta d\theta =  Q dQ

we obtain,

.. math::
   N \sigma \;
   S(Q,E) \;
   \frac{Q dQ}{2 k^2_i}

Or we can rewrite it as

.. math::
   \frac{d^2 \sigma}{dE_f dQ}
   = N \sigma \;
   S(Q,E) \;
   \frac{Q}{2 k^2_i}



Coherent inelastic phonon kernel for powder sample
--------------------------------------------------

From Squire, the double differential cross section
for coherent inelastic phonon scattering that excites
one phonon is
(the expression for scattering that annhilates one phonon can
be treated similarly)

.. math:: 
   \left( \frac{d^2 \sigma}{d\Omega dE_f} \right)_{coh+1} =
   \frac{\sigma_{coh}}{4\pi} 
   \frac{k_f}{k_i}
   \frac{\left( 2\pi \right)^3}{v_0}
   e^{-2W}
   \frac{1}{2M} 
   \sum_{\bold Q}
   \frac{\left( {\bold Q}\cdot {\bold e}_{{\bold Q},\alpha}\right)^2}
   {\omega_{{\bold Q},\alpha}} 
   \langle n_{{\bold Q},\alpha} + 1 \rangle
   \delta(\omega_i-\omega_f-\omega_{{\bold Q},\alpha}) 
   \delta({\bold k}_i-{\bold k}_f - {\bold Q} )


We want to compute the total cross section for a specific :math:`\bold Q`.
Note that the differential solid angle above is for the scattered neutron,
i.e., :math:`d\Omega = d\Omega_f`.
Also note that for ideal powder sample, there are small crystallites
inside the sample, and their orientation are uniformly and randomly
distributed in the :math:`4\pi` solid angle.
Therefore, the integration we are looking for is

.. math:: 
   \sigma_{\bold Q} = \int dE_f d\Omega_f \frac{d\Omega_i}{4\pi}
   \left( \frac{d^2 \sigma}{d\Omega dE_f} \right)_{\bold Q}
   :label: sigma_Q

where

.. math::
   \left( \frac{d^2 \sigma}{d\Omega dE_f} \right)_{\bold Q} =
   \frac{\sigma_{coh}}{4\pi} 
   \frac{k_f}{k_i}
   \frac{\left( 2\pi \right)^3}{v_0}
   e^{-2W}
   \frac{1}{2M} 
   \frac{\left( {\bold Q}\cdot {\bold e}_{{\bold Q},\alpha}\right)^2}
   {\omega_{{\bold Q},\alpha}} 
   \langle n_{{\bold Q},\alpha} + 1 \rangle
   \delta(\omega_i-\omega_f-\omega_{{\bold Q},\alpha}) 
   \delta({\bold k}_i-{\bold k}_f - {\bold Q} )
   :label: dd_sigma_Q
   
We observe that

.. math::
   k_i^2 + Q^2 - 2k_i Q \cos\theta = k_f^2

where :math:`\theta` is the angle
between :math:`\bold k_i` and :math:`\bold Q`.
Differentiate the equation and we obtain:

.. math::
   \frac{2m}{\hbar^2} dE_f = 2 k_i Q \sin\theta d\theta
   :label: diff_kiQkf_geom

Since :math:`{\bold k_i}` is at a cone about :math:`\bold Q`
at angle :math:`\theta`, we have

.. math::
   d\Omega_i = 2\pi \sin\theta d\theta
   :label: dOmega_i

On the other hand,

.. math::
   d{\bold k_f} = k_f^2 dk_f d\Omega_f = \frac{m k_f}{\hbar^2} dE_f d\Omega_f
   :label: d_k_f

Plug Eqs :eq:`dd_sigma_Q`, :eq:`diff_kiQkf_geom`, :eq:`dOmega_i`, :eq:`d_k_f` into :eq:`sigma_Q`, we obtain

.. math::
   \sigma_{\bold Q} = 
   \frac{\sigma_{coh}}{4\pi} 
   \frac{k_f}{k_i}
   \frac{\left( 2\pi \right)^3}{v_0}
   e^{-2W}
   \frac{\hbar^2 ({\bold Q}\cdot {\bold e})^2}{2M \hbar\omega} 
   \langle n + 1 \rangle
   \frac{1}{2 k_i k_f Q}
   
In the implementation, we need to randomly select a branch and a 
:math:`\bold Q`, and then compute 
:math:`\sigma_{\bold Q}`.
Due to randomly selection of :math:`\bold Q`, 
a multiplication factor of 
number of possible Q points to choose from.
Consider the number of Q points in one reciprocal
unitcell for one phonon branch is N, or 
the number of unit cells in one crystal,
we obtain the multiplication factor as

.. math::
   N \frac{V_{r,accessible}}{v_{0r}}

where :math:`V_{r,accessible}` is the reciprocal
volume accessible by the scattering process, which
depends on the incident neutron energy, and
:math:`v_{0r}` is the volume of the reciprocal unit cell.
Note that :math:`N \sigma_{coh}` is actually taken care of
elsewhere, and :math:`v_{0r}=   \frac{\left( 2\pi \right)^3}{v_0}` 
the probablity multiplication factor is

.. math::
   \frac{1}{4\pi} 
   \frac{k_f}{k_i}
   e^{-2W}
   \frac{\hbar^2 ({\bold Q}\cdot {\bold e})^2}{2M \hbar\omega} 
   \langle n + 1 \rangle
   \frac{V_{r,accessible}}{2 k_i k_f Q}


One-phonon coherent inelastic scattering, single crystal
--------------------------------------------------------

.. note::
   Under construction

Now we are considering more complex examples. Suppose we are working on a single-crystal sample. For now, we are only concerned with coherent inelastic scattering with one-phonon processes. First let us look at the differential cross section of one-phonon emission:

.. math::
   \left( \frac{d^2 \sigma}{d\Omega dE_f} \right)_{coh+1} =
   \frac{\sigma_{coh}}{4\pi} \frac{k_f}{k_i}
   \frac{\left( 2\pi \right)^3}{v_0}\frac{1}{2M} 
   e^{-2W}
   \sum_{\bold Q}\frac{\left( {\bold Q}\cdot {\bold e}_{{\bold Q},\alpha}\right)^2}
   {\omega_{{\bold Q},\alpha}} \langle n_{{\bold Q},\alpha} + 1 \rangle
   \delta(\omega_i-\omega_f-\omega_{{\bold Q},\alpha}) 
   \delta({\bold k}_i-{\bold k}_f - {\bold Q} )

where :math:`{\bold Q}` is the wave vector of phonon, :math:`\alpha` is the index for phonon branch, :math:`\omega_{{\bold Q},\alpha}` is the phonon enregy, :math:`i` and :math:`f` represents initial and final states of neutron, :math:`\sigma_{coh}` is the coherent scattering cross section, :math:`v_0` is the volume of the unit cell, :math:`M` is the mass of the atom.

For convenience, define

.. math::
   C = \frac{\sigma_{coh}}{4\pi} \frac{k_f}{k_i}
   \frac{\left( 2\pi \right)^3}{v_0}\frac{1}{2M} e^{-2W}

In the case of large crystal, the density of Q points in the reciprocal space is high, and the summation over :math:`{\bold Q}` can be replaced by an integration:

.. math::
   \sum_{\bold Q} = \int \frac{V}{(2\pi)^3} d{\bold Q}

(C.1) reduces to 

.. math::
   \left( \frac{d^2 \sigma}{d\Omega dE_f} \right)_{coh+1}
   =C \times
   \frac{V}{(2\pi)^3} 
   \left.\left[ 
   \frac{\left( {\bold Q}\cdot {\bold e}_{{\bold Q},\alpha}\right)^2}
   {\omega_{{\bold Q},\alpha}} \langle n_{{\bold Q},\alpha} + 1 \rangle
   \delta(\omega_i-\omega_f-\omega_{{\bold Q},\alpha})
   \right]\right|_{{\bold Q}={\bold k}_i-{\bold k}_f}

The "evaluate at" symbol reminds us the momentum conservation condition resulted from the integration of one of the delta functions in (C.1).

We now want to evaluate the differntial cross section 
:math:`\frac{d\sigma}{d\Omega}`
by doing an integration over :math:`E_f`

This means that we fix the scattering direction, :math:`\frac{{\bold k}_f}{k_f}`. By changing :math:`E_f`, we are changing the length of scattering wave vector, :math:`k_f`, and therefore changing :math:`{\bold Q}` and :math:`\omega_{{\bold Q},\alpha}`

Thus

.. math::
   \int \delta(\omega_i-\omega_f-\omega_{{\bold Q},\alpha}) d E_f
   = \frac{\hbar}{ d(\omega_f + \omega_{{\bold Q},\alpha}) / {d\omega_f} } 

The differential cross section is then

.. math::
   \left( \frac{d \sigma}{d\Omega} \right)_{coh+1}
   = C \times \frac{V}{(2\pi)^3} 
   \left.\left[
   \frac{\left( {\bold Q}\cdot {\bold e}_{{\bold Q},\alpha}\right)^2}{\omega_{{\bold Q},\alpha}}
   \langle n_{{\bold Q},\alpha} + 1 \rangle
   \frac{\hbar}{ d(\omega_f + \omega_{{\bold Q},\alpha}) / {d\omega_f} }
   \right]\right|_{
   {\bold Q}={\bold k}_i-{\bold k}_f;
   \omega_{{\bold Q},\alpha}=\omega_i-\omega_f
   }

.. math::
   \left( \frac{d \sigma}{d\Omega} \right)_{coh+1}
   =\frac{\sigma_{coh}}{4\pi} \frac{k_f}{k_i}
   N
   \frac{1}{2M} e^{-2W}
   \left[
   \frac{\left( {\bold Q}\cdot {\bold e}_{{\bold Q},\alpha}\right)^2}{\omega_{{\bold Q},\alpha}}
   \langle n_{{\bold Q},\alpha} + 1 \rangle
   \frac{\hbar}{ d(\omega_f + \omega_{{\bold Q},\alpha}) / {d\omega_f} }
   \right]

in which we neglect the "evaluate at" symbol.

To get scattering probability from scattering cross section, we need a factor of 
:math:`\frac{l}{V}`
where :math:`l` is the length of the path that neutron goes through the sample, and :math:`V` is the volume of the sample.

Also in the previous section we have shown that we need a factor of :math:`4\pi`. 

Considering the absorption along the path, there is another factor of 
:math:`e^{-\frac{\sigma_a(v_i)+\sigma_i}{v_0} l_i} e^{-\frac{\sigma_a(v_f)+\sigma_i}{v_0} l_f}`. 

So the final result of Monte-Carlo probability multiplication factor is

.. math::
   {\sigma_{coh}} \frac{k_f}{k_i}
   \frac{l}{v_0}
   \frac{1}{2M} e^{-2W}
   e^{-\frac{\sigma_a(v_i)+\sigma_i}{v_0} l_i} e^{-\frac{\sigma_a(v_f)+\sigma_i}{v_0} l_f} 
   \left[
   \frac{\left( {\bold Q}\cdot {\bold e}_{{\bold Q},\alpha}\right)^2}{\omega_{{\bold Q},\alpha}}
   \langle n_{{\bold Q},\alpha} + 1 \rangle
   \frac{\hbar}{ d(\omega_f + \omega_{{\bold Q},\alpha}) / {d\omega_f} }
   \right]

where :math:`l_i,\, l_f` are the length of entering and leaving paths.
The incoherent scattering cross section is :math:`\sigma_i`, and

.. math::
   \sigma_a(v) = \sigma_a(2200m/s)\frac{2200}{v}

is the absorption cross section.


Scattering from single crystal analytical dispersion function
-------------------------------------------------------------

.. math::
   \frac{d^2 \sigma}{d\Omega dE_f} =
   \frac{\sigma}{4\pi} 
   \frac{k_f}{k_i}
   N S({\bold Q},E)
   
.. math::
   S({\bold Q},E) = \delta(E-E({\bold Q})) S({\bold Q})

The algorithm first randomly choose a direction in the
4pi solid angle, and that takes care of 
:math:`d\Omega`.

Along a chosen direction :math:`{\bold e}_f`,
we can use :math:`k_f` as 
a parameter, and get two functions for energy transfer:

.. math::
   E1(k_f) = E_i - E_f = E_i - \frac{\hbar^2 k_f^2}{2 m}

and 

.. math::
   E2(k_f) = E({\bold Q}) = E({\bold k}_i - k_f \; {\bold e}_f) 

The delta function in the structure factor requires these two
functions to equal.
We seek to transform the integration of delta function:

.. math::
   \int \delta(E-E({\bold Q})) dE_f = \int \delta(f(k_f)) dk_f \; \frac{dE_f}{dk_f}
   
or

.. math::
   \int \delta(E-E({\bold Q})) dE_f = \left| \frac{d f}{dk_f} \right|^{-1} \; \frac{dE_f}{dk_f}


Advanced topics
---------------

Method::

  bool total_scattering();

by default return false.
Override this method in a kernel to return true
if the kernel has a strongly energy-dependent 
total scattering cross section, such as, in the 
case of powder diffraction.


