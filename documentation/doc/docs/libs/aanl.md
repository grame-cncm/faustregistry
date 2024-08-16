#  aanl.lib 

A library for antialiased nonlinearities. Its official prefix is `aa`. 

This library provides aliasing-suppressed nonlinearities through first-order 
and second-order approximations of continuous-time signals, functions,
and convolution based on antiderivatives. This technique is particularly 
effective if combined with low-factor oversampling, for example, operating
at 96 kHz or 192 kHz sample-rate.

The library contains trigonometric functions as well as other nonlinear 
functions such as bounded and unbounded saturators.

Due to their limited domains or ranges, some of these functions may not 
suitable for audio nonlinear processing or waveshaping, although
they have been included for completeness. Some other functions,
for example, tan() and tanh(), are only available with first-order
antialiasing due to the complexity of the antiderivative of the 
x * f(x) term, particularly because of the necessity of the dilogarithm 
function, which requires special implementation.

Future improvements to this library may include an adaptive
mechanism to set the ill-conditioned cases threshold to improve
performance in varying cases.

Note that the antialiasing functions introduce a delay in the path,
respectively half and one-sample delay for first and second-order functions.

Also note that due to division by differences, it is vital to use
double-precision or more to reduce errors.

The environment identifier for this library is `aa`. After importing
the standard libraries in Faust, the functions below can be called as `aa.function_name`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/aanl.lib](https://github.com/grame-cncm/faustlibraries/blob/master/aanl.lib)
* Reducing the Aliasing in Nonlinear Waveshaping Using Continuous-time Convolution,
Julian Parker, Vadim Zavalishin, Efflam Le Bivic, DAFX, 2016
* [http://dafx16.vutbr.cz/dafxpapers/20-DAFx-16_paper_41-PN.pdf](http://dafx16.vutbr.cz/dafxpapers/20-DAFx-16_paper_41-PN.pdf)

## Auxiliary Functions


----

### `(aa.)clip`

Clipping function.

----

### `(aa.)Rsqrt`

Real-valued sqrt().

----

### `(aa.)Rlog`

Real-valued log().

----

### `(aa.)Rtan`

Real-valued tan().

----

### `(aa.)Racos`

Real-valued acos().

----

### `(aa.)Rasin`

Real-valued asin().

----

### `(aa.)Racosh`

Real-valued acosh()

----

### `(aa.)Rcosh`

Real-valued cosh().

----

### `(aa.)Rsinh`

Real-valued sinh().

----

### `(aa.)Ratanh`

Real-valued atanh().

----

### `(aa.)ADAA1`

 Generalised first-order ADAA function.

#### Usage

```
_ : ADAA1(EPS, f, F1) : _
```

Where:

* `EPS`: a threshold to handle ill-conditioned cases
* `f`: a function that we want to process with ADAA
* `F1`: f's first antiderivative

----

### `(aa.)ADAA2`

 Generalised second-order ADAA function.

#### Usage

```
_ : ADAA2(EPS, f, F1, F2) : _
```

Where:

* `EPS`: a threshold to handle ill-conditioned cases
* `f`: a function that we want to process with ADAA
* `F1`: f's first antiderivative
* `F2`: f's second antiderivative

## Main functions


##  Saturators 


These antialiased saturators perform best with high-amplitude input
signals. If the input is only slightly saturated, hence producing
negligible aliasing, the trivial saturator may result in a better
overall output, as noise can be introduced by first and second ADAA
at low amplitudes. 

Once determining the lowest saturation level for which the antialiased 
functions perform adequately, it might be sensible to cross-fade
between the trivial and the antialiased saturators according to the
amplitude profile of the input signal.

----

### `(aa.)hardclip`


First-order ADAA hard-clip.

The domain of this function is ℝ; its theoretical range is [-1.0; 1.0].

#### Usage
```
_ : aa.hardclip : _
```

----

### `(aa.)hardclip2`


Second-order ADAA hard-clip.

The domain of this function is ℝ; its theoretical range is [-1.0; 1.0].

#### Usage
```
_ : aa.hardclip2 : _
```

----

### `(aa.)cubic1`


First-order ADAA cubic saturator.

The domain of this function is ℝ; its theoretical range is 
[-2.0/3.0; 2.0/3.0].

#### Usage
```
_ : aa.cubic1 : _
```

----

### `(aa.)parabolic`


First-order ADAA parabolic saturator.

The domain of this function is ℝ; its theoretical range is [-1.0; 1.0].

#### Usage
```
_ : aa.parabolic : _
```

----

### `(aa.)parabolic2`


Second-order ADAA parabolic saturator.

The domain of this function is ℝ; its theoretical range is [-1.0; 1.0].

#### Usage
```
_ : aa.parabolic : _
```

----

### `(aa.)hyperbolic`


First-order ADAA hyperbolic saturator.

The domain of this function is ℝ; its theoretical range is ]-1.0; 1.0[.

#### Usage
```
_ : aa.hyperbolic : _
```

----

### `(aa.)hyperbolic2`


Second-order ADAA hyperbolic saturator.

The domain of this function is ℝ; its theoretical range is ]-1.0; 1.0[.

#### Usage
```
_ : aa.hyperbolic2 : _
```

----

### `(aa.)sinarctan`


First-order ADAA sin(atan()) saturator.

The domain of this function is ℝ; its theoretical range is ]-1.0; 1.0[.

#### Usage
```
_ : aa.sinatan : _
```

----

### `(aa.)sinarctan2`


Second-order ADAA sin(atan()) saturator.

The domain of this function is ℝ; its theoretical range is ]-1.0; 1.0[.

#### Usage
```
_ : aa.sinarctan2 : _
```

----

### `(aa.)tanh1`


First-order ADAA tanh() saturator.

The domain of this function is ℝ; its theoretical range is ]-1.0; 1.0[.

#### Usage
```
_ : aa.tanh1 : _
```

----

### `(aa.)arctan`


First-order ADAA atan().

The domain of this function is ℝ; its theoretical range is ]-π/2.0; π/2.0[.

#### Usage
```
_ : aa.arctan : _
```

----

### `(aa.)arctan2`


Second-order ADAA atan().

The domain of this function is ℝ; its theoretical range is ]-π/2.0; π/2.0[.

#### Usage
```
_ : aa.arctan2 : _
```

----

### `(aa.)asinh1`


First-order ADAA asinh() saturator (unbounded).

The domain of this function is ℝ; its theoretical range is ℝ.

#### Usage
```
_ : aa.asinh1 : _
```

----

### `(aa.)asinh2`


Second-order ADAA asinh() saturator (unbounded).

The domain of this function is ℝ; its theoretical range is ℝ.

#### Usage
```
_ : aa.asinh2 : _
```

##  Trigonometry 

These functions are reliable if input signals are within their domains.

----

### `(aa.)cosine1`


First-order ADAA cos().

The domain of this function is ℝ; its theoretical range is [-1.0; 1.0].

#### Usage
```
_ : aa.cosine1 : _
```

----

### `(aa.)cosine2`


Second-order ADAA cos().

The domain of this function is ℝ; its theoretical range is [-1.0; 1.0].

#### Usage
```
_ : aa.cosine2 : _
```

----

### `(aa.)arccos`


First-order ADAA acos().

The domain of this function is [-1.0; 1.0]; its theoretical range is
[π; 0.0].

#### Usage
```
_ : aa.arccos : _
```

----

### `(aa.)arccos2`


Second-order ADAA acos().

The domain of this function is [-1.0; 1.0]; its theoretical range is 
[π; 0.0].

Note that this function is not accurate for low-amplitude or low-frequency 
input signals. In that case, the first-order ADAA arccos() can be used.

#### Usage
```
_ : aa.arccos2 : _
```

----

### `(aa.)acosh1`


First-order ADAA acosh(). 

The domain of this function is ℝ >= 1.0; its theoretical range is ℝ >= 0.0.

#### Usage
```
_ : aa.acosh1 : _
```

----

### `(aa.)acosh2`


Second-order ADAA acosh().

The domain of this function is ℝ >= 1.0; its theoretical range is ℝ >= 0.0.

Note that this function is not accurate for low-frequency input signals. 
In that case, the first-order ADAA acosh() can be used.

#### Usage
```
_ : aa.acosh2 : _
```

----

### `(aa.)sine`


First-order ADAA sin().

The domain of this function is ℝ; its theoretical range is ℝ.

#### Usage
```
_ : aa.sine : _
```

----

### `(aa.)sine2`


Second-order ADAA sin().

The domain of this function is ℝ; its theoretical range is ℝ.

#### Usage
```
_ : aa.sine2 : _
```

----

### `(aa.)arcsin`


First-order ADAA asin().

The domain of this function is [-1.0, 1.0]; its theoretical range is 
[-π/2.0; π/2.0].

#### Usage
```
_ : aa.arcsin : _
```

----

### `(aa.)arcsin2`


Second-order ADAA asin().

The domain of this function is [-1.0, 1.0]; its theoretical range is
[-π/2.0; π/2.0].

Note that this function is not accurate for low-frequency input signals.
In that case, the first-order ADAA asin() can be used.

#### Usage
```
_ : aa.arcsin2 : _
```

----

### `(aa.)tangent`


First-order ADAA tan().

The domain of this function is [-π/2.0; π/2.0]; its theoretical range is ℝ.

#### Usage
```
_ : aa.tangent : _
```

----

### `(aa.)atanh1`


First-order ADAA atanh(). 

The domain of this function is ]-1.0; 1.0[; its theoretical range is ℝ.

#### Usage
```
_ : aa.atanh1 : _
```

----

### `(aa.)atanh2`


Second-order ADAA atanh().

The domain of this function is ]-1.0; 1.0[; its theoretical range is ℝ.

#### Usage
```
_ : aa.atanh2 : _
```
