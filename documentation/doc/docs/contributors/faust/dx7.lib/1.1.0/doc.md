#  dx7.lib 

Yamaha DX7 emulation library. Its official prefix is `dx`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/dx7.lib](https://github.com/grame-cncm/faustlibraries/blob/master/dx7.lib)

----

### `(dx.)dx7_ampf`

DX7 amplitude conversion function. 3 versions of this function
are available:

* `dx7_amp_bpf`: BPF version (same as in the CSOUND toolkit)
* `dx7_amp_func`: estimated mathematical equivalent of `dx7_amp_bpf`
* `dx7_ampf`: default (sugar for `dx7_amp_func`)

#### Usage:

```
dx7AmpPreset : dx7_ampf_bpf : _
```

Where:

* `dx7AmpPreset`: DX7 amplitude value (0-99)

----

### `(dx.)dx7_egraterisef`

DX7 envelope generator rise conversion function. 3 versions of this function
are available:

* `dx7_egraterise_bpf`: BPF version (same as in the CSOUND toolkit)
* `dx7_egraterise_func`: estimated mathematical equivalent of `dx7_egraterise_bpf`
* `dx7_egraterisef`: default (sugar for `dx7_egraterise_func`)

#### Usage:

```
dx7envelopeRise : dx7_egraterisef : _
```

Where:

* `dx7envelopeRise`: DX7 envelope rise value (0-99)

----

### `(dx.)dx7_egraterisepercf`

DX7 envelope generator percussive rise conversion function. 3 versions of
this function are available:

* `dx7_egrateriseperc_bpf`: BPF version (same as in the CSOUND toolkit)
* `dx7_egrateriseperc_func`: estimated mathematical equivalent of `dx7_egrateriseperc_bpf`
* `dx7_egraterisepercf`: default (sugar for `dx7_egrateriseperc_func`)

#### Usage:

```
dx7envelopePercRise : dx7_egraterisepercf : _
```

Where:

* `dx7envelopePercRise`: DX7 envelope percussive rise value (0-99)

----

### `(dx.)dx7_egratedecayf`

DX7 envelope generator decay conversion function. 3 versions of
this function are available:

* `dx7_egratedecay_bpf`: BPF version (same as in the CSOUND toolkit)
* `dx7_egratedecay_func`: estimated mathematical equivalent of `dx7_egratedecay_bpf`
* `dx7_egratedecayf`: default (sugar for `dx7_egratedecay_func`)

#### Usage:

```
dx7envelopeDecay : dx7_egratedecayf : _
```

Where:

* `dx7envelopeDecay`: DX7 envelope decay value (0-99)

----

### `(dx.)dx7_egratedecaypercf`

DX7 envelope generator percussive decay conversion function. 3 versions of
this function are available:

* `dx7_egratedecayperc_bpf`: BPF version (same as in the CSOUND toolkit)
* `dx7_egratedecayperc_func`: estimated mathematical equivalent of `dx7_egratedecayperc_bpf`
* `dx7_egratedecaypercf`: default (sugar for `dx7_egratedecayperc_func`)

#### Usage:

```
dx7envelopePercDecay : dx7_egratedecaypercf : _
```

Where:

* `dx7envelopePercDecay`: DX7 envelope decay value (0-99)

----

### `(dx.)dx7_eglv2peakf`

DX7 envelope level to peak conversion function. 3 versions of
this function are available:

* `dx7_eglv2peak_bpf`: BPF version (same as in the CSOUND toolkit)
* `dx7_eglv2peak_func`: estimated mathematical equivalent of `dx7_eglv2peak_bpf`
* `dx7_eglv2peakf`: default (sugar for `dx7_eglv2peak_func`)

#### Usage:

```
dx7Level : dx7_eglv2peakf : _
```

Where:

* `dx7Level`: DX7 level value (0-99)

----

### `(dx.)dx7_velsensf`

DX7 velocity sensitivity conversion function.

#### Usage:

```
dx7Velocity  : dx7_velsensf : _
```

Where:

* `dx7Velocity`: DX7 level value (0-8)

----

### `(dx.)dx7_fdbkscalef`

DX7 feedback scaling conversion function.

#### Usage:

```
dx7Feedback  : dx7_fdbkscalef : _
```

Where:

* `dx7Feedback`: DX7 feedback value

----

### `(dx.)dx7_op`

DX7 Operator. Implements a phase-modulable sine wave oscillator connected
to a DX7 envelope generator.

#### Usage:

```
dx7_op(freq,phaseMod,outLev,R1,R2,R3,R4,L1,L2,L3,L4,keyVel,rateScale,type,gain,gate) : _
```

Where:

* `freq`: frequency of the oscillator
* `phaseMod`: phase deviation (-1 - 1)
* `outLev`: preset output level (0-99)
* `R1`: preset envelope rate 1 (0-99)
* `R2`: preset envelope rate 2 (0-99)
* `R3`: preset envelope rate 3 (0-99)
* `R4`: preset envelope rate 4 (0-99)
* `L1`: preset envelope level 1 (0-99)
* `L2`: preset envelope level 2 (0-99)
* `L3`: preset envelope level 3 (0-99)
* `L4`: preset envelope level 4 (0-99)
* `keyVel`: preset key velocity sensitivity (0-99)
* `rateScale`: preset envelope rate scale
* `type`: preset operator type
* `gain`: general gain
* `gate`: trigger signal

----

### `(dx.)dx7_algo`

DX7 algorithms. Implements the 32 DX7 algorithms (a quick Google search
should give your more details on this). Each algorithm uses 6 operators.

#### Usage:

```
dx7_algo(algN,egR1,egR2,egR3,egR4,egL1,egL2,egL3,egL4,outLevel,keyVelSens,ampModSens,opMode,opFreq,opDetune,opRateScale,feedback,lfoDelay,lfoDepth,lfoSpeed,freq,gain,gate) : _
```

Where:

* `algN`: algorithm number (0-31, should be an int...)
* `egR1`: preset envelope rates 1 (a list of 6 values between 0-99)
* `egR2`: preset envelope rates 2 (a list of 6 values between 0-99)
* `egR3`: preset envelope rates 3 (a list of 6 values between 0-99)
* `egR4`: preset envelope rates 4 (a list of 6 values between 0-99)
* `egL1`: preset envelope levels 1 (a list of 6 values between 0-99)
* `egL2`: preset envelope levels 2 (a list of 6 values between 0-99)
* `egL3`: preset envelope levels 3 (a list of 6 values between 0-99)
* `egL4`: preset envelope levels 4 (a list of 6 values between 0-99)
* `outLev`: preset output levels (a list of 6 values between 0-99)
* `keyVel`: preset key velocity sensitivities (a list of 6 values between 0-99)
* `ampModSens`: preset amplitude sensitivities (a list of 6 values between 0-99)
* `opMode`: preset operator mode (a list of 6 values between 0-1)
* `opFreq`: preset operator frequencies (a list of 6 values between 0-99)
* `opDetune`: preset operator detuning (a list of 6 values between 0-99)
* `opRateScale`: preset operator rate scale (a list of 6 values between 0-99)
* `feedback`: preset operator feedback (a list of 6 values between 0-99)
* `lfoDelay`: preset LFO delay (a list of 6 values between 0-99)
* `lfoDepth`: preset LFO depth (a list of 6 values between 0-99)
* `lfoSpeed`: preset LFO speed (a list of 6 values between 0-99)
* `freq`: fundamental frequency
* `gain`: general gain
* `gate`: trigger signal

----

### `(dx.)dx7_ui`

Generic DX7 function where all parameters are controllable using UI elements.
The `master-with-mute` branch must be used for this function to work...
This function is MIDI-compatible.

#### Usage

```
dx7_ui : _
```
