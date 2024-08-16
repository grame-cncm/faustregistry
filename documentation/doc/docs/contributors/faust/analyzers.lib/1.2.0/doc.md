#  analyzers.lib 

Analyzers library. Its official prefix is `an`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/analyzers.lib](https://github.com/grame-cncm/faustlibraries/blob/master/analyzers.lib)

## Amplitude Tracking


----

### `(an.)abs_envelope_rect`

Absolute value average with moving-average algorithm.

#### Usage

```
_ : abs_envelope_rect(period) : _
```

Where:

* `period`: sets the averaging frame in seconds

----

### `(an.)abs_envelope_tau`

Absolute value average with one-pole lowpass and tau response 
(see [filters.lib](https://faustlibraries.grame.fr/libs/filters/)).

#### Usage

```
_ : abs_envelope_tau(period) : _
```

Where:

* `period`: (time to decay by 1/e) sets the averaging frame in secs

----

### `(an.)abs_envelope_t60`

Absolute value average with one-pole lowpass and t60 response
(see [filters.lib](https://faustlibraries.grame.fr/libs/filters/)).

#### Usage

```
_ : abs_envelope_t60(period) : _
```

Where:

* `period`: (time to decay by 60 dB) sets the averaging frame in secs

----

### `(an.)abs_envelope_t19`

Absolute value average with one-pole lowpass and t19 response
(see [filters.lib](https://faustlibraries.grame.fr/libs/filters/)).

#### Usage

```
_ : abs_envelope_t19(period) : _
```

Where:

* `period`: (time to decay by 1/e^2.2) sets the averaging frame in secs

----

### `(an.)amp_follower`

Classic analog audio envelope follower with infinitely fast rise and
exponential decay.  The amplitude envelope instantaneously follows
the absolute value going up, but then floats down exponentially.

`amp_follower` is a standard Faust function.

#### Usage

```
_ : amp_follower(rel) : _
```

Where:

* `rel`: release time = amplitude-envelope time-constant (sec) going down

#### References

* Musical Engineer's Handbook, Bernie Hutchins, Ithaca NY
* 1975 Electronotes Newsletter, Bernie Hutchins

----

### `(an.)amp_follower_ud`

Envelope follower with different up and down time-constants
(also called a "peak detector").

#### Usage

```
   _ : amp_follower_ud(att,rel) : _
```

Where:

* `att`: attack time = amplitude-envelope time constant (sec) going up
* `rel`: release time = amplitude-envelope time constant (sec) going down

#### Note

We assume rel >> att.  Otherwise, consider rel ~ max(rel,att).
For audio, att is normally faster (smaller) than rel (e.g., 0.001 and 0.01).
Use `amp_follower_ar` below to remove this restriction.

#### Reference

* "Digital Dynamic Range Compressor Design --- A Tutorial and Analysis", by
  Dimitrios Giannoulis, Michael Massberg, and Joshua D. Reiss
*   [https://www.eecs.qmul.ac.uk/~josh/documents/2012/GiannoulisMassbergReiss-dynamicrangecompression-JAES2012.pdf](https://www.eecs.qmul.ac.uk/~josh/documents/2012/GiannoulisMassbergReiss-dynamicrangecompression-JAES2012.pdf)

----

### `(an.)amp_follower_ar`

Envelope follower with independent attack and release times. The
release can be shorter than the attack (unlike in `amp_follower_ud`
above).

#### Usage

```
_ : amp_follower_ar(att,rel) : _
```

Where:

* `att`: attack time = amplitude-envelope time constant (sec) going up
* `rel`: release time = amplitude-envelope time constant (sec) going down


----

### `(an.)ms_envelope_rect`

Mean square with moving-average algorithm.

#### Usage

```
_ : ms_envelope_rect(period) : _
```

Where:

* `period`: sets the averaging frame in secs

----

### `(an.)ms_envelope_tau`

Mean square average with one-pole lowpass and tau response
(see [filters.lib](https://faustlibraries.grame.fr/libs/filters/)).

#### Usage

```
_ : ms_envelope_tau(period) : _
```

Where:

* `period`: (time to decay by 1/e) sets the averaging frame in secs

----

### `(an.)ms_envelope_t60`

Mean square with one-pole lowpass and t60 response 
(see [filters.lib](https://faustlibraries.grame.fr/libs/filters/)).

#### Usage

```
_ : ms_envelope_t60(period) : _
```

Where:

* `period`: (time to decay by 60 dB) sets the averaging frame in secs

----

### `(an.)ms_envelope_t19`

Mean square with one-pole lowpass and t19 response 
(see [filters.lib](https://faustlibraries.grame.fr/libs/filters/)).

#### Usage

```
_ : ms_envelope_t19(period) : _
```

Where:

* `period`: (time to decay by 1/e^2.2) sets the averaging frame in secs

----

### `(an.)rms_envelope_rect`

Root mean square with moving-average algorithm.

#### Usage

```
_ : rms_envelope_rect(period) : _
```

Where:

* `period`: sets the averaging frame in secs

----

### `(an.)rms_envelope_tau`

Root mean square with one-pole lowpass and tau response 
(see [filters.lib](https://faustlibraries.grame.fr/libs/filters/)).

#### Usage

```
_ : rms_envelope_tau(period) : _
```

Where:

* `period`: (time to decay by 1/e) sets the averaging frame in secs

----

### `(an.)rms_envelope_t60`

Root mean square with one-pole lowpass and t60 response 
(see [filters.lib](https://faustlibraries.grame.fr/libs/filters/)).

#### Usage

```
_ : rms_envelope_t60(period) : _
```

Where:

* `period`: (time to decay by 60 dB) sets the averaging frame in secs

----

### `(an.)rms_envelope_t19`

Root mean square with one-pole lowpass and t19 response 
(see [filters.lib](https://faustlibraries.grame.fr/libs/filters/)).

#### Usage

```
_ : rms_envelope_t19(period) : _
```

Where:

* `period`: (time to decay by 1/e^2.2) sets the averaging frame in secs

----

### `(an.)zcr`

Zero-crossing rate (ZCR) with one-pole lowpass averaging based on the tau 
constant. It outputs an index between 0 and 1 at a desired analysis frame. 
The ZCR of a signal correlates with the noisiness [Gouyon et al. 2000] and 
the spectral centroid [Herrera-Boyer et al. 2006] of a signal. 
For sinusoidal signals, the ZCR can be multiplied by ma.SR/2 and used
as a frequency detector. For example, it can be deployed as a
computationally efficient adaptive mechanism for automatic Larsen
suppression.

#### Usage

```
_ : zcr(tau) : _
```

Where:

* `tau`: (time to decay by e^-1) sets the averaging frame in seconds.

## Adaptive Frequency Analysis


----

### `(an.)pitchTracker`


This function implements a pitch-tracking algorithm by means of 
zero-crossing rate analysis and adaptive low-pass filtering. The design
is based on the algorithm described in [this tutorial (section 2.2)](https://pdfslide.net/documents/faust-tutorial2.html).

#### Usage

```
_ : pitchTracker(N, tau) : _
```

Where:

* `N`: a constant numerical expression, sets the order of the low-pass filter, which
 determines the sensitivity of the algorithm for signals where partials are
 stronger than the fundamental frequency.
* `tau`: response time in seconds based on exponentially-weighted averaging with tau time-constant. See [https://ccrma.stanford.edu/~jos/st/Exponentials.html](https://ccrma.stanford.edu/~jos/st/Exponentials.html).

----

### `(an.)spectralCentroid`


This function implements a time-domain spectral centroid by means of RMS 
measurements and adaptive crossover filtering. The weight difference of the
upper and lower spectral powers are used to recursively adjust the crossover
cutoff so that the system (minimally) oscillates around a balancing point.

Unlike block processing techniques such as FFT, this algorithm provides
continuous measurements and fast response times. Furthermore, when providing
input signals that are spectrally sparse, the algorithm will output a 
logarithmic measure of the centroid, which is perceptually desirable for
musical applications. For example, if the input signal is the combination
of three tones at 1000, 2000, and 4000 Hz, the centroid will be the middle
octave.

#### Usage

```
_ : spectralCentroid(nonlinearity, tau) : _
```

Where:

* `nonlinearity`: a boolean to activate or deactivate nonlinear integration. The 
 nonlinear function is useful to improve stability with very short response times 
 such as .001 <= tau <= .005 , otherwise, the nonlinearity may reduce precision.
* `tau`: response time in seconds based on exponentially-weighted averaging with tau time-constant. See [https://ccrma.stanford.edu/~jos/st/Exponentials.html](https://ccrma.stanford.edu/~jos/st/Exponentials.html).

#### Reference:
 Sanfilippo, D. (2021). Time-Domain Adaptive Algorithms for Low- and High-Level 
 Audio Information Processing. Computer Music Journal, 45(1), 24-38.

#### Example:

 `process = os.osc(500) + os.osc(1000) + os.osc(2000) + os.osc(4000) + os.osc(8000) : an.spectralCentroid(1, .001);`


## Spectrum-Analyzers

Spectrum-analyzers split the input signal into a bank of parallel signals, one for
each spectral band. They are related to the Mth-Octave Filter-Banks in `filters.lib`.
The documentation of this library contains more details about the implementation.
The parameters are:

* `M`: number of band-slices per octave (>1)
* `N`: total number of bands (>2)
* `ftop` = upper bandlimit of the Mth-octave bands (<SR/2)

In addition to the Mth-octave output signals, there is a highpass signal
containing frequencies from ftop to SR/2, and a "dc band" lowpass signal
containing frequencies from 0 (dc) up to the start of the Mth-octave bands.
Thus, the N output signals are:
```
highpass(ftop), MthOctaveBands(M,N-2,ftop), dcBand(ftop*2^(-M*(N-1)))
```

A Spectrum-Analyzer is defined here as any band-split whose bands span
the relevant spectrum, but whose band-signals do not
necessarily sum to the original signal, either exactly or to within an
allpass filtering. Spectrum analyzer outputs are normally at least nearly
"power complementary", i.e., the power spectra of the individual bands
sum to the original power spectrum (to within some negligible tolerance).

#### Increasing Channel Isolation

Go to higher filter orders - see Regalia et al. or Vaidyanathan (cited
below) regarding the construction of more aggressive recursive
filter-banks using elliptic or Chebyshev prototype filters.

#### References

* "Tree-structured complementary filter banks using all-pass sections",
  Regalia et al., IEEE Trans. Circuits & Systems, CAS-34:1470-1484, Dec. 1987
* "Multirate Systems and Filter Banks", P. Vaidyanathan, Prentice-Hall, 1993
* Elementary filter theory: [https://ccrma.stanford.edu/~jos/filters/](https://ccrma.stanford.edu/~jos/filters/)

----

### `(an.)mth_octave_analyzer`

Octave analyzer.
`mth_octave_analyzer[N]` are standard Faust functions.

#### Usage
```
_ : mth_octave_analyzer(O,M,ftop,N) : par(i,N,_) // Oth-order Butterworth
_ : mth_octave_analyzer6e(M,ftop,N) : par(i,N,_) // 6th-order elliptic
```

Also for convenience:

```
_ : mth_octave_analyzer3(M,ftop,N) : par(i,N,_) // 3d-order Butterworth
_ : mth_octave_analyzer5(M,ftop,N) : par(i,N,_) // 5th-order Butterworth
mth_octave_analyzer_default = mth_octave_analyzer6e;
```

Where:

* `O`: (odd) order of filter used to split each frequency band into two
* `M`: number of band-slices per octave
* `ftop`: highest band-split crossover frequency (e.g., 20 kHz)
* `N`: total number of bands (including dc and Nyquist)

## Mth-Octave Spectral Level

Spectral Level: display (in bargraphs) the average signal level in each spectral band.

----

### `(an.)mth_octave_spectral_level6e`

Spectral level display.

#### Usage:

```
_ : mth_octave_spectral_level6e(M,ftop,NBands,tau,dB_offset) : _
```

Where:

* `M`: bands per octave
* `ftop`: lower edge frequency of top band
* `NBands`: number of passbands (including highpass and dc bands),
* `tau`: spectral display averaging-time (time constant) in seconds,
* `dB_offset`: constant dB offset in all band level meters.

Also for convenience:

```
mth_octave_spectral_level_default = mth_octave_spectral_level6e;
spectral_level = mth_octave_spectral_level(2,10000,20);
```

----

### `(an.)[third|half]_octave_[analyzer|filterbank]`

A bunch of special cases based on the different analyzer functions described above:

```
third_octave_analyzer(N) = mth_octave_analyzer_default(3,10000,N);
third_octave_filterbank(N) = mth_octave_filterbank_default(3,10000,N);
half_octave_analyzer(N) = mth_octave_analyzer_default(2,10000,N);
half_octave_filterbank(N) = mth_octave_filterbank_default(2,10000,N);
octave_filterbank(N) = mth_octave_filterbank_default(1,10000,N);
octave_analyzer(N) = mth_octave_analyzer_default(1,10000,N);
```

#### Usage

See `mth_octave_spectral_level_demo` in `demos.lib`.

## Arbritary-Crossover Filter-Banks and Spectrum Analyzers

These are similar to the Mth-octave analyzers above, except that the
band-split frequencies are passed explicitly as arguments.

----

### `(an.)analyzer`

Analyzer.

#### Usage

```
_ : analyzer(O,freqs) : par(i,N,_) // No delay equalizer
```

Where:

* `O`: band-split filter order (ODD integer required for filterbank[i])
* `freqs`: (fc1,fc2,...,fcNs) [in numerically ascending order], where
          Ns=N-1 is the number of octave band-splits
          (total number of bands N=Ns+1).

If frequencies are listed explicitly as arguments, enclose them in parens:

```
_ : analyzer(3,(fc1,fc2)) : _,_,_
```

##  Fast Fourier Transform (fft) and its Inverse (ifft) 

Sliding FFTs that compute a rectangularly windowed FFT each sample.

----

### `(an.)goertzelOpt` 

Optimized Goertzel filter. 

#### Usage

```
_ : goertzelOpt(freq,n) : _
```

Where:

* `freq`: frequency to be analyzed
* `n`: the Goertzel block size

#### Reference

* [https://en.wikipedia.org/wiki/Goertzel_algorithm](https://en.wikipedia.org/wiki/Goertzel_algorithm)

----

### `(an.)goertzelComp` 

Complex Goertzel filter. 

#### Usage

```
_ : goertzelComp(freq,n) : _
```

Where:

* `freq`: frequency to be analyzed
* `n`: the Goertzel block size

#### Reference

* [https://en.wikipedia.org/wiki/Goertzel_algorithm](https://en.wikipedia.org/wiki/Goertzel_algorithm)

----

### `(an.)goertzel` 

Same as [`goertzelOpt`](#goertzelopt). 

#### Usage

```
_ : goertzel(freq,n) : _
```

Where:

* `freq`: frequency to be analyzed
* `n`: the Goertzel block size

#### Reference

* [https://en.wikipedia.org/wiki/Goertzel_algorithm](https://en.wikipedia.org/wiki/Goertzel_algorithm)

----

### `(an.)fft` 

Fast Fourier Transform (FFT).

#### Usage

```
si.cbus(N) : fft(N) : si.cbus(N)
```

Where:

* `si.cbus(N)` is a bus of N complex signals, each specified by real and imaginary parts:
  (r0,i0), (r1,i1), (r2,i2), ...
* `N` is the FFT size (must be a power of 2: 2,4,8,16,... known at compile time) 
* `fft(N)` performs a length `N` FFT for complex signals (radix 2)
* The output is a bank of N complex signals containing the complex spectrum over time:
  (R0, I0), (R1,I1), ...
  - The dc component is (R0,I0), where I0=0 for real input signals.

FFTs of Real Signals:

* To perform a sliding FFT over a real input signal, you can say
```
process = signal : an.rtocv(N) : an.fft(N);
```
where `an.rtocv` converts a real (scalar) signal to a complex vector signal having a zero imaginary part.

  * See `an.rfft_analyzer_c` (in `analyzers.lib`) and related functions for more detailed usage examples.

  * Use `an.rfft_spectral_level(N,tau,dB_offset)` to display the power spectrum of a real signal.

  * See `dm.fft_spectral_level_demo(N)` in `demos.lib` for an example GUI driving `an.rfft_spectral_level()`.

#### Reference

* [Decimation-in-time (DIT) Radix-2 FFT](https://cnx.org/contents/zmcmahhR@7/Decimation-in-time-DIT-Radix-2)


----

### `(an.)ifft`

Inverse Fast Fourier Transform (IFFT).

#### Usage

```
si.cbus(N) : ifft(N) : si.cbus(N)
```

Where:

* N is the IFFT size (power of 2)
* Input is a complex spectrum represented as interleaved real and imaginary parts:
  (R0, I0), (R1,I1), (R2,I2), ...
* Output is a bank of N complex signals giving the complex signal in the time domain:
  (r0, i0), (r1,i1), (r2,i2), ...
