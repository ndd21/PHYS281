---
title: Gravitational simulation
authors:
    - Iain Bertram
    - Matthew Pitkin
    - Brooke Simmons
    - Neil Drummond
date: 2025-12-07
---

# Gravitational simulation

The [final project](#project-description) for PHYS281 involves writing
a Python program to simulate the motion of several "particles" (or
"bodies") under the mutual influence of their gravitational fields.
You will then use your program to perform gravitational simulations
and write up your findings in a report.

To understand what is involved in a gravitational simulation, let's
start by considering various scenarios of increasing complexity in
which one or more particles move under the influence of gravity.

## Particle in a uniform gravitational field

First, suppose we wish to simulate the motion of a particle in a
cannonball-like trajectory close to the surface of the Earth. In this
case we can approximate the acceleration by

$$
  \vec{a} = -g\hat{j} \approx -9.81 \hat{j} ~ \mathrm{m} \, \mathrm{s}^{-2},
$$

where $\hat{j}$ is a unit vector in the vertically upwards direction.

To characterise the motion of the particle in this uniform
gravitational field we need to calculate the particle's position
$\vec{r}=(x,y,z)$ and velocity $\vec{v}=(v_x,v_y,v_z)$ as functions of
time $t$.

The velocity of the particle is

$$
\vec{v} = \frac{\mathrm{d}\vec{r}}{\mathrm{d}t}
$$

and the acceleration of the particle is

$$
\vec{a} = \frac{\mathrm{d}\vec{v}}{\mathrm{d}t}.
$$

In general Newton's second law of motion gives us an expression for
the acceleration $\vec{a}$ of the particle, so that we can regard the
two equations above as coupled first-order ordinary differential
equations.

In this simple example the acceleration is constant and we can of
course just solve the equations analytically by integration. The
familiar expressions for the solution are

$$
\begin{align}
  \vec{v} & =  \vec{v}_{0} + \vec{a} t \\
  \vec{r} & =  \vec{r}_{0} + \vec{v}_{0} t + \frac{1}{2} \vec{a} t^{2},
\end{align}
$$

where the initial position and velocity at time $t=0$ are
$\vec{r}_{0}$ and $\vec{v}_{0}$, respectively. As long as the
acceleration $\vec{a}$ is constant and uniform, these equations will
be accurate.

Nevertheless, we would like to develop ways of finding numerical
solutions to the equations of motion, so that we can move on to tackle
the more general case in which the acceleration varies in time or
depends on the position or velocity of the particle, and analytical
solutions are not available. The simplest numerical approach for
solving the equations of motion is known as the [Euler
method](https://en.wikipedia.org/wiki/Euler_method) (or Euler forward
method). It is an iterative algorithm that allows us to calculate the
approximate position and velocity of a particle at time $t+\Delta{t}$
if we know the position and velocity at the slightly earlier time
$t$. The iteration scheme has the form

$$
\begin{align}
  \vec{r}_{n+1} & \approx \vec{r}_n + \vec{v}_n \Delta t \\
  \vec{v}_{n+1} & \approx \vec{v}_n + \vec{a}_n \Delta t,
\end{align}
$$

where the subscript $n$ denotes the $n$th iteration. $\vec{r}_0$ and
$\vec{v}_0$ are the initial position and velocity of the particle at
time $t=0$.  The small time interval $\Delta t$ is often referred to
as the "time step" (although the phrase "$n$th time step" refers to
the $n$th iteration, which gives us the approximate state of the
system at time $t_n=n\Delta t$).  The update equations of the Euler
method are actually just the first couple of terms of the Taylor
series expansions of the position and velocity, and hence we expect
that an error of order $\Delta t^2$ will be introduced at each
iteration, so that the cumulative error over a fixed time period will
be of order $\Delta t$. Alternative algorithms will be discussed later
on, but for now the Euler method will suffice.

## Particle in a nonuniform gravitational field

If we want to consider a more complicated case of motion in the
Earth's gravitational field then we can take into account the
variation of gravitational acceleration with distance $r=|\vec{r}|$
from the Earth's centre using the expression

$$
\vec{a} = -\frac{G M_\mathrm{E}}{r^2} \hat{r} = -\frac{G M_\mathrm{E}}{r^3} \vec{r}
$$

for values of $r$ greater than the Earth's radius $R_\mathrm{E}=
6380\,\mathrm{km}$. The mass of the Earth is $M_\mathrm{E} \approx
5.974\!\times\!10^{24}\,\mathrm{kg}$ and $G \approx 6.6743 \times
10^{-11}\,\mathrm{m}^3\,\mathrm{kg}^{-1}\,\mathrm{s}^{-2}$ is the
gravitational constant. $\hat{r}=\vec{r}/r$ is a unit vector in the
radial direction. We have taken the origin to lie at the centre of the
Earth and we have assumed that the Earth is a uniform sphere.

Solving for the motion of the particle analytically is much more
challenging than in the previously considered case of a uniform
gravitational field; however, performing a simulation of the motion of
the particle is hardly any more difficult than it was before.  We
simply need to compute the acceleration of the particle as $\vec{a} =
-\frac{G M_\mathrm{E}}{r^3} \vec{r}$ at each iteration, and then
continue to use e.g. the Euler method to update the position and
velocity.

One familiar analytical result for motion in this gravitational field
is the case of circular motion, which can be obtained by setting the
gravitational acceleration of the particle equal to its centripetal
acceleration.  Circular motion provides a good test case for examining
the accuracy of a numerical simulation of motion under gravity. You
are probably aware of the more general analytical result for the
orbital motion of a satellite about the Earth: the trajectory is an
ellipse, with the centre of the Earth lying at a focus of the ellipse.

Next we consider an important problem that cannot be solved
analytically.

## Multiple particles interacting via gravity (e.g., the major bodies in the Solar System)

Consider the case of $N$ massive particles moving under the influence
of each other's gravity. In this section, the subscript $i$ on
position $\vec{r}_i=(x_i,y_i,z_i)$, velocity
$\vec{v}_i=({v_x}_i,{v_y}_i,{v_z}_i)$ and acceleration
$\vec{a}_i=({a_x}_i,{a_y}_i,{a_z}_i)$ indicates that we are referring
to the $i$th particle.  The net acceleration of particle $i$ with mass
$m_i$ is

$$
\vec{a}_i = \sum^{N}_{j\neq i}{\frac{-Gm_j}{|\vec{r}_{ij}|^2} \hat{r}_{ij}} = -G \sum^{N}_{j\neq i}{\frac{m_j}{|\vec{r}_{ij}|^3} \vec{r}_{ij}},
$$

where $\vec{r}_{ij}=\vec{r}_i-\vec{r}_j$ is the displacement vector
from the $j^{\mathrm{th}}$ mass to the $i^{\mathrm{th}}$ mass. In this
case, to determine the acceleration of a given particle, we need to
know the locations of all the other particles in the simulation. Note
that the sum of all forces acting on all particles should be zero at
all times due to Newton's third law in the absence of an external
field. If we move one particle before calculating the force due to that
particle on all the other particles in the simulation then (unless
great care is taken) the program will violate Newton's third law and
hence conservation laws will be broken.

## Different methods of simulating kinematics

Regardless of the details of your final project you are going to need
to have a way of approximating the motion of your system.  Earlier, we
stated Euler's method for updating the position and velocity of a
single particle; here we generalise this method to the motion of $N$
particles by introducing a $3N$-dimensional vector of all the particle
positions, $\vec{R}=(x_1,y_1,z_1,x_2,y_2,z_2,\ldots,x_N,y_N,z_N)$,
along with the corresponding $3N$-dimensional vectors of all particle
velocities
$\vec{V}=({v_x}_1,{v_y}_1,{v_z}_1,\ldots,{v_x}_N,{v_y}_N,{v_z}_N)$ and
accelerations
$\vec{A}=({a_x}_1,{a_y}_1,{a_z}_1,\ldots,{a_x}_N,{a_y}_N,{a_z}_N)$.
For a small time interval $\Delta t$, the change in accelerations is
small and the changes in positions and velocities between the $n$th
time step and the $(n+1)$th time step are approximately given by
Euler's method:

$$
\begin{align}
  \vec{R}_{n+1} & \approx \vec{R}_n + \vec{V}_n \Delta{t} \\
  \vec{V}_{n+1} & \approx \vec{V}_n + \vec{A}_n \Delta{t}.
\end{align}
$$

As stated above, this is based on a Taylor expansion of the positions
and velocities:

$$
\begin{align}
\vec{R}_{n+1} & = \vec{R}_n + \vec{V}_n \Delta{t} + \mathcal{O}\left( \Delta t^2\right) \\
\vec{V}_{n+1} & = \vec{V}_n + \vec{A}_n \Delta{t} + \mathcal{O}\left( \Delta t^2\right),
\end{align}
$$

where $\mathcal{O}\left(\Delta t^2\right)$ signifies contributions
proportional to $\Delta t^2$.  If $\Delta t$ is small enough then
these higher-order contributions can be ignored. The error in any
given step is given by the truncation of the Taylor expansion, and for
Euler's method is of order $\Delta t^2$. These errors accumulate each
time the iteration scheme is applied, and hence the error in a
simulation of fixed duration $T$ is of order $\Delta t$ (because the
cumulative error is proportional to $N_\text{steps} \Delta t^2$ for
$N_\text{steps}$ iterations, but the total duration of the simulation
is $T=N_\text{steps} \Delta t$, so the cumulative error for fixed $T$
is proportional to $T \Delta t$). In the following paragraphs other
algorithms are very briefly introduced. *The errors in these
algorithms are not discussed here, but an investigation of the errors
could form a part of your project.*

As well as not being very accurate, for oscillatory systems the Euler
method can be unstable. An alternative method called the
[*Euler-Cromer*
method](https://en.wikipedia.org/wiki/Semi-implicit_Euler_method) (or
semi-implicit Euler method) uses the velocities at the _end_ of the
step rather than the beginning of the step, and should give more
stable results.  The Euler-Cromer update scheme is

$$
\begin{align}
\vec{V}_{n+1} & \approx \vec{V}_n + \vec{A}_n \Delta{t} \\
\vec{R}_{n+1} & \approx \vec{R}_n + \vec{V}_{n+1} \Delta{t}.
\end{align}
$$

An obvious improvement to the Euler and Euler-Cromer methods would be
to compute the velocities and accelerations in the _middle_ of the
interval $\Delta t$. This suggests a method called the *midpoint*
algorithm. The algorithm involves the use of the Euler method to
estimate the midpoint positions $\vec{X}_\text{mid}$ and velocities
$\vec{V}_\text{mid}$ at time $t_\text{mid} = t + \Delta t/2$. The
forces and accelerations are then computed at this midpoint:

$$
\begin{align}
  \forall i\in\{1\ldots N\}, \qquad \vec{a}_{in} & = \vec{F}_i\left( \vec{R}_n, \vec{V}_n, t_n \right)/m_i \\
  \vec{V}_{\mathrm{mid}} & \approx \vec{V}_n + \frac{1}{2}\vec{A}_n \Delta{t}\\
  \vec{R}_{\mathrm{mid}} & \approx \vec{R}_n + \frac{1}{2}\vec{V}_n \Delta{t}\\
  \forall i\in\{1\ldots N\}, \qquad \vec{a}_{i,\mathrm{mid}} & \approx \vec{F}_i\left(\vec{R}_{\mathrm{mid}}, \vec{V}_{\mathrm{mid}}, t_n+\frac{1}{2}\Delta{t} \right)/m_i,
\end{align}
$$

where $\vec{F}_i\left( \vec{R}, \vec{V}, t \right)$ is the force on
particle $i$ at time $t$ when the particle positions and velocities
are $\vec{R}$ and $\vec{V}$, respectively.  We can then update the
positions and velocities as

$$
\begin{align}
    \vec{V}_{n+1} & \approx \vec{V}_n + \vec{A}_{\mathrm{mid}} \Delta{t} \\
    \vec{R}_{n+1} & \approx \vec{R}_n + \vec{V}_{\mathrm{mid}} \Delta{t}.
\end{align}
$$

Finally we examine a widely used alternative known as the [*velocity
Verlet* algorithm](https://en.wikipedia.org/wiki/Verlet_integration),
which looks similar to the familiar equations of motion for constant
acceleration, but uses the average of the accelerations at the start
and end of the step to calculate the updated velocity.  The Verlet
scheme is

$$
\begin{align}
\vec{R}_{n+1} & \approx \vec{R}_n + \vec{V}_n
\Delta{t} + \frac{1}{2}\vec{A}_n \Delta t^2 \\
  \vec{V}_{n+1} & \approx \vec{V}_n + \frac{1}{2} \left( \vec{A}_{n+1} + \vec{A}_n \right)  \Delta{t}.
\end{align}
$$

Clearly we need some way of estimating $\vec{A}_{n+1}$. If the
accelerations only depend on positions, we can evaluate
$\vec{A}_{n+1}$ as soon as we have updated the positions to
$\vec{R}_{n+1}$.  For velocity-dependent forces, $\vec{A}_{n+1}$ can
be approximated by first stepping forwards using any of the algorithms
mentioned above, calculating the accelerations, and then applying the
Verlet update scheme.

Beyond these algorithms one can also consider higher-order methods
such as the well-known
[Runge-Kutta](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods)
schemes, which are very widely used in physics simulations.

## Assessing the accuracy of a simulation

As in the case of [numerical integration](numerical-integration.md),
most physics simulations require approximations, which introduce
errors (i.e., inaccuracies) into the results. There are various ways
to investigate the sizes of these errors:

- Apply the simulation program to a system for which there is an
  analytical solution to the equations of motion, so that the
  predictions of the simulation can be directly tested against the
  exact results. This approach has the advantage of allowing one to
  calculate unambiguously the errors due to numerical
  approximations. However, it does not guarantee that the errors will
  be the same when the simulation program is applied to a situation
  for which there is not an analytical solution.

- Apply the simulation program to a system for which there are
  experimental or observational data, so that the predictions of the
  simulation can be directly tested against reality. This is
  ultimately what physics is all about, and hence is a good
  approach. However, experimental data often contain many additional
  subtle effects which may not be included in the simulation, so it is
  not always easy to understand where any discrepancies come from:
  e.g., do the discrepancies arise due to missing physics or the
  omission of particles from the simulation, or due to numerical
  approximations in the simulation?  Furthermore, experimental results
  themselves are not always free of errors or misinterpretations.

- Compare the predictions of different numerical simulation
  algorithms, or the predictions of the same algorithm with different
  simulation parameters (e.g., time steps), to see if the results
  are consistent.  Making such comparisons is an essential aspect of
  developing and improving simulation methods.  However, great care is
  needed when drawing conclusions from such comparisons.  It is not
  always clear which (if any) of the simulation results should be
  regarded as being reliable.

- For a range of systems, investigate whether the simulation conserves
  quantities that ought to be conserved, e.g., total energy, or total
  linear momentum, or total angular momentum. Although conservation of
  energy etc. does not guarantee that the details of the simulation
  are accurate, it provides a quick global check of the simulation's
  performance.

You will need to think carefully how to use these approaches to assess
the accuracy of your simulations.

## Project description

The aims of this project are: to write a Python program to simulate
the motion of massive bodies interacting via gravitational forces; to
test the accuracy and reliability of your simulation program; to use
your program to generate some scientifically interesting results; and
to write up your findings in a report.

You are free to develop your simulation program however you wish, but
the two predefined exercises (Final Project Parts 1 and 2 on MOODLE)
provide a good starting point (e.g., the `Particle` class), which can
be expanded and adapted into a more fully formed simulation code.  It
may be helpful to build up your simulation program in stages of
increasing complexity:

1. write a program that simulates a pair of massive particles
interacting with each other in two or three dimensions (e.g., Earth
and an artificial satellite, as in the exercises on MOODLE);

2. expand this into a program that simulates a set of three massive
particles interacting in three dimensions (e.g., the Sun, Earth and
Jupiter);

3. generalise this to a program that can be used to simulate many
interacting massive particles in three dimensions (e.g., all the major
bodies of the Solar System).

To evolve the positions and velocities of the particles in time the
Euler, Euler-Cromer and/or other numerical approximation methods
should be used.

Your program should include code for testing that the simulation works
and code for testing the accuracy of the results produced. For
example, you could include code for simulating simple cases and
comparing the results with analytical solutions, or code for
calculating properties such as orbit periods that can easily be
compared with observed results. It is important to check that the
simulation conserves the **total** energy, linear momentum and angular
momentum to an acceptable level. The results of your tests should be
presented in your report.  Your tests should compare different
numerical approximation methods and consider the effects of changing
the time step.

Your simulation can include additional physics or simulate
gravitational systems other than the Solar System as long as you can
provide justifiable tests of the validity of your program.  However,
if you want to simulate something much more challenging, it might be
advisable to discuss your proposed project with the lecturer.

Please note that PHYS281 is an open-ended project. By completing the
exercises on MOODLE you have been equipped with basic tools (the Euler
and Euler-Cromer methods) for simulating the motion of two bodies
subject to gravitational attraction; it is then up to you to take
these tools, generalise and improve them, and decide what aspects of
gravitational simulation you would like to focus on and what questions
you would like to ask.  E.g.: What sort of accuracy can be achieved
over what sort of time scale in simulations of the Solar System using
different methods?  How sensitive is the motion of a few-body
gravitational system to the choice of initial conditions?  Can you
calculate the trajectory of a space probe?  What happens to the Solar
System if another star passes close by?  How do the shapes and
orientations of planetary orbits change over time?  Better still,
invent your own question(s) that can be answered using your simulation
program!

For more information and advice on the code and report, including
guideline marking grids, please read the [Marking criteria
page](markinggrid.md).

## Solar System ephemerides

### JPL Horizons

If you are simulating the Solar System you may want to use a set of
accurate values to initialise the positions and velocities of the
Solar System bodies (known as an *ephemeris*; plural:
*ephemerides*). You can get ephemerides from the online JPL Horizons
page at
[https://ssd.jpl.nasa.gov/horizons.cgi](https://ssd.jpl.nasa.gov/horizons.cgi).
You will initially see the following settings:

<div style="font-family:monospace;"}>
&nbsp;&nbsp;&nbsp;Ephemeris Type [change]: <b>OBSERVER</b></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Target Body [change]: <b>Mars</b> [499]</br>
Observer Location [change]: 	<b>Geocentric</b> [500]</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Time Span [change]: 	Start=<b>2020-10-28</b>, Stop=<b>2020-11-27</b>, Step=<b>1 d</b></br>
&nbsp;&nbsp;&nbsp;Table Settings [change]: defaults</br>
&nbsp;&nbsp;&nbsp;Display/Output [change]: default (formatted HTML)</br>
</div>

To get a Solar System body's initial conditions you should do the
following:

* For "Ephemeris Type" click on "change", select "Vector Table" and
  click on the "Use Selection Above" button.

* To change the "Target Body" click on "change" and search for the
  body that you want. Note that you can treat the Earth-Moon system as
  one particle by selecting "Earth-Moon Barycenter".  (N.b.,
  "Barycentre" just means "centre of mass".)

* For "Coordinate Origin" (which will appear when you switch to the
  "Vector Table" above) leave it as "**Solar System Barycenter**
  (**SSB**) [500@0]". This is the centre of mass of the entire Solar
  System.

* For "Time Span" you can either leave it as it is, in which case it
  will default to today, or click on "change" to specify a start date,
  end date and time step between outputs. Make sure to use the same
  start time for all the bodies in your simulation.

* For "Table Settings" click on "change", then in the "Select vector
  table output" drop-down menu select "Type 2 (state vector
  {x,y,z,vx,vy,vz})". This means the ephemeris will return the 3D
  position and velocity coordinates of the selected body. In "Optional
  vector-table settings:" select the "output units" you require from
  the options; "km & km/s" is recommended.

* For "Display/Output" you can either leave this as the default, which
  will show the information on a formatted HTML webpage, or select to
  download it as a text file.

If you had selected Venus as the body you would have got the following
information on the webpage:

<table border="1" cellpadding="8" cellspacing="0" bgcolor="#EEEEEE">
<tr>
<td align="left" nowrap>
<pre> Revised: July 31, 2013                 Venus                           299 / 2
 
 PHYSICAL DATA (updated 2020-Oct-19):
  Vol. Mean Radius (km) =  6051.84+-0.01 Density (g/cm^3)      =  5.204
  Mass x10^23 (kg)      =    48.685      Volume (x10^10 km^3)  = 92.843
  Sidereal rot. period  =   243.018484 d Sid. Rot. Rate (rad/s)= -0.00000029924
  Mean solar day        =   116.7490 d   Equ. gravity  m/s^2   =  8.870
  Mom. of Inertia       =     0.33       Core radius (km)      = ~3200
  Geometric Albedo      =     0.65       Potential Love # k2   = ~0.25
  GM (km^3/s^2)         = 324858.592     Equatorial Radius, Re = 6051.893 km
  GM 1-sigma (km^3/s^2) =    +-0.006     Mass ratio (Sun/Venus)= 408523.72
  Atmos. pressure (bar) =  90            Max. angular diam.    =   60.2"
  Mean Temperature (K)  = 735            Visual mag. V(1,0)    =   -4.40
  Obliquity to orbit    = 177.3 deg      Hill's sphere rad.,Rp =  167.1
  Sidereal orb. per., y =   0.61519726   Orbit speed, km/s     =   35.021
  Sidereal orb. per., d = 224.70079922   Escape speed, km/s    =   10.361
                                 Perihelion  Aphelion    Mean
  Solar Constant (W/m^2)         2759         2614       2650
  Maximum Planetary IR (W/m^2)    153         153         153
  Minimum Planetary IR (W/m^2)    153         153         153
</pre>
</td></tr>
</table>

This provides you with the mass of the planet (note that the value of
`GM`, which is the gravitational constant multiplied by the mass, is
known more accurately that the mass alone).

This will be followed by:

<table border="1" cellpadding="8" cellspacing="0" bgcolor="#EEEEEE">
<tr>
<td align="left" nowrap>
<pre> 
 
*******************************************************************************
Ephemeris / WWW_USER Wed Oct 28 03:36:54 2020 Pasadena, USA      / Horizons
*******************************************************************************
Target body name: Venus (299)                     {source: DE431mx}
Center body name: Solar System Barycenter (0)     {source: DE431mx}
Center-site name: BODY CENTER
*******************************************************************************
Start time      : A.D. 2020-Oct-28 00:00:00.0000 TDB
Stop  time      : A.D. 2020-Nov-27 00:00:00.0000 TDB
Step-size       : 1440 minutes
*******************************************************************************
Center geodetic : 0.00000000,0.00000000,0.0000000 {E-lon(deg),Lat(deg),Alt(km)}
Center cylindric: 0.00000000,0.00000000,0.0000000 {E-lon(deg),Dxy(km),Dz(km)}
Center radii    : (undefined)                                                  
Output units    : KM-S
Output type     : GEOMETRIC cartesian states
Output format   : 2 (position and velocity)
Reference frame : Ecliptic of J2000.0
*******************************************************************************
JDTDB
   X     Y     Z
   VX    VY    VZ
*******************************************************************************
$$SOE
2459150.500000000 = A.D. 2020-Oct-28 00:00:00.0000 TDB 
 X =-6.534481694069970E+07 Y = 8.684311014650232E+07 Z = 4.909705470917884E+06
 VX=-2.815084272627433E+01 VY=-2.121345485459670E+01 VZ= 1.333142304405859E+00
2459151.500000000 = A.D. 2020-Oct-29 00:00:00.0000 TDB 
 X =-6.775102432791176E+07 Y = 8.497624142281163E+07 Z = 5.022920220211159E+06
 VX=-2.754469579780248E+01 VY=-2.199823147018513E+01 VZ= 1.287394944661386E+00
...
</pre>
</table>

After the header information, each line gives a date and time, first
as a [Julian Date](https://en.wikipedia.org/wiki/Julian_day), then in
a more familiar format, followed by the X, Y and Z positions, and then
the VX, VY and VZ velocity components.

You will need to do this for each particle that you want to include in
your simulation.

If referencing the JPL Horizons webpage in your report you can use the
following citation:

> J. D. Giorgini *et al.*, *JPL's On-Line Solar System Ephemeris and Data
Service*, Bull. Am. Astron. Soc. **28**, 1099 (1997).

or BibTeX entry:

```latex
@INPROCEEDINGS{1997BAAS...29.1099G,
       author = { {Giorgini}, J.~D. and {Yeomans}, D.~K. and {Chamberlin}, A.~B. and
         {Chodas}, P.~W. and {Jacobson}, R.~A. and {Keesey}, M.~S. and
         {Lieske}, J.~H. and {Ostro}, S.~J. and {Standish}, E.~M. and
         {Wimberly}, R.~N.},
        title = "{JPL's On-Line Solar System Ephemeris and Data Service}",
    booktitle = {Bull. Am. Astron. Soc.},
         year = {1997},
       volume = {28},
        month = September,
        pages = {1099},
       adsurl = {https://ui.adsabs.harvard.edu/abs/1997BAAS...29.1099G},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

### Solar System ephemerides using Python

There are Python packages that you can use to download JPL ephemerides
of the Solar System bodies automatically rather than going through the
[JPL Horizons](https://ssd.jpl.nasa.gov/horizons.cgi) website.

To do this you will first need to install several packages. If you are
using Anaconda, the [astropy](https://www.astropy.org/) package should
already be installed, but if not you can install it via the _Anaconda
Navigator_. After opening _Anaconda Navigator_, in the left-hand
border panel click on "Environments". In the panel containing the
search box with "Search Environments" make sure you have selected the
"base (root)" environment (this is the environment that VS Code uses
by default). In the furthest right panel, click on the dropdown menu
containing "Installed" and select "All" to see available
packages. Then in the "Search Packages" box type "astropy".
[astropy](https://www.astropy.org/) should be listed as an installable
package, so click on the check box next to it and click on "Apply" in
the bottom right-hand corner. This should install astropy (it may take
a minute or two).

The following additional packages are required, but are not currently
available through the _Anaconda Navigator_:

* [jplephem](https://github.com/brandon-rhodes/python-jplephem)

* [spiceypy](https://spiceypy.readthedocs.io/en/master/)

* [poliastro](https://docs.poliastro.space/en/stable/)

However, these can be installed within a terminal. Open the _Anaconda
Powershell Prompt_ (either via the _Anaconda Navigator_ or within _VS
Code_) and type:

```bash
pip install jplephem spiceypy
pip install https://github.com/poliastro/poliastro/archive/main.zip
```

First you need to set the time at which you wish to generate the Solar
System ephemeris. To do this, you need to use an
[`astropy.time.Time`](https://docs.astropy.org/en/stable/api/astropy.time.Time.html#astropy.time.Time)
object:

```python
from astropy.time import Time

# Get the time at 5pm on 27th Nov 2019.
t = Time("2019-11-27 17:00:00.0", scale="tdb")
```

To get the positions and velocities of a given Solar System body you
need to use the astropy
[`get_body_barycentric_posvel`](https://docs.astropy.org/en/stable/api/astropy.coordinates.get_body_barycentric_posvel.html#astropy.coordinates.get_body_barycentric_posvel)
function, passing it the time and the name of the body you wish to
use:

```python
from astropy.coordinates import get_body_barycentric_posvel

# Get position and velocity of the Sun.
pos, vel = get_body_barycentric_posvel("sun", t, ephemeris="jpl")
```

The first time you run this it will download a large ephemeris
file. Subsequently, the file will not need to be re-downloaded as it
should be locally cached. This file contains the positions and
velocities of the Sun and planets (including the Moon and Pluto), but
not any other Solar System bodies.

The valid body names that you can pass to
 `get_body_barycentric_posvel` are: 'sun', 'mercury', 'venus',
 'earth-moon-barycenter', 'earth', 'moon', 'mars', 'jupiter',
 'saturn', 'uranus', 'neptune', 'pluto', ...

The positions and velocities are by default returned in [equatorial
coordinates](https://en.wikipedia.org/wiki/Equatorial_coordinate_system),
but a more useful representation (and that given by default in JPL
Horizons) is in the [ecliptic
coordinate](https://en.wikipedia.org/wiki/Ecliptic_coordinate_system)
frame. To convert to this frame you can use functions from spiceypy:

```python
from spiceypy import sxform, mxvg

# Make a "state vector" of positions and velocities (in metres and metres/second, respectively).
statevec = [
    pos.xyz[0].to("m").value,
    pos.xyz[1].to("m").value,
    pos.xyz[2].to("m").value,
    vel.xyz[0].to("m/s").value,
    vel.xyz[1].to("m/s").value,
    vel.xyz[2].to("m/s").value,
]

# Get transformation matrix to the ecliptic (use time in Julian Days).
trans = sxform("J2000", "ECLIPJ2000", t.jd)

# Transform state vector to ecliptic.
statevececl = mxvg(trans, statevec)

# Get positions and velocities.
position = [statevececl[0], statevececl[1], statevececl[2]]
velocity = [statevececl[3], statevececl[4], statevececl[5]]
```

You can get planetary masses by using the poliastro package:

```python
from poliastro import constants
from astropy.constants import G  # Newton's gravitational constant

# Sun mass (converting to kg).
msun = (constants.GM_sun / G).value

# Earth mass.
mearth = (constants.GM_earth / G).value 
```

Finally, you can use these to create a `Particle` (or equivalent)
object.

If using astropy the appropriate citations for your report are given
[here](https://www.astropy.org/acknowledging.html#acknowledging-or-citing-astropy). For
the [jplephem](https://github.com/brandon-rhodes/python-jplephem),
[poliastro](https://docs.poliastro.space/en/stable/index.html) and
[spiceypy](https://spiceypy.readthedocs.io/en/master/index.html)
packages you can cite their associated webpages.

### Moons

Suppose you wanted the positions and velocities of Jupiter's
moons. You could download the appropriate ephemeris file and get them
as follows:

```python
# URL of a file containing Jupiter ephemeris - this is a 1.2 Gb file!
# The version number (365) is OK in November 2023.  Might need updating in future years.
JUPEPH = "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/jup365.bsp"  

# Get Io (see https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/aa_summaries.txt for kernel numbers).
body = [(0, 5), (5, 501)]  # kernel chain going from SSB->Jupiter barycentre then Jupiter barycentre -> Io

pos, vel = get_body_barycentric_posvel(body, t, ephemeris=JUPEPH)
```

You can search for ephemeris files of other Solar System bodies
(comets, asteroids, moons of the outer planets) at the webpage
[here](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/).

## Frequently asked questions

Here is a selection of common questions, issues and things to check.

> Do I need to produce an animation showing planets orbiting the Sun?

No.  You need to produce informative results and graphs that can go in
your report.  Plotting trajectories on a graph can be an excellent way
of visualising the predictions of your simulation program, but
animations will not work in a report.

> The particles in my simulation fly apart or rush together. Why?

There are a few things to check if your simulation is "exploding" or
"imploding":

* Check that your acceleration vectors point in the correct direction:
  the contribution to the acceleration of body A due to body B should
  be *towards* body B.  If this is the other way round then you are
  simulating anti-gravity!

* Check that your initial conditions (positions and velocities) and
  masses are in consistent units and also are consistent with the
  units of your value of the gravitational constant. E.g., if your
  velocities are in $\text{km}\,\text{hr}^{-1}$, but $G$ is in
  $\text{N}\,\text{m}^2\,\text{kg}^{-2}$ your simulation will not
  produce correct results.

* Check all your initial conditions. Have you remembered to include
  the Sun!?

> The Sun is making cycloids (semi-circles). Why?

This is expected: the Sun is not fixed and is pulled about the
planets.  If there is also a net drift in the Sun's position then you
may want to work with coordinates referenced to the Solar System
barycentre.

> My simulation isn't very stable, and the planets seem to wander
  off. Why?

There are a few things to check in this case:

* Check your initial conditions. Do you use consistent units for all
  planets? Could you have made copy-paste errors for some planets?

* Check your simulation time-step values. If your time step is too
  large then the simulated trajectories will rapidly accumulate errors
  and the planets may drift out of orbit. You can study this as part
  of your project!

* Check that your algorithms respect Newton's third law.

> Momentum doesn't appear to be conserved. Why not?

Check that you are calculating the correct thing. You need to
calculate the total linear momentum of all particles, but you must sum
their individual linear momentum **vectors** before taking the
magnitude, rather than summing their individual magnitudes.

Similar comments apply in the case of the total angular momentum.

> My simulation program is completely broken. Help!

To debug your program it is often helpful to do the following:

1. Read through your code and make sure you understand what each line
  is supposed to be doing.

2. Try to find the simplest case in which your program fails (e.g.,
  the smallest number of bodies and the smallest number of steps).
  This will make it quicker to run tests and make the output less
  complicated when you are searching for the bug.

3. Insert `print` statements to see whether variables and arrays hold
   the values that you expect them to hold at each stage of the
   calculation.  For larger projects in the future, it may be helpful
   to learn how to use a debugger such as
   [pdb](https://docs.python.org/3/library/pdb.html); however, given
   the timescale of the PHYS281 project, it is probably easiest just
   to insert `print` statements in your code.

One way to investigate problems in your program is to simplify it
until you can get it to work, and then build it back up again bit by
bit. E.g., if it is not working for three bodies then check whether a
two-body simulation works.

A few things to check for:

* Check that the contributions to the acceleration of a given particle
  are summed together correctly and that the acceleration is
  initialised to zero at every iteration before the contributions are
  added up.

* Make sure not to try to calculate a spurious contribution to the
  acceleration of a particle due to a gravitational force from itself!
  The separation of a particle from itself is zero, so you will
  probably get division-by-zero errors if you try to do this.

> My simulation results do not precisely match the JPL
  ephemerides. Why not?

The JPL ephemerides use numerical methods beyond those mentioned in
this course. They also include nearly all the Solar System bodies (all
planets, minor planets, significant asteroids) and general
relativistic effects. Therefore, you should not expect to match
precisely the JPL ephemerides. However, studying the differences and
discussing their potential causes may be interesting material for your
report.

> My simulation program works, but is creakingly slow.  How can I
  speed it up?

Python is an interpreted language, and a gravitational simulation
written in Python is literally about a thousand times slower than the
equivalent program written in Fortran (a compiled language).
Nevertheless, you can take steps to speed up your program: where
possible "vectorise" by applying operations to whole NumPy arrays
rather than looping over Cartesian directions and/or particles (e.g.,
when updating positions and velocities); exploit Newton's third law to
halve the number of force calculations; and pull common factors out of
sums to reduce the number of operations.  For bottlenecks such as the
calculation of forces and accelerations, you might wish to investigate
using a just-in-time Python compiler such as
[Numba](https://numba.pydata.org/); this may speed up your program
more than tenfold.
