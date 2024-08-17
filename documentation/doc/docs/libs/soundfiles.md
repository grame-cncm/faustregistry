#  soundfiles.lib 

A library to handle soundfiles in Faust. Its official prefix is `so`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/soundfiles.lib](https://github.com/grame-cncm/faustlibraries/blob/master/soundfiles.lib)

## Functions Reference


----

### `(so.)loop`

Play a soundfile in a loop taking into account its sampling rate.
`loop` is a standard Faust function.

#### Usage

```
loop(sf, part) : si.bus(outputs(sf))
```

Where:

* `sf`: the soundfile
* `part`: the part in the soundfile list of sounds


----

### `(so.)loop_speed`

Play a soundfile in a loop taking into account its sampling rate, with speed control.
`loop_speed` is a standard Faust function.

#### Usage

```
loop_speed(sf, part, speed) : si.bus(outputs(sf))
```

Where:

* `sf`: the soundfile
* `part`: the part in the soundfile list of sounds
* `speed`: the speed between 0 and n


----

### `(so.)loop_speed_level`

Play a soundfile in a loop taking into account its sampling rate, with speed and level controls.
`loop_speed_level` is a standard Faust function.

#### Usage

```
loop_speed_level(sf, part, speed, level) : si.bus(outputs(sf))
```

Where:

* `sf`: the soundfile
* `part`: the part in the soundfile list of sounds
* `speed`: the speed between 0 and n
* `level`: the volume between 0 and n

