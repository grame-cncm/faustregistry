#  vaeffects.lib 

A library of virtual analog filter effects. Its official prefix is `ve`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/vaeffects.lib](https://github.com/grame-cncm/faustlibraries/blob/master/vaeffects.lib)

## Moog Filters


----

### `(ve.)moog_vcf`

Moog "Voltage Controlled Filter" (VCF) in "analog" form. Moog VCF
implemented using the same logical block diagram as the classic
analog circuit.  As such, it neglects the one-sample delay associated
with the feedback path around the four one-poles.
This extra delay alters the response, especially at high frequencies
(see reference [1] for details).
See `moog_vcf_2b` below for a more accurate implementation.

#### Usage

```
_ : moog_vcf(res,fr) : _
```
Where:

* `res`: normalized amount of corner-resonance between 0 and 1 
(0 is no resonance, 1 is maximum)
* `fr`: corner-resonance frequency in Hz (less than SR/6.3 or so)

#### References
* [https://ccrma.stanford.edu/~stilti/papers/moogvcf.pdf](https://ccrma.stanford.edu/~stilti/papers/moogvcf.pdf)
* [https://ccrma.stanford.edu/~jos/pasp/vegf.html](https://ccrma.stanford.edu/~jos/pasp/vegf.html)

----

### `(ve.)moog_vcf_2b[n]`

Moog "Voltage Controlled Filter" (VCF) as two biquads. Implementation
of the ideal Moog VCF transfer function factored into second-order
sections. As a result, it is more accurate than `moog_vcf` above, but
its coefficient formulas are more complex when one or both parameters
are varied.  Here, res is the fourth root of that in `moog_vcf`, so, as
the sampling rate approaches infinity, `moog_vcf(res,fr)` becomes equivalent
to `moog_vcf_2b[n](res^4,fr)` (when res and fr are constant).
`moog_vcf_2b` uses two direct-form biquads (`tf2`).
`moog_vcf_2bn` uses two protected normalized-ladder biquads (`tf2np`).

#### Usage

```
_ : moog_vcf_2b(res,fr) : _
_ : moog_vcf_2bn(res,fr) : _
```

Where:

* `res`: normalized amount of corner-resonance between 0 and 1
	(0 is min resonance, 1 is maximum)
* `fr`: corner-resonance frequency in Hz

----

### `(ve.)moogLadder`

Virtual analog model of the 4th-order Moog Ladder, which is arguably the 
most well-known ladder filter in analog synthesizers. Several 
1st-order filters are cascaded in series. Feedback is then used, in part, to 
control the cut-off frequency and the resonance.

#### References

[Zavalishin 2012] (revision 2.1.2, February 2020): 

* [https://www.native-instruments.com/fileadmin/ni_media/downloads/pdf/VAFilterDesign_2.1.2.pdf](https://www.native-instruments.com/fileadmin/ni_media/downloads/pdf/VAFilterDesign_2.1.2.pdf)

This fix is based on Lorenzo Della Cioppa's correction to Pirkle's implementation; see this post: 
https://www.kvraudio.com/forum/viewtopic.php?f=33&t=571909

#### Usage

```
_ : moogLadder(normFreq,Q) : _
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: quality factor between .707 (0 feedback coefficient) to 25 (feedback = 4, which is the self-oscillating threshold).

----

### `(ve.)moogHalfLadder`

Virtual analog model of the 2nd-order Moog Half Ladder (simplified version of
`(ve.)moogLadder`). Several 1st-order filters are cascaded in series. 
Feedback is then used, in part, to control the cut-off frequency and the 
resonance.

This filter was implemented in Faust by Eric Tarr during the 
[2019 Embedded DSP With Faust Workshop](https://ccrma.stanford.edu/workshops/faust-embedded-19/).

#### References

* [https://www.willpirkle.com/app-notes/virtual-analog-moog-half-ladder-filter](https://www.willpirkle.com/app-notes/virtual-analog-moog-half-ladder-filter)
* [http://www.willpirkle.com/Downloads/AN-8MoogHalfLadderFilter.pdf](http://www.willpirkle.com/Downloads/AN-8MoogHalfLadderFilter.pdf)

#### Usage

```
_ : moogHalfLadder(normFreq,Q) : _
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

----

### `(ve.)diodeLadder`

4th order virtual analog diode ladder filter. In addition to the individual 
states used within each independent 1st-order filter, there are also additional 
feedback paths found in the block diagram. These feedback paths are labeled 
as connecting states. Rather than separately storing these connecting states 
in the Faust implementation, they are simply implicitly calculated by 
tracing back to the other states (`s1`,`s2`,`s3`,`s4`) each recursive step.

This filter was implemented in Faust by Eric Tarr during the 
[2019 Embedded DSP With Faust Workshop](https://ccrma.stanford.edu/workshops/faust-embedded-19/).

#### References

* [https://www.willpirkle.com/virtual-analog-diode-ladder-filter/](https://www.willpirkle.com/virtual-analog-diode-ladder-filter/)
* [http://www.willpirkle.com/Downloads/AN-6DiodeLadderFilter.pdf](http://www.willpirkle.com/Downloads/AN-6DiodeLadderFilter.pdf)

#### Usage

```
_ : diodeLadder(normFreq,Q) : _
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

## Korg 35 Filters

The following filters are virtual analog models of the Korg 35 low-pass 
filter and high-pass filter found in the MS-10 and MS-20 synthesizers.
The virtual analog models for the LPF and HPF are different, making these 
filters more interesting than simply tapping different states of the same 
circuit. 

These filters were implemented in Faust by Eric Tarr during the 
[2019 Embedded DSP With Faust Workshop](https://ccrma.stanford.edu/workshops/faust-embedded-19/).

#### Filter history:

* [https://secretlifeofsynthesizers.com/the-korg-35-filter/](https://secretlifeofsynthesizers.com/the-korg-35-filter/)

----

### `(ve.)korg35LPF`

Virtual analog models of the Korg 35 low-pass filter found in the MS-10 and 
MS-20 synthesizers.

#### Usage

```
_ : korg35LPF(normFreq,Q) : _
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

----

### `(ve.)korg35HPF`

Virtual analog models of the Korg 35 high-pass filter found in the MS-10 and 
MS-20 synthesizers.

#### Usage

```
_ : korg35HPF(normFreq,Q) : _
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

## Oberheim Filters

The following filter (4 types) is an implementation of the virtual analog 
model described in Section 7.2 of the Will Pirkle book, "Designing Software 
Synthesizer Plug-ins in C++". It is based on the block diagram in Figure 7.5. 

The Oberheim filter is a state-variable filter with soft-clipping distortion 
within the circuit. 

In many VA filters, distortion is accomplished using the "tanh" function. 
For this Faust implementation, that distortion function was replaced with 
the `(ef.)cubicnl` function.

----

### `(ve.)oberheim`

Generic multi-outputs Oberheim filter that produces the BSF, BPF, HPF and LPF outputs (see description above).

#### Usage

```
_ : oberheim(normFreq,Q) : _,_,_,_
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

----

### `(ve.)oberheimBSF`

Band-Stop Oberheim filter (see description above). 
Specialize the generic implementation: keep the first BSF output, 
the compiler will only generate the needed code.

#### Usage

```
_ : oberheimBSF(normFreq,Q) : _
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

----

### `(ve.)oberheimBPF`

Band-Pass Oberheim filter (see description above).
Specialize the generic implementation: keep the second BPF output, 
the compiler will only generate the needed code.

#### Usage

```
_ : oberheimBPF(normFreq,Q) : _
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

----

### `(ve.)oberheimHPF`

High-Pass Oberheim filter (see description above).
Specialize the generic implementation: keep the third HPF output, 
the compiler will only generate the needed code.

#### Usage

```
_ : oberheimHPF(normFreq,Q) : _
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

----

### `(ve.)oberheimLPF`

Low-Pass Oberheim filter (see description above). 
Specialize the generic implementation: keep the fourth LPF output,
the compiler will only generate the needed code.

#### Usage

```
_ : oberheimLPF(normFreq,Q) : _
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

## Sallen Key Filters

The following filters were implemented based on VA models of synthesizer 
filters.

The modeling approach is based on a Topology Preserving Transform (TPT) to 
resolve the delay-free feedback loop in the corresponding analog filters.  

The primary processing block used to build other filters (Moog, Korg, etc.) is
based on a 1st-order Sallen-Key filter. 

The filters included in this script are 1st-order LPF/HPF and 2nd-order 
state-variable filters capable of LPF, HPF, and BPF.  

#### Resources:

* Vadim Zavalishin (2018) "The Art of VA Filter Design", v2.1.0
* [https://www.native-instruments.com/fileadmin/ni_media/downloads/pdf/VAFilterDesign_2.1.0.pdf](https://www.native-instruments.com/fileadmin/ni_media/downloads/pdf/VAFilterDesign_2.1.0.pdf)
* Will Pirkle (2014) "Resolving Delay-Free Loops in Recursive Filters Using 
* the Modified Härmä Method", AES 137 [http://www.aes.org/e-lib/browse.cfm?elib=17517](http://www.aes.org/e-lib/browse.cfm?elib=17517)
* Description and diagrams of 1st- and 2nd-order TPT filters: 
* [https://www.willpirkle.com/706-2/](https://www.willpirkle.com/706-2/)

----

### `(ve.)sallenKeyOnePole`

Sallen-Key generic One Pole filter that produces the LPF and HPF outputs (see description above).

For the Faust implementation of this filter, recursion (`letrec`) is used 
for storing filter "states". The output (e.g. `y`) is calculated by using 
the input signal and the previous states of the filter.
During the current recursive step, the states of the filter (e.g. `s`) for 
the next step are also calculated.
Admittedly, this is not an efficient way to implement a filter because it 
requires independently calculating the output and each state during each 
recursive step. However, it works as a way to store and use "states"
within the constraints of Faust. 
The simplest example is the 1st-order LPF (shown on the cover of Zavalishin 
* 2018 and Fig 4.3 of [https://www.willpirkle.com/706-2/](https://www.willpirkle.com/706-2/)). Here, the input 
signal is split in parallel for the calculation of the output signal, `y`, and 
the state `s`. The value of the state is only used for feedback to the next 
step of recursion. It is blocked (!) from also being routed to the output. 
A trick used for calculating the state `s` is to observe that the input to 
the delay block is the sum of two signal: what appears to be a feedforward 
path and a feedback path. In reality, the signals being summed are identical 
(signal*2) plus the value of the current state.

#### Usage

```
_ : sallenKeyOnePole(normFreq) : _,_
```

Where:

* `normFreq`: normalized frequency (0-1)

----

### `(ve.)sallenKeyOnePoleLPF`

Sallen-Key One Pole lowpass filter (see description above).
Specialize the generic implementation: keep the first LPF output, 
the compiler will only generate the needed code.

#### Usage

```
_ : sallenKeyOnePoleLPF(normFreq) : _
```

Where:

* `normFreq`: normalized frequency (0-1)

----

### `(ve.)sallenKeyOnePoleHPF`

Sallen-Key One Pole Highpass filter (see description above). The dry input 
signal is routed in parallel to the output. The LPF'd signal is subtracted 
from the input so that the HPF remains.
Specialize the generic implementation: keep the second HPF output, 
the compiler will only generate the needed code.

#### Usage

```
_ : sallenKeyOnePoleHPF(normFreq) : _
```

Where:

* `normFreq`: normalized frequency (0-1)

----

### `(ve.)sallenKey2ndOrder`

Sallen-Key generic 2nd order filter that produces the LPF, BPF and HPF outputs. 

This is a 2nd-order Sallen-Key state-variable filter. The idea is that by 
"tapping" into different points in the circuit, different filters 
(LPF,BPF,HPF) can be achieved. See Figure 4.6 of 
* [https://www.willpirkle.com/706-2/](https://www.willpirkle.com/706-2/)

This is also a good example of the next step for generalizing the Faust 
programming approach used for all these VA filters. In this case, there are 
three things to calculate each recursive step (`y`,`s1`,`s2`). For each thing, the 
circuit is only calculated up to that point. 

Comparing the LPF to BPF, the output signal (`y`) is calculated similarly. 
Except, the output of the BPF stops earlier in the circuit. Similarly, the 
states (`s1` and `s2`) only differ in that `s2` includes a couple more terms 
beyond what is used for `s1`. 

#### Usage

```
_ : sallenKey2ndOrder(normFreq,Q) : _,_,_
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

----

### `(ve.)sallenKey2ndOrderLPF`

Sallen-Key 2nd order lowpass filter (see description above). 
Specialize the generic implementation: keep the first LPF output,
the compiler will only generate the needed code.

#### Usage

```
_ : sallenKey2ndOrderLPF(normFreq,Q) : _
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

----

### `(ve.)sallenKey2ndOrderBPF`

Sallen-Key 2nd order bandpass filter (see description above). 
Specialize the generic implementation: keep the second BPF output, 
the compiler will only generate the needed code.

#### Usage

```
_ : sallenKey2ndOrderBPF(normFreq,Q) : _
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

----

### `(ve.)sallenKey2ndOrderHPF`

Sallen-Key 2nd order highpass filter (see description above). 
Specialize the generic implementation: keep the third HPF output, 
the compiler will only generate the needed code.

#### Usage

```
_ : sallenKey2ndOrderHPF(normFreq,Q) : _
```

Where:

* `normFreq`: normalized frequency (0-1)
* `Q`: q

## Effects


----

### `(ve.)wah4`

Wah effect, 4th order.
`wah4` is a standard Faust function.

#### Usage

```
_ : wah4(fr) : _
```

Where:

* `fr`: resonance frequency in Hz

#### Reference

* [https://ccrma.stanford.edu/~jos/pasp/vegf.html](https://ccrma.stanford.edu/~jos/pasp/vegf.html)

----

### `(ve.)autowah`

Auto-wah effect.
`autowah` is a standard Faust function.

#### Usage

```
_ : autowah(level) : _
```

Where:

* `level`: amount of effect desired (0 to 1).

----

### `(ve.)crybaby`

Digitized CryBaby wah pedal.
`crybaby` is a standard Faust function.

#### Usage

```
_ : crybaby(wah) : _
```

Where:

* `wah`: "pedal angle" from 0 to 1

#### Reference

* [https://ccrma.stanford.edu/~jos/pasp/vegf.html](https://ccrma.stanford.edu/~jos/pasp/vegf.html)

----

### `(ve.)vocoder`

A very simple vocoder where the spectrum of the modulation signal
is analyzed using a filter bank.
`vocoder` is a standard Faust function.

#### Usage

```
_ : vocoder(nBands,att,rel,BWRatio,source,excitation) : _
```

Where:

* `nBands`: Number of vocoder bands
* `att`: Attack time in seconds
* `rel`: Release time in seconds
* `BWRatio`: Coefficient to adjust the bandwidth of each band (0.1 - 2)
* `source`: Modulation signal
* `excitation`: Excitation/Carrier signal
