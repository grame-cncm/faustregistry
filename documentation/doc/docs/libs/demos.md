#  demos.lib 

This library contains a set of demo functions based on examples located in the
`/examples` folder. Its official prefix is `dm`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/demos.lib](https://github.com/grame-cncm/faustlibraries/blob/master/demos.lib)

## Analyzers


----

### `(dm.)mth_octave_spectral_level_demo`

Demonstrate mth_octave_spectral_level in a standalone GUI.

#### Usage
```
_ : mth_octave_spectral_level_demo(BandsPerOctave) : _
_ : spectral_level_demo : _ // 2/3 octave
```

## Filters


----

### `(dm.)parametric_eq_demo`

A parametric equalizer application.

#### Usage:

```
_ : parametric_eq_demo : _
```

----

### `(dm.)spectral_tilt_demo`

A spectral tilt application.

#### Usage

```
_ : spectral_tilt_demo(N) : _ 
```

Where:

* `N`: filter order (integer)

All other parameters interactive

----

### `(dm.)mth_octave_filterbank_demo` and `(dm.)filterbank_demo`

Graphic Equalizer: each filter-bank output signal routes through a fader.

#### Usage

```
_ : mth_octave_filterbank_demo(M) : _
_ : filterbank_demo : _
```

Where:

* `M`: number of bands per octave

## Effects


----

### `(dm.)cubicnl_demo`

Distortion demo application.

#### Usage:

```
_ : cubicnl_demo : _
```

----

### `(dm.)gate_demo`

Gate demo application.

#### Usage

```
_,_ : gate_demo : _,_
```

----

### `(dm.)compressor_demo`

Compressor demo application.

#### Usage

```
_,_ : compressor_demo : _,_
```

----

### `(dm.)moog_vcf_demo`

Illustrate and compare all three Moog VCF implementations above.

#### Usage

```
_ : moog_vcf_demo : _
```

----

### `(dm.)wah4_demo`

Wah pedal application.

#### Usage

```
_ : wah4_demo : _
```

----

### `(dm.)crybaby_demo`

Crybaby effect application.

#### Usage

```
_ : crybaby_demo : _
```

----

### `(dm.)flanger_demo`

Flanger effect application.

#### Usage

```
_,_ : flanger_demo : _,_
```

----

### `(dm.)phaser2_demo`

Phaser effect demo application.

#### Usage

```
_,_ : phaser2_demo : _,_
```

----

### `(dm.)tapeStop_demo`

Stereo tape-stop effect.

#### Usage

```
_,_ : tapeStop_demo : _,_
```

## Reverbs


----

### `(dm.)freeverb_demo`

Freeverb demo application.

#### Usage

```
_,_ : freeverb_demo : _,_
```

----

### `(dm.)stereo_reverb_tester`

Handy test inputs for reverberator demos below.

#### Usage

```
_,_ : stereo_reverb_tester(gui_group) : _,_
```
For suppressing the `gui_group` input, pass it as `!`.
(See `(dm.)fdnrev0_demo` for an example of its use).

----

### `(dm.)fdnrev0_demo`

A reverb application using `fdnrev0`.

#### Usage

```
_,_,_,_ : fdnrev0_demo(N,NB,BBSO) : _,_
```

Where:

* `N`: feedback Delay Network (FDN) order / number of delay lines used =
   order of feedback matrix / 2, 4, 8, or 16 [extend primes array below for
   32, 64, ...]
* `NB`: number of frequency bands / Number of (nearly) independent T60 controls
   / Integer 3 or greater
* `BBSO` : butterworth band-split order / order of lowpass/highpass bandsplit
   used at each crossover freq / odd positive integer

----

### `(dm.)zita_rev_fdn_demo`

Reverb demo application based on `zita_rev_fdn`.

#### Usage

```
si.bus(8) : zita_rev_fdn_demo : si.bus(8)
```

----

### `(dm.)zita_light`

Light version of `dm.zita_rev1` with only 2 UI elements.

#### Usage

```
_,_ : zita_light : _,_
```

----

### `(dm.)zita_rev1`

Example GUI for `zita_rev1_stereo` (mostly following the Linux `zita-rev1` GUI).

Only the dry/wet and output level parameters are "dezippered" here. If
parameters are to be varied in real time, use `smooth(0.999)` or the like
in the same way.

#### Usage

```
_,_ : zita_rev1 : _,_
```

#### Reference

* [http://www.kokkinizita.net/linuxaudio/zita-rev1-doc/quickguide.html](http://www.kokkinizita.net/linuxaudio/zita-rev1-doc/quickguide.html)

----

### `(dm.)vital_rev_demo`

Example GUI for `vital_rev` with all parameters exposed.

#### Usage

```
_,_ : vital_rev_demo : _,_
```


----

### `(dm.)reverbTank_demo`


This is a stereo reverb following the "ReverbTank" example in [1],
although some parameter ranges and scaling have been adjusted.
It is an unofficial version of the Spin Semiconductor® Reverb.
Other relevant instructional material can be found in [2-4].

#### Usage
```
_,_ : reverbTank_demo : _,_
```

#### References
* [1] Pirkle, W. C. (2019). Designing audio effect plugins in C++ (2nd ed.). Chapter 17.14.

* [2] Spin Semiconductor. (n.d.). Reverberation. Retrieved 2024-04-16, from [http://www.spinsemi.com/knowledge_base/effects.html#Reverberation](http://www.spinsemi.com/knowledge_base/effects.html#Reverberation)

* [3] Zölzer, U. (2022). Digital audio signal processing (3rd ed.). Chapter 7, Figure 7.39.

* [4] Valhalla DSP. (2010, August 25). RIP Keith Barr. Retrieved 2024-04-16, from [https://valhalladsp.com/2010/08/25/rip-keith-barr/](https://valhalladsp.com/2010/08/25/rip-keith-barr/)

----

### `(dm.)dattorro_rev_demo`

Example GUI for `dattorro_rev` with all parameters exposed and additional
dry/wet and output gain control.

#### Usage

```
_,_ : dattorro_rev_demo : _,_
```


----

### `(dm.)jprev_demo`

Example GUI for `jprev` with all parameters exposed. 

#### Usage

```
_,_ : jprev_demo : _,_
```


----

### `(dm.)greyhole_demo`

Example GUI for `greyhole` with all parameters exposed. 

#### Usage

```
_,_ : greyhole_demo : _,_
```


## Generators


----

### `(dm.)sawtooth_demo`

An application demonstrating the different sawtooth oscillators of Faust.

#### Usage

```
sawtooth_demo : _
```

----

### `(dm.)virtual_analog_oscillator_demo`

Virtual analog oscillator demo application.

#### Usage

```
virtual_analog_oscillator_demo : _
```

----

### `(dm.)oscrs_demo` 

Simple application demoing filter based oscillators.

#### Usage

```
oscrs_demo : _
```

----

### `(dm.)velvet_noise_demo`

Listen to velvet_noise!

#### Usage

```
velvet_noise_demo : _
```

----

### `(dm.)latch_demo`

Illustrate latch operation.

#### Usage

```
echo 'import("stdfaust.lib");' > latch_demo.dsp
echo 'process = dm.latch_demo;' >> latch_demo.dsp
faust2octave latch_demo.dsp
Octave:1> plot(faustout);
```

----

### `(dm.)envelopes_demo`

Illustrate various envelopes overlaid, including their gate * 1.1.

#### Usage

```
echo 'import("stdfaust.lib");' > envelopes_demo.dsp
echo 'process = dm.envelopes_demo;' >> envelopes_demo.dsp
faust2octave envelopes_demo.dsp
Octave:1> plot(faustout);
```

----

### `(dm.)fft_spectral_level_demo`

Make a real-time spectrum analyzer using FFT from analyzers.lib.

#### Usage

```
echo 'import("stdfaust.lib");' > fft_spectral_level_demo.dsp
echo 'process = dm.fft_spectral_level_demo;' >> fft_spectral_level_demo.dsp
Mac:
  faust2caqt fft_spectral_level_demo.dsp
  open fft_spectral_level_demo.app
Linux GTK:
  faust2jack fft_spectral_level_demo.dsp
  ./fft_spectral_level_demo
Linux QT:
  faust2jaqt fft_spectral_level_demo.dsp
  ./fft_spectral_level_demo
```

----

### `(dm.)reverse_echo_demo(nChans)`

Multichannel echo effect with reverse delays.

#### Usage

```
echo 'import("stdfaust.lib");' > reverse_echo_demo.dsp
echo 'nChans = 3; // Any integer > 1 should work here' >> reverse_echo_demo.dsp
echo 'process = dm.reverse_echo_demo(nChans);' >> reverse_echo_demo.dsp
Mac:
  faust2caqt reverse_echo_demo.dsp
  open reverse_echo_demo.app
Linux GTK:
  faust2jack reverse_echo_demo.dsp
  ./reverse_echo_demo
Linux QT:
  faust2jaqt reverse_echo_demo.dsp
  ./reverse_echo_demo
Etc.
```

----

### `(dm.)pospass_demo`

Use Positive-Pass Filter pospass() to frequency-shift a sine tone.
First, a real sinusoid is converted to its analytic-signal form
using pospass() to filter out its negative frequency component.
Next, it is multiplied by a modulating complex sinusoid at the
shifting frequency to create the frequency-shifted result.
The real and imaginary parts are output to channels 1 & 2.
For a more interesting frequency-shifting example, check the
"Use Mic" checkbox to replace the input sinusoid by mic input.
Note that frequency shifting is not the same as frequency scaling.
A frequency-shifted harmonic signal is usually not harmonic.
Very small frequency shifts give interesting chirp effects when
there is feedback around the frequency shifter.

#### Usage

```
echo 'import("stdfaust.lib");' > pospass_demo.dsp
echo 'process = dm.pospass_demo;' >> pospass_demo.dsp
Mac:
  faust2caqt pospass_demo.dsp
  open pospass_demo.app
Linux GTK:
  faust2jack pospass_demo.dsp
  ./pospass_demo
Linux QT:
  faust2jaqt pospass_demo.dsp
  ./pospass_demo
Etc.
```

----

### `(dm.)exciter`

Psychoacoustic harmonic exciter, with GUI.

#### Usage

```
_ : exciter : _
```

#### References

* [https://secure.aes.org/forum/pubs/ebriefs/?elib=16939](https://secure.aes.org/forum/pubs/ebriefs/?elib=16939)
* [https://www.researchgate.net/publication/258333577_Modeling_the_Harmonic_Exciter](https://www.researchgate.net/publication/258333577_Modeling_the_Harmonic_Exciter)

----

### `(dm.)vocoder_demo`

Use example of the vocoder function where an impulse train is used
as excitation.

#### Usage

```
_ : vocoder_demo : _
```

----

### `(dm.)colored_noise_demo`

A coloured noise signal generator.

#### Usage

```
colored_noise_demo : _
```

