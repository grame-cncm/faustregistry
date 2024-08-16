#  envelopes.lib 

This library contains a collection of envelope generators. Its official prefix is `en`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/envelopes.lib](https://github.com/grame-cncm/faustlibraries/blob/master/envelopes.lib)

## Functions Reference


----

### `(en.)ar`

AR (Attack, Release) envelope generator (useful to create percussion envelopes).
`ar` is a standard Faust function.

#### Usage

```
ar(at,rt,t) : _
```

Where:

* `at`: attack (sec)
* `rt`: release (sec)
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)asr`

ASR (Attack, Sustain, Release) envelope generator.
`asr` is a standard Faust function.

#### Usage

```
asr(at,sl,rt,t) : _
```

Where:

* `at`: attack (sec)
* `sl`: sustain level (between 0..1)
* `rt`: release (sec)
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)adsr`

ADSR (Attack, Decay, Sustain, Release) envelope generator.
`adsr` is a standard Faust function.

#### Usage

```
adsr(at,dt,sl,rt,t) : _
```

Where:

* `at`: attack time (sec)
* `dt`: decay time (sec)
* `sl`: sustain level (between 0..1)
* `rt`: release time (sec)
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)adsrf_bias`

ADSR (Attack, Decay, Sustain, Release, Final) envelope generator with
control over bias on each segment, and toggle for legato.

#### Usage

```
adsrf_bias(at,dt,sl,rt,final,b_att,b_dec,b_rel,legato,t) : _
```

Where:

* `at`: attack time (sec)
* `dt`: decay time (sec)
* `sl`: sustain level (between 0..1)
* `rt`: release time (sec)
* `final`: final level (between 0..1) but less than or equal to `sl`
* `b_att`: bias during attack (between 0..1) where 0.5 is no bias.
* `b_dec`: bias during decay (between 0..1) where 0.5 is no bias.
* `b_rel`: bias during release (between 0..1) where 0.5 is no bias.
* `legato`: toggle for legato. If disabled, envelopes "re-trigger" from zero.
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)adsr_bias`

ADSR (Attack, Decay, Sustain, Release) envelope generator with
control over bias on each segment, and toggle for legato.

#### Usage

```
adsr_bias(at,dt,sl,rt,b_att,b_dec,b_rel,legato,t) : _
```

Where:

* `at`: attack time (sec)
* `dt`: decay time (sec)
* `sl`: sustain level (between 0..1)
* `rt`: release time (sec)
* `b_att`: bias during attack (between 0..1) where 0.5 is no bias.
* `b_dec`: bias during decay (between 0..1) where 0.5 is no bias.
* `b_rel`: bias during release (between 0..1) where 0.5 is no bias.
* `legato`: toggle for legato. If disabled, envelopes "re-trigger" from zero.
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)ahdsrf_bias`

AHDSR (Attack, Hold, Decay, Sustain, Release, Final) envelope generator
with control over bias on each segment, and toggle for legato.

#### Usage

```
ahdsrf_bias(at,ht,dt,sl,rt,final,b_att,b_dec,b_rel,legato,t) : _
```

Where:

* `at`: attack time (sec)
* `ht`: hold time (sec)
* `dt`: decay time (sec)
* `sl`: sustain level (between 0..1)
* `rt`: release time (sec)
* `final`: final level (between 0..1) but less than or equal to `sl`
* `b_att`: bias during attack (between 0..1) where 0.5 is no bias.
* `b_dec`: bias during decay (between 0..1) where 0.5 is no bias.
* `b_rel`: bias during release (between 0..1) where 0.5 is no bias.
* `legato`: toggle for legato. If disabled, envelopes "re-trigger" from zero.
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)ahdsr_bias`

AHDSR (Attack, Hold, Decay, Sustain, Release) envelope generator
with control over bias on each segment, and toggle for legato.

#### Usage

```
ahdsr_bias(at,ht,dt,sl,rt,final,b_att,b_dec,b_rel,legato,t) : _
```

Where:

* `at`: attack time (sec)
* `ht`: hold time (sec)
* `dt`: decay time (sec)
* `sl`: sustain level (between 0..1)
* `rt`: release time (sec)
* `final`: final level (between 0..1) but less than or equal to `sl`
* `b_att`: bias during attack (between 0..1) where 0.5 is no bias.
* `b_dec`: bias during decay (between 0..1) where 0.5 is no bias.
* `b_rel`: bias during release (between 0..1) where 0.5 is no bias.
* `legato`: toggle for legato. If disabled, envelopes "re-trigger" from zero.
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)smoothEnvelope`

An envelope with an exponential attack and release.
`smoothEnvelope` is a standard Faust function.

#### Usage

```
smoothEnvelope(ar,t) : _
```

* `ar`: attack and release duration (sec)
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)arfe`

ARFE (Attack and Release-to-Final-value Exponentially) envelope generator.
Approximately equal to `smoothEnvelope(Attack/6.91)` when Attack == Release.

#### Usage

```
arfe(at,rt,fl,t) : _
```

Where:

* `at`: attack (sec)
* `rt`: release (sec)
* `fl`: final level to approach upon release (such as 0)
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)are`

ARE (Attack, Release) envelope generator with Exponential segments.
Approximately equal to `smoothEnvelope(Attack/6.91)` when Attack == Release.

#### Usage

```
are(at,rt,t) : _
```

Where:

* `at`: attack (sec)
* `rt`: release (sec)
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)asre`

ASRE (Attack, Sustain, Release) envelope generator with Exponential segments.

#### Usage

```
asre(at,sl,rt,t) : _
```

Where:

* `at`: attack (sec)
* `sl`: sustain level (between 0..1)
* `rt`: release (sec)
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)adsre`

ADSRE (Attack, Decay, Sustain, Release) envelope generator with Exponential
segments.

#### Usage

```
adsre(at,dt,sl,rt,t) : _
```

Where:

* `at`: attack (sec)
* `dt`: decay (sec)
* `sl`: sustain level (between 0..1)
* `rt`: release (sec)
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)ahdsre`

AHDSRE (Attack, Hold, Decay, Sustain, Release) envelope generator with Exponential
segments.

#### Usage

```
ahdsre(at,ht,dt,sl,rt,t) : _
```

Where:

* `at`: attack (sec)
* `ht`: hold (sec)
* `dt`: decay (sec)
* `sl`: sustain level (between 0..1)
* `rt`: release (sec)
* `t`: trigger signal (attack is triggered when `t>0`, release is triggered
when `t=0`)

----

### `(en.)dx7envelope`

DX7 operator envelope generator with 4 independent rates and levels. It is
essentially a 4 points BPF.

#### Usage

```
dx7_envelope(R1,R2,R3,R4,L1,L2,L3,L4,t) : _
```

Where:

* `RN`: rates in seconds
* `LN`: levels (0-1)
* `t`: trigger signal
