#  compressors.lib 

A library of compressor effects. Its official prefix is `co`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/compressors.lib](https://github.com/grame-cncm/faustlibraries/blob/master/compressors.lib)

## Conversion Tools

Useful conversion tools for compressors.

----

### `(co.)ratio2strength `

Most compressors have a ratio parameter to define the amount of compression.
A ratio of 1 means no compression, a ratio of 2 means that for every dB the input goes above the threshold,
the output gets turned down half a dB.
To use a compressor as a brick wall limiter, the ratio needs to be infinity.
This is hard to express in a faust UI element, and overcompression can not be expressed at all,
therefore most compressors in this library use a strength parameter instead, where
0 means no compression, 1 means hard limiting and  bigger than 1 means over-compression.

This utility converts a ratio to a strength.

#### Usage

```
ratio2strength(ratio) : _
```

Where:

* `ratio`:  compression ratio, between 1 and infinity (1=no compression, infinity means hard limiting)

----

### `(co.)strength2ratio `

Most compressors have a ratio parameter to define the amount of compression.
A ratio of 1 means no compression, a ratio of 2 means that for every dB the input goes above the threshold,
the output gets turned down half a dB.
To use a compressor as a brick wall limiter, the ratio needs to be infinity.
This is hard to express in a faust UI element, and overcompression can not be expressed at all,
therefore most compressors in this library use a strength parameter instead, where
0 means no compression, 1 means hard limiting and bigger than 1 means over-compression.

This utility converts a strength to a ratio.

#### Usage

```
strength2ratio(strength) : _
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)

## Functions Reference


----

### `(co.)peak_compression_gain_mono_db`

Mono dynamic range compressor gain computer with dB output.
`peak_compression_gain_mono_db` is a standard Faust function.

#### Usage

```
_ : peak_compression_gain_mono_db(strength,thresh,att,rel,knee,prePost) : _
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log domain return-to-threshold detector

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

----

### `(co.)peak_compression_gain_N_chan_db`

N channels dynamic range compressor gain computer with dB output.
`peak_compression_gain_N_chan_db` is a standard Faust function.

#### Usage

```
si.bus(N) : peak_compression_gain_N_chan_db(strength,thresh,att,rel,knee,prePost,link,N) : si.bus(N)
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-threshold detector
* `link`: the amount of linkage between the channels: 0 = each channel is independent, 1 = all channels have the same amount of gain reduction
* `N`: the number of channels of the compressor, known at compile time

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

----

### `(co.)FFcompressor_N_chan`

Feed forward N channels dynamic range compressor.
`FFcompressor_N_chan` is a standard Faust function.

#### Usage

```
si.bus(N) : FFcompressor_N_chan(strength,thresh,att,rel,knee,prePost,link,meter,N) : si.bus(N)
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-threshold detector
* `link`: the amount of linkage between the channels: 0 = each channel is independent, 1 = all channels have the same amount of gain reduction
* `meter`: a gain reduction meter. It can be implemented like so:
`meter = _<:(_, (ba.linear2db:max(maxGR):meter_group((hbargraph("[1][unit:dB][tooltip: gain reduction in dB]", maxGR, 0))))):attach;`
* `N`: the number of channels of the compressor, known at compile time

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

----

### `(co.)FBcompressor_N_chan`

Feed back N channels dynamic range compressor.
`FBcompressor_N_chan` is a standard Faust function.

#### Usage

```
si.bus(N) : FBcompressor_N_chan(strength,thresh,att,rel,knee,prePost,link,meter,N) : si.bus(N)
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-threshold detector
* `link`: the amount of linkage between the channels. 0 = each channel is independent, 1 = all channels have the same amount of gain reduction
* `meter`: a gain reduction meter. It can be implemented with:
`meter = _ <: (_,(ba.linear2db:max(maxGR):meter_group((hbargraph("[1][unit:dB][tooltip: gain reduction in dB]", maxGR, 0))))):attach;`
or it can be omitted by defining `meter = _;`.
* `N`: the number of channels of the compressor, known at compile time

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

----

### `(co.)FBFFcompressor_N_chan`

Feed forward / feed back N channels dynamic range compressor.
The feedback part has a much higher strength, so they end up sounding similar.
`FBFFcompressor_N_chan` is a standard Faust function.

#### Usage

```
si.bus(N) : FBFFcompressor_N_chan(strength,thresh,att,rel,knee,prePost,link,FBFF,meter,N) : si.bus(N)
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-threshold detector
* `link`: the amount of linkage between the channels: 0 = each channel is independent, 1 = all channels have the same amount of gain reduction
* `FBFF`: fade between feed forward (0) and feed back (1) compression
* `meter`: a gain reduction meter. It can be implemented like so:
`meter = _<:(_,(max(maxGR):meter_group((hbargraph("[1][unit:dB][tooltip: gain reduction in dB]", maxGR, 0))))):attach;`
* `N`: the number of channels of the compressor, known at compile time

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

----

### `(co.)RMS_compression_gain_mono_db`

Mono RMS dynamic range compressor gain computer with dB output.
`RMS_compression_gain_mono_db` is a standard Faust function.

#### Usage

```
_ : RMS_compression_gain_mono_db(strength,thresh,att,rel,knee,prePost) : _
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-threshold detector

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

----

### `(co.)RMS_compression_gain_N_chan_db`

RMS N channels dynamic range compressor gain computer with dB output.
`RMS_compression_gain_N_chan_db` is a standard Faust function.

#### Usage

```
si.bus(N) : RMS_compression_gain_N_chan_db(strength,thresh,att,rel,knee,prePost,link,N) : si.bus(N)
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-threshold detector
* `link`: the amount of linkage between the channels: 0 = each channel is independent, 1 = all channels have the same amount of gain reduction
* `N`: the number of channels of the compressor

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

----

### `(co.)RMS_FBFFcompressor_N_chan`

RMS feed forward / feed back N channels dynamic range compressor.
The feedback part has a much higher strength, so they end up sounding similar.
`RMS_FBFFcompressor_N_chan` is a standard Faust function.

#### Usage

```
si.bus(N) : RMS_FBFFcompressor_N_chan(strength,thresh,att,rel,knee,prePost,link,FBFF,meter,N) : si.bus(N)
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-threshold detector
* `link`: the amount of linkage between the channels: 0 = each channel is independent, 1 = all channels have the same amount of gain reduction
* `FBFF`: fade between feed forward (0) and feed back (1) compression.
* `meter`: a gain reduction meter. It can be implemented with:
`meter = _<:(_,(max(maxGR):meter_group((hbargraph("[1][unit:dB][tooltip: gain reduction in dB]", maxGR, 0))))):attach;`
* `N`: the number of channels of the compressor, known at compile time

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

To save CPU we cheat a bit, in a similar way as in the original libs:
instead of crosfading between two sets of gain calculators as above,
we take the `abs` of the audio from both the FF and FB, and crossfade between those,
and feed that into one set of gain calculators
again the strength is much higher when in FB mode, but implemented differently.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

----

### `(co.)RMS_FBcompressor_peak_limiter_N_chan`

N channel RMS feed back compressor into peak limiter feeding back into the FB compressor.
By combining them this way, they complement each other optimally:
the RMS compressor doesn't have to deal with the peaks,
and the peak limiter get's spared from the steady state signal.
The feedback part has a much higher strength, so they end up sounding similar.
`RMS_FBcompressor_peak_limiter_N_chan` is a standard Faust function.

#### Usage

```
si.bus(N) : RMS_FBcompressor_peak_limiter_N_chan(strength,thresh,threshLim,att,rel,knee,link,meter,meterLim,N) : si.bus(N)
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `threshLim`: dB level threshold above which the brickwall limiter kicks in
* `att`: attack time = time constant (sec) when level & compression going up
this is also used as the release time of the limiter
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
the limiter uses a knee half this size
* `link`: the amount of linkage between the channels: 0 = each channel is independent, 1 = all channels have the same amount of gain reduction
* `meter`: compressor gain reduction meter. It can be implemented with:
`meter = _<:(_,(max(maxGR):meter_group((hbargraph("[1][unit:dB][tooltip: gain reduction in dB]", maxGR, 0))))):attach;`
* `meterLim`: brickwall limiter gain reduction meter. It can be implemented with:
`meterLim = _<:(_,(max(maxGR):meter_group((hbargraph("[1][unit:dB][tooltip: gain reduction in dB]", maxGR, 0))))):attach;`
* `N`: the number of channels of the compressor, known at compile time

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

## Linear gain computer section

The gain computer functions in this section have been replaced by a version that outputs dBs,
but we retain the linear output version for backward compatibility.

----

### `(co.)peak_compression_gain_mono`

Mono dynamic range compressor gain computer with linear output.
`peak_compression_gain_mono` is a standard Faust function.

#### Usage

```
_ : peak_compression_gain_mono(strength,thresh,att,rel,knee,prePost) : _
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-threshold detector

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

----

### `(co.)peak_compression_gain_N_chan`

N channels dynamic range compressor gain computer with linear output.
`peak_compression_gain_N_chan` is a standard Faust function.

#### Usage

```
si.bus(N) : peak_compression_gain_N_chan(strength,thresh,att,rel,knee,prePost,link,N) : si.bus(N)
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-threshold detector
* `link`: the amount of linkage between the channels: 0 = each channel is independent, 1 = all channels have the same amount of gain reduction
* `N`: the number of channels of the compressor, known at compile time

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

----

### `(co.)RMS_compression_gain_mono`

Mono RMS dynamic range compressor gain computer with linear output.
`RMS_compression_gain_mono` is a standard Faust function.

#### Usage

```
_ : RMS_compression_gain_mono(strength,thresh,att,rel,knee,prePost) : _
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-threshold detector

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

----

### `(co.)RMS_compression_gain_N_chan`

RMS N channels dynamic range compressor gain computer with linear output.
`RMS_compression_gain_N_chan` is a standard Faust function.

#### Usage

```
si.bus(N) : RMS_compression_gain_N_chan(strength,thresh,att,rel,knee,prePost,link,N) : si.bus(N)
```

Where:

* `strength`: strength of the compression (0 = no compression, 1 means hard limiting, >1 means over-compression)
* `thresh`: dB level threshold above which compression kicks in
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression
* `knee`: a gradual increase in gain reduction around the threshold:
below thresh-(knee/2) there is no gain reduction,
above thresh+(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-threshold detector
* `link`: the amount of linkage between the channels: 0 = each channel is independent, 1 = all channels have the same amount of gain reduction
* `N`: the number of channels of the compressor, known at compile time

It uses a strength parameter instead of the traditional ratio, in order to be able to
function as a hard limiter.
For that you'd need a ratio of infinity:1, and you cannot express that in Faust.

Sometimes even bigger ratios are useful:
for example a group recording where one instrument is recorded with both a close microphone and a room microphone,
and the instrument is loud enough in the room mic when playing loud, but you want to boost it when it is playing soft.

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* Digital Dynamic Range Compressor Design,
A Tutorial and Analysis,
Dimitrios GIANNOULIS (<Dimitrios.Giannoulis@eecs.qmul.ac.uk>),
Michael MASSBERG (<michael@massberg.org>),
and Josuah D.REISS (<josh.reiss@eecs.qmul.ac.uk>)

## Original versions section

The functions in this section are largely superseded by the limiters above, but we
retain them for backward compatibility and for situations in which a more permissive,
MIT-style license is required.

----

### `(co.)compressor_lad_mono`

Mono dynamic range compressor with lookahead delay.
`compressor_lad_mono` is a standard Faust function.

#### Usage

```
_ : compressor_lad_mono(lad,ratio,thresh,att,rel) : _
```

Where:

* `lad`: lookahead delay in seconds (nonnegative) - gets rounded to nearest sample.
         The effective attack time is a good setting
* `ratio`: compression ratio (1 = no compression, >1 means compression)
           Ratios: 4 is moderate compression, 8 is strong compression,
           12 is mild limiting, and 20 is pretty hard limiting at the threshold
* `thresh`: dB level threshold above which compression kicks in (0 dB = max level)
* `att`: attack time = time constant (sec) when level & compression are going up
* `rel`: release time = time constant (sec) coming out of compression

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* [https://ccrma.stanford.edu/~jos/filters/Nonlinear_Filter_Example_Dynamic.html](https://ccrma.stanford.edu/~jos/filters/Nonlinear_Filter_Example_Dynamic.html)
* Albert Graef's "faust2pd"/examples/synth/compressor_.dsp
* More features: [https://github.com/magnetophon/faustCompressors](https://github.com/magnetophon/faustCompressors)

----

### `(co.)compressor_mono`

Mono dynamic range compressors.
`compressor_mono` is a standard Faust function.

#### Usage

```
_ : compressor_mono(ratio,thresh,att,rel) : _
```

Where:

* `ratio`: compression ratio (1 = no compression, >1 means compression)
           Ratios: 4 is moderate compression, 8 is strong compression,
           12 is mild limiting, and 20 is pretty hard limiting at the threshold
* `thresh`: dB level threshold above which compression kicks in (0 dB = max level)
* `att`: attack time = time constant (sec) when level & compression are going up
* `rel`: release time = time constant (sec) coming out of compression

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* [https://ccrma.stanford.edu/~jos/filters/Nonlinear_Filter_Example_Dynamic.html](https://ccrma.stanford.edu/~jos/filters/Nonlinear_Filter_Example_Dynamic.html)
* Albert Graef's "faust2pd"/examples/synth/compressor_.dsp
* More features: [https://github.com/magnetophon/faustCompressors](https://github.com/magnetophon/faustCompressors)

----

### `(co.)compressor_stereo`

Stereo dynamic range compressors.

#### Usage

```
_,_ : compressor_stereo(ratio,thresh,att,rel) : _,_
```

Where:

* `ratio`: compression ratio (1 = no compression, >1 means compression)
* `thresh`: dB level threshold above which compression kicks in (0 dB = max level)
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* [https://ccrma.stanford.edu/~jos/filters/Nonlinear_Filter_Example_Dynamic.html](https://ccrma.stanford.edu/~jos/filters/Nonlinear_Filter_Example_Dynamic.html)
* Albert Graef's "faust2pd"/examples/synth/compressor_.dsp
* More features: [https://github.com/magnetophon/faustCompressors](https://github.com/magnetophon/faustCompressors)

----

### `(co.)compression_gain_mono`

Compression-gain calculation for dynamic range compressors.

#### Usage

```
_ : compression_gain_mono(ratio,thresh,att,rel) : _
```

Where:

* `ratio`: compression ratio (1 = no compression, >1 means compression)
* `thresh`: dB level threshold above which compression kicks in (0 dB = max level)
* `att`: attack time = time constant (sec) when level & compression going up
* `rel`: release time = time constant (sec) coming out of compression

#### References

* [http://en.wikipedia.org/wiki/Dynamic_range_compression](http://en.wikipedia.org/wiki/Dynamic_range_compression)
* [https://ccrma.stanford.edu/~jos/filters/Nonlinear_Filter_Example_Dynamic.html](https://ccrma.stanford.edu/~jos/filters/Nonlinear_Filter_Example_Dynamic.html)
* Albert Graef's "faust2pd"/examples/synth/compressor_.dsp
* More features: [https://github.com/magnetophon/faustCompressors](https://github.com/magnetophon/faustCompressors)

----

### `(co.)limiter_1176_R4_mono`

A limiter guards against hard-clipping.  It can be
implemented as a compressor having a high threshold (near the
clipping level), fast attack, and high ratio.  Since
the compression ratio is so high, some knee smoothing is
desirable (for softer limiting).  This example is intended
to get you started using compressors as limiters, so all
parameters are hardwired here to nominal values.

`ratio`: 4 (moderate compression).
       See `compressor_mono` comments for a guide to other choices.
       Mike Shipley likes this (lowest) setting on the 1176.
       (Grammy award-winning mixer for Queen, Tom Petty, etc.).

`thresh`: -6 dB, meaning 4:1 compression begins at amplitude 1/2.

`att`: 800 MICROseconds (Note: scaled by ratio in the 1176)
        The 1176 range is said to be 20-800 microseconds.
        Faster attack gives "more bite" (e.g. on vocals),
        and makes hard-clipping less likely on fast overloads.

`rel`: 0.5 s (Note: scaled by ratio in the 1176)
        The 1176 range is said to be 50-1100 ms.

The 1176 also has a "bright, clear eq effect" (use filters.lib if desired).
`limiter_1176_R4_mono` is a standard Faust function.

#### Usage

```
 _ : limiter_1176_R4_mono : _
```

#### Reference:

* [http://en.wikipedia.org/wiki/1176_Peak_Limiter](http://en.wikipedia.org/wiki/1176_Peak_Limiter)

----

### `(co.)limiter_1176_R4_stereo`

A limiter guards against hard-clipping.  It can be
implemented as a compressor having a high threshold (near the
clipping level), fast attack and release, and high ratio.  Since
the ratio is so high, some knee smoothing is
desirable ("soft limiting").  This example is intended
to get you started using `compressor_*` as a limiter, so all
parameters are hardwired to nominal values here.

`ratio`: 4 (moderate compression), 8 (severe compression),
         12 (mild limiting), or 20 to 1 (hard limiting).

`att`: 20-800 MICROseconds (Note: scaled by ratio in the 1176).

`rel`: 50-1100 ms (Note: scaled by ratio in the 1176).

Mike Shipley likes 4:1 (Grammy-winning mixer for Queen, Tom Petty, etc.)
Faster attack gives "more bite" (e.g. on vocals).
He hears a bright, clear eq effect as well (not implemented here).

#### Usage

```
 _,_ : limiter_1176_R4_stereo : _,_
```

#### Reference:

* [http://en.wikipedia.org/wiki/1176_Peak_Limiter](http://en.wikipedia.org/wiki/1176_Peak_Limiter)

## Expanders


----

### `(co.)peak_expansion_gain_N_chan_db`

N channels dynamic range expander gain computer.
`peak_expansion_gain_N_chan_db` is a standard Faust function.

#### Usage

```
si.bus(N) : peak_expansion_gain_N_chan_db(strength,thresh,range,att,hold,rel,knee,prePost,link,maxHold,N) : si.bus(N)
```

Where:

* `strength`: strength of the expansion (0 = no expansion, 100 means gating, <1 means upward compression)
* `thresh`: dB level threshold below which expansion kicks in
* `range`: maximum amount of expansion in dB
* `att`: attack time = time constant (sec) coming out of expansion
* `hold` : hold time (sec)
* `rel`: release time = time constant (sec) going into expansion
* `knee`: a gradual increase in gain reduction around the threshold:
above thresh+(knee/2) there is no gain reduction,
below thresh-(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-range detector
* `link`: the amount of linkage between the channels: 0 = each channel is independent, 1 = all channels have the same amount of gain reduction
* `maxHold`: the maximum hold time in samples, known at compile time
* `N`: the number of channels of the gain computer, known at compile time


----

### `(co.)expander_N_chan`

Feed forward N channels dynamic range expander.
`expander_N_chan` is a standard Faust function.

#### Usage

```
si.bus(N) : expander_N_chan(strength,thresh,range,att,hold,rel,knee,prePost,link,meter,maxHold,N) : si.bus(N)
```

Where:

* `strength`: strength of the expansion (0 = no expansion, 100 means gating, <1 means upward compression)
* `thresh`: dB level threshold below which expansion kicks in
* `range`: maximum amount of expansion in dB
* `att`: attack time = time constant (sec) coming out of expansion
* `hold` : hold time
* `rel`: release time = time constant (sec) going into expansion
* `knee`: a gradual increase in gain reduction around the threshold:
above thresh+(knee/2) there is no gain reduction,
below thresh-(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-range detector
* `link`: the amount of linkage between the channels: 0 = each channel is independent, 1 = all channels have the same amount of gain reduction
* `meter`: a gain reduction meter. It can be implemented like so:
`meter = _<:(_, (ba.linear2db:max(maxGR):meter_group((hbargraph("[1][unit:dB][tooltip: gain reduction in dB]", maxGR, 0))))):attach;`
* `maxHold`: the maximum hold time in samples, known at compile time
* `N`: the number of channels of the expander, known at compile time


----

### `(co.)expanderSC_N_chan`

Feed forward N channels dynamic range expander with sidechain.
`expanderSC_N_chan` is a standard Faust function.

#### Usage

```
si.bus(N) : expanderSC_N_chan(strength,thresh,range,att,hold,rel,knee,prePost,link,meter,maxHold,N,SCfunction,SCswitch,SCsignal) : si.bus(N)
```

Where:

* `strength`: strength of the expansion (0 = no expansion, 100 means gating, <1 means upward compression)
* `thresh`: dB level threshold below which expansion kicks in
* `range`: maximum amount of expansion in dB
* `att`: attack time = time constant (sec) coming out of expansion
* `hold` : hold time
* `rel`: release time = time constant (sec) going into expansion
* `knee`: a gradual increase in gain reduction around the threshold:
above thresh+(knee/2) there is no gain reduction,
below thresh-(knee/2) there is the same gain reduction as without a knee,
and in between there is a gradual increase in gain reduction
* `prePost`: places the level detector either at the input or after the gain computer;
this turns it from a linear return-to-zero detector into a log  domain return-to-range detector
* `link`: the amount of linkage between the channels: 0 = each channel is independent, 1 = all channels have the same amount of gain reduction
* `meter`: a gain reduction meter. It can be implemented like so:
`meter = _<:(_, (ba.linear2db:max(maxGR):meter_group((hbargraph("[1][unit:dB][tooltip: gain reduction in dB]", maxGR, 0))))):attach;`
* `maxHold`: the maximum hold time in samples, known at compile time
* `N`: the number of channels of the expander, known at compile time
* `SCfunction` : a function that get's placed before the level-detector, needs to have a single input and output
* `SCswitch` : use either the regular audio input or the SCsignal as the input for the level detector
* `SCsignal` : an audio signal, to be used as the input for the level detector when SCswitch is 1


## Lookahead Limiters


----

### `(co.)limiter_lad_N`

N-channels lookahead limiter inspired by IOhannes Zmölnig's post, which is 
in turn based on the thesis by Peter Falkner "Entwicklung eines digitalen
Stereo-Limiters mit Hilfe des Signalprozessors DSP56001".
This version of the limiter uses a peak-holder with smoothed
attack and release based on tau time constant filters.

It is also possible to use a time constant that is `2PI*tau` by dividing 
the attack and release times by `2PI`. This time constant allows for 
the amplitude profile to reach `1 - e^(-2PI)` of the final 
peak after the attack time. The input path can be delayed by the same 
amount as the attack time to synchronise input and amplitude profile, 
realising a system that is particularly effective as a colourless
(ideally) brickwall limiter.

Note that the effectiveness of the ceiling settings are dependent on
the other parameters, especially the time constant used for the
smoothing filters and the lookahead delay. 

Similarly, the colourless characteristics are also dependent on attack,
hold, and release times. Since fluctuations above ~15 Hz are
perceived as timbral effects, [Vassilakis and Kendall 2010] it is
reasonable to set the attack time to 1/15 seconds for a smooth amplitude
modulation. On the other hand, the hold time can be set to the
peak-to-peak period of the expected lowest frequency in the signal,
which allows for minimal distortion of the low frequencies. The
release time can then provide a perceptually linear and gradual gain 
increase determined by the user for any specific application.

The scaling factor for all the channels is determined by the loudest peak 
between them all, so that amplitude ratios between the signals are kept.

#### Usage

```
si.bus(N) : limiter_lad_N(N, LD, ceiling, attack, hold, release) : si.bus(N)
```

Where:

* `N`: is the number of channels, known at compile-time
* `LD`: is the lookahead delay in seconds, known at compile-time
* `ceiling`: is the linear amplitude output limit
* `attack`: is the attack time in seconds
* `hold`: is the hold time in seconds
* `release`: is the release time in seconds

Example for a stereo limiter: `limiter_lad_N(2, .01, 1, .01, .1, 1);`

#### Reference:

* [http://iem.at/~zmoelnig/publications/limiter](http://iem.at/~zmoelnig/publications/limiter)

----

### `(co.)limiter_lad_mono`


Specialised case of `limiter_lad_N` mono limiter.

#### Usage

```
_ : limiter_lad_mono(LD, ceiling, attack, hold, release) : _
```

Where:

* `LD`: is the lookahead delay in seconds, known at compile-time
* `ceiling`: is the linear amplitude output limit
* `attack`: is the attack time in seconds
* `hold`: is the hold time in seconds
* `release`: is the release time in seconds

#### Reference:

* [http://iem.at/~zmoelnig/publications/limiter](http://iem.at/~zmoelnig/publications/limiter)

----

### `(co.)limiter_lad_stereo`


Specialised case of `limiter_lad_N` stereo limiter.

#### Usage

```
_,_ : limiter_lad_stereo(LD, ceiling, attack, hold, release) : _,_
```

Where:

* `LD`: is the lookahead delay in seconds, known at compile-time
* `ceiling`: is the linear amplitude output limit
* `attack`: is the attack time in seconds
* `hold`: is the hold time in seconds
* `release`: is the release time in seconds

#### Reference:

* [http://iem.at/~zmoelnig/publications/limiter](http://iem.at/~zmoelnig/publications/limiter)

----

### `(co.)limiter_lad_quad`


Specialised case of `limiter_lad_N` quadraphonic limiter.

#### Usage

```
si.bus(4) : limiter_lad_quad(LD, ceiling, attack, hold, release) : si.bus(4)
```

Where:

* `LD`: is the lookahead delay in seconds, known at compile-time
* `ceiling`: is the linear amplitude output limit
* `attack`: is the attack time in seconds
* `hold`: is the hold time in seconds
* `release`: is the release time in seconds

#### Reference:

* [http://iem.at/~zmoelnig/publications/limiter](http://iem.at/~zmoelnig/publications/limiter)

----

### `(co.)limiter_lad_bw`


Specialised case of `limiter_lad_N` and ready-to-use unit-amplitude mono 
limiting function. This implementation, in particular, uses `2PI*tau`
time constant filters for attack and release smoothing with
synchronised input and gain signals. 

This function's best application is to be used as a brickwall limiter with 
the least colouring artefacts while keeping a not-so-slow release curve. 
Tests have shown that, given a pop song with 60 dB of amplification
and a 0-dB-ceiling, the loudest peak recorded was ~0.38 dB.

#### Usage

```
_ : limiter_lad_bw : _
```

#### Reference:

* [http://iem.at/~zmoelnig/publications/limiter](http://iem.at/~zmoelnig/publications/limiter)
