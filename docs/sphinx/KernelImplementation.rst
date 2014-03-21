.. _kernel-implementation:

Kernel implementation
=====================

Basics
------
Kernel represents a kind of scattering mechanism in a homogeneous
neutron scatterer.



Coherent inelastic phonon kernel for powder sample
--------------------------------------------------

From Squire, the double differential cross section
for coherent inelastic phonon scattering that excites
one phonon is

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
   \frac{1}{2k_i k_f Q}
   


