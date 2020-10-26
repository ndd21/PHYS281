---
title: Gravity simulation
authors:
    - Iain Bertram
    - Matthew Pitkin
    - Brooke Simmons
date: 2020-10-07
---

# Gravity simulation

The final project is to develop a physics simulation in which a physical system evolves with time.
An interesting type of system to consider is the motion of several particles or extended bodies
under the mutual influence of their gravitational fields. This is the example that we will use as
the starting point of the final project for this module.

There is plenty of scope to develop the simple gravitational field simulations described here into
simulations of more complicated systems and you are welcome to extend your project to involve
different physical systems, forces, etc. Initially though you should start by following the steps
presented below. You may find that doing this takes all of the available time or you may find that
you have plenty of extra time to simulate other systems. Either way you will need to write up your
findings in a report as detailed at the end of this [section](#project-description), so make sure
that you leave enough time for this.

As in the case of [numerical integration](../numerical-integration/index.html), most physics
simulations will require some amount of approximation which will introduce an error (i.e., an
inaccuracy) in the results from the simulation. There are various ways to establish the size of this
error:

- Apply the simulation to a system where there is an analytical solution to the equations of motion
  so that the predictions of the simulation can be directly tested against the known results. This
  approach has the advantage of allowing you to unambiguously calculate the size of any error in the
  simulation due to approximations, etc. However, it does not guarantee that the simulation will
  have the same size of error when it is applied to a regime for which there is not an analytical
  solution.
- Apply the simulation to a system for which there is experimental data so that the simulation can
  be directly tested against reality. In some ways this is of course what physics is all about and
  so is a good approach. The difficulty here is that experimental data often contains many
  additional subtle effects which may not be in your simulation so it may not be easy to understand
  where any discrepancies come from.
- For a range of systems, consider whether the simulation conserves quantities that you would expect
  to be conserved, e.g., energy, or total linear or angular momentum. Although conservation of
  energy, etc does not guarantee that the details of the simulation are accurate, it provides a
  quick global check of the simulation's properties.

You are going to want to consider carefully how to use these approaches to assess the accuracy of
your own simulations.

Let's consider the various steps in developing a general simulation of particle motion in
gravitational fields.

## A "Particle" in The Earth’s Gravitational Field


To start off with, we want to simulate the trajectory of a particle in a cannonball-like trajectory
close to the surface of the Earth. We need to bear in mind from the start that we are going to want
to create a simulation that is easily extendable to the more general case where the acceleration due
to gravity is not constant and may depend on other bodies involved in the simulation. It would be
easy to forget this and just write a simulation that can only simulate the parabolic trajectories of
a particle close to the surface of the Earth, but with a bit of thought we can save a lot of time
later on.

For simplicity, our simulation can be considered initially to be in 2 dimensions: the $x$-direction
which is parallel to the ground, and the $y$-direction which is perpendicular to the ground. We are
of course inherently here assuming the surface of the Earth can be treated as being approximately
flat as long as we consider fairly short trajectories. Later on we can remove this assumption.

In this case we can represent the approximate acceleration by:
$$
  \vec{a} = g = -9.81 \hat{j}  \, {\mathrm m} {\mathrm s}^{-2}.
$$

To characterise the motion of particles in this uniform gravitational field we will need to be able
to calculate the changes in the particle's position $\vec{x}$, and velocity $\vec{v}$ as a function
of time, $t$.

For many (although not all) physical systems we can write the velocity
$$
  \vec{v}(t) = \int^{t} \vec{a}(\vec{x}, t) dt,
$$
and position
$$
  \vec{x}(t) = \int^{t} \vec{v}(\vec{x}, t) dt,
$$
where $\vec{a}(t)$ is the acceleration of the particle and we have restricted ourselves here to
considering a single particle. Equivalently, these can be written as a pair of differential
equations
$$
\vec{v}(t) = \frac{\mathrm{d}\vec{x}(t)}{\mathrm{d}t},
$$
and
$$
\vec{a}(t) = \frac{\mathrm{d}\vec{v}(t)}{\mathrm{d}t}.
$$

In this simple example the acceleration is constant and we can of course just solve the equations
analytically to give the the basic equations of motion for constant, uniform acceleration (i.e.
there is no spatial or temporal dependence). The familiar equations are:

$$
\begin{align}
  \vec{v} & =  \vec{v_{0}} + \vec{a} t \\
  \vec{x} & =  \vec{x_{0}} + \vec{v_{0}} t + \frac{1}{2} \vec{a} t^{2}
\end{align}
$$

where the initial position and velocity at time $t=0$ are given by $\vec{x_{0}}$ and $\vec{v_{0}}$,
respectively. As long as the acceleration is constant and uniform, these equations will be accurate
and hence our simulation will not be very interesting.

We would instead like an approximate numerical solution to the equations of motion, so that we can
consider the general case where the acceleration is not constant/uniform and analytical solutions
are therefore not always available. In addition, we'd like to track the evolution of the system as
time increases, so we don't just want the positions and velocities at a time $t$, we want to know
them at intermediate times too. The simplest approach to this is known as the [Euler
method](https://en.wikipedia.org/wiki/Euler_method) (or Euler forward method). It is an iterative
algorithm which allows us to calculate the approximate position and velocity at time $t+\Delta{t}$
given that we know them at the slightly earlier time $t$. It has the form

$$
\begin{align}
  \vec{v}_{n+1} & \approx \vec{v}_n + \vec{a}_n \Delta t, \\
  \vec{x}_{n+1} & \approx \vec{x}_n + \vec{v}_n \Delta t,
\end{align}
$$

where we assume that the acceleration is approximately constant for the small duration $\Delta t$
and the label $n$ denotes the start of this time step and $n+1$ the end of this time step. As when
we were considering numerical integration methods, this approach is actually just the first couple
of terms of a Taylor series expansion and we expect that there will be an error of order $(\Delta
t)^2$ each time we apply this iterative formula, so that the cumulative error over a fixed time will
be of order $\Delta t$. Alternative algorithms are discussed later, but for now the Euler algorithm
will suffice.

If we want to consider a slightly more complicated case of motion in the Earth's gravitational field
then we can take into account the variation of acceleration due to gravity with distance from the
Earth's centre $r$ using

$$
\vec{g} = -\frac{G M_E}{r^2} \hat{r}
$$

for values of $r$ greater than the Earth's radius $R_E= 6380\,\mathrm{km}$. The mass of the Earth is
given approximately by $M_E = 5.974\!\times\!10^{24}\,\mathrm{kg}$ and $G$ is the gravitational
constant.

Care must be taken when defining the direction of the field or you could easily end up simulating
anti-gravity!

From this point on you are entirely free to develop your simulation in any way you wish but do skip
ahead and read the project description thoroughly first! The next two sections detail one way in
which you could develop your code with a view to developing a simulation of the Solar System, but
you can pick another goal.

## Particle traversing a tunnel through the Earth's core

In principle, we already know everything we need to know in order to simulate the general motion of
a system of particle's moving under the influence of each other's gravitational fields. However,
rather than jump immediately to this scenario we could also consider the following. It is clear that
the acceleration at the surface of the Earth is given by:

$$
\vec{g} = -\frac{G M_E}{R^{2}_E} \hat{r}.
$$

We could simulate the path of a projectile dropped from the Earth's surface into a hole that runs
through the centre of the Earth in a straight line, i.e., in a radial direction.

Assuming that the projectile has no component of velocity tangential to the Earth's surface, this is
a one-dimensional problem (which simplifies matters considerably). The gravitational field strength
will depend on the distance of the object from the centre of the Earth. To calculate the
gravitational field we need the mass of the part of the Earth contained within a sphere of radius
$r$ such that:

$$
\frac{m}{M_E} = \frac{\frac{4}{3} \pi r^{3}}{\frac{4}{3}\pi R^3_E} = \frac{r^3}{R^3_E}.
$$

So the gravitational field will be given by:

$$
\vec{g} = -\frac{Gm}{r^2}\hat{r} = -G \frac{M_E}{r^2} \frac{r^3}{R^3_E}\hat{r}
  = -G \frac{M_E}{R^3_E}r \hat{r}
$$

Hopefully it is clear from this result that we would expect the motion of a projectile dropped into
this hole to be simple harmonic motion. You may want to use this as optional test of your code. You
will clearly have to add new methods to represent the gravitational field inside the Earth. At this
point it is quite likely you will start to see significant limitations of the Euler algorithm. You
should read ahead to the discussion of alternative algorithms as you are likely to want to use the
[Euler-Cromer](https://en.wikipedia.org/wiki/Semi-implicit_Euler_method) algorithm. Depending on how
much time you have, you may want to skip this simulation entirely and move on with your own project
plans, but either way you are likely going to want to replace the Euler algorithm with something
more robust.

## Orbiting Massive Particles (E.g, Planets)

Consider the case of "N" massive particles moving under the influence of each others’ gravity. The
net acceleration of a particle with mass $m_i$ will be given by

$$
\vec{a_i} = \sum^{N}_{j\neq i}{\frac{-Gm_j}{|r_{ij}|^2} \hat{r}_{ij}},
$$

where $\vec{r}_{ij}$ is the displacement vector from the $j^{\mathrm{th}}$ mass to the
$i^{\mathrm{th}}$ mass. In this case, to determine the field that is affecting a given particle we
need to know the locations of all the other particles in our simulation. Notice that the sum of all
forces acting on all particles should be zero at all times. This result is just due to Newton's
third law in the absence of an external field. Note that if we move one particle before calculating
the effect of that particle on all the other particles in our simulation then (unless great care is
taken) out code will violate Newton's third law. This is unlikely to be a good idea.

Note that when coding up the above equation you can calculate each dimension independently, i.e., in the $x$-dimension

$$
{a_x}_i = \sum^N_{j \neq i} \frac{-G m_j}{|r_{ij}|^2}\frac{({r_x}_i - {r_x}_j)}{|r_{ij}|}
$$

where, even for one dimension, $|r_{ij}|$ is still the total magnitude of the difference in positions between two particles, given by:

$$
|r_{ij}| = \left(({r_x}_i - {r_x}_j)^2 + ({r_y}_i - {r_y}_j)^2 + ({r_z}_i - {r_z}_j)^2\right)^{1/2}.
$$

Be careful to make sure the indices of the values in $({r_x}_i - {r_x}_j)$ are in the correct order,
so that the acceleration on object $i$ caused by object $j$ points towards object $j$.

## Different methods of simulating kinematics

Regardless of the details of your final project you are going to need to have a way of approximating
the motion of your system. We have assumed earlier that for a small interval of time $\Delta t$ that
the change in acceleration is small and that the resulting change in position and velocity is given
by 

$$
\begin{align}
  \vec{v}_{n+1} & \approx \vec{v}_n + \vec{a}_n \Delta{t},  \\
  \vec{x}_{n+1} & \approx \vec{x}_n + \vec{v}_n \Delta{t} 
\end{align}
$$

which we've already referred to as Euler's Method. As stated, this is based on a Taylor expansion of
the standard equations of motion to give

$$
\begin{align}
\vec{v}_{n+1} & = \vec{v}_n + a_n \Delta{t} + {\mathcal{O}}\left( \left(\Delta t \right)^2\right),\\
\vec{x}_{n+1} & = \vec{x}_n + \vec{v}_n \Delta{t} + {\mathcal{O}}\left( \left(\Delta t \right)^2\right),
\end{align}
$$

where ${\mathcal{O}}\left( \left(\Delta t \right)^2\right)$ signifies contributions of higher order.
If $\Delta t$ has a small enough value these higher-order contributions will be small and can be
safely ignored. This is the assumption made by Euler's Method. The error in any given step is given
by the truncation of the expansion and in this case is of order $(\Delta t)^2$. This error will
accumulate each time the iteration is applied and hence the error in a simulation of fixed duration
will be of order $\Delta t$. In the following paragraphs other algorithms are introduced. The errors
in each of these approximations is not discussed but an investigation of this could form a part of
your project.

As well as not being very accurate, for oscillatory systems the *Euler* method can be unstable. An
alternative method called the *Euler-Cromer*, uses the velocity at the end of the step rather than
the beginning of the step and should give more stable results

$$
\begin{align}
\vec{v}_{n+1} & \approx \vec{v}_n + \vec{a}_n \Delta{t},\\
\vec{x}_{n+1} & \approx \vec{x}_n + \vec{v}_{n+1} \Delta{t}.
\end{align}
$$

It is also possible that it may be better to compute the velocity in the middle of the interval
$\Delta t$. This calculation is called the *Euler-Richardson* algorithm. This is particularly useful
for velocity-dependent forces. This algorithm requires use of the *Euler* method to calculate the
intermediate position $x_{\mathrm mid}$ and velocity $v_{\mathrm mid}$ at time $t_{\mathrm mid} = t
+ \Delta t/2$. The force and acceleration are then computed for this mid-point.

$$
\begin{align}
  \vec{a}_n & = \vec{F}\left( \vec{x}_n, \vec{v}_n, t_n \right)/m \\
  \vec{v}_{\mathrm{mid}} & \approx \vec{v}_n + \frac{1}{2}\vec{a}_n \Delta{t}\\
  \vec{x}_{\mathrm{mid}} & \approx \vec{x}_n + \frac{1}{2}\vec{v}_n \Delta{t}\\
  \vec{a}_{\mathrm{mid}} & \approx \vec{F}\left(\vec{x}_{\mathrm mid}, \vec{v}_{\mathrm{mid}}, t+\frac{1}{2}\Delta{t} \right)/m,
\end{align}
$$

so that

$$
\begin{align}
    \vec{v}_{n+1} & \approx \vec{v}_n + \vec{a}_{\mathrm{mid}} \Delta{t},\\
    \vec{x}_{n+1} & \approx \vec{x}_n + \vec{v}_{\mathrm{mid}} \Delta{t}.
\end{align}
$$

Finally we can look at a simpler alternative known as the *Verlet* algorithm that is similar to the
familiar equations of motion for constant acceleration. This uses the acceleration calculated at the
end position to calculate the updated velocity which helps smooth out any changes in the
acceleration. It is given by

$$
\begin{align}
\vec{x}_{n+1} & \approx \vec{x}_n + \vec{v}_n
\Delta{t} + \frac{1}{2}\vec{a}_n \left(\Delta t \right)^2,\\
  \vec{v}_{n+1} & \approx \vec{v}_n + \frac{1}{2} \left( \vec{a}_{n+1} + \vec{a}_n \right)  \Delta{t}.
\end{align}
$$

Clearly in this case we need some way of estimating $\vec{a}_{n+1}$. This can be achieved by using
any of the algorithms/methods mentioned above first and then applying Verlet.

Beyond these algorithms you can also consider higher-order algorithms such as the well-known
[Runge-Kutta](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods) algorithms which are very
widely used in physics simulations. The Runge-Kutta algorithms aren't discussed in detail here as it
can be troublesome to correctly turn them into code, but you are welcome to implement them if you
wish. The algorithms listed above are likely to be sufficiently accurate for most projects you are
likely to attempt in this module. In fact, you will probably get acceptable results by just using
the simple Euler-Cromer algorithm.

## Project description

To summarise the above description, the aim of this project is to produce a simulation of the motion
of multiple massive bodies interacting under the influence of their gravitational fields, e.g., the
Solar System. This can be built up in stages of increasing complexity, i.e.:

1. a single massive particle in a static field;
2. a pair of massive particles interacting with each other in 1, 2 and 3 dimensions;
3. a set or 3 or more massive particles interacting in 3 dimensions;
4. supplying initial conditions to the simulation based on masses, positions and velocities of solar system bodies.

To evolve the motion of the particles in the simulation the Euler, Euler-Cromer or other numerical
approximation methods should be used.

You are free to produce the simulation as you wish, but the two pre-defined exercises that are part
of the project provide a good starting point (i.e., the `Particle` class) for expansion to a
more fully formed simulation. You can use the results from these exercises as part of your final
report.

The simulation you write should come with some tests that show that it works as expected, e.g., tests of parts
of the code or simple systems against analytical calculations. Useful tests are checking that the
simulation conserves **total** linear momentum or angular momentum to an acceptable level. The tests should ideally compare simulations produced using more than one numerical approximation method, with quantitative evaluation of the differences.

The simulation can include additional physics or simulate systems other than the solar system provided that you can provide justifiable tests of its validity.
