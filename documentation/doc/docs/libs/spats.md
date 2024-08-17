#  spats.lib 

This library contains a collection of tools for sound spatialization.
Its official prefix is `sp`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/spats.lib](https://github.com/grame-cncm/faustlibraries/blob/master/spats.lib)

----

### `(sp.)panner`

A simple linear stereo panner.
`panner` is a standard Faust function.

#### Usage

```
_ : panner(g) : _,_
```

Where:

* `g`: the panning (0-1)

----

### `(sp.)constantPowerPan`

Apply the constant power pan rule to a stereo signal.
The channels are not respatialized. Their gains are simply
adjusted. A pan of 0 preserves the left channel and silences
the right channel. A pan of 1 has the opposite effect.
A pan value of 0.5 applies a gain of 0.5 to both channels. 

#### Usage

```
_,_ : constantPowerPan(p) : _,_
```

Where:

* `p`: the panning (0-1)

----

### `(sp.)spat`

GMEM SPAT: n-outputs spatializer.
`spat` is a standard Faust function.

#### Usage

```
_ : spat(N,r,d) : si.bus(N)
```

Where:

* `N`: number of outputs (a constant numerical expression)
* `r`: rotation (between 0 et 1)
* `d`: distance of the source (between 0 et 1)

----

### `(sp.)stereoize`

Transform an arbitrary processor `p` into a stereo processor with 2 inputs
and 2 outputs.

#### Usage

```
_,_ : stereoize(p) : _,_
```

Where:

* `p`: the arbitrary processor
