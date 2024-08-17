#  quantizers.lib 

Faust Frequency Quantization Library. Its official prefix is `qu`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/quantizers.lib](https://github.com/grame-cncm/faustlibraries/blob/master/quantizers.lib)

## Functions Reference


----

### `(qu.)quantize`

Configurable frequency quantization tool. Output only the frequencies that are part of the specified scale.
Works for positive audio frequencies.

#### Usage

```
_ : quantize(rf,nl) : _
```
Where :

* `rf` : frequency of the root note of the scale
* `nl` : list of the ratio of the frequencies of each note in relation to the root frequency

----

### `(qu.)quantizeSmoothed`

Configurable frequency quantization tool. Output frequencies that are closer to the frequencies of the specified scale notes.
Works for positive audio frequencies.


#### Usage

```
_ : quantizeSmoothed(rf,nl) : _
nl = (1,1.2,1.4,1.7);
```
Where :

* `rf` : frequency of the root note of the scale
* `nl` : list of the ratio of the frequencies of each note in relation to the root frequency

----

### `(qu.)ionian`

List of the frequency ratios of the notes of the ionian mode.

#### Usage
```
_ : quantize(rf,ionian) : _
```

Where:

* `rf`: frequency of the root note of the scale

----

### `(qu.)dorian`

List of the frequency ratios of the notes of the dorian mode.

#### Usage
```
_ : quantize(rf,dorian) : _
```

Where:

* `rf`: frequency of the root note of the scale

----

### `(qu.)phrygian`

List of the frequency ratios of the notes of the phrygian mode.

#### Usage
```
_ : quantize(rf,phrygian) : _
```

Where:

* `rf`: frequency of the root note of the scale

----

### `(qu.)lydian`

List of the frequency ratios of the notes of the lydian mode.

#### Usage
```
_ : quantize(rf,lydian) : _
```

Where:

* `rf`: frequency of the root note of the scale

----

### `(qu.)mixo`

List of the frequency ratios of the notes of the mixolydian mode.

#### Usage
```
_ : quantize(rf,mixo) : _
```

Where:

* `rf`: frequency of the root note of the scale

----

### `(qu.)eolian`

List of the frequency ratios of the notes of the eolian mode.

#### Usage
```
_ : quantize(rf,eolian) : _
```

Where:

* `rf`: frequency of the root note of the scale

----

### `(qu.)locrian`

List of the frequency ratios of the notes of the locrian mode.

#### Usage
```
_ : quantize(rf,locrian) : _
```

Where:

* `rf`: frequency of the root note of the scale

----

### `(qu.)pentanat`

List of the frequency ratios of the notes of the pythagorean tuning for the minor pentatonic scale.

#### Usage
```
_ : quantize(rf,pentanat) : _
```

Where:

* `rf`: frequency of the root note of the scale

----

### `(qu.)kumoi`

List of the frequency ratios of the notes of the kumoijoshi, the japanese pentatonic scale.

#### Usage
```
_ : quantize(rf,kumoi) : _
```

Where:

* `rf`: frequency of the root note of the scale

----

### `(qu.)natural`

List of the frequency ratios of the notes of the natural major scale.

#### Usage
```
_ : quantize(rf,natural) : _
```

Where:

* `rf`: frequency of the root note of the scale

----

### `(qu.)dodeca`

List of the frequency ratios of the notes of the dodecaphonic scale.

#### Usage
```
_ : quantize(rf,dodeca) : _
```

Where:

* `rf`: frequency of the root note of the scale

----

### `(qu.)dimin`

List of the frequency ratios of the notes of the diminished scale.

#### Usage
```
_ : quantize(rf,dimin) : _
```

Where:

* `rf`: frequency of the root note of the scale

----

### `(qu.)penta`

List of the frequency ratios of the notes of the minor pentatonic scale.

#### Usage
```
_ : quantize(rf,penta) : _
```

Where:

* `rf`: frequency of the root note of the scale
