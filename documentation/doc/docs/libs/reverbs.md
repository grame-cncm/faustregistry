#  reverbs.lib 

A library of reverb effects. Its official prefix is `re`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/reverbs.lib](https://github.com/grame-cncm/faustlibraries/blob/master/reverbs.lib)

## Schroeder Reverberators


----

### `(re.)jcrev`

This artificial reverberator take a mono signal and output stereo
(`satrev`) and quad (`jcrev`). They were implemented by John Chowning
in the MUS10 computer-music language (descended from Music V by Max
Mathews).  They are Schroeder Reverberators, well tuned for their size.
Nowadays, the more expensive freeverb is more commonly used (see the
Faust examples directory).

`jcrev` reverb below was made from a listing of "RV", dated April 14, 1972,
which was recovered from an old SAIL DART backup tape.
John Chowning thinks this might be the one that became the
well known and often copied JCREV.

`jcrev` is a standard Faust function.

#### Usage

```
_ : jcrev : _,_,_,_
```

----

### `(re.)satrev`

This artificial reverberator take a mono signal and output stereo
(`satrev`) and quad (`jcrev`).  They were implemented by John Chowning
in the MUS10 computer-music language (descended from Music V by Max
Mathews).  They are Schroeder Reverberators, well tuned for their size.
Nowadays, the more expensive freeverb is more commonly used (see the
Faust examples directory).

`satrev` was made from a listing of "SATREV", dated May 15, 1971,
which was recovered from an old SAIL DART backup tape.
John Chowning thinks this might be the one used on his
often-heard brass canon sound examples, one of which can be found at
* [https://ccrma.stanford.edu/~jos/wav/FM-BrassCanon2.wav](https://ccrma.stanford.edu/~jos/wav/FM-BrassCanon2.wav).

#### Usage

```
_ : satrev : _,_
```

## Feedback Delay Network (FDN) Reverberators


----

### `(re.)fdnrev0`

Pure Feedback Delay Network Reverberator (generalized for easy scaling).
`fdnrev0` is a standard Faust function.

#### Usage

```
<1,2,4,...,N signals> <:
fdnrev0(MAXDELAY,delays,BBSO,freqs,durs,loopgainmax,nonl) :>
<1,2,4,...,N signals>
```

Where:

* `N`: 2, 4, 8, ...  (power of 2)
* `MAXDELAY`: power of 2 at least as large as longest delay-line length
* `delays`: N delay lines, N a power of 2, lengths preferably coprime
* `BBSO`: odd positive integer = order of bandsplit desired at freqs
* `freqs`: NB-1 crossover frequencies separating desired frequency bands
* `durs`: NB decay times (t60) desired for the various bands
* `loopgainmax`: scalar gain between 0 and 1 used to "squelch" the reverb
* `nonl`: nonlinearity (0 to 0.999..., 0 being linear)

#### Reference

* [https://ccrma.stanford.edu/~jos/pasp/FDN_Reverberation.html](https://ccrma.stanford.edu/~jos/pasp/FDN_Reverberation.html)

----

### `(re.)zita_rev_fdn`

Internal 8x8 late-reverberation FDN used in the FOSS Linux reverb `zita-rev1`
by Fons Adriaensen <fons@linuxaudio.org>.  This is an FDN reverb with
allpass comb filters in each feedback delay in addition to the
damping filters.

#### Usage

```
si.bus(8) : zita_rev_fdn(f1,f2,t60dc,t60m,fsmax) : si.bus(8)
```

Where:

* `f1`: crossover frequency (Hz) separating dc and midrange frequencies
* `f2`: frequency (Hz) above f1 where T60 = t60m/2 (see below)
* `t60dc`: desired decay time (t60) at frequency 0 (sec)
* `t60m`: desired decay time (t60) at midrange frequencies (sec)
* `fsmax`: maximum sampling rate to be used (Hz)

#### Reference

* [http://www.kokkinizita.net/linuxaudio/zita-rev1-doc/quickguide.html](http://www.kokkinizita.net/linuxaudio/zita-rev1-doc/quickguide.html)
* [https://ccrma.stanford.edu/~jos/pasp/Zita_Rev1.html](https://ccrma.stanford.edu/~jos/pasp/Zita_Rev1.html)

----

### `(re.)zita_rev1_stereo`

Extend `zita_rev_fdn` to include `zita_rev1` input/output mapping in stereo mode.
`zita_rev1_stereo` is a standard Faust function.

#### Usage

```
_,_ : zita_rev1_stereo(rdel,f1,f2,t60dc,t60m,fsmax) : _,_
```

Where:

`rdel`  = delay (in ms) before reverberation begins (e.g., 0 to ~100 ms)
(remaining args and refs as for `zita_rev_fdn` above)

----

### `(re.)zita_rev1_ambi`

Extend `zita_rev_fdn` to include `zita_rev1` input/output mapping in
"ambisonics mode", as provided in the Linux C++ version.

#### Usage

```
_,_ : zita_rev1_ambi(rgxyz,rdel,f1,f2,t60dc,t60m,fsmax) : _,_,_,_
```

Where:

`rgxyz` = relative gain of lanes 1,4,2 to lane 0 in output (e.g., -9 to 9)
  (remaining args and references as for zita_rev1_stereo above)

----

### `(re.)vital_rev`

A port of the reverb from the Vital synthesizer. All input parameters
have been normalized to a continuous [0,1] range, making them easy to modulate.
The scaling of the parameters happens inside the function.

#### Usage

```
_,_ : vital_rev(prelow, prehigh, lowcutoff, highcutoff, lowgain, highgain, chorus_amt, chorus_freq, predelay, time, size, mix) : _,_ 
```

Where:

* `prelow`: In the pre-filter, this is the cutoff frequency of a high-pass filter (hence a low value).
* `prehigh`: In the pre-filter, this is the cutoff frequency of a low-pass filter (hence a high value).
* `lowcutoff`: In the feedback filter stage, this is the cutoff frequency of a low-shelf filter.
* `highcutoff`: In the feedback filter stage, this is the cutoff frequency of a high-shelf filter.
* `lowgain`: In the feedback filter stage, this is the gain of a low-shelf filter.
* `highgain`: In the feedback filter stage, this is the gain of a high-shelf filter.
* `chorus_amt`: The amount of chorus modulation in the main delay lines.
* `chorus_freq`: The LFO rate of chorus modulation in the main delay lines.
* `predelay`: The amount of pre-delay time.
* `time`: The decay time of the reverb.
* `size`: The size of the room.
* `mix`: A wetness value to use in a final dry/wet mixer.

## Freeverb


----

### `(re.)mono_freeverb`

A simple Schroeder reverberator primarily developed by "Jezar at Dreampoint" that
is extensively used in the free-software world. It uses four Schroeder allpasses in
series and eight parallel Schroeder-Moorer filtered-feedback comb-filters for each
audio channel, and is said to be especially well tuned.

`mono_freeverb` is a standard Faust function.

#### Usage

```
_ : mono_freeverb(fb1, fb2, damp, spread) : _
```

Where:

* `fb1`: coefficient of the lowpass comb filters (0-1)
* `fb2`: coefficient of the allpass comb filters (0-1)
* `damp`: damping of the lowpass comb filter (0-1)
* `spread`: spatial spread in number of samples (for stereo)

#### License
While this version is licensed LGPL (with exception) along with other GRAME
library functions, the file freeverb.dsp in the examples directory of older
Faust distributions, such as faust-0.9.85, was released under the BSD license,
which is less restrictive.

----

### `(re.)stereo_freeverb`

A simple Schroeder reverberator primarily developed by "Jezar at Dreampoint" that
is extensively used in the free-software world. It uses four Schroeder allpasses in
series and eight parallel Schroeder-Moorer filtered-feedback comb-filters for each
audio channel, and is said to be especially well tuned.

#### Usage

```
_,_ : stereo_freeverb(fb1, fb2, damp, spread) : _,_
```

Where:

* `fb1`: coefficient of the lowpass comb filters (0-1)
* `fb2`: coefficient of the allpass comb filters (0-1)
* `damp`: damping of the lowpass comb filter (0-1)
* `spread`: spatial spread in number of samples (for stereo)

## Dattorro Reverb


----

### `(re.)dattorro_rev`

Reverberator based on the Dattorro reverb topology. This implementation does
not use modulated delay lengths (excursion).

#### Usage

```
_,_ : dattorro_rev(pre_delay, bw, i_diff1, i_diff2, decay, d_diff1, d_diff2, damping) : _,_
```

Where:

* `pre_delay`: pre-delay in samples (fixed at compile time)
* `bw`: band-width filter (pre filtering); (0 - 1)
* `i_diff1`: input diffusion factor 1; (0 - 1)
* `i_diff2`: input diffusion factor 2;
* `decay`: decay rate; (0 - 1); infinite decay = 1.0
* `d_diff1`: decay diffusion factor 1; (0 - 1)
* `d_diff2`: decay diffusion factor 2;
* `damping`: high-frequency damping; no damping = 0.0

#### Reference

* [https://ccrma.stanford.edu/~dattorro/EffectDesignPart1.pdf](https://ccrma.stanford.edu/~dattorro/EffectDesignPart1.pdf)

----

### `(re.)dattorro_rev_default`

Reverberator based on the Dattorro reverb topology with reverb parameters from the
original paper.
This implementation does not use modulated delay lengths (excursion) and
uses zero length pre-delay.

#### Usage

```
_,_ : dattorro_rev_default : _,_
```

#### Reference

* [https://ccrma.stanford.edu/~dattorro/EffectDesignPart1.pdf](https://ccrma.stanford.edu/~dattorro/EffectDesignPart1.pdf)

## JPverb and Greyhole Reverbs


----

### `(re.)jpverb`

An algorithmic reverb (stereo in/out), inspired by the lush chorused sound 
of certain vintage Lexicon and Alesis reverberation units. 
Designed to sound great with synthetic sound sources, rather than sound like a realistic space.

#### Usage

```
_,_ : jpverb(t60, damp, size, early_diff, mod_depth, mod_freq, low, mid, high, low_cutoff, high_cutoff) : _,_
```

Where:

* `t60`: approximate reverberation time in seconds ([0.1..60] sec) (T60 - the time for the reverb to decay by 60db when damp == 0 ). Does not effect early reflections
* `damp`: controls damping of high-frequencies as the reverb decays. 0 is no damping, 1 is very strong damping. Values should be in the range ([0..1])
* `size`: scales size of delay-lines within the reverberator, producing the impression of a larger or smaller space. Values below 1 can sound metallic. Values should be in the range [0.5..5]
* `early_diff`: controls shape of early reflections. Values of 0.707 or more produce smooth exponential decay. Lower values produce a slower build-up of echoes. Values should be in the range ([0..1])
* `mod_depth`: depth ([0..1]) of delay-line modulation. Use in combination with `mod_freq` to set amount of chorusing within the structure
* `mod_freq`: frequency ([0..10] Hz) of delay-line modulation. Use in combination with `mod_depth` to set amount of chorusing within the structure
* `low`: multiplier ([0..1]) for the reverberation time within the low band
* `mid`: multiplier ([0..1]) for the reverberation time within the mid band
* `high`: multiplier ([0..1]) for the reverberation time within the high band
* `low_cutoff`: frequency (100..6000 Hz) at which the crossover between the low and mid bands of the reverb occurs
* `high_cutoff`: frequency (1000..10000 Hz) at which the crossover between the mid and high bands of the reverb occurs

#### Reference

* [https://doc.sccode.org/Overviews/DEIND.html](https://doc.sccode.org/Overviews/DEIND.html)

----

### `(re.)greyhole`

A complex echo-like effect (stereo in/out), inspired by the classic Eventide effect of a similar name. 
The effect consists of a diffuser (like a mini-reverb, structurally similar to the one used in `jpverb`)
connected in a feedback system with a long, modulated delay-line. 
Excels at producing spacey washes of sound.

#### Usage

```
_,_ : greyhole(dt, damp, size, early_diff, feedback, mod_depth, mod_freq) : _,_
```

Where:

* `dt`: approximate reverberation time in seconds ([0.1..60 sec])
* `damp`: controls damping of high-frequencies as the reverb decays. 0 is no damping, 1 is very strong damping. Values should be between ([0..1])
* `size`: control of relative "room size" roughly in the range ([0.5..3])
* `early_diff`: controls pattern of echoes produced by the diffuser. At very low values, the diffuser acts like a delay-line whose length is controlled by the 'size' parameter. Medium values produce a slow build-up of echoes, giving the sound a reversed-like quality. Values of 0.707 or greater than produce smooth exponentially decaying echoes. Values should be in the range ([0..1])
* `feedback`: amount of feedback through the system. Sets the number of repeating echoes. A setting of 1.0 produces infinite sustain. Values should be in the range ([0..1])
* `mod_depth`: depth ([0..1]) of delay-line modulation. Use in combination with `mod_freq` to produce chorus and pitch-variations in the echoes
* `mod_freq`: frequency ([0..10] Hz) of delay-line modulation. Use in combination with `mod_depth` to produce chorus and pitch-variations in the echoes

#### Reference

* [https://doc.sccode.org/Overviews/DEIND.html](https://doc.sccode.org/Overviews/DEIND.html)
