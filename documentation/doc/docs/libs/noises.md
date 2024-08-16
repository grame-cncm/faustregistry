#  noises.lib 

Faust Noise Generator Library. Its official prefix is `no`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/noises.lib](https://github.com/grame-cncm/faustlibraries/blob/master/noises.lib)

## Functions Reference


----

### `(no.)noise`

White noise generator (outputs random number between -1 and 1).
`noise` is a standard Faust function.

#### Usage

```
noise : _
```

----

### `(no.)multirandom`

Generates multiple decorrelated random numbers in parallel.

#### Usage
```
multirandom(N) : si.bus(N)
```

Where:

* `N`: the number of decorrelated random numbers in parallel, a constant numerical expression

----

### `(no.)multinoise`

Generates multiple decorrelated noises in parallel.

#### Usage

```
multinoise(N) : si.bus(N)
```

Where:

* `N`: the number of decorrelated random numbers in parallel, a constant numerical expression

----

### `(no.)noises`

A convenient wrapper around multinoise.

#### Usage

```
noises(N,i) : _
```

Where:

* `N`: the number of decorrelated random numbers in parallel, a constant numerical expression
* `i`: the selected random number (i in [0..N[)

----

### `(no.)randomseed`

A random seed based on the foreign function `arc4random`
(see man arc4random). Used in `rnoise`, `rmultirandom`, etc. to 
avoid having the same pseudo random sequence at each run.

WARNING: using the foreign function `arc4random`, so only available in C/C++ and LLVM backends.

#### Usage

```
randomseed : _
```


----

### `(no.)rnoise`

A randomized white noise generator (outputs random number between -1 and 1).

WARNING: using the foreign function `arc4random`, so only available in C/C++ and LLVM backends.

#### Usage

```
rnoise : _
```

----

### `(no.)rmultirandom`

Generates multiple decorrelated random numbers in parallel.

WARNING: using the foreign function `arc4random`, so only available in C/C++ and LLVM backends.

#### Usage
```
rmultirandom(N) : _
```

Where:

* `N`: the number of decorrelated random numbers in parallel, a constant numerical expression

----

### `(no.)rmultinoise`

Generates multiple decorrelated noises in parallel.

WARNING: using the foreign function `arc4random`, so only available in C/C++ and LLVM backends.

#### Usage

```
rmultinoise(N) : _
```

Where:

* `N`: the number of decorrelated random numbers in parallel, a constant numerical expression

----

### `(no.)rnoises`

A convenient wrapper around rmultinoise.

WARNING: using the foreign function `arc4random`, so only available in C/C++ and LLVM backends.

#### Usage

```
rnoises(N,i) : _
```

Where:

* `N`: the number of decorrelated random numbers in parallel
* `i`: the selected random number (i in [0..N[)

----

### `(no.)pink_noise`

Pink noise (1/f noise) generator (third-order approximation covering the audio band well).
`pink_noise` is a standard Faust function.

#### Usage
```
pink_noise : _
```

#### Reference
* [https://ccrma.stanford.edu/~jos/sasp/Example_Synthesis_1_F_Noise.html](https://ccrma.stanford.edu/~jos/sasp/Example_Synthesis_1_F_Noise.html)

#### Alternatives
Higher-order approximations covering any frequency band can be obtained using
```
no.noise : fi.spectral_tilt(order,lowerBandLimit,Bandwidth,p)
```
where `p=-0.5` means filter rolloff `f^(-1/2)` which gives 1/f rolloff in the
power spectral density, and can be changed to other real values.

#### Example
// pink_noise_compare.dsp - compare three pinking filters
```
process = pink_noises with {
    f0 = 35; // Lower bandlimit in Hz
    bw3 = 0.7 * ma.SR/2.0 - f0; // Bandwidth in Hz, 3rd order case
    bw9 = 0.8 * ma.SR/2.0 - f0; // Bandwidth in Hz, 9th order case
    pink_tilt_3 = fi.spectral_tilt(3,f0,bw3,-0.5);
    pink_tilt_9 = fi.spectral_tilt(9,f0,bw9,-0.5);
    pink_noises = 1-1' <:
      no.pink_filter, // original designed by invfreqz in Octave
      pink_tilt_3,    // newer method using the same filter order
      pink_tilt_9;    // newer method using a higher filter order
};
```

#### Output of Example
```
faust2octave pink_noise_compare.dsp
Octave:1> semilogx(20*log10(abs(fft(faustout,8192))(1:4096,:)));
...
```
<img alt="pink_noise_demo figure" src="https://ccrma.stanford.edu/wiki/Images/8/86/Tpinkd.jpg" width="600" />

----

### `(no.)pink_noise_vm`

Multi pink noise generator.

#### Usage

```
pink_noise_vm(N) : _
```

Where:

* `N`: number of latched white-noise processes to sum,
	not to exceed sizeof(int) in C++ (typically 32).

#### References

* [http://www.dsprelated.com/showarticle/908.php](http://www.dsprelated.com/showarticle/908.php)
* [http://www.firstpr.com.au/dsp/pink-noise/#Voss-McCartney](http://www.firstpr.com.au/dsp/pink-noise/#Voss-McCartney)

----

### `(no.)lfnoise`, `(no.)lfnoise0` and `(no.)lfnoiseN`

Low-frequency noise generators (Butterworth-filtered downsampled white noise).

#### Usage

```
lfnoise0(rate) : _   // new random number every int(SR/rate) samples or so
lfnoiseN(N,rate) : _ // same as "lfnoise0(rate) : lowpass(N,rate)" [see filters.lib]
lfnoise(rate) : _    // same as "lfnoise0(rate) : seq(i,5,lowpass(N,rate))" (no overshoot)
```

#### Example

(view waveforms in faust2octave):

```
rate = SR/100.0; // new random value every 100 samples (SR from music.lib)
process = lfnoise0(rate),   // sampled/held noise (piecewise constant)
          lfnoiseN(3,rate), // lfnoise0 smoothed by 3rd order Butterworth LPF
          lfnoise(rate);    // lfnoise0 smoothed with no overshoot
```

----

### `(no.)sparse_noise`

Sparse noise generator.

#### Usage

```
sparse_noise(f0) : _
```

Where:

* ` f0`: average frequency of noise impulses per second

Random impulses in the amplitude range -1 to 1 are generated
at an average rate of f0 impulses per second.

#### Reference

* See velvet_noise

----

### `(no.)velvet_noise_vm`

Velvet noise generator.

#### Usage

```
velvet_noise(amp, f0) : _
```

Where:

* `amp`: amplitude of noise impulses (positive and negative)
* ` f0`: average frequency of noise impulses per second

#### Reference

* Matti Karjalainen and Hanna Jarvelainen,
  "Reverberation Modeling Using Velvet Noise",
  in Proc. 30th Int. Conf. Intelligent Audio Environments (AES07),
  March 2007.


----

### `(no.)gnoise`

Approximate zero-mean, unit-variance Gaussian white noise generator.

#### Usage

```
gnoise(N) : _
```

Where:

* `N`: number of uniform random numbers added to approximate Gaussian white noise

#### Reference

* See Central Limit Theorem


----

### `(no.)colored_noise`

Generates a colored noise signal with an arbitrary spectral
roll-off factor (alpha) over the entire audible frequency range
(20-20000 Hz). The output is normalized so that an equal RMS
level is maintained for different values of alpha.

#### Usage

```
colored_noise(N,alpha) : _
```

Where:

* `N`: desired integer filter order (constant numerical expression)
* `alpha`: slope of roll-off, between -1 and 1. -1 corresponds to 
brown/red noise, -1/2 pink noise, 0 white noise, 1/2 blue noise,
and 1 violet/azure noise.

#### Examples
See `dm.colored_noise_demo`.

