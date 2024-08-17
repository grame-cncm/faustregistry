#  physmodels.lib 

Faust physical modeling library. Its official prefix is `pm`.

This library provides an environment to facilitate physical modeling of musical
instruments. It contains dozens of functions implementing low and high level
elements going from a simple waveguide to fully operational models with
built-in UI, etc.

It is organized as follows:

* [Global Variables](#global-variables): useful pre-defined variables for
physical modeling (e.g., speed of sound, etc.).
* [Conversion Tools](#conversion-tools-1): conversion functions specific
to physical modeling (e.g., length to frequency, etc.).
* [Bidirectional Utilities](#bidirectional-utilities): functions to create
bidirectional block diagrams for physical modeling.
* [Basic Elements](#basic-elements-1): waveguides, specific types of filters, etc.
* [String Instruments](#string-instruments): various types of strings
(e.g., steel, nylon, etc.), bridges, guitars, etc.
* [Bowed String Instruments](#bowed-string-instruments): parts and models
specific to bowed string instruments (e.g., bows, bridges, violins, etc.).
* [Wind Instrument](#wind-instruments): parts and models specific to wind
instruments (e.g., reeds, mouthpieces, flutes, clarinets, etc.).
* [Exciters](#exciters): pluck generators, "blowers", etc.
* [Modal Percussions](#modal-percussions): percussion instruments based on
modal models.
* [Vocal Synthesis](#vocal-synthesis): functions for various vocal synthesis
techniques (e.g., fof, source/filter, etc.) and vocal synthesizers.
* [Misc Functions](#misc-functions): any other functions that don't fit in
the previous category (e.g., nonlinear filters, etc.).

This library is part of the Faust Physical Modeling ToolKit.
More information on how to use this library can be found on this [page](https://ccrma.stanford.edu/~rmichon/pmFaust) or this [video](https://faust.grame.fr/community/events/#introduction-to-the-faust-physical-modeling-toolkit-romain-michon). Tutorials on how to make
physical models of musical instruments using Faust can be found
[here](https://ccrma.stanford.edu/~rmichon/faustTutorials/#making-physical-models-of-musical-instruments-with-faust) as well.

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/physmodels.lib](https://github.com/grame-cncm/faustlibraries/blob/master/physmodels.lib)

## Global Variables

Useful pre-defined variables for physical modeling.

----

### `(pm.)speedOfSound`

Speed of sound in meters per second (340m/s).

----

### `(pm.)maxLength`

The default maximum length (3) in meters of strings and tubes used in this
library. This variable should be overriden to allow longer strings or tubes.

## Conversion Tools

Useful conversion tools for physical modeling.

----

### `(pm.)f2l`

Frequency to length in meters.

#### Usage

```
f2l(freq) : distanceInMeters
```

Where:

* `freq`: the frequency

----

### `(pm.)l2f`

Length in meters to frequency.

#### Usage

```
l2f(length) : freq
```

Where:

* `length`: length/distance in meters

----

### `(pm.)l2s`

Length in meters to number of samples.

#### Usage

```
l2s(l) : numberOfSamples
```

Where:

* `l`: length in meters

## Bidirectional Utilities

Set of fundamental functions to create bi-directional block diagrams in Faust.
These elements are used as the basis of this library to connect high level
elements (e.g., mouthpieces, strings, bridge, instrument body, etc.). Each
block has 3 inputs and 3 outputs. The first input/output carry left going
waves, the second input/output carry right going waves, and the third
input/output is used to carry any potential output signal to the end of the
algorithm.

----

### `(pm.)basicBlock`

Empty bidirectional block to be used with [`chain`](#chain): 3 signals ins
and 3 signals out.

#### Usage

```
chain(basicBlock : basicBlock : etc.)
```

----

### `(pm.)chain`

Creates a chain of bidirectional blocks.
Blocks must have 3 inputs and outputs. The first input/output carry left
going waves, the second input/output carry right going waves, and the third
input/output is used to carry any potential output signal to the end of the
algorithm. The implied one sample delay created by the `~` operator is
generalized to the left and right going waves. Thus, `n` blocks in `chain()`
will add an `n` samples delay to both left and right going waves.

#### Usage

```
leftGoingWaves,rightGoingWaves,mixedOutput : chain( A : B ) : leftGoingWaves,rightGoingWaves,mixedOutput
with{
		A = _,_,_;
};
```

----

### `(pm.)inLeftWave`

Adds a signal to left going waves anywhere in a [`chain`](#chain) of blocks.

#### Usage

```
model(x) = chain(A : inLeftWave(x) : B)
```

Where `A` and `B` are bidirectional blocks and `x` is the signal added to left
going waves in that chain.

----

### `(pm.)inRightWave`

Adds a signal to right going waves anywhere in a [`chain`](#chain) of blocks.

#### Usage

```
model(x) = chain(A : inRightWave(x) : B)
```

Where `A` and `B` are bidirectional blocks and `x` is the signal added to right
going waves in that chain.

----

### `(pm.)in`

Adds a signal to left and right going waves anywhere in a [`chain`](#chain)
of blocks.

#### Usage

```
model(x) = chain(A : in(x) : B)
```

Where `A` and `B` are bidirectional blocks and `x` is the signal added to
left and right going waves in that chain.

----

### `(pm.)outLeftWave`

Sends the signal of left going waves to the output channel of the [`chain`](#chain).

#### Usage

```
chain(A : outLeftWave : B)
```

Where `A` and `B` are bidirectional blocks.

----

### `(pm.)outRightWave`

Sends the signal of right going waves to the output channel of the [`chain`](#chain).

#### Usage

```
chain(A : outRightWave : B)
```

Where `A` and `B` are bidirectional blocks.

----

### `(pm.)out`

Sends the signal of right and left going waves to the output channel of the
[`chain`](#chain).

#### Usage

```
chain(A : out : B)
```

Where `A` and `B` are bidirectional blocks.

----

### `(pm.)terminations`

Creates terminations on both sides of a [`chain`](#chain) without closing
the inputs and outputs of the bidirectional signals chain. As for
[`chain`](#chain), this function adds a 1 sample delay to the bidirectional
signal, both ways. Of course, this function can be nested within a
[`chain`](#chain).

#### Usage

```
terminations(a,b,c)
with{
};
```

----

### `(pm.)lTermination`

Creates a termination on the left side of a [`chain`](#chain) without
closing the inputs and outputs of the bidirectional signals chain. This
function adds a 1 sample delay near the termination and can be nested
within another [`chain`](#chain).

#### Usage

```
lTerminations(a,b)
with{
};
```

----

### `(pm.)rTermination`

Creates a termination on the right side of a [`chain`](#chain) without
closing the inputs and outputs of the bidirectional signals chain. This
function adds a 1 sample delay near the termination and can be nested
within another [`chain`](#chain).

#### Usage

```
rTerminations(b,c)
with{
};
```

----

### `(pm.)closeIns`

Closes the inputs of a bidirectional chain in all directions.

#### Usage

```
closeIns : chain(...) : _,_,_
```

----

### `(pm.)closeOuts`

Closes the outputs of a bidirectional chain in all directions except for the
main signal output (3d output).

#### Usage

```
_,_,_ : chain(...) : _
```

----

### `(pm.)endChain`

Closes the inputs and outputs of a bidirectional chain in all directions
except for the main signal output (3d output).

#### Usage

```
endChain(chain(...)) : _
```

## Basic Elements

Basic elements for physical modeling (e.g., waveguides, specific filters,
etc.).

----

### `(pm.)waveguideN`

A series of waveguide functions based on various types of delays (see
[`fdelay[n]`](#fdelayn)).

#### List of functions

* `waveguideUd`: unit delay waveguide
* `waveguideFd`: fractional delay waveguide
* `waveguideFd2`: second order fractional delay waveguide
* `waveguideFd4`: fourth order fractional delay waveguide

#### Usage

```
chain(A : waveguideUd(nMax,n) : B)
```

Where:

* `nMax`: the maximum length of the delays in the waveguide
* `n`: the length of the delay lines in samples.

----

### `(pm.)waveguide`

Standard `pm.lib` waveguide (based on [`waveguideFd4`](#waveguiden)).

#### Usage

```
chain(A : waveguide(nMax,n) : B)
```

Where:

* `nMax`: the maximum length of the delays in the waveguide
* `n`: the length of the delay lines in samples.

----

### `(pm.)bridgeFilter`

Generic two zeros bridge FIR filter (as implemented in the
[STK](https://ccrma.stanford.edu/software/stk/)) that can be used to
implement the reflectance violin, guitar, etc. bridges.

#### Usage

```
_ : bridge(brightness,absorption) : _
```

Where:

* `brightness`: controls the damping of high frequencies (0-1)
* `absorption`: controls the absorption of the brige and thus the t60 of
the string plugged to it (0-1) (1 = 20 seconds)

----

### `(pm.)modeFilter`

Resonant bandpass filter that can be used to implement a single resonance
(mode).

#### Usage

```
_ : modeFilter(freq,t60,gain) : _
```

Where:

* `freq`: mode frequency
* `t60`: mode resonance duration (in seconds)
* `gain`: mode gain (0-1)

## String Instruments

Low and high level string instruments parts. Most of the elements in
this section can be used in a bidirectional chain.

----

### `(pm.)stringSegment`

A string segment without terminations (just a simple waveguide).

#### Usage

```
chain(A : stringSegment(maxLength,length) : B)
```

Where:

* `maxLength`: the maximum length of the string in meters (should be static)
* `length`: the length of the string in meters

----

### `(pm.)openString`

A bidirectional block implementing a basic "generic" string with a
selectable excitation position. Lowpass filters are built-in and
allow to simulate the effect of dispersion on the sound and thus
to change the "stiffness" of the string.

#### Usage

```
chain(... : openString(length,stiffness,pluckPosition,excitation) : ...)
```

Where:

* `length`: the length of the string in meters
* `stiffness`: the stiffness of the string (0-1) (1 for max stiffness)
* `pluckPosition`: excitation position (0-1) (1 is bottom)
* `excitation`: the excitation signal

----

### `(pm.)nylonString`

A bidirectional block implementing a basic nylon string with selectable
excitation position. This element is based on [`openString`](#openstring)
and has a fix stiffness corresponding to that of a nylon string.

#### Usage

```
chain(... : nylonString(length,pluckPosition,excitation) : ...)
```

Where:

* `length`: the length of the string in meters
* `pluckPosition`: excitation position (0-1) (1 is bottom)
* `excitation`: the excitation signal

----

### `(pm.)steelString`

A bidirectional block implementing a basic steel string with selectable
excitation position. This element is based on [`openString`](#openstring)
and has a fix stiffness corresponding to that of a steel string.

#### Usage

```
chain(... : steelString(length,pluckPosition,excitation) : ...)
```

Where:

* `length`: the length of the string in meters
* `pluckPosition`: excitation position (0-1) (1 is bottom)
* `excitation`: the excitation signal

----

### `(pm.)openStringPick`

A bidirectional block implementing a "generic" string with selectable
excitation position. It also has a built-in pickup whose position is the
same as the excitation position. Thus, moving the excitation position
will also move the pickup.

#### Usage

```
chain(... : openStringPick(length,stiffness,pluckPosition,excitation) : ...)
```

Where:

* `length`: the length of the string in meters
* `stiffness`: the stiffness of the string (0-1) (1 for max stiffness)
* `pluckPosition`: excitation position (0-1) (1 is bottom)
* `excitation`: the excitation signal

----

### `(pm.)openStringPickUp`

A bidirectional block implementing a "generic" string with selectable
excitation position and stiffness. It also has a built-in pickup whose
position can be independenly selected. The only constraint is that the
pickup has to be placed after the excitation position.

#### Usage

```
chain(... : openStringPickUp(length,stiffness,pluckPosition,excitation) : ...)
```

Where:

* `length`: the length of the string in meters
* `stiffness`: the stiffness of the string (0-1) (1 for max stiffness)
* `pluckPosition`: pluck position between the top of the string and the
pickup (0-1) (1 for same as pickup position)
* `pickupPosition`: position of the pickup on the string (0-1) (1 is bottom)
* `excitation`: the excitation signal

----

### `(pm.)openStringPickDown`

A bidirectional block implementing a "generic" string with selectable
excitation position and stiffness. It also has a built-in pickup whose
position can be independenly selected. The only constraint is that the
pickup has to be placed before the excitation position.

#### Usage

```
chain(... : openStringPickDown(length,stiffness,pluckPosition,excitation) : ...)
```

Where:

* `length`: the length of the string in meters
* `stiffness`: the stiffness of the string (0-1) (1 for max stiffness)
* `pluckPosition`: pluck position on the string (0-1) (1 is bottom)
* `pickupPosition`: position of the pickup between the top of the string
and the excitation position (0-1) (1 is excitation position)
* `excitation`: the excitation signal

----

### `(pm.)ksReflexionFilter`

The "typical" one-zero Karplus-strong feedforward reflexion filter. This
filter will be typically used in a termination (see below).

#### Usage

```
terminations(_,chain(...),ksReflexionFilter)
```

----

### `(pm.)rStringRigidTermination`

Bidirectional block implementing a right rigid string termination (no damping,
just phase inversion).

#### Usage

```
chain(rStringRigidTermination : stringSegment : ...)
```

----

### `(pm.)lStringRigidTermination`

Bidirectional block implementing a left rigid string termination (no damping,
just phase inversion).

#### Usage

```
chain(... : stringSegment : lStringRigidTermination)
```

----

### `(pm.)elecGuitarBridge`

Bidirectional block implementing a simple electric guitar bridge. This
block is based on [`bridgeFilter`](#bridgeFilter). The bridge doesn't
implement transmittance since it is not meant to be connected to a
body (unlike acoustic guitar). It also partially sets the resonance
duration of the string with the nuts used on the other side.

#### Usage

```
chain(... : stringSegment : elecGuitarBridge)
```

----

### `(pm.)elecGuitarNuts`

Bidirectional block implementing a simple electric guitar nuts. This
block is based on [`bridgeFilter`](#bridgeFilter) and does essentially
the same thing as [`elecGuitarBridge`](#elecguitarbridge), but on the
other side of the chain. It also partially sets the resonance duration of
the string with the bridge used on the other side.

#### Usage

```
chain(elecGuitarNuts : stringSegment : ...)
```

----

### `(pm.)guitarBridge`

Bidirectional block implementing a simple acoustic guitar bridge. This
bridge damps more hight frequencies than
[`elecGuitarBridge`](#elecguitarbridge) and implements a transmittance
filter. It also partially sets the resonance duration of the string with
the nuts used on the other side.

#### Usage

```
chain(... : stringSegment : guitarBridge)
```

----

### `(pm.)guitarNuts`

Bidirectional block implementing a simple acoustic guitar nuts. This
nuts damps more hight frequencies than
[`elecGuitarNuts`](#elecguitarnuts) and implements a transmittance
filter. It also partially sets the resonance duration of the string with
the bridge used on the other side.

#### Usage

```
chain(guitarNuts : stringSegment : ...)
```

----

### `(pm.)idealString`

An "ideal" string with rigid terminations and where the plucking position
and the pick-up position are the same. Since terminations are rigid, this
string will ring forever.

#### Usage

```
1-1' : idealString(length,reflexion,xPosition,excitation)
```

With:
* `length`: the length of the string in meters
* `pluckPosition`: the plucking position (0.001-0.999)
* `excitation`: the input signal for the excitation.

----

### `(pm.)ks`

A Karplus-Strong string (in that case, the string is implemented as a
one dimension waveguide).

#### Usage

```
ks(length,damping,excitation) : _
```

Where:

* `length`: the length of the string in meters
* `damping`: string damping (0-1)
* `excitation`: excitation signal

----

### `(pm.)ks_ui_MIDI`

Ready-to-use, MIDI-enabled Karplus-Strong string with buil-in UI.

#### Usage

```
ks_ui_MIDI : _
```

----

### `(pm.)elecGuitarModel`

A simple electric guitar model (without audio effects, of course) with
selectable pluck position.
This model implements a single string. Additional strings should be created
by making a polyphonic application out of this function. Pitch is changed by
changing the length of the string and not through a finger model.

#### Usage

```
elecGuitarModel(length,pluckPosition,mute,excitation) : _
```

Where:

* `length`: the length of the string in meters
* `pluckPosition`: pluck position (0-1) (1 is on the bridge)
* `mute`: mute coefficient (1 for no mute and 0 for instant mute)
* `excitation`: excitation signal

----

### `(pm.)elecGuitar`

A simple electric guitar model with steel strings (based on
[`elecGuitarModel`](#elecguitarmodel)) implementing an excitation
model.
This model implements a single string. Additional strings should be created
by making a polyphonic application out of this function.

#### Usage

```
elecGuitar(length,pluckPosition,trigger) : _
```

Where:

* `length`: the length of the string in meters
* `pluckPosition`: pluck position (0-1) (1 is on the bridge)
* `mute`: mute coefficient (1 for no mute and 0 for instant mute)
* `gain`: gain of the pluck (0-1)
* `trigger`: trigger signal (1 for on, 0 for off)

----

### `(pm.)elecGuitar_ui_MIDI`

Ready-to-use MIDI-enabled electric guitar physical model with built-in UI.

#### Usage

```
elecGuitar_ui_MIDI : _
```

----

### `(pm.)guitarBody`

WARNING: not implemented yet!
Bidirectional block implementing a simple acoustic guitar body.

#### Usage

```
chain(... : guitarBody)
```

----

### `(pm.)guitarModel`

A simple acoustic guitar model with steel strings and selectable excitation
position. This model implements a single string. Additional strings should be created
by making a polyphonic application out of this function. Pitch is changed by
changing the length of the string and not through a finger model.
WARNING: this function doesn't currently implement a body (just strings and
bridge).

#### Usage

```
guitarModel(length,pluckPosition,excitation) : _
```

Where:

* `length`: the length of the string in meters
* `pluckPosition`: pluck position (0-1) (1 is on the bridge)
* `excitation`: excitation signal

----

### `(pm.)guitar`

A simple acoustic guitar model with steel strings (based on
[`guitarModel`](#guitarmodel)) implementing an excitation model.
This model implements a single string. Additional strings should be created
by making a polyphonic application out of this function.

#### Usage

```
guitar(length,pluckPosition,trigger) : _
```

Where:

* `length`: the length of the string in meters
* `pluckPosition`: pluck position (0-1) (1 is on the bridge)
* `gain`: gain of the excitation
* `trigger`: trigger signal (1 for on, 0 for off)

----

### `(pm.)guitar_ui_MIDI`

Ready-to-use MIDI-enabled steel strings acoustic guitar physical model with
built-in UI.

#### Usage

```
guitar_ui_MIDI : _
```

----

### `(pm.)nylonGuitarModel`

A simple acoustic guitar model with nylon strings and selectable excitation
position. This model implements a single string. Additional strings should be created
by making a polyphonic application out of this function. Pitch is changed by
changing the length of the string and not through a finger model.
WARNING: this function doesn't currently implement a body (just strings and
bridge).

#### Usage

```
nylonGuitarModel(length,pluckPosition,excitation) : _
```

Where:

* `length`: the length of the string in meters
* `pluckPosition`: pluck position (0-1) (1 is on the bridge)
* `excitation`: excitation signal

----

### `(pm.)nylonGuitar`

A simple acoustic guitar model with nylon strings (based on
[`nylonGuitarModel`](#nylonguitarmodel)) implementing an excitation model.
This model implements a single string. Additional strings should be created
by making a polyphonic application out of this function.

#### Usage

```
nylonGuitar(length,pluckPosition,trigger) : _
```

Where:

* `length`: the length of the string in meters
* `pluckPosition`: pluck position (0-1) (1 is on the bridge)
* `gain`: gain of the excitation (0-1)
* `trigger`: trigger signal (1 for on, 0 for off)

----

### `(pm.)nylonGuitar_ui_MIDI`

Ready-to-use MIDI-enabled nylon strings acoustic guitar physical model with
built-in UI.

#### Usage

```
nylonGuitar_ui_MIDI : _
```

----

### `(pm.)modeInterpRes`

Modular string instrument resonator based on IR measurements made on 3D 
printed models. The 2D space allowing for the control of the shape and the
scale of the model is enabled by interpolating between modes parameters.
More information about this technique/project can be found here: 
* [https://ccrma.stanford.edu/~rmichon/3dPrintingModeling/](https://ccrma.stanford.edu/~rmichon/3dPrintingModeling/).

#### Usage

```
_ : modeInterpRes(nModes,x,y) : _
```

Where:

* `nModes`: number of modeled modes (40 max)
* `x`: shape of the resonator (0: square, 1: square with rounded corners, 2: round)
* `y`: scale of the resonator (0: small, 1: medium, 2: large)

----

### `(pm.)modularInterpBody`

Bidirectional block implementing a modular string instrument resonator 
(see [`modeInterpRes`](#pm.modeinterpres)).

#### Usage

```
chain(... : modularInterpBody(nModes,shape,scale) : ...)
```

Where:

* `nModes`: number of modeled modes (40 max)
* `shape`: shape of the resonator (0: square, 1: square with rounded corners, 2: round)
* `scale`: scale of the resonator (0: small, 1: medium, 2: large)

----

### `(pm.)modularInterpStringModel`

String instrument model with a modular body (see 
[`modeInterpRes`](#pm.modeinterpres) and 
* [https://ccrma.stanford.edu/~rmichon/3dPrintingModeling/](https://ccrma.stanford.edu/~rmichon/3dPrintingModeling/)).

#### Usage

```
modularInterpStringModel(length,pluckPosition,shape,scale,bodyExcitation,stringExcitation) : _
```

Where:

* `stringLength`: the length of the string in meters
* `pluckPosition`: pluck position (0-1) (1 is on the bridge)
* `shape`: shape of the resonator (0: square, 1: square with rounded corners, 2: round)
* `scale`: scale of the resonator (0: small, 1: medium, 2: large)
* `bodyExcitation`: excitation signal for the body
* `stringExcitation`: excitation signal for the string

----

### `(pm.)modularInterpInstr`

String instrument with a modular body (see 
[`modeInterpRes`](#pm.modeinterpres) and 
* [https://ccrma.stanford.edu/~rmichon/3dPrintingModeling/](https://ccrma.stanford.edu/~rmichon/3dPrintingModeling/)).

#### Usage

```
modularInterpInstr(stringLength,pluckPosition,shape,scale,gain,tapBody,triggerString) : _
```

Where:

* `stringLength`: the length of the string in meters
* `pluckPosition`: pluck position (0-1) (1 is on the bridge)
* `shape`: shape of the resonator (0: square, 1: square with rounded corners, 2: round)
* `scale`: scale of the resonator (0: small, 1: medium, 2: large)
* `gain`: of the string excitation
* `tapBody`: send an impulse in the body of the instrument where the string is connected (1 for on, 0 for off)
* `triggerString`: trigger signal for the string (1 for on, 0 for off)

----

### `(pm.)modularInterpInstr_ui_MIDI`

Ready-to-use MIDI-enabled string instrument with a modular body (see 
[`modeInterpRes`](#pm.modeinterpres) and 
* [https://ccrma.stanford.edu/~rmichon/3dPrintingModeling/](https://ccrma.stanford.edu/~rmichon/3dPrintingModeling/))
with built-in UI.

#### Usage

```
modularInterpInstr_ui_MIDI : _
```

## Bowed String Instruments

Low and high level basic string instruments parts. Most of the elements in
this section can be used in a bidirectional chain.

----

### `(pm.)bowTable`

Extremely basic bow table that can be used to implement a wide range of
bow types for many different bowed string instruments (violin, cello, etc.).

#### Usage

```
excitation : bowTable(offeset,slope) : _
```

Where:

* `excitation`: an excitation signal
* `offset`: table offset
* `slope`: table slope

----

### `(pm.)violinBowTable`

Violin bow table based on [`bowTable`](#bowtable).

#### Usage

```
bowVelocity : violinBowTable(bowPressure) : _
```

Where:

* `bowVelocity`: velocity of the bow/excitation signal (0-1)
* `bowPressure`: bow pressure on the string (0-1)

----

### `(pm.)bowInteraction`

Bidirectional block implementing the interaction of a bow in a
[`chain`](#chain).

#### Usage

```
chain(... : stringSegment : bowInteraction(bowTable) : stringSegment : ...)
```

Where:

* `bowTable`: the bow table

----

### `(pm.)violinBow`

Bidirectional block implementing a violin bow and its interaction with
a string.

#### Usage

```
chain(... : stringSegment : violinBow(bowPressure,bowVelocity) : stringSegment : ...)
```

Where:

* `bowVelocity`: velocity of the bow / excitation signal (0-1)
* `bowPressure`: bow pressure on the string (0-1)

----

### `(pm.)violinBowedString`

Violin bowed string bidirectional block with controllable bow position.
Terminations are not implemented in this model.

#### Usage

```
chain(nuts : violinBowedString(stringLength,bowPressure,bowVelocity,bowPosition) : bridge)
```

Where:

* `stringLength`: the length of the string in meters
* `bowVelocity`: velocity of the bow / excitation signal (0-1)
* `bowPressure`: bow pressure on the string (0-1)
* `bowPosition`: the position of the bow on the string (0-1)

----

### `(pm.)violinNuts`

Bidirectional block implementing simple violin nuts. This function is
based on [`bridgeFilter`](#bridgefilter).

#### Usage

```
chain(violinNuts : stringSegment : ...)
```

----

### `(pm.)violinBridge`

Bidirectional block implementing a simple violin bridge. This function is
based on [`bridgeFilter`](#bridgefilter).

#### Usage

```
chain(... : stringSegment : violinBridge
```

----

### `(pm.)violinBody`

Bidirectional block implementing a simple violin body (just a simple
resonant lowpass filter).

#### Usage

```
chain(... : stringSegment : violinBridge : violinBody)
```

----

### `(pm.)violinModel`

Ready-to-use simple violin physical model. This model implements a single
string. Additional strings should be created
by making a polyphonic application out of this function. Pitch is changed
by changing the length of the string (and not through a finger model).

#### Usage

```
violinModel(stringLength,bowPressure,bowVelocity,bridgeReflexion,
bridgeAbsorption,bowPosition) : _
```

Where:

* `stringLength`: the length of the string in meters
* `bowVelocity`: velocity of the bow / excitation signal (0-1)
* `bowPressure`: bow pressure on the string (0-1))
* `bowPosition`: the position of the bow on the string (0-1)

----

### `(pm.)violin_ui`

Ready-to-use violin physical model with built-in UI.

#### Usage

```
violinModel_ui : _
```

----

### `(pm.)violin_ui_MIDI`

Ready-to-use MIDI-enabled violin physical model with built-in UI.

#### Usage

```
violin_ui_MIDI : _
```

## Wind Instruments

Low and high level basic wind instruments parts. Most of the elements in
this section can be used in a bidirectional chain.

----

### `(pm.)openTube`

A tube segment without terminations (same as [`stringSegment`](#stringsegment)).

#### Usage

```
chain(A : openTube(maxLength,length) : B)
```

Where:

* `maxLength`: the maximum length of the tube in meters (should be static)
* `length`: the length of the tube in meters

----

### `(pm.)reedTable`

Extremely basic reed table that can be used to implement a wide range of
single reed types for many different instruments (saxophone, clarinet, etc.).

#### Usage

```
excitation : reedTable(offeset,slope) : _
```

Where:

* `excitation`: an excitation signal
* `offset`: table offset
* `slope`: table slope

----

### `(pm.)fluteJetTable`

Extremely basic flute jet table.

#### Usage

```
excitation : fluteJetTable : _
```

Where:

* `excitation`: an excitation signal

----

### `(pm.)brassLipsTable`

Simple brass lips/mouthpiece table. Since this implementation is very basic
and that the lips and tube of the instrument are coupled to each other, the
length of that tube must be provided here.

#### Usage

```
excitation : brassLipsTable(tubeLength,lipsTension) : _
```

Where:

* `excitation`: an excitation signal (can be DC)
* `tubeLength`: length in meters of the tube connected to the mouthpiece
* `lipsTension`: tension of the lips (0-1) (default: 0.5)

----

### `(pm.)clarinetReed`

Clarinet reed based on [`reedTable`](#reedtable) with controllable
stiffness.

#### Usage

```
excitation : clarinetReed(stiffness) : _
```

Where:

* `excitation`: an excitation signal
* `stiffness`: reed stiffness (0-1)

----

### `(pm.)clarinetMouthPiece`

Bidirectional block implementing a clarinet mouthpiece as well as the various
interactions happening with traveling waves. This element is ready to be
plugged to a tube...

#### Usage

```
chain(clarinetMouthPiece(reedStiffness,pressure) : tube : etc.)
```

Where:

* `pressure`: the pressure of the air flow (DC) created by the virtual performer (0-1).
This can also be any kind of signal that will directly injected in the mouthpiece
(e.g., breath noise, etc.).
* `reedStiffness`: reed stiffness (0-1)

----

### `(pm.)brassLips`

Bidirectional block implementing a brass mouthpiece as well as the various
interactions happening with traveling waves. This element is ready to be
plugged to a tube...

#### Usage

```
chain(brassLips(tubeLength,lipsTension,pressure) : tube : etc.)
```

Where:

* `tubeLength`: length in meters of the tube connected to the mouthpiece
* `lipsTension`: tension of the lips (0-1) (default: 0.5)
* `pressure`: the pressure of the air flow (DC) created by the virtual performer (0-1).
This can also be any kind of signal that will directly injected in the mouthpiece
(e.g., breath noise, etc.).

----

### `(pm.)fluteEmbouchure`

Bidirectional block implementing a flute embouchure as well as the various
interactions happening with traveling waves. This element is ready to be
plugged between tubes segments...

#### Usage

```
chain(... : tube : fluteEmbouchure(pressure) : tube : etc.)
```

Where:

* `pressure`: the pressure of the air flow (DC) created by the virtual
performer (0-1).
This can also be any kind of signal that will directly injected in the
mouthpiece (e.g., breath noise, etc.).

----

### `(pm.)wBell`

Generic wind instrument bell bidirectional block that should be placed at
the end of a [`chain`](#chain).

#### Usage

```
chain(... : wBell(opening))
```

Where:

* `opening`: the "opening" of bell (0-1)

----

### `(pm.)fluteHead`

Simple flute head implementing waves reflexion.

#### Usage

```
chain(fluteHead : tube : ...)
```

----

### `(pm.)fluteFoot`

Simple flute foot implementing waves reflexion and dispersion.

#### Usage

```
chain(... : tube : fluteFoot)
```

----

### `(pm.)clarinetModel`

A simple clarinet physical model without tone holes (pitch is changed by
changing the length of the tube of the instrument).

#### Usage

```
clarinetModel(length,pressure,reedStiffness,bellOpening) : _
```

Where:

* `tubeLength`: the length of the tube in meters
* `pressure`: the pressure of the air flow created by the virtual performer (0-1).
This can also be any kind of signal that will directly injected in the mouthpiece
(e.g., breath noise, etc.).
* `reedStiffness`: reed stiffness (0-1)
* `bellOpening`: the opening of bell (0-1)

----

### `(pm.)clarinetModel_ui`

Same as [`clarinetModel`](#clarinetModel) but with a built-in UI. This function
doesn't implement a virtual "blower", thus `pressure` remains an argument here.

#### Usage

```
clarinetModel_ui(pressure) : _
```

Where:

* `pressure`: the pressure of the air flow created by the virtual performer (0-1).
This can also be any kind of signal that will be directly injected in the mouthpiece
(e.g., breath noise, etc.).

----

### `(pm.)clarinet_ui`

Ready-to-use clarinet physical model with built-in UI based on
[`clarinetModel`](#clarinetmodel).

#### Usage

```
clarinet_ui : _
```

----

### `(pm.)clarinet_ui_MIDI`

Ready-to-use MIDI compliant clarinet physical model with built-in UI.

#### Usage

```
clarinet_ui_MIDI : _
```

----

### `(pm.)brassModel`

A simple generic brass instrument physical model without pistons
(pitch is changed by changing the length of the tube of the instrument).
This model is kind of hard to control and might not sound very good if
bad parameters are given to it...

#### Usage

```
brassModel(tubeLength,lipsTension,mute,pressure) : _
```

Where:

* `tubeLength`: the length of the tube in meters
* `lipsTension`: tension of the lips (0-1) (default: 0.5)
* `mute`: mute opening at the end of the instrument (0-1) (default: 0.5)
* `pressure`: the pressure of the air flow created by the virtual performer (0-1).
This can also be any kind of signal that will directly injected in the mouthpiece
(e.g., breath noise, etc.).

----

### `(pm.)brassModel_ui`

Same as [`brassModel`](#brassModel) but with a built-in UI. This function
doesn't implement a virtual "blower", thus `pressure` remains an argument here.

#### Usage

```
brassModel_ui(pressure) : _
```

Where:

* `pressure`: the pressure of the air flow created by the virtual performer (0-1).
This can also be any kind of signal that will be directly injected in the mouthpiece
(e.g., breath noise, etc.).

----

### `(pm.)brass_ui`

Ready-to-use brass instrument physical model with built-in UI based on
[`brassModel`](#brassmodel).

#### Usage

```
brass_ui : _
```

----

### `(pm.)brass_ui_MIDI`

Ready-to-use MIDI-controllable brass instrument physical model with built-in UI.

#### Usage

```
brass_ui_MIDI : _
```

----

### `(pm.)fluteModel`

A simple generic flute instrument physical model without tone holes
(pitch is changed by changing the length of the tube of the instrument).

#### Usage

```
fluteModel(tubeLength,mouthPosition,pressure) : _
```

Where:

* `tubeLength`: the length of the tube in meters
* `mouthPosition`: position of the mouth on the embouchure (0-1) (default: 0.5)
* `pressure`: the pressure of the air flow created by the virtual performer (0-1).
This can also be any kind of signal that will directly injected in the mouthpiece
(e.g., breath noise, etc.).

----

### `(pm.)fluteModel_ui`

Same as [`fluteModel`](#fluteModel) but with a built-in UI. This function
doesn't implement a virtual "blower", thus `pressure` remains an argument here.

#### Usage

```
fluteModel_ui(pressure) : _
```

Where:

* `pressure`: the pressure of the air flow created by the virtual performer (0-1).
This can also be any kind of signal that will be directly injected in the mouthpiece
(e.g., breath noise, etc.).

----

### `(pm.)flute_ui`

Ready-to-use flute physical model with built-in UI based on
[`fluteModel`](#flutemodel).

#### Usage

```
flute_ui : _
```

----

### `(pm.)flute_ui_MIDI`

Ready-to-use MIDI-controllable flute physical model with built-in UI.

#### Usage

```
flute_ui_MIDI : _
```

## Exciters

Various kind of excitation signal generators.

----

### `(pm.)impulseExcitation`

Creates an impulse excitation of one sample.

#### Usage

```
gate = button('gate');
impulseExcitation(gate) : chain;
```

Where:

* `gate`: a gate button

----

### `(pm.)strikeModel`

Creates a filtered noise excitation.

#### Usage

```
gate = button('gate');
strikeModel(LPcutoff,HPcutoff,sharpness,gain,gate) : chain;
```

Where:

* `HPcutoff`: highpass cutoff frequency
* `LPcutoff`: lowpass cutoff frequency
* `sharpness`: sharpness of the attack and release (0-1)
* `gain`: gain of the excitation
* `gate`: a gate button/trigger signal (0/1)

----

### `(pm.)strike`

Strikes generator with controllable excitation position.

#### Usage

```
gate = button('gate');
strike(exPos,sharpness,gain,gate) : chain;
```

Where:

* `exPos`: excitation position wiht 0: for max low freqs and 1: for max high
freqs. So, on membrane for example, 0 would be the middle and 1 the edge
* `sharpness`: sharpness of the attack and release (0-1)
* `gain`: gain of the excitation
* `gate`: a gate button/trigger signal (0/1)

----

### `(pm.)pluckString`

Creates a plucking excitation signal.

#### Usage

```
trigger = button('gate');
pluckString(stringLength,cutoff,maxFreq,sharpness,trigger)
```

Where:

* `stringLength`: length of the string to pluck
* `cutoff`: cutoff ratio (1 for default)
* `maxFreq`: max frequency ratio (1 for default)
* `sharpness`: sharpness of the attack and release (1 for default)
* `gain`: gain of the excitation (0-1)
* `trigger`: trigger signal (1 for on, 0 for off)

----

### `(pm.)blower`

A virtual blower creating a DC signal with some breath noise in it.

#### Usage

```
blower(pressure,breathGain,breathCutoff) : _
```

Where:

* `pressure`: pressure (0-1)
* `breathGain`: breath noise gain (0-1) (recommended: 0.005)
* `breathCutoff`: breath cuttoff frequency (Hz) (recommended: 2000)

----

### `(pm.)blower_ui`

Same as [`blower`](#blower) but with a built-in UI.

#### Usage

```
blower : somethingToBeBlown
```

## Modal Percussions

High and low level functions for modal synthesis of percussion instruments.

----

### `(pm.)djembeModel`

Dirt-simple djembe modal physical model. Mode parameters are empirically
calculated and don't correspond to any measurements or 3D model. They
kind of sound good though :).

#### Usage

```
excitation : djembeModel(freq)
```

Where:

* `excitation`: excitation signal
* `freq`: fundamental frequency of the bar

----

### `(pm.)djembe`

Dirt-simple djembe modal physical model. Mode parameters are empirically
calculated and don't correspond to any measurements or 3D model. They
kind of sound good though :).

This model also implements a virtual "exciter".

#### Usage

```
djembe(freq,strikePosition,strikeSharpness,gain,trigger)
```

Where:

* `freq`: fundamental frequency of the model
* `strikePosition`: strike position (0 for the middle of the membrane and
1 for the edge)
* `strikeSharpness`: sharpness of the strike (0-1, default: 0.5)
* `gain`: gain of the strike
* `trigger`: trigger signal (0: off, 1: on)

----

### `(pm.)djembe_ui_MIDI`

Simple MIDI controllable djembe physical model with built-in UI.

#### Usage

```
djembe_ui_MIDI : _
```

----

### `(pm.)marimbaBarModel`

Generic marimba tone bar modal model.

This model was generated using
`mesh2faust` from a 3D CAD model of a marimba tone bar
(`libraries/modalmodels/marimbaBar`). The corresponding CAD model is that
of a C2 tone bar (original fundamental frequency: ~65Hz). While
`marimbaBarModel` allows to translate the harmonic content of the generated
sound by providing a frequency (`freq`), mode transposition has limits and
the model will sound less and less like a marimba tone bar as it
diverges from C2. To make an accurate model of a marimba, we'd want to have
an independent model for each bar...

This model contains 5 excitation positions going linearly from the center
bottom to the center top of the bar. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

#### Usage

```
excitation : marimbaBarModel(freq,exPos,t60,t60DecayRatio,t60DecaySlope)
```

Where:

* `excitation`: excitation signal
* `freq`: fundamental frequency of the bar
* `exPos`: excitation position (0-4)
* `t60`: T60 in seconds (recommended value: 0.1)
* `t60DecayRatio`: T60 decay ratio (recommended value: 1)
* `t60DecaySlope`: T60 decay slope (recommended value: 5)

----

### `(pm.)marimbaResTube`

Simple marimba resonance tube.

#### Usage

```
marimbaResTube(tubeLength,excitation)
```

Where:

* `tubeLength`: the length of the tube in meters
* `excitation`: the excitation signal (audio in)

----

### `(pm.)marimbaModel`

Simple marimba physical model implementing a single tone bar connected to
tube. This model is scalable and can be adapted to any size of bar/tube
(see [`marimbaBarModel`](#marimbabarmodel) to know more about the
limitations of this type of system).

#### Usage

```
excitation : marimbaModel(freq,exPos) : _
```

Where:

* `freq`: the frequency of the bar/tube couple
* `exPos`: excitation position (0-4)

----

### `(pm.)marimba`

Simple marimba physical model implementing a single tone bar connected to
tube. This model is scalable and can be adapted to any size of bar/tube
(see [`marimbaBarModel`](#marimbabarmodel) to know more about the
limitations of this type of system).

This function also implement a virtual exciter to drive the model.

#### Usage

```
excitation : marimba(freq,strikePosition,strikeCutoff,strikeSharpness,gain,trigger) : _
```

Where:

* `excitation`: the excitation signal
* `freq`: the frequency of the bar/tube couple
* `strikePosition`: strike position (0-4)
* `strikeCutoff`: cuttoff frequency of the strike genarator (recommended: ~7000Hz)
* `strikeSharpness`: sharpness of the strike (recommended: ~0.25)
* `gain`: gain of the strike (0-1)
* `trigger` signal (0: off, 1: on)

----

### `(pm.)marimba_ui_MIDI`

Simple MIDI controllable marimba physical model with built-in UI
implementing a single tone bar connected to
tube. This model is scalable and can be adapted to any size of bar/tube
(see [`marimbaBarModel`](#marimbabarmodel) to know more about the
limitations of this type of system).

#### Usage

```
marimba_ui_MIDI : _
```

----

### `(pm.)churchBellModel`

Generic church bell modal model generated by `mesh2faust` from
`libraries/modalmodels/churchBell`.

Modeled after T. Rossing and R. Perrin, Vibrations of Bells, Applied
Acoustics 2, 1987.

Model height is 301 mm.

This model contains 7 excitation positions going linearly from the
bottom to the top of the bell. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

#### Usage

```
excitation : churchBellModel(nModes,exPos,t60,t60DecayRatio,t60DecaySlope)
```

Where:

* `excitation`: the excitation signal
* `nModes`: number of synthesized modes (max: 50)
* `exPos`: excitation position (0-6)
* `t60`: T60 in seconds (recommended value: 0.1)
* `t60DecayRatio`: T60 decay ratio (recommended value: 1)
* `t60DecaySlope`: T60 decay slope (recommended value: 5)

----

### `(pm.)churchBell`

Generic church bell modal model.

Modeled after T. Rossing and R. Perrin, Vibrations of Bells, Applied
Acoustics 2, 1987.

Model height is 301 mm.

This model contains 7 excitation positions going linearly from the
bottom to the top of the bell. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

This function also implement a virtual exciter to drive the model.

#### Usage

```
excitation : churchBell(strikePosition,strikeCutoff,strikeSharpness,gain,trigger) : _
```

Where:

* `excitation`: the excitation signal
* `strikePosition`: strike position (0-6)
* `strikeCutoff`: cuttoff frequency of the strike genarator (recommended: ~7000Hz)
* `strikeSharpness`: sharpness of the strike (recommended: ~0.25)
* `gain`: gain of the strike (0-1)
* `trigger` signal (0: off, 1: on)

----

### `(pm.)churchBell_ui`

Church bell physical model based on [`churchBell`](#churchbell) with
built-in UI.

#### Usage

```
churchBell_ui : _
```

----

### `(pm.)englishBellModel`

English church bell modal model generated by `mesh2faust` from
`libraries/modalmodels/englishBell`.

Modeled after D.Bartocha and Baron, Influence of Tin Bronze Melting and
Pouring Parameters on Its Properties and Bell' Tone, Archives of Foundry
Engineering, 2016.

Model height is 1 m.

This model contains 7 excitation positions going linearly from the
bottom to the top of the bell. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

#### Usage

```
excitation : englishBellModel(nModes,exPos,t60,t60DecayRatio,t60DecaySlope)
```

Where:

* `excitation`: the excitation signal
* `nModes`: number of synthesized modes (max: 50)
* `exPos`: excitation position (0-6)
* `t60`: T60 in seconds (recommended value: 0.1)
* `t60DecayRatio`: T60 decay ratio (recommended value: 1)
* `t60DecaySlope`: T60 decay slope (recommended value: 5)

----

### `(pm.)englishBell`

English church bell modal model.

Modeled after D.Bartocha and Baron, Influence of Tin Bronze Melting and
Pouring Parameters on Its Properties and Bell' Tone, Archives of Foundry
Engineering, 2016.

Model height is 1 m.

This model contains 7 excitation positions going linearly from the
bottom to the top of the bell. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

This function also implement a virtual exciter to drive the model.

#### Usage

```
excitation : englishBell(strikePosition,strikeCutoff,strikeSharpness,gain,trigger) : _
```

Where:

* `excitation`: the excitation signal
* `strikePosition`: strike position (0-6)
* `strikeCutoff`: cuttoff frequency of the strike genarator (recommended: ~7000Hz)
* `strikeSharpness`: sharpness of the strike (recommended: ~0.25)
* `gain`: gain of the strike (0-1)
* `trigger` signal (0: off, 1: on)

----

### `(pm.)englishBell_ui`

English church bell physical model based on [`englishBell`](#englishbell) with
built-in UI.

#### Usage

```
englishBell_ui : _
```

----

### `(pm.)frenchBellModel`

French church bell modal model generated by `mesh2faust` from
`libraries/modalmodels/frenchBell`.

Modeled after D.Bartocha and Baron, Influence of Tin Bronze Melting and
Pouring Parameters on Its Properties and Bell' Tone, Archives of Foundry
Engineering, 2016.

Model height is 1 m.

This model contains 7 excitation positions going linearly from the
bottom to the top of the bell. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

#### Usage

```
excitation : frenchBellModel(nModes,exPos,t60,t60DecayRatio,t60DecaySlope)
```

Where:

* `excitation`: the excitation signal
* `nModes`: number of synthesized modes (max: 50)
* `exPos`: excitation position (0-6)
* `t60`: T60 in seconds (recommended value: 0.1)
* `t60DecayRatio`: T60 decay ratio (recommended value: 1)
* `t60DecaySlope`: T60 decay slope (recommended value: 5)

----

### `(pm.)frenchBell`

French church bell modal model.

Modeled after D.Bartocha and Baron, Influence of Tin Bronze Melting and
Pouring Parameters on Its Properties and Bell' Tone, Archives of Foundry
Engineering, 2016.

Model height is 1 m.

This model contains 7 excitation positions going linearly from the
bottom to the top of the bell. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

This function also implement a virtual exciter to drive the model.

#### Usage

```
excitation : frenchBell(strikePosition,strikeCutoff,strikeSharpness,gain,trigger) : _
```

Where:

* `excitation`: the excitation signal
* `strikePosition`: strike position (0-6)
* `strikeCutoff`: cuttoff frequency of the strike genarator (recommended: ~7000Hz)
* `strikeSharpness`: sharpness of the strike (recommended: ~0.25)
* `gain`: gain of the strike (0-1)
* `trigger` signal (0: off, 1: on)

----

### `(pm.)frenchBell_ui`

French church bell physical model based on [`frenchBell`](#frenchbell) with
built-in UI.

#### Usage

```
frenchBell_ui : _
```

----

### `(pm.)germanBellModel`

German church bell modal model generated by `mesh2faust` from
`libraries/modalmodels/germanBell`.

Modeled after D.Bartocha and Baron, Influence of Tin Bronze Melting and
Pouring Parameters on Its Properties and Bell' Tone, Archives of Foundry
Engineering, 2016.

Model height is 1 m.

This model contains 7 excitation positions going linearly from the
bottom to the top of the bell. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

#### Usage

```
excitation : germanBellModel(nModes,exPos,t60,t60DecayRatio,t60DecaySlope)
```

Where:

* `excitation`: the excitation signal
* `nModes`: number of synthesized modes (max: 50)
* `exPos`: excitation position (0-6)
* `t60`: T60 in seconds (recommended value: 0.1)
* `t60DecayRatio`: T60 decay ratio (recommended value: 1)
* `t60DecaySlope`: T60 decay slope (recommended value: 5)

----

### `(pm.)germanBell`

German church bell modal model.

Modeled after D.Bartocha and Baron, Influence of Tin Bronze Melting and
Pouring Parameters on Its Properties and Bell' Tone, Archives of Foundry
Engineering, 2016.

Model height is 1 m.

This model contains 7 excitation positions going linearly from the
bottom to the top of the bell. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

This function also implement a virtual exciter to drive the model.

#### Usage

```
excitation : germanBell(strikePosition,strikeCutoff,strikeSharpness,gain,trigger) : _
```

Where:

* `excitation`: the excitation signal
* `strikePosition`: strike position (0-6)
* `strikeCutoff`: cuttoff frequency of the strike genarator (recommended: ~7000Hz)
* `strikeSharpness`: sharpness of the strike (recommended: ~0.25)
* `gain`: gain of the strike (0-1)
* `trigger` signal (0: off, 1: on)

----

### `(pm.)germanBell_ui`

German church bell physical model based on [`germanBell`](#germanbell) with
built-in UI.

#### Usage

```
germanBell_ui : _
```

----

### `(pm.)russianBellModel`

Russian church bell modal model generated by `mesh2faust` from
`libraries/modalmodels/russianBell`.

Modeled after D.Bartocha and Baron, Influence of Tin Bronze Melting and
Pouring Parameters on Its Properties and Bell' Tone, Archives of Foundry
Engineering, 2016.

Model height is 2 m.

This model contains 7 excitation positions going linearly from the
bottom to the top of the bell. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

#### Usage

```
excitation : russianBellModel(nModes,exPos,t60,t60DecayRatio,t60DecaySlope)
```

Where:

* `excitation`: the excitation signal
* `nModes`: number of synthesized modes (max: 50)
* `exPos`: excitation position (0-6)
* `t60`: T60 in seconds (recommended value: 0.1)
* `t60DecayRatio`: T60 decay ratio (recommended value: 1)
* `t60DecaySlope`: T60 decay slope (recommended value: 5)

----

### `(pm.)russianBell`

Russian church bell modal model.

Modeled after D.Bartocha and Baron, Influence of Tin Bronze Melting and
Pouring Parameters on Its Properties and Bell' Tone, Archives of Foundry
Engineering, 2016.

Model height is 2 m.

This model contains 7 excitation positions going linearly from the
bottom to the top of the bell. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

This function also implement a virtual exciter to drive the model.

#### Usage

```
excitation : russianBell(strikePosition,strikeCutoff,strikeSharpness,gain,trigger) : _
```

Where:

* `excitation`: the excitation signal
* `strikePosition`: strike position (0-6)
* `strikeCutoff`: cuttoff frequency of the strike genarator (recommended: ~7000Hz)
* `strikeSharpness`: sharpness of the strike (recommended: ~0.25)
* `gain`: gain of the strike (0-1)
* `trigger` signal (0: off, 1: on)

----

### `(pm.)russianBell_ui`

Russian church bell physical model based on [`russianBell`](#russianbell) with
built-in UI.

#### Usage

```
russianBell_ui : _
```

----

### `(pm.)standardBellModel`

Standard church bell modal model generated by `mesh2faust` from
`libraries/modalmodels/standardBell`.

Modeled after T. Rossing and R. Perrin, Vibrations of Bells, Applied
Acoustics 2, 1987.

Model height is 1.8 m.

This model contains 7 excitation positions going linearly from the
bottom to the top of the bell. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

#### Usage

```
excitation : standardBellModel(nModes,exPos,t60,t60DecayRatio,t60DecaySlope)
```

Where:

* `excitation`: the excitation signal
* `nModes`: number of synthesized modes (max: 50)
* `exPos`: excitation position (0-6)
* `t60`: T60 in seconds (recommended value: 0.1)
* `t60DecayRatio`: T60 decay ratio (recommended value: 1)
* `t60DecaySlope`: T60 decay slope (recommended value: 5)

----

### `(pm.)standardBell`

Standard church bell modal model.

Modeled after T. Rossing and R. Perrin, Vibrations of Bells, Applied
Acoustics 2, 1987.

Model height is 1.8 m.

This model contains 7 excitation positions going linearly from the
bottom to the top of the bell. Obviously, a model with more excitation
position could be regenerated using `mesh2faust`.

This function also implement a virtual exciter to drive the model.

#### Usage

```
excitation : standardBell(strikePosition,strikeCutoff,strikeSharpness,gain,trigger) : _
```

Where:

* `excitation`: the excitation signal
* `strikePosition`: strike position (0-6)
* `strikeCutoff`: cuttoff frequency of the strike genarator (recommended: ~7000Hz)
* `strikeSharpness`: sharpness of the strike (recommended: ~0.25)
* `gain`: gain of the strike (0-1)
* `trigger` signal (0: off, 1: on)

----

### `(pm.)standardBell_ui`

Standard church bell physical model based on [`standardBell`](#standardbell) with
built-in UI.

#### Usage

```
standardBell_ui : _
```

## Vocal Synthesis

Vocal synthesizer functions (source/filter, fof, etc.).

----

### `(pm.)formantValues`

Formant data values.

The formant data used here come from the CSOUND manual
* [http://www.csounds.com/manual/html/](http://www.csounds.com/manual/html/).

#### Usage

```
ba.take(j+1,formantValues.f(i)) : _
ba.take(j+1,formantValues.g(i)) : _
ba.take(j+1,formantValues.bw(i)) : _
```

Where:

* `i`: formant number
* `j`: (voiceType*nFormants)+vowel
* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor, 3:
soprano, 4: tenor)
* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u)

----

### `(pm.)voiceGender`

Calculate the gender for the provided `voiceType` value. (0: male, 1: female)

#### Usage

```
voiceGender(voiceType) : _
```

Where:

* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor, 3: soprano, 4: tenor)

----

### `(pm.)skirtWidthMultiplier`

Calculates value to multiply bandwidth to obtain `skirtwidth`
for a Fof filter.

#### Usage

```
skirtWidthMultiplier(vowel,freq,gender) : _
```

Where:

* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u)
* `freq`: the fundamental frequency of the excitation signal
* `gender`: gender of the voice used in the fof filter (0: male, 1: female)

----

### `(pm.)autobendFreq`

Autobends the center frequencies of formants 1 and 2 based on
the fundamental frequency of the excitation signal and leaves
all other formant frequencies unchanged. Ported from `chant-lib`.

#### Reference

* [https://ccrma.stanford.edu/~rmichon/chantLib/](https://ccrma.stanford.edu/~rmichon/chantLib/).

#### Usage

```
_ : autobendFreq(n,freq,voiceType) : _
```

Where:

* `n`: formant index
* `freq`: the fundamental frequency of the excitation signal
* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor, 3: soprano, 4: tenor)
* input is the center frequency of the corresponding formant

----

### `(pm.)vocalEffort`

Changes the gains of the formants based on the fundamental
frequency of the excitation signal. Higher formants are
reinforced for higher fundamental frequencies.
Ported from `chant-lib`.

#### Reference

* [https://ccrma.stanford.edu/~rmichon/chantLib/](https://ccrma.stanford.edu/~rmichon/chantLib/).

#### Usage

```
_ : vocalEffort(freq,gender) : _
```

Where:

* `freq`: the fundamental frequency of the excitation signal
* `gender`: the gender of the voice type (0: male, 1: female)
* input is the linear amplitude of the formant

----

### `(pm.)fof`

Function to generate a single Formant-Wave-Function.

#### Reference

* [https://ccrma.stanford.edu/~mjolsen/pdfs/smc2016_MOlsenFOF.pdf](https://ccrma.stanford.edu/~mjolsen/pdfs/smc2016_MOlsenFOF.pdf).

#### Usage

```
_ : fof(fc,bw,a,g) : _
```

Where:

* `fc`: formant center frequency,
* `bw`: formant bandwidth (Hz),
* `sw`: formant skirtwidth (Hz)
* `g`: linear scale factor (g=1 gives 0dB amplitude response at fc)
* input is an impulse signal to excite filter

----

### `(pm.)fofSH`

FOF with sample and hold used on `bw` and a parameter
used in the filter-cycling FOF function `fofCycle`.

#### Reference

* [https://ccrma.stanford.edu/~mjolsen/pdfs/smc2016_MOlsenFOF.pdf](https://ccrma.stanford.edu/~mjolsen/pdfs/smc2016_MOlsenFOF.pdf).

#### Usage

```
_ : fofSH(fc,bw,a,g) : _
```

Where: all parameters same as for [`fof`](#fof)

----

### `(pm.)fofCycle`

FOF implementation where time-varying filter parameter noise is
mitigated by using a cycle of `n` sample and hold FOF filters.

#### Reference

* [https://ccrma.stanford.edu/~mjolsen/pdfs/smc2016_MOlsenFOF.pdf](https://ccrma.stanford.edu/~mjolsen/pdfs/smc2016_MOlsenFOF.pdf).

#### Usage

```
_ : fofCycle(fc,bw,a,g,n) : _
```

Where:

* `n`: the number of FOF filters to cycle through
* all other parameters are same as for [`fof`](#fof)

----

### `(pm.)fofSmooth`

FOF implementation where time-varying filter parameter
noise is mitigated by lowpass filtering the filter
parameters `bw` and `a` with [smooth](#smooth).

#### Usage

```
_ : fofSmooth(fc,bw,sw,g,tau) : _
```

Where:

* `tau`: the desired smoothing time constant in seconds
* all other parameters are same as for [`fof`](#fof)

----

### `(pm.)formantFilterFofCycle`

Formant filter based on a single FOF filter.
Formant parameters are linearly interpolated allowing to go smoothly from
one vowel to another. A cycle of `n` fof filters with sample-and-hold is
used so that the fof filter parameters can be varied in realtime.
This technique is more robust but more computationally expensive than
[`formantFilterFofSmooth`](#formantFilterFofSmooth).Voice type can be
selected but must correspond to
the frequency range of the provided source to be realistic.

#### Usage

```
_ : formantFilterFofCycle(voiceType,vowel,nFormants,i,freq) : _
```

Where:

* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor,
		  3: soprano, 4: tenor)
* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u)
* `nFormants`: number of formant regions in frequency domain, typically 5
* `i`: formant number (i.e. 0 - 4) used to index formant data value arrays
* `freq`: fundamental frequency of excitation signal. Used to calculate
        rise time of envelope

----

### `(pm.)formantFilterFofSmooth`

Formant filter based on a single FOF filter.
Formant parameters are linearly interpolated allowing to go smoothly from
one vowel to another. Fof filter parameters are lowpass filtered
to mitigate possible noise from varying them in realtime.
Voice type can be selected but must correspond to
the frequency range of the provided source to be realistic.

#### Usage

```
_ : formantFilterFofSmooth(voiceType,vowel,nFormants,i,freq) : _
```

Where:

* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor,
		  3: soprano, 4: tenor)
* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u)
* `nFormants`: number of formant regions in frequency domain, typically 5
* `i`: formant number (i.e. 1 - 5) used to index formant data value arrays
* `freq`: fundamental frequency of excitation signal. Used to calculate
        rise time of envelope

----

### `(pm.)formantFilterBP`

Formant filter based on a single resonant bandpass filter.
Formant parameters are linearly interpolated allowing to go smoothly from
one vowel to another. Voice type can be selected but must correspond to
the frequency range of the provided source to be realistic.

#### Usage

```
_ : formantFilterBP(voiceType,vowel,nFormants,i,freq) : _
```

Where:

* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor, 3: soprano, 4: tenor)
* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u)
* `nFormants`: number of formant regions in frequency domain, typically 5
* `i`: formant index used to index formant data value arrays
* `freq`: fundamental frequency of excitation signal.

----

### `(pm.)formantFilterbank`

Formant filterbank which can use different types of filterbank
functions and different excitation signals. Formant parameters are
linearly interpolated allowing to go smoothly from one vowel to another.
Voice type can be selected but must correspond to the frequency range
of the provided source to be realistic.

#### Usage

```
_ : formantFilterbank(voiceType,vowel,formantGen,freq) : _
```

Where:

* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor, 3: soprano, 4: tenor)
* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u)
* `formantGen`: the specific formant filterbank function
 (i.e. FormantFilterbankBP, FormantFilterbankFof,...)
* `freq`: fundamental frequency of excitation signal. Needed for FOF
 version to calculate rise time of envelope

----

### `(pm.)formantFilterbankFofCycle`

Formant filterbank based on a bank of fof filters.
Formant parameters are linearly interpolated allowing to go smoothly from
one vowel to another. Voice type can be selected but must correspond to
the frequency range of the provided source to be realistic.

#### Usage

```
_ : formantFilterbankFofCycle(voiceType,vowel,freq) : _
```

Where:

* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor, 3: soprano, 4: tenor)
* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u)
* `freq`: the fundamental frequency of the excitation signal. Needed to calculate the skirtwidth 
of the FOF envelopes and for the autobendFreq and vocalEffort functions

----

### `(pm.)formantFilterbankFofSmooth`

Formant filterbank based on a bank of fof filters.
Formant parameters are linearly interpolated allowing to go smoothly from
one vowel to another. Voice type can be selected but must correspond to
the frequency range of the provided source to be realistic.

#### Usage

```
_ : formantFilterbankFofSmooth(voiceType,vowel,freq) : _
```

Where:

* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor, 3: soprano, 4: tenor)
* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u)
* `freq`: the fundamental frequency of the excitation signal. Needed to
calculate the skirtwidth of the FOF envelopes and for the
autobendFreq and vocalEffort functions

----

### `(pm.)formantFilterbankBP`

Formant filterbank based on a bank of resonant bandpass filters.
Formant parameters are linearly interpolated allowing to go smoothly from
one vowel to another. Voice type can be selected but must correspond to
the frequency range of the provided source to be realistic.

#### Usage

```
_ : formantFilterbankBP(voiceType,vowel,freq) : _
```

Where:

* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor, 3: soprano, 4: tenor)
* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u)
* `freq`: the fundamental frequency of the excitation signal. Needed for the autobendFreq and vocalEffort functions

----

### `(pm.)SFFormantModel`

Simple formant/vocal synthesizer based on a source/filter model. The `source`
and `filterbank` must be specified by the user. `filterbank` must take the same
input parameters as [`formantFilterbank`](#formantFilterbank) (`BP`/`FofCycle`
/`FofSmooth`).
Formant parameters are linearly interpolated allowing to go smoothly from
one vowel to another. Voice type can be selected but must correspond to
the frequency range of the synthesized voice to be realistic.

#### Usage

```
SFFormantModel(voiceType,vowel,exType,freq,gain,source,filterbank,isFof) : _
```

Where:

* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor, 3: soprano, 4: tenor)
* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u
* `exType`: voice vs. fricative sound ratio (0-1 where 1 is 100% fricative)
* `freq`: the fundamental frequency of the source signal
* `gain`: linear gain multiplier to multiply the source by
* `isFof`: whether model is FOF based (0: no, 1: yes)

----

### `(pm.)SFFormantModelFofCycle`

Simple formant/vocal synthesizer based on a source/filter model. The source
is just a periodic impulse and the "filter" is a bank of FOF filters.
Formant parameters are linearly interpolated allowing to go smoothly from
one vowel to another. Voice type can be selected but must correspond to
the frequency range of the synthesized voice to be realistic. This model
does not work with noise in the source signal so exType has been removed
and model does not depend on SFFormantModel function.

#### Usage

```
SFFormantModelFofCycle(voiceType,vowel,freq,gain) : _
```

Where:

* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor, 3: soprano, 4: tenor)
* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u
* `freq`: the fundamental frequency of the source signal
* `gain`: linear gain multiplier to multiply the source by

----

### `(pm.)SFFormantModelFofSmooth`

Simple formant/vocal synthesizer based on a source/filter model. The source
is just a periodic impulse and the "filter" is a bank of FOF filters.
Formant parameters are linearly interpolated allowing to go smoothly from
one vowel to another. Voice type can be selected but must correspond to
the frequency range of the synthesized voice to be realistic.

#### Usage

```
SFFormantModelFofSmooth(voiceType,vowel,freq,gain) : _
```

Where:

* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor, 3: soprano, 4: tenor)
* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u
* `freq`: the fundamental frequency of the source signal
* `gain`: linear gain multiplier to multiply the source by

----

### `(pm.)SFFormantModelBP`

Simple formant/vocal synthesizer based on a source/filter model. The source
is just a sawtooth wave and the "filter" is a bank of resonant bandpass filters.
Formant parameters are linearly interpolated allowing to go smoothly from
one vowel to another. Voice type can be selected but must correspond to
the frequency range of the synthesized voice to be realistic.

The formant data used here come from the CSOUND manual
* [http://www.csounds.com/manual/html/](http://www.csounds.com/manual/html/).

#### Usage

```
SFFormantModelBP(voiceType,vowel,exType,freq,gain) : _
```

Where:

* `voiceType`: the voice type (0: alto, 1: bass, 2: countertenor, 3: soprano, 4: tenor)
* `vowel`: the vowel (0: a, 1: e, 2: i, 3: o, 4: u
* `exType`: voice vs. fricative sound ratio (0-1 where 1 is 100% fricative)
* `freq`: the fundamental frequency of the source signal
* `gain`: linear gain multiplier to multiply the source by

----

### `(pm.)SFFormantModelFofCycle_ui`

Ready-to-use source-filter vocal synthesizer with built-in user interface.

#### Usage

```
SFFormantModelFofCycle_ui : _
```

----

### `(pm.)SFFormantModelFofSmooth_ui`

Ready-to-use source-filter vocal synthesizer with built-in user interface.

#### Usage

```
SFFormantModelFofSmooth_ui : _
```

----

### `(pm.)SFFormantModelBP_ui`

Ready-to-use source-filter vocal synthesizer with built-in user interface.

#### Usage

```
SFFormantModelBP_ui : _
```

----

### `(pm.)SFFormantModelFofCycle_ui_MIDI`

Ready-to-use MIDI-controllable source-filter vocal synthesizer.

#### Usage

```
SFFormantModelFofCycle_ui_MIDI : _
```

----

### `(pm.)SFFormantModelFofSmooth_ui_MIDI`

Ready-to-use MIDI-controllable source-filter vocal synthesizer.

#### Usage

```
SFFormantModelFofSmooth_ui_MIDI : _
```

----

### `(pm.)SFFormantModelBP_ui_MIDI`

Ready-to-use MIDI-controllable source-filter vocal synthesizer.

#### Usage

```
SFFormantModelBP_ui_MIDI : _
```

##  Misc Functions 

Various miscellaneous functions.

----

### `(pm.)allpassNL`

Bidirectional block adding nonlinearities in both directions in a chain.
Nonlinearities are created by modulating the coefficients of a passive
allpass filter by the signal it is processing.

#### Usage

```
chain(... : allpassNL(nonlinearity) : ...)
```

Where:

* `nonlinearity`: amount of nonlinearity to be added (0-1)

----

### `(pm).modalModel`


Implement multiple resonance modes using resonant bandpass filters.

#### Usage

```
_ : modalModel(n, freqs, t60s, gains) : _
```

Where:

* `n`: number of given modes
* `freqs` : list of filter center freqencies
* `t60s` : list of mode resonance durations (in seconds)
* `gains` : list of mode gains (0-1)

For example, to generate a model with 2 modes (440 Hz and 660 Hz, a
fifth) where the higher one decays faster and is attenuated:

```
os.impulse : modalModel(2, (440, 660),
                           (0.5, 0.25),
                           (ba.db2linear(-1), ba.db2linear(-6)) : _
```

Further reading: [Grumiaux et. al., 2017:
Impulse-Response and CAD-Model-Based Physical Modeling in
Faust](https://raw.githubusercontent.com/grame-cncm/faust/master-dev/tools/physicalModeling/ir2dsp/lacPaper2017.pdf)

