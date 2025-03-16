.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

.. _time_theory:

====================
Time-domain Analysis
====================

The problem and the solution
----------------------------

A fundamental aspect of loudspeaker modeling is the ability to calculate the time-domain response of a driver in free air, or in a specified enclosure, given prior calculation of the frequency response.   Whereas the low-frequency electroacoustic theory of Benson, Thiele and Small  may be used to compute the steady-state pressure (SPL), velocity and excursion of a loudspeaker as a function of frequency, it remains to compute the time-domain impulse and step responses by inverse Laplace transform. This is done analytically by Benson :cite:`benson:1993` for simple closed boxes by decomposing the :math:`s`-domain response function into a sum of poles such that the Laplace transform can be inverted using exponential and related functions. For more complicated polynomial filters, numerical methods based on computing eigenvalues of the companion matrix are often used.  This approach does not generalize to non-polynomial response functions which inevitably require a numerical treatment, most often by discrete Fourier inversion methods.

In these notes we describe a numerical approach to invert Laplace transforms required for computation of the time-domain response of loudspeakers.  The method is an adaptation of the method of Weideman :cite:`weideman:2007`, with suitable modifications to accomodate the analytic structure found in typical audio applications.  In comparison to Fourier method, however, the Weideman method is significantly more efficient and accurate, yet it is straightforward to implement without the need for third-party mathematical libraries.  Thus it can be implemented in existing box-modeling software with little effort.

Response function representation
--------------------------------

Consider the driven linear system

.. math::
   :label: eq.basic
	
   {\cal D} \, x(t) = f(t) \; ,

where :math:`x` is a generalized displacement, :math:`f` is a generalized force, and :math:`{\cal D}` is a linear operator.  We remark that :math:`{\cal D}` can contain integrals, derivatives or fractional derivatives.   Taking the Laplace transform of Eq. :eq:`eq.basic` and solving for :math:`X(s)` yields the response function form of the linear system:

.. math::
   X(s) = R(s) F(s) \; .

Here, :math:`X(s)` and :math:`F(s)` are the Laplace transforms of :math:`x(t)` and :math:`f(t)`,

.. math::
   \begin{eqnarray}
   X(s) & = & {\cal L}[x] \doteq \int_0^\infty dt \, e^{-st} x(t) \; , \\
   F(s) & = & {\cal L}[f] \doteq \int_0^\infty dt \, e^{-st} f(t) \; .
   \end{eqnarray}


and :math:`R(s)` is the response function.  One can solve for :math:`x(t)` by inverting the Laplace transform

.. math::
   x(t) = {\cal L}^{-1} \left[ R(s) F(s) \right] \; ,

where the inverse is defined in terms of the Bromwich integral

.. math::
   :label: eq.brom
	
   x(t) = {\cal L}^{-1} \left[ X \right] \doteq \frac{1}{2 \pi i} \int_{\sigma-i\infty}^{\sigma+i\infty} ds \, e^{st} X(s) \; .

Here, :math:`\sigma` is chosen so that the contour lies to the right of all singularities of the integrand, as illustrated in :numref:`zplane`.  So long as the contour remains to the right of these singularities, the Cauchy integral theorem :cite:`greene:2006` guarantees that the value of the integral is independent of the path of integration.

.. subfigure:: A
   :width: 50%
   :name: zplane
   :align: center
	
   .. image:: images/time_paper/zplane.png

   Complex plane illustrating Bromwich inversion contour (dashed line) for a hypothetical case.  The contour must lie to the right of all poles and branch cuts.  Also shown is the unit circle, poles typical of a 4\ :sup:`th`-order Butterworth filter, and a branch cut (wavy curve) at :math:`s=0`.


Impulse response
................

The impulse response is generated using the Dirac delta function :math:`\delta(t)` as the driving force:

.. math:: f(t) = \delta(t) \Longleftrightarrow F(s) = 1 \; .

The required inverse transform is thus

.. math:: \xim(t) =  {\cal L}^{-1} \left[R(s)\right] \; .

In the solution of inhomogeneous differential equations, when :math:`\cal{D}` is a linear differential operator, the impulse response :math:`\xim` is equivalently called the *Green's function* for :eq:`eq.basic`.

Step response
.............

The step response is generated using the Heaviside step function :math:`H(t)` as the driving force:

.. math:: f(t) = H(t) \Longleftrightarrow F(s) = 1/s

The required inverse transform is thus

.. math:: \xs(t) =  {\cal L}^{-1} \left[\frac{R(s)}{s}\right]


The step and delta functions are related according to

.. math:: \frac{dH}{dt} \doteq \dot{H} = \delta(t) \; ,

where this formula is rigorously justified in terms of generalized functions :cite:`zemanian:1965`.  Note that, in this paper, a dot denotes a time derivative.

General system response
.......................

Using the convolution property of the inverse transform, it is easy to show that

.. math::
   \begin{eqnarray}
   x(t) &=& \int_0^t d\tp \, \xim(\tp) f(t-\tp) \; , \\
   &=& \int_0^t d\tp \, \xs(\tp) \dot{f}(t-\tp) \; .
   \end{eqnarray}

Evidently, one can also compute the step response by integration of the impulse response,

.. math::
  \xs(t) = \int_0^t d\tp \, \xim(\tp) \; .

A simple example outlining the calculation of impulse and step responses for a simple linear oscillator is given in the Appendix. In the following sections we will focus on the step response, :math:`\xs`, because it avoids the singularity present in the impulse response.  The step response is typically computed in box modeling programs.

Application to transducer response
----------------------------------

In the present paper, we choose to formulate the inverse problem using a dimensionless time :math:`t = \ws \tau`, where :math:`\tau` is the physical time, and :math:`\ws = 2 \pi \fs` is the resonant frequency of the loudspeaker driver.  To illustrate the inversion process for a simple case, we consider the steady-state pressure response for an undamped, closed box :cite:`benson:1993`. In this case, the response function takes the form of a 2\ :sup:`nd`-order high-pass filter

.. math::
   :label: eq.hp2
	
   R(s) = \frac{s^2}{\displaystyle s^2 + \frac{s}{\qts} + 1 + \alpha} \; ,

where :math:`\alpha \doteq \cms/\cmb` is the compliance ratio and :math:`\qts` is the driver total :math:`Q`.  In these expressions, :math:`\cms` is the mechanical compliance of the driver suspension, and :math:`\cmb` is the equivalent mechanical compliance of the interior of the closed box.  Further, :math:`1/\qts = 1/\qes + 1/\qms`, where :math:`\qes` and :math:`\qms` are the electrical and mechanical :math:`Q` factors of the driver.

For the special choice of :math:`\alpha=0` (i.e., the infinite baffle limit :math:`\cmb \rightarrow \infty`) and :math:`\qts = 0.5`, we can write the inversion integral for the step response as

.. math::
   :label: eq.simple
	
   \xs(t) = \frac{1}{2 \pi i} \int_{\sigma-i\infty}^{\sigma+i\infty} ds \, e^{st}
   \, \frac{s}{s^2 + 2s + 1} \; .

The integrand contains a pole of order 2 at :math:`s=-1`, in which case we can close the contour to the left and use the residue theorem to give

.. math::
   :label: eq.residue
	
   \xs(t) = \frac{\partial}{\partial s}\left. \left(s e^{st}\right) \right|_{s = -1} = e^{-t} (1-t) \; .

In the more realistic case of vented and damped enclosures, the same method based on analytic contour integration will work in principle, although locating the poles and computing residues may become tedious and complicated.  In practical cases, the residue calculation is done numerically by computing eigenvalues of the *companion matrix* :cite:`edelman:1995`.  Importantly, the residue-based methods described above are applicable only to rational functions, and fail in the general case for which the driver circuit model contains semi-inductance :cite:`thorborg:2011` or viscoelastic creep :cite:`knudsen:1993,thorborg:2010,thorborg:2013,novak:2016`. In this case the frequency-domain response function will contain elements described by functions with branch points -- for example, :math:`\sqrt{s}` or :math:`\ln(s)`.  One must then return to the Bromwich integral in Eq. :eq:`eq.brom` and perform the contour integration numerically.

The problem of numerical inversion of the Laplace transform has been an active area of research since the 1960s :cite:`bellman:1966`, with an important method developed by Talbot in 1979 :cite:`talbot:1979`.  There is no single best method; rather, the most suitable method will in general depend on the nature of the problem. To illustrate the convergence issues associated with inversion of the transform, consider again the example of Eq. :eq:`eq.simple`.  As a straightforward attempt to evaluate the Bromwich integral directly, one can put the integration contour on the imaginary axis :math:`s=iy`.  In this case the Bromwich integral, Eq. :eq:`eq.simple`, reduces to the inverse Fourier transform

.. math::
   :label: eq.ift

   \xs(t) = \frac{1}{2\pi} \int_{-\infty}^\infty dy \, e^{i y t} \, \frac{iy}{(iy)^2 + 2iy + 1} \; .

The conversion of the Bromwich integral to a Fourier integral is always possible when the singularities of the transfer function lie in the left half-plane (i.e., when the linear system is *stable*).  This integral can be performed analytically to yield

.. math::
   :label: eq.direct

   \begin{eqnarray}
   \xs(t)
   & = &~ \frac{1}{\pi} \int_0^\infty dy \, \frac{2y^2 \cos(yt) + (y^3-y) \sin(yt)}{(1+y^2)^2} \; , \\
   & = &~ e^{-t} (1-t) \; .
   \end{eqnarray}

As required, the analytic solution in Eq. :eq:`eq.direct`, obtained by directvintegration of the infinite (Fourier) integral, is the same as that obtained in Eq. :eq:`eq.residue` by contour integration.  However, consideration of the Fourier integral above reveals a serious deficiency; namely, that the integral decays very slowly at large values of :math:`y`:

.. math::
  \frac{2y^2 \cos(yt) + (y^3-y) \sin(yt)}{(1+y^2)^2} \sim \frac{\sin(yt)}{y}
  \; \text{as}\; y \rightarrow \infty \; .

Thus, at small times :math:`t \ll 1`, extremely large values of :math:`y` (i.e., very high frequencies in the Fourier sense) must be retained to accurately evaluate the integral.  This is in contrast to the previous contour integration, which can determine the integral exactly via any closed contour surrounding the pole at :math:`s = iy = -1`.  The implication is that a numerical method based on integration along a vertical contour will be fundamentally inefficient, quite independent of the numerical quadrature method.  Let us take this illustration further by explicitly constructing a numerical inversion, via *inverse discrete Fourier transform* (iDFT), and rewrite the integral as

.. math::
   :label: eq.cont
	
   \xs(t) = \int_{-\wmax}^{\wmax} dy \, e^{iyt} \frac{R(iy)}{iy} + E(\wmax) \; .

Above, :math:`E(\wmax)` is the error resulting from truncation of the limits of integration, and, as before, :math:`R(s) = s^2/(s^2+2s+1)`.  If we let :math:`t_n = n \Delta t` and :math:`y_k = k \Delta y` then

.. math::
   :label: eq.dft

   x_n = \sum_{k=-N/2}^{N/2-1} e^{2\pi i kn/N} \, G_k \; , \quad n = 0, \ldots, N-1 \; ,

where :math:`x_n` is an approximation to :math:`\xs(t_n)`, :math:`G_k = R(ik\Delta y)/(ik)`, :math:`\wmax = N \Delta y/2`, and :math:`\Delta y \Delta t = 2\pi/ N`.  Eq. :eq:`eq.dft` thus expresses :math:`x_n` as the
iDFT of :math:`G_k`.  In the limit :math:`N \rightarrow \infty`, :math:`x_n` will exactly recover the finite integral in Eq. :eq:`eq.cont`, but will always differ from :math:`\xs(t_n)` by the truncation error :math:`E(\wmax)`. To illustrate the poor accuracy obtained in a typical case, consider a transducer with :math:`\fs = 100` Hz and choose :math:`f_\mathrm{max} = 32` kHz and :math:`n=8000`. Then

.. math:: |\xs(t_n) - x_n| \sim E(\wmax) \sim 1.5 \times 10^{-3} \; ,

when :math:`t_n \sim 0.1`.  Considering the very high resolution, this is a surprisingly large truncation error.  The error is not a consequence of any particular deficiency of the iDFT itself, but rather of the vertical Fourier contour.  This issue is well-recognized in the literature and numerous methods to overcome the poor convergence have been developed.

Weideman method
---------------

Instead of the vertical contour, we will use an approach based on deforming the contour into the left half-plane.  Although the basic approach is due to Talbot :cite:`talbot:1979`, we use the more recent optimal method due to Weideman :cite:`weideman:2007`, with modifications to suit the problem of loudspeaker response.  It should be emphasized that application of the method requires the response function to be known as an analytic function of the complex variable :math:`s`.

Weideman treats both a parabolic and hyperbolic contour, but we consider only the parabolic one:

.. math::
   :label: eq.parabola
	
   s(u) = \mu \left( i u + 1 \right)^2 \, , \quad - \infty < u < \infty \; .

The integration rule is trapezoidal

.. math::
   :label: eq.trap

   \xs(t) = \frac{\Delta}{2\pi i} \sum_{k=-N}^N e^{s_k t} \frac{R(s_k)}{s_k} s^\prime(u_k) \; ,

where :math:`s_k \doteq s(u_k)`, :math:`s^\prime = ds/du = 2\mu(i-u)` and :math:`u_k = k \Delta`. Although
Eq. :eq:`eq.trap` provides a discrete approximation to the integral for any values of :math:`\Delta` and :math:`\mu`, Weideman shows that the optimal parameters for the parabolic contour are

.. math::
   :label: eq.hmu
	
   \Delta_\mathrm{opt} = \frac{3}{N} \quad \text{and} \quad \mu_\mathrm{opt} = \frac{\pi}{12} \frac{N}{t} \; .

So long as the contour is acceptable (not passing through singularities during deformation into the parabola), the method is remarkably accurate.  We remark that the algorithm can be applied for any value of :math:`t > 0`, and the optimal parameters must be recomputed for every value of :math:`t` according to Eq. :eq:`eq.hmu`. In Ref. :cite:`weideman:2007`, the emphasis is on solving problems for which singularities lie on the negative real axis, in which case there are no restrictions on the smallness of :math:`\mu`.  For :math:`t` sufficiently large, however, the magnitude of :math:`\mu_\mathrm{opt}` will shrink so much that a pole is crossed.  Since we expect poles approximately in the range :math:`|s| \sim 1` (for example, a Butterworth filter has all poles on the left half of the unit circle), we must ensure that :math:`2 \mu > y_\mathrm{max}`, where :math:`y_\mathrm{max}` is the maximum height of a pole, and :math:`2 \mu` is the point at which upper-half of the parabola intersects the imaginary axis.  To see this, note from Eq. :eq:`eq.parabola` that :math:`s(1) = \mu (1+i)^2 = 2i\mu`.

Application to box response
---------------------------

To modify the Weideman algorithm to prevent pole crossing, it is instructive to consider in detail the behaviour of the response function for an undamped, vented box.  This is written as

.. math::
   R(s) = \frac{s^4}{\displaystyle \left(s^2+h^2\right) \left( 1 + \frac{s}{\qts} + s^2\right)
    + \alpha s^2} \; .

The new parameter :math:`h = \wpb / \ws`, where :math:`\wpb` is resonant frequency of the vented enclosure, transforms the response into a 4\ :sup:`th`-order filter with four poles in the left half-plane.   Small :cite:`small:1973b` refers to :math:`h` as the *system tuning ratio*.  Typical vented alignments choose :math:`h \sim 1`. The pole locations for this response function can be computed analytically in some special cases -- most notably when the denominator coincides with the 4\ :sup:`th`-order Butterworth polynomial:

.. math::
   :label: eq.but
	
   \begin{eqnarray}
   h^2 & = & 1 , \; \alpha = \sqrt{2} \\
   1/\qts & = & 2\cos(\pi/8)+2\cos(3\pi/8) \doteq 1/Q_4 \; .
   \end{eqnarray}

Note that :math:`Q_4 \simeq 0.382683`. Then the poles occur on the unit circle at :math:`s_k = \exp(i\theta_k)`, where

.. math::
   \theta_k = \left\{ \frac{5\pi}{8} , \frac{7\pi}{8} , \frac{9\pi}{8} , \frac{11\pi}{8}\right\} \; .

In the general case, the poles can be computed using a numerical root-finding method.  In :numref:`butter` we show the root locus for different parameter variations away from the Butterworth case.

.. subfigure:: ABC
   :gap: 6px
   :align: center
   :name: butter

   .. image:: images/time_paper/root-q.png

   .. image:: images/time_paper/root-a.png

   .. image:: images/time_paper/root-h.png

   Complex plane illustrating parabolic Weideman inversion contour for :math:`\mu=1` and poles of the response function.  Baseline parameter values are those for the Butterworth filter, as defined in Eqs. :eq:`eq.but`.  Starting from the baseline values, we scan :math:`\qts` in (a), :math:`\alpha` in (b) and :math:`h` in (c).  Plot (c) shows that large values of :math:`h` can give rise to a pole crossing, which must be avoided.  Darker circles indicate larger values of the scanned parameter.

The root loci illustrate that, for a Butterworth filter, :math:`\mu > 1` would be more than adequate to ensure that the parabolic contour always passes over the poles. However, in the limit of large tuning ratio, :math:`h \gg 1`, which corresponds to port tuning much higher than the driver resonant frequency, the two poles associated with the port resonance can be shown to occur at :math:`s \sim \pm i h -\alpha/(2h)`.  This behaviour is illustrated in :numref:`butter`.c.  Thus we would want to ensure that :math:`\mu > \max\left(1,h\right)`. Bearing these observations in mind, we can specify the required modifications to
Weideman's algorithm as follows: choose a value of :math:`N_0` to give desired integration accuracy at short time. Using this value of :math:`N_0`, define the critical parameters

.. math::
   :label: eq.m1

   \mu_c \doteq \max\left\{1,h\right\} \quad \text{and} \quad t_c \doteq \frac{\pi N_0}{12 \mu_c} \; .

If :math:`t < t_c`, set

.. math::
   :label: eq.m2
	
   \mu = \frac{\pi N_0}{12 \, t} \;, \quad N = N_0 \; , \quad \Delta = \frac{3}{N}

Otherwise, for :math:`t \geq t_c`, choose

.. math::
   :label: eq.m3

   \mu = \mu_c \; , \quad N = \left\lceil N_0 \, \frac{t}{t_c} \, \right\rceil \; , \quad \Delta = \frac{3}{N} \; ,

where :math:`\lceil \cdot \rceil` is the ceiling function (i.e., the smallest integer greater than or equal to the argument). In other words, when :math:`t < t_c`, we decrease :math:`\mu` at fixed :math:`N` to stay on the optimal contour.  When :math:`t > t_c`, we must increase :math:`N` to stay on the optimal contour for fixed :math:`\mu_c`. In practice, the method is conservative insofar as :math:`N` increases more rapidly than necessary to maintain accuracy.  For more complicated response functions, some method to determine the maximum height of the pole should be used, and that value should replace :math:`h` in the previous formulae. Since the minimum height of the parabolic contour in the left half-plane is :math:`y = 2 \mu`, the method above is conservative in that it ensures the contour is at least *double* the height of the highest pole.  To justify this choice, refer again to :numref:`butter` c.  The plot shows that not only will the choice :math:`\mu=1` fail when :math:`h > 2`, but that as the pole nears the contour, the integrand will vary rapidly, giving a large error in the trapezoidal integration scheme.  Thus, the choice :math:`\mu_c \doteq \max\left(1,h\right)` will ensure the contour is well-above the highest pole.

Result with viscoelastic suspension
-----------------------------------

To test the accuracy of the method for a more realistic case, we consider the previous vented box example but including the effects of viscoelastic compliance (suspension creep).  For the compliance function we choose the so-called *three-parameter creep* (3PC) model of Ritter and Agerkvist :cite:`ritter:2010`.

.. math::
   :label: eq.3pc
	
   \cms \longrightarrow \clog \left[ 1-\beta \ln \left( \frac{s}{s+s_0} \right) \right] \; .

The 3PC model includes both logarithmic creep and frequency-dependent damping. It is a generalization of the earlier LOG model of suspension creep :cite:`knudsen:1993`, and introduces a parameter :math:`s_0` to ensure that the frequency-dependent compliance :math:`\cms(s)` is nonnegative at high frequency. The form of the compliance in Eq. :eq:`eq.3pc` is equivalent to the original form given in Ref. :cite:`ritter:2010`, but written more compactly.  Some aspects of the algebra required to establish the equivalence is given in the Appendix.  We further remark that in Eq. :eq:`eq.3pc`, :math:`\beta` is the parameter of viscoelasticity (the creep parameter), which in the work by Ritter and Agerkvist (and the original work by Knudsen and Jensen) was represented by :math:`\lambda`. The conversion between the representations is clarified in Appendix A.4 of Ref. :cite:`candy:2017`.

Proceeding, the vented box response function can be modified to include the effects of viscoelasticity by writing

.. subfigure:: AB
   :gap: 6px
   :align: center
   :name: fig.perror

   .. image:: images/time_paper/p.png

   .. image:: images/time_paper/error.png

   Left plot shows time-domain step response :math:`\xs(t)` corresponding to :math:`R(s)` given in Eq. :eq:`eq.pcreep` with :math:`h`, :math:`\qts` and :math:`\alpha` corresponding to the Butterworth values.  Time dependence is shown with creep (solid curve, :math:`\beta=0.5`) and without creep (dotted curve, :math:`\beta=0`. Right plot shows absolute error, :math:`\Delta x_\mathrm{S} = | x_\mathrm{S}^{(N_0)}- x_\mathrm{S}^{(32)}|`, in inverse calculation for undamped vented box response function :math:`R(z)`.  Here, :math:`x_\mathrm{S}^{(N_0)}` refers to a numerical calculation with the given starting value :math:`N_0`.

.. math::
   :label: eq.pcreep
	
   R(s) = \frac{s^4}{\displaystyle \left(s^2+h^2\right) \left( \frac{1}{c(s)} + \frac{s}{\qts} + s^2\right) + \alpha s^2} \; ,

where :math:`c(s)` is an analytic function

.. math:: c(s) \doteq 1-\beta \ln \frac{s}{s+2} \; ,

that multiplies the static suspension compliance, :math:`\clog`.  In this example, we have chosen :math:`s_0=2`, corresponding to a transition frequency that is double the resonant frequency, but in practical cases other values may apply.  Note that when replacing the static compliance with the 3PC model, the meaning of :math:`\rms` will change in response to the frequency-dependent damping effect (originating from the imaginary part of the logarithm). We emphasize that due to the branch cut :math:`s \in [-2,0]`, the inverse transform of :math:`R(s)/s` *cannot* be computed by traditional transform tables or a straightforward integration. :numref:`fig.perror` shows the time-domain step response as computed using the method of the present paper. The solid and dashed curves, respectively, show the response with and without the creep function.  We can also give
an indication of the resolution required to give acceptable results.  Also in :numref:`fig.perror` we plot the absolute inversion error as a function of the initial number of nodes, :math:`N_0`.  We remark that eventually all curves overlap at sufficiently large :math:`t` for which :math:`\mu = 1`. These results show that the present method can compute the inverse efficiently to nearly machine precision.  In fact, in generating :numref:`fig.perror`, it was sufficient to use :math:`N_0 \leq 32`.  This is surprising given the apparent computational complexity of the integral in Eq. :eq:`eq.direct`.

Although the Fourier approach of Eq. :eq:`eq.dft` can be modified to give some accuracy improvement, it is manifestly less computationally efficient than the more elegant contour method. The latter with :math:`N = 2 N_0 + 1 = 17` gives better accuracy than the Fourier method with :math:`N = 8000`, and with :math:`N = 65` points, the modified Weideman contour method returns an answer correct to nearly the full machine precision!

Nonlinear driver simulation
---------------------------

To illustrate how the present inversion method can be applied to time-domain simulation of (nonlinear) driven loudspeaker response, consider the time-domain differential equations that describe the driver displacement
:math:`x(\tau)` :cite:`kaizer:1987`:

.. math::
   :label: eq.i
	
   \begin{eqnarray}
   V(\tau) &=& \re + \le \frac{dI}{d\tau} + \bl(x) \frac{dx}{d\tau} \; , \\
   \bl(x) \, I &=& \mms \frac{d^2 x}{d\tau^2} + \rms \frac{dx}{d\tau} + \frac{x}{\cms} \; .
   \end{eqnarray}

Here, the unknown functions are :math:`x(\tau)` and :math:`I(\tau)`, with :math:`V(\tau)` a known driving voltage.  Also, :math:`\re` and :math:`\le` are the voice coil resistance and inductance, :math:`\mms` is the moving mass, :math:`\rms` is the suspension damping, and :math:`\cms` the suspension compliance.  In these equations, the force-factor :math:`\bl(x)` can be considered to be a nonlinear function of :math:`x`.  Normally, viscoelastic compliance is not modeled because of the difficulty in treating the rightmost compliance term above. However, according to the present formulation, we should replace the term :math:`x/\cms` with

.. math:: {\cal L}^{-1} \left[  \frac{X(s)}{\clog} \frac{1}{1+\beta\ln(1+s_0/s)} \right] \; ,

where :math:`\clog` is a new constant compliance, :math:`\beta` is a measure of the strength of the viscoelastic behaviour, and :math:`s_0` is a parameter that characterizes the transition frequency between viscoelastic :math:`(s < s_0)` and simple elastic :math:`(s \gg s_0)` behaviour.  Here, we have introduced the Laplace variable :math:`s` corresponding to the dimensionless time :math:`t = \ws \tau`, such that :math:`\ws \doteq 1/\sqrt{\mms \clog}` is the resonant frequency of the system in the limit :math:`\beta \rightarrow 0`. We can rearrange terms slightly to write the required inverse transform as

.. math:: \frac{x(t)}{\clog} - \frac{\beta}{\clog} {\cal L}^{-1} \left[ G(s) X(s) \right] \; ,

where

.. math:: G(s) \doteq \frac{\ln(1+s_0/s)}{1+\beta \ln(1+s_0/s)} \; .

According to the convolution theorem, the time domain response can be written explicitly as

.. math::
   :label: eq.conv
	
   \frac{x(t)}{\clog} - \frac{\beta}{\clog} \int_0^t d\tp \, g(t-\tp) x(\tp) \; ,

where :math:`g(t) = {\cal L}^{-1} [G(s)]`.  Thus, the original differential equations describing :math:`x(\tau)` and :math:`I(\tau)` are transformed into integro-differential form.  For completeness, we note that the modified equation for the transducer motion is

.. math:: f(t) = \ddot{x} + \frac{\dot{x}}{\qms} + x - \beta \displaystyle \int_0^t d\tp \, g(t-\tp) x(\tp) \; .

where :math:`f = \clog \bl(x) I(t)` is a normalized force (with the same units as the displacement), and a dot denotes a time derivative, as in Sec.~1. The effect of viscoelasticity is reflected in the convolution integral above.  The integral samples the entire time history :math:`x(\tp)` for :math:`0 \leq \tp \leq t`, which reflects the memory effect inherent to viscoelastic materials.  The memory is controlled by the kernel :math:`g`; systems with weak memory will have :math:`g` that decays rapidly. With the proposed modified Weideman contour method, the inverse transform :math:`g(t)` can be computed to machine precision at any desired values of :math:`t`.  Sample plots of :math:`g(t)` for different values of :math:`\beta` are shown in :numref:`ft`. Finally, it is worth noting that in the limit :math:`\beta \rightarrow 0` we can carry out the inverse transform exactly according to

.. math:: g(t) \sim {\cal L}^{-1} \left[ \ln(1+s_0/s) \right] = \frac{1-e^{-s_0 t}}{t} \; .

The addition of the convolution to the time-domain formulation is analogous to the more formal state-space approach of King :cite:`king:2015` that focuses exclusively on a fractional derivative model of compliance.  In the case of fractional derivatives, however, the inverse transform :math:`g(t)` can be computed analytically, and the convolution written as a Riemann-Liouville fractional integral.

.. subfigure:: A
   :width: 50%
   :name: ft
   :align: center

   .. image:: images/time_paper/ft.png

   Convolution kernel function :math:`g(t) = {\cal L}^{-1} [G(s)]` of Eq. :eq:`eq.conv` as computed by the Weideman inversion method. Plots are shown for :math:`s_0=2` and four values of :math:`\beta`.

Summary of inversion method
---------------------------

In these notes we have outlined a modification to the Weideman method for numerical calculation of the inverse Laplace transform.  The modified method is suitable for calculating the time-domain loudspeaker response and can be implemented in only a few lines of code.  The complete algorithm is summarized by Eqs. :eq:`eq.trap`, :eq:`eq.m1`, :eq:`eq.m2` and :eq:`eq.m3`.  Importantly, it can be applied to nonstandard frequency-domain response functions containing branch cuts, as encountered in advanced transducer models with semi-inductance in the motor or viscoelasticity in the suspension. Alternatively, this method can be used as a simple and rapid method to compute the time-domain response for simple polynomial response functions.

Appendices
----------

Simplification of the Ritter 3PC compliance model
.................................................

In Eq. (13) of a paper by Ritter and Agerkvist :cite:`ritter:2010`, the viscoelastic compliance contains a logarithmic term that is expressed as

.. math:: \log_{10} \left[ \frac{i \omega \tau_\mathrm{min} e^{-i \beta}}{\sqrt{1+\omega^2\tau_\mathrm{min}^2}} \right] \; .

In this expression, :math:`\beta=\tan^{-1}(\tau_\mathrm{min} \omega)` is the phase angle. We remark that Ritter's :math:`\beta` is unrelated to :math:`\beta` in these notes.  By defining :math:`s_0 \doteq 1/\tau_\mathrm{min}`, setting :math:`s=i\omega`, and expanding the complex exponential, we can rewrite this as

.. math:: \log_{10} \left[ \frac{(s/s_0)}{\sqrt{1-s^2/s_0^2}} \left( \cos\beta - i \sin\beta\right) \right] \; .

Next, using the identities

.. math::
   \sin\beta = \frac{\omega/s_0}{\sqrt{1+\omega^2/s_0^2}} \; ,
   \quad
   \cos\beta = \frac{1}{\sqrt{1+\omega^2/s_0^2}} \; ,

which follow from :math:`\tan\beta = \omega/s_0`, we can write the argument as

.. math::
   \log_{10} \left[ \frac{(s/s_0) \left( 1-s/s_0 \right)}{1-s^2/s_0^2} \right] =
   \log_{10} \left( \frac{s}{s+s_0} \right) \; ,

which is the argument used in Eq. :eq:`eq.3pc`.

Sample Python code for inverse transform
........................................

The following Python code implements the algorithm of Eq. :eq:`eq.trap` as applied to the closed box response function of Eq. :eq:`eq.hp2`.

.. literalinclude:: example_code/weideman.py
   :linenos:
