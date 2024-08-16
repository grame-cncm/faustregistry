#  maths.lib 

 Mathematic library for Faust. Its official prefix is `ma`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/maths.lib](https://github.com/grame-cncm/faustlibraries/blob/master/maths.lib)

## Functions Reference


----

### `(ma.)SR`

Current sampling rate given at init time. Constant during program execution.

#### Usage

```
SR : _
```

----

### `(ma.)T`

Current sample duration in seconds computed from the sampling rate given at init time. Constant during program execution.

#### Usage

```
T : _
```

----

### `(ma.)BS`

Current block-size. Can change during the execution at each block.

#### Usage

```
BS : _
```

----

### `(ma.)PI`

Constant PI in double precision.

#### Usage

```
PI : _
```

----

### `(ma.)deg2rad`

Convert degrees to radians.

#### Usage

```
45. : deg2rad
```

----

### `(ma.)rad2deg`

Convert radians to degrees.

#### Usage

```
ma.PI : rad2deg
```

----

### `(ma.)E`

Constant e in double precision.

#### Usage

```
E : _
```

----

### `(ma.)EPSILON`

Constant EPSILON available in simple/double/quad precision, 
as defined in the [floating-point standard](https://en.wikipedia.org/wiki/IEEE_754) 
and [machine epsilon](https://en.wikipedia.org/wiki/Machine_epsilon), 
that is smallest positive number such that `1.0 + EPSILON != 1.0`.

#### Usage

```
EPSILON : _
```

----

### `(ma.)MIN`

Constant MIN available in simple/double/quad precision (minimal positive value).

#### Usage

```
MIN : _
```

----

### `(ma.)MAX`

Constant MAX available in simple/double/quad precision (maximal positive value).

#### Usage

```
MAX : _
```

----

### `(ma.)FTZ`

Flush to zero: force samples under the "maximum subnormal number"
to be zero. Usually not needed in C++ because the architecture
file take care of this, but can be useful in JavaScript for instance.

#### Usage

```
_ : FTZ : _
```

#### Reference

* [http://docs.oracle.com/cd/E19957-01/806-3568/ncg_math.html](http://docs.oracle.com/cd/E19957-01/806-3568/ncg_math.html)

----

### `(ma.)copysign`

Changes the sign of x (first input) to that of y (second input).

#### Usage

```
_,_ : copysign : _
```

----

### `(ma.)neg`

Invert the sign (-x) of a signal.

#### Usage

```
_ : neg : _
```

----

### `(ma.)not`

Bitwise `not` implemented with [xor](https://faustdoc.grame.fr/manual/syntax/#xor-primitive) as `not(x) = x xor -1;`.
So working regardless of the size of the integer, assuming negative numbers in two's complement.

#### Usage

```
_ : not : _
```

----

### `(ma.)sub(x,y)`

Subtract `x` and `y`.

#### Usage

```
_,_ : sub : _
```

----

### `(ma.)inv`

Compute the inverse (1/x) of the input signal.

#### Usage

```
_ : inv : _
```

----

### `(ma.)cbrt`

Computes the cube root of of the input signal.

#### Usage

```
_ : cbrt : _
```

----

### `(ma.)hypot`

Computes the euclidian distance of the two input signals
sqrt(x*x+y*y) without undue overflow or underflow.

#### Usage

```
_,_ : hypot : _
```

----

### `(ma.)ldexp`

Takes two input signals: x and n, and multiplies x by 2 to the power n.

#### Usage

```
_,_ : ldexp : _
```

----

### `(ma.)scalb`

Takes two input signals: x and n, and multiplies x by 2 to the power n.

#### Usage

```
_,_ : scalb : _
```

----

### `(ma.)log1p`

Computes log(1 + x) without undue loss of accuracy when x is nearly zero.

#### Usage

```
_ : log1p : _
```

----

### `(ma.)logb`

Return exponent of the input signal as a floating-point number.

#### Usage

```
_ : logb : _
```

----

### `(ma.)ilogb`

Return exponent of the input signal as an integer number.

#### Usage

```
_ : ilogb : _
```

----

### `(ma.)log2`

Returns the base 2 logarithm of x.

#### Usage

```
_ : log2 : _
```

----

### `(ma.)expm1`

Return exponent of the input signal minus 1 with better precision.

#### Usage

```
_ : expm1 : _
```

----

### `(ma.)acosh`

Computes the principle value of the inverse hyperbolic cosine
of the input signal.

#### Usage

```
_ : acosh : _
```

----

### `(ma.)asinh`

Computes the inverse hyperbolic sine of the input signal.

#### Usage

```
_ : asinh : _
```

----

### `(ma.)atanh`

Computes the inverse hyperbolic tangent of the input signal.

#### Usage

```
_ : atanh : _
```

----

### `(ma.)sinh`

Computes the hyperbolic sine of the input signal.

#### Usage

```
_ : sinh : _
```

----

### `(ma.)cosh`

Computes the hyperbolic cosine of the input signal.

#### Usage

```
_ : cosh : _
```

----

### `(ma.)tanh`

Computes the hyperbolic tangent of the input signal.

#### Usage

```
_ : tanh : _
```

----

### `(ma.)erf`

Computes the error function of the input signal.

#### Usage

```
_ : erf : _
```

----

### `(ma.)erfc`

Computes the complementary error function of the input signal.

#### Usage

```
_ : erfc : _
```

----

### `(ma.)gamma`

Computes the gamma function of the input signal.

#### Usage

```
_ : gamma : _
```

----

### `(ma.)lgamma`

Calculates the natural logorithm of the absolute value of
the gamma function of the input signal.

#### Usage

```
_ : lgamma : _
```

----

### `(ma.)J0`

Computes the Bessel function of the first kind of order 0
of the input signal.

#### Usage

```
_ : J0 : _
```

----

### `(ma.)J1`

Computes the Bessel function of the first kind of order 1
of the input signal.

#### Usage

```
_ : J1 : _
```

----

### `(ma.)Jn`

Computes the Bessel function of the first kind of order n
(first input signal) of the second input signal.

#### Usage

```
_,_ : Jn : _
```

----

### `(ma.)Y0`

Computes the linearly independent Bessel function of the second kind
of order 0 of the input signal.

#### Usage

```
_ : Y0 : _
```

----

### `(ma.)Y1`

Computes the linearly independent Bessel function of the second kind
of order 1 of the input signal.

#### Usage

```
_ : Y0 : _
```

----

### `(ma.)Yn`

Computes the linearly independent Bessel function of the second kind
of order n (first input signal) of the second input signal.

#### Usage

```
_,_ : Yn : _
```

----

### `(ma.)fabs`, `(ma.)fmax`, `(ma.)fmin`

Just for compatibility...

```
fabs = abs
fmax = max
fmin = min
```

----

### `(ma.)np2`

Gives the next power of 2 of x.

#### Usage

```
np2(n) : _
```

Where:

* `n`: an integer

----

### `(ma.)frac`

Gives the fractional part of n.

#### Usage

```
frac(n) : _
```

Where:

* `n`: a decimal number

----

### `(ma.)modulo`

Modulus operation.

#### Usage

```
modulo(x,y) : _
```

Where:

* `x`: the numerator
* `y`: the denominator

----

### `(ma.)isnan`

Return non-zero if x is a NaN.

#### Usage

```
isnan(x)
_ : isnan : _
```

Where:

* `x`: signal to analyse

----

### `(ma.)isinf`

Return non-zero if x is a positive or negative infinity.

#### Usage

```
isinf(x)
_ : isinf : _
```

Where:

* `x`: signal to analyse

----

### `(ma.)chebychev`

Chebychev transformation of order N.

#### Usage

```
_ : chebychev(N) : _
```

Where:

* `N`: the order of the polynomial, a constant numerical expression

#### Semantics

```
T[0](x) = 1,
T[1](x) = x,
T[n](x) = 2x*T[n-1](x) - T[n-2](x)
```

#### Reference

* [http://en.wikipedia.org/wiki/Chebyshev_polynomial](http://en.wikipedia.org/wiki/Chebyshev_polynomial)

----

### `(ma.)chebychevpoly`

Linear combination of the first Chebyshev polynomials.

#### Usage

```
_ : chebychevpoly((c0,c1,...,cn)) : _
```

Where:

* `cn`: the different Chebychevs polynomials such that:
	chebychevpoly((c0,c1,...,cn)) = Sum of chebychev(i)*ci

#### Reference

* [http://www.csounds.com/manual/html/chebyshevpoly.html](http://www.csounds.com/manual/html/chebyshevpoly.html)

----

### `(ma.)diffn`

Negated first-order difference.

#### Usage

```
_ : diffn : _
```

----

### `(ma.)signum`

The signum function signum(x) is defined as
-1 for x<0, 0 for x==0, and 1 for x>0.

#### Usage

```
_ : signum : _
```

----

### `(ma.)nextpow2`

The nextpow2(x) returns the lowest integer m such that
2^m >= x.

#### Usage

```
2^nextpow2(n) : _
```
Useful for allocating delay lines, e.g., 
```
delay(2^nextpow2(maxDelayNeeded), currentDelay);
```

----

### `(ma.)zc`

Indicator function for zero-crossing: it returns 1 if a zero-crossing
occurs, 0 otherwise.

#### Usage

```
_ : zc : _
```

----

### `(ma.)primes`

Return the n-th prime using a waveform primitive. Note that primes(0) is 2,
primes(1) is 3, and so on. The waveform is length 2048, so the largest
precomputed prime is primes(2047) which is 17863.

#### Usage

```
_ : primes : _
```
