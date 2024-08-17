#  signals.lib 

A library of basic elements to handle signals in Faust. Its official prefix is `si`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/signals.lib](https://github.com/grame-cncm/faustlibraries/blob/master/signals.lib)

## Functions Reference


----

### `(si.)bus`

Put N cables in parallel.
`bus` is a standard Faust function.

#### Usage

```
bus(N)
bus(4) : _,_,_,_
```

Where:

* `N`: is an integer known at compile time that indicates the number of parallel cables

----

### `(si.)block`

Block - terminate N signals.
`block` is a standard Faust function.

#### Usage

```
si.bus(N) : block(N)
```

Where:

* `N`: the number of signals to be blocked known at compile time 

----

### `(si.)interpolate`

Linear interpolation between two signals.

#### Usage

```
_,_ : interpolate(i) : _
```

Where:

* `i`: interpolation control between 0 and 1 (0: first input; 1: second input)

----

### `(si.)repeat`

Repeat an effect N time(s) and take the parallel sum of all
intermediate buses.

#### References
* [https://github.com/orlarey/presentation-compilateur-faust/blob/master/slides.pdf](https://github.com/orlarey/presentation-compilateur-faust/blob/master/slides.pdf)

#### Usage

```
si.bus(inputs(FX)) : repeat(N, FX) : si.bus(outputs(FX))
```

Where:

* `N`: Number of repetitions, minimum of 1, a constant numerical expression 
* `FX`: an arbitrary effect (N inputs and N outputs) that will be repeated

Example 1:
```
process = repeat(2, dm.zita_light) : _*.5,_*.5;
```

Example 2:
```
N = 4;
C = 2;
fx(i) = i+1, par(j, C, @(i*5000));
process = 0, si.bus(C) : repeat(N, fx) : !, par(i, C, _*.2/N);
```

----

### `(si.)smoo`

Smoothing function based on `smooth` ideal to smooth UI signals
(sliders, etc.) down. Approximately, this is a 7 Hz one-pole
low-pass considering the coefficient calculation:
   exp(-2pi*CF/SR).

`smoo` is a standard Faust function.

#### Usage

```
hslider(...) : smoo;
```

----

### `(si.)polySmooth`

A smoothing function based on `smooth` that doesn't smooth when a
trigger signal is given. This is very useful when making
polyphonic synthesizer to make sure that the value of the parameter
is the right one when the note is started.

#### Usage

```
hslider(...) : polySmooth(g,s,d) : _
```

Where:

* `g`: the gate/trigger signal used when making polyphonic synths
* `s`: the smoothness (see `smooth`)
* `d`: the number of samples to wait before the signal start being
    smoothed after `g` switched to 1

----

### `(si.)smoothAndH`

A smoothing function based on `smooth` that holds its output
signal when a trigger is sent to it. This feature is convenient
when implementing polyphonic instruments to prevent some
smoothed parameter to change when a note-off event is sent.

#### Usage

```
hslider(...) : smoothAndH(g,s) : _
```

Where:

* `g`: the hold signal (0 for hold, 1 for bypass)
* `s`: the smoothness (see `smooth`)

----

### `(si.)bsmooth`

Block smooth linear interpolation during a block of samples (given by the `ma.BS` value).

#### Usage

```
hslider(...) : bsmooth : _
```

----

### `(si.)dot`

Dot product for two vectors of size N.

#### Usage

```
si.bus(N), si.bus(N) : dot(N) : _
```

Where:

* `N`: size of the vectors (int, must be known at compile time)

----

### `(si.)smooth`

Exponential smoothing by a unity-dc-gain one-pole lowpass.
`smooth` is a standard Faust function.

#### Usage:

```
_ : si.smooth(ba.tau2pole(tau)) : _
```

Where:

* `tau`: desired smoothing time constant in seconds, or

```
hslider(...) : smooth(s) : _
```

Where:

* `s`: smoothness between 0 and 1. s=0 for no smoothing, s=0.999 is "very smooth",
s>1 is unstable, and s=1 yields the zero signal for all inputs.
The exponential time-constant is approximately 1/(1-s) samples, when s is close to
(but less than) 1.

#### References:

* [https://ccrma.stanford.edu/~jos/mdft/Convolution_Example_2_ADSR.html](https://ccrma.stanford.edu/~jos/mdft/Convolution_Example_2_ADSR.html)
* [https://ccrma.stanford.edu/~jos/aspf/Appendix_B_Inspecting_Assembly.html](https://ccrma.stanford.edu/~jos/aspf/Appendix_B_Inspecting_Assembly.html)

----

### `(si.)smoothq`

Smoothing with continuously variable curves from Exponential to Linear, with a constant time.

#### Usage

```
_ : smoothq(time, q) : _;
```

Where:

* `time`: seconds to reach target
* `q`: curve shape (between 0..1, 0 is Exponential, 1 is Linear)

----

### `(si.)cbus`

N parallel cables for complex signals.
`cbus` is a standard Faust function.

#### Usage

```
cbus(N)
cbus(4) : (r0,i0), (r1,i1), (r2,i2), (r3,i3)
```

Where:

* `N`: is an integer known at compile time that indicates the number of parallel cables.
* each complex number is represented by two real signals as (real,imag)

----

### `(si.)cmul`

Multiply two complex signals pointwise.
`cmul` is a standard Faust function.

#### Usage

```
(r1,i1) : cmul(r2,i2) : (_,_)
```

Where:

* Each complex number is represented by two real signals as (real,imag), so
- `(r1,i1)` = real and imaginary parts of signal 1
- `(r2,i2)` = real and imaginary parts of signal 2

----

### `(si.)cconj`

Complex conjugation of a (complex) signal.
`cconj` is a standard Faust function.

#### Usage

```
(r1,i1) : cconj : (_,_)
```

Where:

* Each complex number is represented by two real signals as (real,imag), so
- `(r1,i1)` = real and imaginary parts of the input signal
- `(r1,-i1)` = real and imaginary parts of the output signal

----

### `(si.)onePoleSwitching`

One pole filter with independent attack and release times.

#### Usage

```
_ : onePoleSwitching(att,rel) : _
```

Where:

* `att`: the attack tau time constant in second
* `rel`: the release tau time constant in second


----

### `(si.)rev`

Reverse the input signal by blocks of n>0 samples. `rev(1)` is the indentity
function. `rev(n)` has a latency of `n-1` samples.

#### Usage

```
_ : rev(n) : _
```

Where:

* `n`: the block size in samples

----

### `(si.)vecOp`


This function is a generalisation of Faust's iterators such as `prod` and
`sum`, and it allows to perform operations on an arbitrary number of
vectors, provided that they all have the same length. Unlike Faust's
iterators `prod` and `sum` where the vector size is equal to one and the 
vector space dimension must be specified by the user, this function will 
infer the vector space dimension and vector size based on the vectors list 
that we provide.

The outputs of the function are equal to the vector size, whereas the
number of inputs is dependent on whether the elements of the vectors
provided expect an incoming signal themselves or not. We will see a
clarifying example later; in general, the number of total inputs will
be the sum of the inputs in each input vector.

Note that we must provide a list of at least two vectors, each with a size 
that is greater or equal to one.

#### Usage

```
     si.bus(inputs(vectorsList)) : vecOp((vectorsList), op) : si.bus(outputs(ba.take(1, vectorsList)));
```

#### Where

* `vectorsList`: is a list of vectors
* `op`: is a two-input, one-output operator

For example, consider the following vectors lists:

     v0 = (0 , 1 , 2 , 3);
     v1 = (4 , 5 , 6 , 7);
     v2 = (8 , 9 , 10 , 11);
     v3 = (12 , 13 , 14 , 15);
     v4 = (+(16) , _ , 18 , *(19));
     vv = (v0 , v1 , v2 , v3);

Although Faust has limitations for list processing, these vectors can be
combined or processed individually.

If we do:

     process = vecOp(v0, +);

the function will deduce a vector space of dimension equal to four and 
a vector length equal to one. Note that this is equivalent to writing:

     process = v0 : sum(i, 4, _);

Similarly, we can write:

     process = vecOp((v0 , v1), *) :> _;

and we have a dimension-two space and length-four vectors. This is the dot 
product between vectors v0 and v1, which is equivalent to writing:

     process = v0 , v1 : dot(4);

The examples above have no inputs, as none of the elements of the vectors
expect inputs. On the other hand, we can write:

     process = vecOp((v4 , v4), +);

and the function will have six inputs and four outputs, as each vector
has three of the four elements expecting an input, times two, as the two
input vectors are identical.

Finally, we can write:

     process = vecOp(vv, &);

to perform the bitwise AND on all the elements at the same position in 
each vector, having dimension equal to the vector length equal to four.

Or even:

     process = vecOp((vv , vv), &);

which gives us a dimension equal to two, and a vector size equal to sixteen.

For a more practical use-case, this is how we can implement a time-invariant
feedback delay network with Hadamard matrix:

     N = 4;
     normalisation = 1.0 / sqrt(N);
     coeffVec = par(i, N, .99 * normalisation);
     delVec = par(i, N, (i + 1) * 3);
     process = vecOp((si.bus(N) , si.bus(N)), +) ~ 
         vecOp((vecOp((ro.hadamard(N) , coeffVec), *) , delVec), @);


----

### `(si.)bpar`

Balanced `par` where the repeated expression doesn't depend on a variable.
The built-in `par` is implemented as an unbalanced tree, and also has
to substitute the variable into the repeated expression, which is expensive
even when the variable doesn't appear. This version is implemented as a
balanced tree (which allows node reuse during tree traversal) and also
doesn't search for the variable. This can be much faster than `par` to compile.

#### Usage

```
si.bus(N * inputs(f)) : bpar(N, f) : si.bus(N * outputs(f))
```

Where:

* `N`: number of repetitions, minimum 1, a constant numerical expression
* `f`: an arbitrary expression

Example:
```
// square each of 4000 inputs
process = si.bpar(4000, (_ <: _, _ : *));
```


----

### `(si.)bsum`

Balanced `sum`, see `si.bpar`.

#### Usage

```
si.bus(N * inputs(f)) : bsum(N, f) : _
```

Where:

* `N`: number of repetitions, minimum 1, a constant numerical expression
* `f`: an arbitrary expression with 1 output.

Example:
```
// square each of 1000 inputs and add the results
process = si.bsum(1000, (_ <: _, _ : *));
```

----

### `(si.)bprod`

Balanced `prod`, see `si.bpar`.

#### Usage

```
si.bus(N * inputs(f)) : bprod(N, f) : _
```

Where:

* `N`: number of repetitions, minimum 1, a constant numerical expression
* `f`: an arbitrary expression with 1 output.

Example:
```
// Add 8000 consecutive inputs (in pairs) and multiply the results
process = si.bprod(4000, +);
```
