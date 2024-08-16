#  synths.lib 

This library contains a collection of synthesizers. Its official prefix is `sy`. 

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/synths.lib](https://github.com/grame-cncm/faustlibraries/blob/master/synths.lib)

----

### `(sy.)popFilterDrum`

A simple percussion instrument based on a "popped" resonant bandpass filter.
`popFilterDrum` is a standard Faust function.

#### Usage

```
popFilterDrum(freq,q,gate) : _
```

Where:

* `freq`: the resonance frequency of the instrument in Hz
* `q`: the q of the res filter (typically, 5 is a good value)
* `gate`: the trigger signal (0 or 1)

----

### `(sy.)dubDub`

A simple synth based on a sawtooth wave filtered by a resonant lowpass.
`dubDub` is a standard Faust function.

#### Usage

```
dubDub(freq,ctFreq,q,gate) : _
```

Where:

* `freq`: frequency of the sawtooth in Hz
* `ctFreq`: cutoff frequency of the filter
* `q`: Q of the filter
* `gate`: the trigger signal (0 or 1)

----

### `(sy.)sawTrombone`

A simple trombone based on a lowpassed sawtooth wave.
`sawTrombone` is a standard Faust function.

#### Usage

```
sawTrombone(freq,gain,gate) : _
```

Where:

* `freq`: the frequency in Hz
* `gain`: the gain (0-1)
* `gate`: the gate (0 or 1)

----

### `(sy.)combString`

Simplest string physical model ever based on a comb filter.
`combString` is a standard Faust function.

#### Usage

```
combString(freq,res,gate) : _
```

Where:

* `freq`: the frequency of the string in Hz
* `res`: string T60 (resonance time) in second
* `gate`: trigger signal (0 or 1)

----

### `(sy.)additiveDrum`

A simple drum using additive synthesis.
`additiveDrum` is a standard Faust function.

#### Usage

```
additiveDrum(freq,freqRatio,gain,harmDec,att,rel,gate) : _
```

Where:

* `freq`: the resonance frequency of the drum in Hz
* `freqRatio`: a list of ratio to choose the frequency of the mode in
               function of `freq` e.g.(1 1.2 1.5 ...). The first element should always
               be one (fundamental).
* `gain`: the gain of each mode as a list (1 0.9 0.8 ...). The first element
          is the gain of the fundamental.
* `harmDec`: harmonic decay ratio (0-1): configure the speed at which
             higher modes decay compare to lower modes.
* `att`: attack duration in second
* `rel`: release duration in second
* `gate`: trigger signal (0 or 1)

----

### `(sy.)fm`

An FM synthesizer with an arbitrary number of modulators connected as a sequence.
`fm` is a standard Faust function.

#### Usage

```
freqs = (300,400,...);
indices = (20,...);
fm(freqs,indices) : _
```

Where:

* `freqs`: a list of frequencies where the first one is the frequency of the carrier
           and the others, the frequency of the modulator(s)
* `indices`: the indices of modulation (Nfreqs-1)

## Drum Synthesis

Drum Synthesis ported in Faust from a version written in [Elementary](https://www.elementary.audio/) 
and JavaScript by Nick Thompson. 

#### Reference

* [https://www.nickwritesablog.com/drum-synthesis-in-javascript/](https://www.nickwritesablog.com/drum-synthesis-in-javascript/)

----

### `(sy.)kick`

Kick drum synthesis via a pitched sine sweep.

#### Usage 

```
kick(pitch, click, attack, decay, drive, gate) : _
```

Where:

* `pitch`: the base frequency of the kick drum in Hz
* `click`: the speed of the pitch envelope, tuned for [0.005s, 1s]
* `attack`: attack time in seconds, tuned for [0.005s, 0.4s]
* `decay`: decay time in seconds, tuned for [0.005s, 4.0s]
* `drive`: a gain multiplier going into the saturator. Tuned for [1, 10]
* `gate`: the gate which triggers the amp envelope

#### Reference

* [https://github.com/nick-thompson/drumsynth/blob/master/kick.js](https://github.com/nick-thompson/drumsynth/blob/master/kick.js)

----

### `(sy.)clap`

Clap synthesis via filtered white noise.

#### Usage 

```
clap(tone, attack, decay, gate) : _
```

Where:

* `tone`: bandpass filter cutoff frequency, tuned for [400Hz, 3500Hz]
* `attack`: attack time in seconds, tuned for [0s, 0.2s]
* `decay`: decay time in seconds, tuned for [0s, 4.0s]
* `gate`: the gate which triggers the amp envelope

#### Reference

* [https://github.com/nick-thompson/drumsynth/blob/master/clap.js](https://github.com/nick-thompson/drumsynth/blob/master/clap.js)

----

### `(sy.)hat`

Hi hat drum synthesis via phase modulation.

#### Usage 

```
hat(pitch, tone, attack, decay, gate): _
```

Where:

* `pitch`: base frequency in the range [317Hz, 3170Hz]
* `tone`: bandpass filter cutoff frequency, tuned for [800Hz, 18kHz]
* `attack`: attack time in seconds, tuned for [0.005s, 0.2s]
* `decay`: decay time in seconds, tuned for [0.005s, 4.0s]
* `gate`: the gate which triggers the amp envelope

#### Reference

* [https://github.com/nick-thompson/drumsynth/blob/master/hat.js](https://github.com/nick-thompson/drumsynth/blob/master/hat.js)
