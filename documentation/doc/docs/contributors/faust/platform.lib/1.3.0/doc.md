#  platform.lib 

A library to handle platform specific code in Faust. Its official prefix is `pl`.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/platform.lib](https://github.com/grame-cncm/faustlibraries/blob/master/platform.lib)

----

### `(pl.)SR`

Current sampling rate (between 1 and 192000Hz). Constant during
program execution. Setting this value to a constant will allow the
compiler to optimize the code by computing constant expressions at
compile time, and can be valuable for performance, especially on
embedded systems.

----

### `(pl.)BS`

Current block-size (between 1 and 16384 frames). Can change during the execution.

----

### `(pl.)tablesize`

Oscillator table size. This value is used to define the size of the
table used by the oscillators. It is usually a power of 2 and can be lowered
to save memory. The default value is 65536.
