#  fds.lib 

This library allows to build linear, explicit finite difference schemes
physical models in 1 or 2 dimensions using an approach based on the cellular
automata formalism. Its official prefix is `fd`. 

In order to use the library, one needs to discretize the linear partial
differential equation of the desired system both at boundaries and in-between
them, thus obtaining a set of explicit recursion relations. Each one
of these will provide, for each spatial point the scalar coefficients to be
multiplied by the states of the current and past neighbour points.

Coefficients need to be stacked in parallel in order to form a coefficients
matrix for each point in the mesh. It is necessary to provide one matrix for
coefficients matrices are defined, they need to be placed in parallel and
ordered following the desired mesh structure (i.e., coefficients for the top
left boundaries will come first, while bottom right boundaries will come
last), to form a *coefficients scheme*, which can be used with the library
functions.
## Sources
Here are listed some works on finite difference schemes and cellular
automata thet were the basis for the implementation of this library

* S. Bilbao, Numerical Sound Synthesis.Chichester, UK: John Wiley Sons,
Ltd, 2009
* P. Narbel, "Qualitative and quantitative cellular automata from
differential equations," Lecture Notes in Computer Science, vol. 4173,
pp. 112–121, 10 2006
* X.-S. Yang and Y. Young, Cellular Automata, PDEs, and Pattern Formation.
Chapman & Hall/CRC, 092005, ch. 18, pp. 271–282.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/fds.lib](https://github.com/grame-cncm/faustlibraries/blob/master/fds.lib)

## Model Construction

Once the coefficients scheme is defined, the user can simply call one of
these functions to obtain a fully working physical model. They expect to
receive a force input signal for each mesh point and output the state of each
point. Interpolation operators can be used to drive external forces to the
desired points, and to get the signal only from a certain area of the mesh.

----

### `(fd.)model1D`

This function can be used to obtain a physical model in 1 dimension.
Takes a force input signal for each point and outputs the state of each
point.

#### Usage

```
si.bus(points) : model1D(points,R,T,scheme) : si.bus(points)
```

Where:

* `points`: size of the mesh in points
* `R`: neighbourhood radius, indicates how many side points are needed (i.e.
       if R=1 the mesh depends on one point on the left and one on the right)
* `T`: time coefficient, indicates how much steps back in time are needed (i.
       e. if T=1 the maximum delay needed for a neighbour state is 1 sample)
* `scheme`: coefficients scheme

----

### `(fd.)model2D`

This function can be used to obtain a physical model in 2 dimension.
Takes a force input signal for each point and outputs the state of each
point.
IMPORTANT: 2D models with more than 30x20 points might crash the c++
compiler. 2D models need to be compiled with the command line compiler,
the online one presents some issues.

#### Usage

```
si.bus(pointsX*pointsY) : model2D(pointsX,pointsY,R,T,scheme) :
   si.bus(pointsX*pointsY)
```

Where:

* `pointsX`: horizontal size of the mesh in points
* `pointsY`: vertical size of the mesh in points
* `R`: neighbourhood radius, indicates how many side points are needed (i.e.
       if R=1 the mesh depends on one point on the left and one on the right)
* `T`: time coefficient, indicates how much steps back in time are needed (i.
       e. if T=1 the maximum delay needed for a neighbour state is 1 sample)
* `scheme`: coefficients scheme

## Interpolation

Interpolation functions can be used to drive the input signals to the
correct mesh points, or to get the output signal from the
desired points. All the interpolation functions allow to change the
input/output points at run time. In general, all these functions get in
input a number of connections, and output the same number of connections,
where each signal is multiplied by zero except the ones specified by the
arguments.

----

### `(fd.)stairsInterp1D`

Stairs interpolator in 1 dimension. Takes a number of signals and outputs
the same number of signals, where each one is multiplied by zero except the
one specified by the argument. This can vary at run time (i.e. a slider),
but must be an integer.

#### Usage

```
si.bus(points) : stairsInterp1D(points,point) : si.bus(points)
```

Where:

* `points`: total number of points in the mesh
* `point`: number of the desired nonzero signal

----

### `(fd.)stairsInterp2D`

Stairs interpolator in 2 dimensions. Similar to the 1-D version.

#### Usage

```
si.bus(pointsX*pointsY) : stairsInterp2D(pointsX,pointsY,pointX,pointY) :
   si.bus(pointsX*pointsY)
```

Where:

* `pointsX`: total number of points in the X direction
* `pointsY`: total number of points in the Y direction
* `pointX`: horizontal index of the desired nonzero signal
* `pointY`: vertical index of the desired nonzero signal

----

### `(fd.)linInterp1D`

Linear interpolator in 1 dimension. Takes a number of signals and outputs
the same number of signals, where each one is multiplied by zero except two
signals around a floating point index. This is essentially a Faust
implementation of the $J(x_i)$ operator, not scaled by the spatial step.
(see Stefan Bilbao's book, Numerical Sound Synthesis). The index can vary
at run time.

#### Usage

```
si.bus(points) : linInterp1D(points,point) : si.bus(points)
```

Where:

* `points`: total number of points in the mesh
* `point`: floating point index

----

### `(fd.)linInterp2D`

Linear interpolator in 2 dimensions. Similar to the 1 D version.

#### Usage

```
si.bus(pointsX*pointsY) : linInterp2D(pointsX,pointsY,pointX,pointY) :
   si.bus(pointsX*pointsY)
```

Where:

* `pointsX`: total number of points in the X direction
* `pointsY`: total number of points in the Y direction
* `pointX`: horizontal float index
* `pointY`: vertical float index

----

### `(fd.)stairsInterp1DOut`

Stairs interpolator in 1 dimension. Similar to `stairsInterp1D`, except it
outputs only the desired signal.

#### Usage

```
si.bus(points) : stairsInterp1DOut(points,point) : _
```

Where:

* `points`: total number of points in the mesh
* `point`: number of the desired nonzero signal

----

### `(fd.)stairsInterp2DOut`

Stairs interpolator in 2 dimensions which outputs only one signal.

#### Usage

```
si.bus(pointsX*pointsY) : stairsInterp2DOut(pointsX,pointsY,pointX,pointY) : _
```

Where:

* `pointsX`: total number of points in the X direction
* `pointsY`: total number of points in the Y direction
* `pointX`: horizontal index of the desired nonzero signal
* `pointY`: vertical index of the desired nonzero signal

----

### `(fd.)linInterp1DOut`

Linear interpolator in 1 dimension. Similar to `stairsInterp1D`, except it
sums each output signal and provides only one output value.

#### Usage

```
si.bus(points) : linInterp1DOut(points,point) : _
```

Where:

* `points`: total number of points in the mesh
* `point`: floating point index

----

### `(fd.)stairsInterp2DOut`

Linear interpolator in 2 dimensions which outputs only one signal.

#### Usage

```
si.bus(pointsX*pointsY) : linInterp2DOut(pointsX,pointsY,pointX,pointY) : _
```

Where:

* `pointsX`: total number of points in the X direction
* `pointsY`: total number of points in the Y direction
* `pointX`: horizontal float index
* `pointY`: vertical float index

## Routing

The routing functions are used internally by the model building functions,
but can also be taken separately. These functions route the forces, the
coefficients scheme and the neighbours’ signals into the correct scheme
points and take as input, in this order: the coefficients block, the
feedback signals and the forces. In output they provide, in order, for each
scheme point: the force signal, the coefficient matrices and the neighbours’
signals. These functions are based on the Faust route primitive.

----

### `(fd.)route1D`

Routing function for 1 dimensional schemes.

#### Usage

```
si.bus((2*R+1)*(T+1)*points),si.bus(points*2) : route1D(points, R, T) :
   si.bus((1 + ((2*R+1)*(T+1)) + (2*R+1))*points)
```

Where:

* `points`: total number of points in the mesh
* `R`: neighbourhood radius
* `T`: time coefficient

----

### `(fd.)route2D`

Routing function for 2 dimensional schemes.

#### Usage

```
si.bus((2*R+1)^2*(T+1)*pointsX*pointsY),si.bus(pointsX*pointsY*2) :
   route2D(pointsX, pointsY, R, T) :
       si.bus((1 + ((2*R+1)^2*(T+1)) + (2*R+1)^2)*pointsX*pointsY)
```

Where:

* `pointsX`: total number of points in the X direction
* `pointsY`: total number of points in the Y direction
* `R`: neighbourhood radius
* `T`: time coefficient

## Scheme Operations

The scheme operation functions are used internally by the model building
functions but can also be taken separately. The schemePoint function is
where the update equation is actually calculated. The `buildScheme` functions
are used to stack in parallel several schemePoint blocks, according to the
choosed mesh size.

----

### `(fd.)schemePoint`

This function calculates the next state for each mesh point, in order to
form a scheme, several of these blocks need to be stacked in parallel.
This function takes in input, in order, the force, the coefficient matrices
and the neighbours’ signals and outputs the next point state.

#### Usage

```
_,si.bus((2*R+1)^D*(T+1)),si.bus((2*R+1)^D) : schemePoint(R,T,D) : _
```

Where:

* `R`: neighbourhood radius
* `T`: time coefficient
* `D`: scheme spatial dimensions (i.e. 1 if 1-D, 2 if 2-D)

----

### `(fd.)buildScheme1D`

This function is used to stack in parallel several schemePoint functions in
1 dimension, according to the number of points.

#### Usage

```
si.bus((1 + ((2*R+1)*(T+1)) + (2*R+1))*points) : buildScheme1D(points,R,T) :
   si.bus(points)
```

Where:

* `points`: total number of points in the mesh
* `R`: neighbourhood radius
* `T`: time coefficient

----

### `(fd.)buildScheme2D`

This function is used to stack in parallel several schemePoint functions in
2 dimensions, according to the number of points in the X and Y directions.

#### Usage

```
si.bus((1 + ((2*R+1)^2*(T+1)) + (2*R+1)^2)*pointsX*pointsY) :
   buildScheme2D(pointsX,pointsY,R,T) : si.bus(pointsX*pointsY)
```

Where:

* `pointsX`: total number of points in the X direction
* `pointsY`: total number of points in the Y direction
* `R`: neighbourhood radius
* `T`: time coefficient

## Interaction Models

Here are defined two physically based interaction algorithms: a hammer and
a bow. These functions need to be coupled to the mesh pde, in the point
where the interaction happens: to do so, the mesh output signals can be fed
back and driven into the force block using the interpolation operators.
The latters can be also used to drive the single force output signal to the
correct scheme points.

----

### `(fd.)hammer`

Implementation of a nonlinear collision model. The hammer is essentially a
finite difference scheme of a linear damped oscillator, which is coupled
with the mesh through the collision model (see Stefan Bilbao's book,
Numerical Sound Synthesis).

#### Usage

```
_ :hammer(coeff,omega0Sqr,sigma0,kH,alpha,k,offset,fIn) : _
```

Where:

* `coeff`: output force scaling coefficient
* `omega0Sqr`: squared angular frequency of the hammer oscillator
* `sigma0`: damping coefficient of the hammer oscillator
* `kH`: hammer stiffness coefficient
* `alpha`: nonlinearity parameter
* `k`: time sampling step (the same as for the mesh)
* `offset`: distance between the string and the hammer at rest in meters
* `fIn`: hammer excitation signal (i.e. a button)

----

### `(fd.)bow`

Implementation of a nonlinear friction based interaction model that induces
Helmholtz motion. (see Stefan Bilbao's book, Numerical Sound Synthesis).

#### Usage

```
_ :bow(coeff,alpha,k,vb) : _
```

Where:

* `coeff`: output force scaling coefficient
* `alpha`: nonlinearity parameter
* `k`: time sampling step (the same as for the mesh)
* `vb`: bow velocity [m/s]
