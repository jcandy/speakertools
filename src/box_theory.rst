.. |dmn| mathmacro:: \Delta_{mn}
..{\ca}{C_\mathrm{A}}
.. |ma| mathmacro:: M_\mathrm{A}
..{\sd}{S_\mathrm{D}}
..{\ad}{a_\mathrm{D}}
..{\sdp}{S_\mathrm{P}}
..{\adp}{a_\mathrm{P}}
..{\sbx}{S_\mathrm{B}}
..{\caf}{C_\mathrm{af}}
..{\cth}{C_\mathrm{th}}
..{\cua}{C_\mathrm{ua}}
..{\raf}{R_\mathrm{af}}
..{\rth}{R_\mathrm{th}}
..{\cfu}{C^*_\mathrm{A}}
..{\rfu}{R^*_\mathrm{A}}
..{\ws}{\omega_s}
..{\ve}{\eta_v}

Speakerbench Box Theory
=======================

History of enclosure models
---------------------------

The standard theory of loudspeaker enclosures was popularized by Small, although the same essential theory was presented by Benson in much more detail in his series of articles *Theory and Design of Loudspeaker Enclosures* :cite:`benson:1993`

Acoustical impedances for unfilled box
--------------------------------------

In Eq. (7.131) of Beranek :cite:`beranek:2019`, the acoustical impedances for an unfilled enclosure are derived by solving the Helmholtz equation in an unfilled rectangular enclosure. Although Beranek attempts to treat the effect of back-wall lining, we consider infinite (rigid) back-wall impedance. To extract the effective compliance and mass, we expand :math:`Z_{pq}` in powers of :math:`s` to obtain

.. math::
   Z_{pq} \sim \frac{1}{s \ca } + s \ma \, \epsilon_{pq} \; .

Here, :math:`\epsilon_{pq}` is a dimensionless :math:`2\!\times\!2` array

.. math::
   :label: eq.eps
   \epsilon_{pq} = \frac{1}{3} + \frac{4}{\pi} \sum_{m,n} \gamma_{mn} \frac{\coth(\pi \dmn)}{\dmn}
  \cos\left(\theta_p\right) \cos\left(\theta_q\right) \frac{J_1\left(\beta_p \right)}{\beta_p}  \frac{J_1\left(\beta_q \right)}{\beta_q} \; ,

where in :eq:`eq.eps` we have defined

.. math::
  \theta_p = &~ \frac{n \pi y_p}{l_y} \\
  \beta_p = &~ \frac{\pi a_p}{l_z}\dmn \\
  \dmn^2 = &~ \left( \frac{m l_z}{l_x} \right)^2 + \left( \frac{n l_z}{l_y} \right)^2 . \\
  \gamma_{mn} = &~ 4-2 \left( \delta_{m0}+\delta_{n0} \right)


The index $p=1$ corresponds to the driver (subscript $D$) and $p=2$ corresponds to the port (subscript $P$). We have chosen simple normalizing acoustic compliance and mass,
%
\begin{align}
  \ca = &~ \frac{V}{\rho c^2} = C_\mathrm{MB} \sd^2 \; , \\
  \ma = &~ \frac{\rho l_z}{\sbx} \; , 
\end{align}
%
where $\sbx = l_x l_y$ is the baffle area, $l_z$ is the enclosure depth, $\sd = \pi \ad^2$ is the driver area, and $V= l_z l_y l_z$ is the enclosure volume. The circuit diagram for a low-frequency T-network system for an undamped vented box (box connected to a tube) is illustrated in Fig.~\ref{fig.genbox}.
%
\newcommand\com[1]{\textcolor{red}{#1}}
\begin{figure}[H]
  \centering
  \includegraphics{box_port_lf.pdf}
  \label{fig.genbox}
  \caption{Circuit diagram for low-frequency unfilled box (BOX) connected to transmission-line tube (PORT), which radiates into free air. \com{NOTE: need to update port for arbitrary freq, add radiation resistance}.}
\end{figure}

\subsection*{Connection to Beranek factor}

\noindent
The Beranek factor $B$ is related to the piston self-interaction coefficient $\epsilon_{11}$ and defines the acoustic mass $M$ when the port is blocked:
%
\begin{equation}
  M_{11} \doteq \epsilon_{11} \ma =  \frac{B \rho}{\pi\ad} \; .
\end{equation}
%
Thus, we can define $B$ in terms of $\epsilon_{11}$ as
%
\begin{equation}
  B = \pi \epsilon_{11} \frac{l_z \ad}{l_x l_y} \; .
\end{equation}

\subsection*{End correction due to box mass}

The interior of the box provides an end correction to the port mass. In the case where the port is \textit{external} to the box (internal flange), the exterior end correction is the usual unflanged value
%
\begin{equation}
  \Delta l_\mathrm{port} = 0.6 \, \adp
\end{equation}
%
whereas the internal correction is
%
\begin{equation}
  \Delta l_\mathrm{port} = \frac{\epsilon_{22}-\epsilon_{21}}{l_x l_y} \, l_x \sdp
\end{equation}

\section{Treatment of absorption}

To incorporate box absorption, we consider the parallel circuit treated by Futtrup \cite{futtrup:2011} based on the earlier work by Leach \cite{leach:1989}
%
\begin{figure}
  \centering
  \includegraphics[width=6in]{q_futtrup.png}
  \caption{Reproduction of Fig.~3 from \cite{futtrup:2011}.}
\end{figure}
%
To extract the essential acoustic compliance and resistance of this circuit, we short the masses and take $R_\mathrm{mf} \gg R_\mathrm{af}$. By Taylor-expanding the impedance, we can calculate the series combination of compliance $\cfu$ and resistance $\rfu$ as
%
\begin{align}
  \cfu =&~ \caf + \cth + \cua
  \label{eq.cfu} \\
  \rfu =&~ \raf \left(\frac{\caf+\cth}{\cfu}\right)^2 + \rth \left(\frac{\cth}{\cfu} \right)^2
  \label{eq.rfu}
\end{align}
%
These results suggest that we can describe the effect of fill with two empirical parameters: $Q_a$ and $\ve$. $Q_a$ is an analog of the box absorption of the classical Benson/Small theory, and $\ve$ is an effective volume expansion coefficient which should lie in the range $1.0 < \ve < 1.4$. The precise definitions are
%
\begin{align}
  \ve \doteq &~ \frac{\cfu}{\ca} \; , \\
  Q_a \doteq &~ \frac{1}{\ws \ca \rfu} \; .
\end{align}
%
Thus we can generalize the classic theory with only a single new added parameter, $\ve$, which characterizes the volume expansion due the conversion from adiabatic to isothermal expansion. The Futtrup theory provides estimates for $\ve$ and $Q_a$ for different materials and fill percentages, as illustrated in Fig.~\ref{fig.qgamma}. Further, in Fig.~\ref{fig.qg2}, we compare the predicted relationship of $Q_a$ versus $\ve$ against experimental measurement in a real filled box.
%
%\begin{figure}
%  \centering
%  \includegraphics[width=4.5in]{qgamma.pdf}
%  \caption{Effective $Q_a$ and $\ve$ for fill inside an MCM test box.}
%  \label{fig.qgamma}
%\end{figure}
%\begin{figure}
%  \centering
%  \includegraphics[width=4.5in]{qg2.pdf}
%  \caption{Effective $Q_a$ versus $\ve$ compared with experimental data.}
%  \label{fig.qg2}
%\end{figure}
%
%\begin{figure}
%  \centering
%  \includegraphics{box_port_q.pdf}
%  \caption{Box model incorporating fill. $\cfu$ and $\rfu$ are defined in Eqs.~\ref{eq.cfu} and %\ref{eq.rfu}. In terms of dimensionless model input parameters, $\rfu$ is controlled by $Q_a$ and $\cfu$ %is controlled by $ve$.}
%  \label{fig.boxq}
%\end{figure}
