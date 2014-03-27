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
The method S(neutron) is more complicated that just
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
