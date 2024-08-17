#  wdmodels.lib 

A library of basic adaptors and methods to help construct Wave Digital Filter models in Faust. Its official prefix is `wd`.
## Library Readme
This library is intended for use for creating Wave Digital (WD) based models of audio circuitry for real-time audio processing within the Faust programming language. The goal is to provide a framework to create real-time virtual-analog audio effects and synthesizers using WD models without the use of C++. Furthermore, we seek to provide access to the technique of WD modeling to those without extensive knowledge of advanced digital signal processing techniques. Finally, we hope to provide a library which can integrate with all aspects of Faust, thus creating a platform for virtual circuit bending. 
The library itself is written in Faust to maintain portability. 

This library is heavily based on Kurt Werner's Dissertation, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters." I have tried to maintain consistent notation between the adaptors appearing within thesis and my adaptor code. The majority of the adaptors found in chapter 1 and chapter 3 are currently supported. 

For inquires about use of this library in a commercial product, please contact dirk [dot] roosenburg [dot] 30 [at] gmail [dot] com.
This documentation is taken directly from the [readme](https://github.com/droosenb/faust-wdf-library). Please refer to it for a more updated version. 

Many of the more in depth comments within the library include jargon. I plan to create videos detailing the theory of WD models.
For now I recommend Kurt Werner's PhD, [Virtual analog modeling of Audio circuitry using Wave Digital Filters](https://searchworks.stanford.edu/view/11891203).   
I have tried to maintain consistent syntax and notation to the thesis. 
This library currently includes the majority of the adaptors covered in chapter 1 and some from chapter 3. 


## Using this Library

Use of this library expects some level of familiarity with WDF techniques, especially simplification and decomposition of electronic circuits into WDF connection trees. I plan to create video to cover both these techniques and use of the library. 

### Quick Start

To get a quick overview of the library, start with the `secondOrderFilters.dsp` code found in [examples](https://github.com/droosenb/faust-wdf-library/tree/main/examples). 
Note that the `wdmodels.lib` library is now embedded in the [online Faust IDE](https://faustide.grame.fr/).

### A Simple RC Filter Model

Creating a model using this library consists fo three steps. First, declare a set of components. 
Second, model the relationship between them using a tree. Finally, build the tree using the libraries build functions.  

First, a set of components is declared using adaptors from the library. 
This list of components is created based on analysis of the circuit using WDF techniques, 
though generally each circuit element (resistor, capacitor, diode, etc.) can be expected to appear 
within the component set. For example, first order RC lowpass filter would require an unadapted voltage source, 
a 47k resistor, and a 10nF capacitor which outputs the voltage across itself. These can be declared with: 

```
vs1(i) = wd.u_voltage(i, no.noise);
r1(i) = wd.resistor(i, 47*10^3);
c1(i) = wd.capacitor_Vout(i, 10*10^-9);
```

Note that the first argument, i, is left un-parametrized. Components must be declared in this form, as the build algorithm expects to receive adaptors which have exactly one parameter. 

Also note that we have chosen to declare a white noise function as the input to our voltage source. 
We could potentially declare this as a direct input to our model, but to do so is more complicated 
process which cannot be covered within this tutorial. For information on how to do this see 
[Declaring Model Parameters as Inputs](#declaring-model-parameters-as-inputs) or see various implementations 
in [examples](https://github.com/droosenb/faust-wdf-library/tree/main/examples).

Second, the declared components and interconnection/structural adaptors (i.e. series, parallel, etc) are arranged 
into the connection tree which is produced from performing WD analysis on the modeled circuit. 
For example, to produce our first order RC lowpass circuit model, the following tree is declared: 

`tree_lowpass = vs1 : wd.series : (r1, c1);`

For more information on how to represent trees in Faust, see [Trees in Faust](#trees-in-faust). 

Finally, the tree is built using the the `buildtree` function. To build and compute our first order 
RC lowpass circuit model, we use:

`process = wd.buildtree(tree_lowpass);`

More information about build functions, see [Model Building Functions](#model-building-functions). 

### Building a Model

After creating a connection tree which consists of WD adaptors, the connection tree must be passed 
to a build function in order to build the model.

##### Automatic model building 

`buildtree(connection_tree)`

The simplest build function for use with basic models. This automatically implements `buildup`, `builddown`, 
and `buildout` to create a working model. However, it gives minimum control to the user and cannot 
currently be used on trees which have parameters declared as inputs.

##### Manual model building

Wave Digital Filters are an explicit state-space model, meaning they use a previous system state 
in order to calculate the current output. This is achieved in Faust by using a single global feedback operator.
The models feed-forward terms are generated using `builddown` and the models feedback terms are generated 
using `buildup`. Thus, the most common model implementation (the method used by `buildtree`) is:

`builddown(connection_tree)~buildup(connection_tree) : buildout(connection_tree)`

Since the `~` operator in Faust will leave feedback terms hanging as outputs, `buildout` is a function provided for convenience. 
It automatically truncates the hanging outputs by identifying leaf components which have an intended output 
and generating an output matrix.

Building the model manually allows for greater user control and is often very helpful in testing. 
Also provided for testing are the `getres` and `parres` functions, which can be used to determine 
the upward-facing port resistance of an element. 

### Declaring Model Parameters as Inputs

When possible, parameters of components should be declared explicitly, meaning they are dependent on a function with no inputs. 
This might be something as simple as integer(declaring a static component), a function dependent on a UI input (declaring a component with variable value), 
or even a time-dependent function like an oscillator (declaring an audio input or circuit bending). 

However, it is often necessary to declare parameters as input. To achieve this there are two possible methods. 
The first and recommended option is to create a separate model function and declare parameters which will later 
be implemented as inputs. This allows inputs to be explicitly declared as component parameters. 
For example, one might use:

```
model(in1) = buildtree(tree)
with {
   ...
   vin(i) = wd.u_voltage(i, in1);
   ...
   tree = vin : ...; 
};
```

In order to simulate an audio input to the circuit. 

Note that the tree and components must be declared inside a `with {...}` statement, or the model's parameters will not be accessible. 

##### The Empty Signal Operator

The Empty signal operator, `_` should NEVER be used to declare a parameter as in input in a wave-digital model. 

Using it will result on breaking the internal routing of the model and thus breaks the model. 
Instead, use explicit declaration as shown directly above. 

### Trees in Faust

Since WD models use connection trees to represent relationships of elements, a comprehensive way to represent trees is critical.
 As there is no current convention for creating trees in Faust, I've developed a method using the existing series and parallel/list 
methods in Faust.

The series operator ` : ` is used to separate parent and child elements. For example the tree:

```
   A
   |
   B
```

is represented by `A : B` in Faust. 

To denote a parent element with multiple child elements, simply use a list `(a1, a2, ... an)` of children connected to a single parent. `
For example the tree:

```
   A
  / \
 B   C

```
is represented by:

`A : (B, C)`

Finally, for a tree with many levels, simply break the tree into subtrees following the above rules and connect 
the subtree as if it was an individual node. For example the tree:

```
      A
     / \
    B   C
   /   / \
  X   Y   Z
```

can be represented by:

```
B_sub = B : X; //B subtree
C_sub = C : (Y, Z); //C subtree
tree = A : (B_sub, C_sub); //full tree
```

or more simply, using parentheses: 

`A : ((B : X), (C : (Y, Z)))`
### How Adaptors are Structured
In wave digital filters, adaptors can be described by the form `b = Sa` where `b` is a vector of output waves `b = (b0, b1, b2, ... bn)`, `a` is a vector of input waves`a = (a0, a1, a2, ... an)`, and `S` is an n x n scattering matrix. 
`S` is dependent on `R`, a list of port resistances `(R0, R1, R2, ... Rn)`. 

The output wave vector `b` can be divided into downward-going and upward-going waves 
(downward-going waves travel down the connection tree, upward-going waves travel up). 
For adapted adaptors, with the zeroth port being the upward-facing port, the downward-going wave vector is `(b1, b2, ... bn)` and the upward-going wave vector is `(b0)`. 
For unadapted adaptors, there are no upward-going waves, so the downward-going wave vector is simply `b = (b0, b1, b2, ... bn)`. 

In order for adaptors to be interpretable by the compiler, they must be structured in a specific way. 
Each adaptor is divided into three cases by their first parameter. This parameter, while accessible by the user, should only be set by the compiler/builder.

All other parameters are value declarations (for components), inputs (for voltage or current ins), or parameter controls (for potentiometers/variable capacitors/variable inductors).

##### First case - downward going waves

`(0, params) => downward-going(R1, ... Rn, a0, a1, ... an)` 
outputs: `(b1, b2, ... bn)`
this function takes any number of port resistances, the downward going wave, and any number of upward going waves as inputs. 
These values/waves are used to calculate the downward going waves coming from this adaptor.

##### Second case 

`(1, params) => upward-going(R1, ... Rn, a1, ... an)`
outputs : `(b0)`
this function takes any number of port resistances and any number of upward going waves as inputs.
These values/waves are used to calculate the upward going wave coming from this adaptor.

##### Third case  

`(2, params) => port-resistance(R1, ... Rn)` 
outputs: `(R0)`
this function takes any number of port resistances as inputs.
These values are used to calculate the upward going port resistance of the element.

##### Unadapted Adaptors

Unadapted adaptor's names will always begin `u_`
An unadapted adaptor MUST be used as the root of the WD connection tree.
Unadapted adaptors can ONLY be used as a root of the WD connection tree. 
While unadapted adaptors contain all three cases, the second and third are purely structural. 
Only the first case should contain computational information. 

### How the Build Functions Work

Expect this section to be added soon! It's currently in progress.

### Acknowledgements

Many thanks to Kurt Werner for helping me to understand wave digital filter models. Without his publications and consultations, the library would not exist. 
Thanks also to my advisors, Rob Owen and Eli Stine whose input was critical to the development of the library.
Finally, thanks to Romain Michon, Stephane Letz, and the Faust Slack for contributing to testing, development, and inspiration when creating the library. 

#### References
* [https://github.com/grame-cncm/faustlibraries/blob/master/wdmodels.lib](https://github.com/grame-cncm/faustlibraries/blob/master/wdmodels.lib)

## Algebraic One Port Adaptors


----

### `(wd.)resistor`

Adapted Resistor.

A basic node implementing a resistor for use within Wave Digital Filter connection trees.

It should be used as a leaf/terminating element of the connection tree.

#### Usage

```
r1(i) = resistor(i, R);
buildtree( A : r1 );
```

Where:

* `i`: index used by model-building functions. Should never be user declared.
* `R` : Resistance/Impedance of the resistor being modeled in Ohms. 

Note: the adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.2.1

----

### `(wd.)resistor_Vout`

Adapted Resistor + voltage Out.

A basic adaptor implementing a resistor for use within Wave Digital Filter connection trees.

It should be used as a leaf/terminating element of the connection tree.
The resistor will also pass the voltage across itself as an output of the model.

#### Usage

```
rout(i) = resistor_Vout(i, R);
buildtree( A : rout ) : _
```

Where:

* `i`: index used by model-building functions. Should never be user declared.
* `R` : Resistance/Impedance of the resistor being modeled in Ohms. 

Note: the adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.2.1

----

### `(wd.)resistor_Iout`

Resistor + current Out.

A basic adaptor implementing a resistor for use within Wave Digital Filter connection trees.

It should be used as a leaf/terminating element of the connection tree.
The resistor will also pass the current through itself as an output of the model.

#### Usage

```
rout(i) = resistor_Iout(i, R);
buildtree( A : rout ) : _
```

Where:

* `i`: index used by model-building functions. Should never be user declared.
* `R` : Resistance/Impedance of the resistor being modeled in Ohms. 

Note: the adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.2.1

----

### `(wd.)u_voltage`

Unadapted Ideal Voltage Source.

An adaptor implementing an ideal voltage source within Wave Digital Filter connection trees.

It should be used as the root/top element of the connection tree.
Can be used for either DC (constant) or AC (signal) voltage sources.

#### Usage

```
v1(i) = u_Voltage(i, ein);
buildtree( v1 : B );
```

Where:

* `i`: index used by model-building functions. Should never be user declared.
* `ein` : Voltage/Potential across ideal voltage source in Volts

Note: only usable as the root of a tree.
The adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.2.2

----

### `(wd.)u_current`

Unadapted Ideal Current Source.

An unadapted adaptor implementing an ideal current source within Wave Digital Filter connection trees.

It should be used as the root/top element of the connection tree.
Can be used for either DC (constant) or AC (signal) current sources.

#### Usage

```
i1(i) = u_current(i, jin);
buildtree( i1 : B );
```

Where:

* `i`: index used by model-building functions. Should never be user declared.
* `jin` : Current through the ideal current source in Amps

Note: only usable as the root of a tree.
The adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.2.3

----

### `(wd.)resVoltage`

Adapted Resistive Voltage Source.

An adaptor implementing a resistive voltage source within Wave Digital Filter connection trees.

It should be used as a leaf/terminating element of the connection tree.
It is comprised of an ideal voltage source in series with a resistor.
Can be used for either DC (constant) or AC (signal) voltage sources.

#### Usage

```
v1(i) = resVoltage(i, R, ein);
buildtree( A : v1 );
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `R` : Resistance/Impedance of the series resistor in Ohms
* `ein` : Voltage/Potential of the ideal voltage source in Volts

Note: the adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.2.4

----

### `(wd.)resVoltage_Vout`

Adapted Resistive Voltage Source + voltage output.

An adaptor implementing an adapted resistive voltage source within Wave Digital Filter connection trees.

It should be used as a leaf/terminating element of the connection tree.
It is comprised of an ideal voltage source in series with a resistor.
Can be used for either DC (constant) or AC (signal) voltage sources.
The resistive voltage source will also pass the voltage across it as an output of the model.

#### Usage

```
vout(i) = resVoltage_Vout(i, R, ein);
buildtree( A : vout ) : _
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `R` : Resistance/Impedance of the series resistor in Ohms
* `ein` : Voltage/Potential across ideal voltage source in Volts

Note: the adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.2.4

----

### `(wd.)u_resVoltage`

Unadapted Resistive Voltage Source.

An unadapted adaptor implementing a resistive voltage source within Wave Digital Filter connection trees.

It should be used as the root/top element of the connection tree.
It is comprised of an ideal voltage source in series with a resistor.
Can be used for either DC (constant) or AC (signal) voltage sources.

#### Usage

```
v1(i) = u_resVoltage(i, R, ein);
buildtree( v1 : B );
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `R` : Resistance/Impedance of the series resistor in Ohms
* `ein` : Voltage/Potential across ideal voltage source in Volts

Note: only usable as the root of a tree.
The adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.2.4

----

### `(wd.)resCurrent`

Adapted Resistive Current Source.

An adaptor implementing a resistive current source within Wave Digital Filter connection trees.

It should be used as a leaf/terminating element of the connection tree.
It is comprised of an ideal current source in parallel with a resistor.
Can be used for either DC (constant) or AC (signal) current sources.

#### Usage

```
i1(i) = resCurrent(i, R, jin);
buildtree( A : i1 );
```

Where:

* `i`: index used by model-building functions. Should never be user declared.
* `R` : Resistance/Impedance of the parallel resistor in Ohms
* `jin` : Current through the ideal current source in Amps

Note: the adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.2.5

----

### `(wd.)u_resCurrent`

Unadapted Resistive Current Source.

An unadapted adaptor implementing a resistive current source within Wave Digital Filter connection trees.

It should be used as the root/top element of the connection tree.
It is comprised of an ideal current source in parallel with a resistor.
Can be used for either DC (constant) or AC (signal) current sources.

#### Usage

```
i1(i) = u_resCurrent(i, R, jin);
buildtree( i1 : B );
```

Where:

* `i`: index used by model-building functions. Should never be user declared.
* `R` : Resistance/Impedance of the series resistor in Ohms
* `jin` : Current through the ideal current source in Amps

Note: only usable as the root of a tree.
The adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.2.5

----

### `(wd.)u_switch`

Unadapted Ideal Switch.

An unadapted adaptor implementing an ideal switch for Wave Digital Filter connection trees.

It should be used as the root/top element of the connection tree

#### Usage

```
s1(i) = u_resCurrent(i, lambda);
buildtree( s1 : B );
```

Where:

* `i`: index used by model-building functions. Should never be user declared.
* `lambda` : switch state control. -1 for closed switch, 1 for open switch.

Note: only usable as the root of a tree.
The adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.2.8

## Reactive One Port Adaptors


----

### `(wd.)capacitor`

Adapted Capacitor.

A basic adaptor implementing a capacitor for use within Wave Digital Filter connection trees.

It should be used as a leaf/terminating element of the connection tree.
This capacitor model was digitized using the bi-linear transform.

#### Usage

```
c1(i) = capacitor(i, R);
buildtree( A : c1 ) : _
```

Where:

* `i`: index used by model-building functions. Should never be user declared.
* `R` : Capacitance/Impedance of the capacitor being modeled in Farads. 

Note: the adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.3.1

----

### `(wd.)capacitor_Vout`

Adapted Capacitor + voltage out.

A basic adaptor implementing a capacitor for use within Wave Digital Filter connection trees.

It should be used as a leaf/terminating element of the connection tree.
The capacitor will also pass the voltage across itself as an output of the model.
This capacitor model was digitized using the bi-linear transform.

#### Usage

```
cout(i) = capacitor_Vout(i, R);
buildtree( A : cout ) : _
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `R` : Capacitance/Impedence of the capacitor being modeled in Farads

Note: the adaptor must be declared as a seperate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.3.1

----

### `(wd.)inductor`

Unadapted Inductor.

A basic adaptor implementing an inductor for use within Wave Digital Filter connection trees.

It should be used as a leaf/terminating element of the connection tree.
This inductor model was digitized using the bi-linear transform.

#### Usage

```
l1(i) = inductor(i, R);
buildtree( A : l1 );
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `R` : Inductance/Impedance of the inductor being modeled in Henries

Note: the adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.3.2

----

### `(wd.)inductor_Vout`

Unadapted Inductor + Voltage out.

A basic adaptor implementing an inductor for use within Wave Digital Filter connection trees.

It should be used as a leaf/terminating element of the connection tree.
The inductor will also pass the voltage across itself as an output of the model.
This inductor model was digitized using the bi-linear transform.

#### Usage

```
lout(i) = inductor_Vout(i, R);
buildtree( A : lout ) : _
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `R` : Inductance/Impedance of the inductor being modeled in Henries

Note: the adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.3.2

## Nonlinear One Port Adaptors


----

### `(wd.)u_idealDiode`

Unadapted Ideal Diode.

An unadapted adaptor implementing an ideal diode for Wave Digital Filter connection trees.

It should be used as the root/top element of the connection tree.

#### Usage

```
buildtree( u_idealDiode : B );
```

Note: only usable as the root of a tree.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 3.2.3

----

### `(wd.)u_chua`

Unadapted Chua Diode.

An adaptor implementing the chua diode / non-linear resistor within Wave Digital Filter connection trees.

It should be used as the root/top element of the connection tree.

#### Usage

```
chua1(i) = u_chua(i, G1, G2, V0);
buildtree( chua1 : B );
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `G1` : resistance parameter 1 of the chua diode
* `G2` : resistance parameter 2 of the chua diode
* `V0` : voltage parameter of the chua diode

Note: only usable as the root of a tree.
The adaptor must be declared as a separate function before integration into the connection tree.
Correct implementation is shown above.

#### Reference

Meerkotter and Scholz, "Digital Simulation of Nonlinear Circuits by Wave Digital Filter Principles"

----

### `(wd.)lambert`

An implementation of the lambert function.
It uses Halley's method of iteration to approximate the output.
Included in the WD library for use in non-linear diode models.
Adapted from K M Brigg's c++ lambert function approximation.

#### Usage

```
lambert(n, itr) : _
```

Where:
* `n`: value at which the lambert function will be evaluated
* `itr`: number of iterations before output


----

### `(wd.)u_diodePair`

Unadapted pair of diodes facing in opposite directions.

An unadapted adaptor implementing two antiparallel diodes for Wave Digital Filter connection trees.
The behavior is approximated using Schottkey's ideal diode law.

#### Usage

```
d1(i) = u_diodePair(i, Is, Vt);
buildtree( d1 : B );
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `Is` : saturation current of the diodes
* `Vt` : thermal resistances of the diodes

Note: only usable as the root of a tree.
Correct implementation is shown above.

#### Reference

K. Werner et al. "An Improved and Generalized Diode Clipper Model for Wave Digital Filters"

----

### `(wd.)u_diodeSingle`

Unadapted single diode.

An unadapted adaptor implementing a single diode for Wave Digital Filter connection trees.
The behavior is approximated using Schottkey's ideal diode law.

#### Usage

```
d1(i) = u_diodeSingle(i, Is, Vt);
buildtree( d1 : B );
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `Is` : saturation current of the diodes
* `Vt` : thermal resistances of the diodes

Note: only usable as the root of a tree.
Correct implementation is shown above.

#### Reference

K. Werner et al. "An Improved and Generalized Diode Clipper Model for Wave Digital Filters"

----

### `(wd.)u_diodeAntiparallel`

Unadapted set of antiparallel diodes with M diodes facing forwards and N diodes facing backwards.

An unadapted adaptor implementing antiparallel diodes for Wave Digital Filter connection trees.
The behavior is approximated using Schottkey's ideal diode law.

#### Usage

```
d1(i) = u_diodeAntiparallel(i, Is, Vt);
buildtree( d1 : B );
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `Is` : saturation current of the diodes
* `Vt` : thermal resistances of the diodes

Note: only usable as the root of a tree.
Correct implementation is shown above.

#### Reference

K. Werner et al. "An Improved and Generalized Diode Clipper Model for Wave Digital Filters"

## Two Port Adaptors


----

### `(wd.)u_parallel2Port`

Unadapted 2-port parallel connection.

An unadapted adaptor implementing a 2-port parallel connection between adaptors for Wave Digital Filter connection trees.
Elements connected to this adaptor will behave as if connected in parallel in circuit.

#### Usage

```
buildtree( u_parallel2Port : (A, B) );
```

Note: only usable as the root of a tree.
This adaptor has no user-accessible parameters. 
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.4.1

----

### `(wd.)parallel2Port`

Adapted 2-port parallel connection.

An adaptor implementing a 2-port parallel connection between adaptors for Wave Digital Filter connection trees.
Elements connected to this adaptor will behave as if connected in parallel in circuit.

#### Usage

```
buildtree( A : parallel2Port : B );
```

Note: this adaptor has no user-accessible parameters. 
It should be used within the connection tree with one previous and one forward adaptor.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.4.1

----

### `(wd.)u_series2Port`

Unadapted 2-port series connection.

An unadapted adaptor implementing a 2-port series connection between adaptors for Wave Digital Filter connection trees.
Elements connected to this adaptor will behave as if connected in series in circuit.

#### Usage

```
buildtree( u_series2Port : (A, B) );
```

Note: only usable as the root of a tree.
This adaptor has no user-accessible parameters. 
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.4.1

----

### `(wd.)series2Port`

Adapted 2-port series connection.

An adaptor implementing a 2-port series connection between adaptors for Wave Digital Filter connection trees.
Elements connected to this adaptor will behave as if connected in series in circuit.

#### Usage

```
buildtree( A : series2Port : B );
```

Note: this adaptor has no user-accessible parameters. 
It should be used within the connection tree with one previous and one forward adaptor.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.4.1

----

### `(wd.)parallelCurrent`

Adapted 2-port parallel connection + ideal current source.

An adaptor implementing a 2-port series connection and internal idealized current source between adaptors for Wave Digital Filter connection trees.
This adaptor connects the two connected elements and an additional ideal current source in parallel.

#### Usage

```
i1(i) = parallelCurrent(i, jin);
buildtree(A : i1 : B);
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `jin` :  Current through the ideal current source in Amps

Note: the adaptor must be declared as a separate function before integration into the connection tree.
It should be used within a connection tree with one previous and one forward adaptor.
Correct implementation is shown above.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.4.2

----

### `(wd.)seriesVoltage`

Adapted 2-port series connection + ideal voltage source.

An adaptor implementing a 2-port series connection and internal ideal voltage source between adaptors for Wave Digital Filter connection trees.
This adaptor connects the two connected adaptors and an additional ideal voltage source in series.

#### Usage

```
v1(i) = seriesVoltage(i, vin)
buildtree( A : v1 : B );
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `vin` :  voltage across the ideal current source in Volts

Note: the adaptor must be declared as a separate function before integration into the connection tree.
It should be used within the connection tree with one previous and one forward adaptor.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.4.2

----

### `(wd.)u_transformer`

Unadapted ideal transformer.

An adaptor implementing an ideal transformer for Wave Digital Filter connection trees.
The first downward-facing port corresponds to the primary winding connections, and the second downward-facing port to the secondary winding connections.

#### Usage

```
t1(i) = u_transformer(i, tr);
buildtree(t1 : (A , B));
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `tr` :  the turn ratio between the windings on the primary and secondary coils

Note: the adaptor must be declared as a separate function before integration into the connection tree.
It may only be used as the root of the connection tree with two forward nodes.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.4.3

----

### `(wd.)transformer`

Adapted ideal transformer.

An adaptor implementing an ideal transformer for Wave Digital Filter connection trees.
The upward-facing port corresponds to the primary winding connections, and the downward-facing port to the secondary winding connections

#### Usage

```
t1(i) = transformer(i, tr);
buildtree(A : t1 : B);
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `tr` :  the turn ratio between the windings on the primary and secondary coils

Note: the adaptor must be declared as a separate function before integration into the connection tree.
It should be used within the connection tree with one backward and one forward nodes.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.4.3

----

### `(wd.)u_transformerActive`

Unadapted ideal active transformer.

An adaptor implementing an ideal transformer for Wave Digital Filter connection trees.
The first downward-facing port corresponds to the primary winding connections, and the second downward-facing port to the secondary winding connections.

#### Usage

```
t1(i) = u_transformerActive(i, gamma1, gamma2);
buildtree(t1 : (A , B));
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `gamma1` :  the turn ratio describing the voltage relationship between the primary and secondary coils
* `gamma2` :  the turn ratio describing the current relationship between the primary and secondary coils

Note: the adaptor must be declared as a separate function before integration into the connection tree.
It may only be used as the root of the connection tree with two forward nodes.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.4.3

----

### `(wd.)transformerActive`

Adapted ideal active transformer.

An adaptor implementing an ideal active transformer for Wave Digital Filter connection trees.
The upward-facing port corresponds to the primary winding connections, and the downward-facing port to the secondary winding connections

#### Usage

```
t1(i) = transformerActive(i, gamma1, gamma2);
buildtree(A : t1 : B);
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `gamma1` :  the turn ratio describing the voltage relationship between the primary and secondary coils
* `gamma2` :  the turn ratio describing the current relationship between the primary and secondary coils

Note: the adaptor must be declared as a separate function before integration into the connection tree.
It should be used within the connection tree with two forward nodes.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.4.3

## Three Port Adaptors


----

### `(wd.)parallel`

Adapted 3-port parallel connection.

An adaptor implementing a 3-port parallel connection between adaptors for Wave Digital Filter connection trees.
This adaptor is used to connect adaptors simulating components connected in parallel in the circuit.

#### Usage

```
buildtree( A : parallel : (B, C) );
```

Note: this adaptor has no user-accessible parameters. 
It should be used within the connection tree with one previous and two forward adaptors.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.5.1

----

### `(wd.)series`

Adapted 3-port series connection.

An adaptor implementing a 3-port series connection between adaptors for Wave Digital Filter connection trees.
This adaptor is used to connect adaptors simulating components connected in series in the circuit.

#### Usage

```

tree = A : (series : (B, C));
```

Note: this adaptor has no user-accessible parameters. 
It should be used within the connection tree with one previous and two forward adaptors.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 1.5.2

## R-Type Adaptors


----

### `(wd.)u_sixportPassive`

Unadapted six-port rigid connection.

An adaptor implementing a six-port passive rigid connection between elements. 
It implements the simplest possible rigid connection found in the Fender Bassman Tonestack circuit.


#### Usage

```

tree = u_sixportPassive : (A, B, C, D, E, F));
```

Note: this adaptor has no user-accessible parameters. 
It should be used within the connection tree with six forward adaptors.

#### Reference

K. Werner, "Virtual Analog Modeling of Audio Circuitry Using Wave Digital Filters", 2.1.5

## Node Creating Functions


----

### `(wd.)genericNode`

Function for generating an adapted node from another faust function or scattering matrix.

This function generates a node which is suitable for use in the connection tree structure. 
`genericNode` separates the function that it is passed into upward-going and downward-going waves. 

#### Usage

```
n1(i) = genericNode(i, scatter, upRes);
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `scatter` : the function which describes the the node's scattering behavior
* `upRes` : the function which describes the node's upward-facing port-resistance

Note: `scatter` must be a function with n inputs, n outputs, and n-1 parameter inputs. 
 input/output 1 will be used as the adapted upward-facing port of the node, ports 2 to n will all be downward-facing. 
 The first input/output pair is assumed to already be adapted - i.e. the output 1 is not dependent on input 1. 
 The parameter inputs will receive the port resistances of the downward-facing ports.

`upRes` must be a function with n-1 parameter inputs and 1 output.
 The parameter inputs will receive the port resistances of the downward-facing ports.
 The output should give the upward-facing port resistance of the node based on the upward-facing port resistances of the input.

 If used on a leaf element (n=1), the model will automatically introduce a one-sample delay. 
 Thus, the output of the node at sample t based on the input, a[t], should be the output one sample ahead, b[t+1]. 
 This may require transformation of the output signal. 


----

### `(wd.)genericNode_Vout`

Function for generating a terminating/leaf node which gives the voltage across itself as a model output.

This function generates a node which is suitable for use in the connection tree structure. 
It also calculates the voltage across the element and gives it as a model output.

#### Usage

```
n1(i) = genericNode_Vout(i, scatter, upRes);
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `scatter` : the function which describes the the node's scattering behavior
* `upRes` : the function which describes the node's upward-facing port-resistance

Note: `scatter` must be a function with 1 input and 1 output. 
 It should give the output from the node based on the incident wave. 
 
 The model will automatically introduce a one-sample delay to the output of the function
 Thus, the output of the node at sample t based on the input, a[t], should be the output one sample ahead, b[t+1]. 
 This may require transformation of the output signal. 

`upRes` must be a function with no inputs and 1 output.
 The output should give the upward-facing port resistance of the node.


----

### `(wd.)genericNode_Iout`

Function for generating a terminating/leaf node which gives the current through itself as a model output.

This function generates a node which is suitable for use in the connection tree structure. 
It also calculates the current through the element and gives it as a model output.

#### Usage

```
n1(i) = genericNode_Iout(i, scatter, upRes);
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `scatter` : the function which describes the the node's scattering behavior
* `upRes` : the function which describes the node's upward-facing port-resistance

Note: `scatter` must be a function with 1 input and 1 output. 
 It should give the output from the node based on the incident wave. 
 
 The model will automatically introduce a one-sample delay to the output of the function.
 Thus, the output of the node at sample t based on the input, a[t], should be the output one sample ahead, b[t+1]. 
 This may require transformation of the output signal. 

`upRes` must be a function with no inputs and 1 output.
 The output should give the upward-facing port resistance of the node.


----

### `(wd.)u_genericNode`

Function for generating an unadapted node from another Faust function or scattering matrix.

This function generates a node which is suitable for use as the root of the connection tree structure. 

#### Usage

```
n1(i) = u_genericNode(i, scatter);
```

Where:

* `i`: index used by model-building functions. Should never be user declared
* `scatter` : the function which describes the the node's scattering behavior

Note: 
`scatter` must be a function with n inputs, n outputs, and n parameter inputs. 
 each input/output pair will be used as a downward-facing port of the node
 the parameter inputs will receive the port resistances of the downward-facing ports.


## Model Building Functions


----

### `(wd.)builddown`

Function for building the structure for calculating waves traveling down the WD connection tree.

It recursively steps through the given tree, parametrizes the adaptors, and builds an algorithm.
It is used in conjunction with the buildup() function to create a model.

#### Usage

```
builddown(A : B)~buildup(A : B);
```

Where: 
 `(A : B)` : is a connection tree composed of WD adaptors

----

### `(wd.)buildup`

Function for building the structure for calculating waves traveling up the WD connection tree.

It recursively steps through the given tree, parametrizes the adaptors, and builds an algorithm.
It is used in conjunction with the builddown() function to create a full structure.

#### Usage

```
builddown(A : B)~buildup(A : B);
```

Where: 
`(A : B)` : is a connection tree composed of WD adaptors

----

### `(wd.)getres`

Function for determining the upward-facing port resistance of a partial WD connection tree.

It recursively steps through the given tree, parametrizes the adaptors, and builds an algorithm.
It is used by the buildup and builddown functions but is also helpful in testing.

#### Usage

```
getres(A : B)~getres(A : B);
```

Where: 
`(A : B)` : is a partial connection tree composed of WD adaptors

Note:
This function cannot be used on a complete WD tree. When called on an unadapted adaptor (u_ prefix), it will create errors.

----

### `(wd.)parres`

Function for determining the upward-facing port resistance of a partial WD connection tree.

It recursively steps through the given tree, parametrizes the adaptors, and builds an algorithm.
It is used by the buildup and builddown functions but is also helpful in testing.
This function is a parallelized version of `getres`.

#### Usage

```
parres((A , B))~parres((A , B));
```

Where: 
`(A , B)` : is a partial connection tree composed of WD adaptors

Note: this function cannot be used on a complete WD tree. When called on an unadapted adaptor (u_ prefix), it will create errors.

----

### `(wd.)buildout`

Function for creating the output matrix for a WD model from a WD connection tree.

It recursively steps through the given tree and creates an output matrix passing only outputs.

#### Usage

```
buildout( A : B );
```

Where: 
`(A : B)` : is a connection tree composed of WD adaptors


----

### `(wd.)buildtree`

Function for building the DSP model from a WD connection tree structure.

It recursively steps through the given tree, parametrizes the adaptors, and builds the algorithm.

#### Usage

```
buildtree(A : B);
```

Where: 
`(A : B)` : a connection tree composed of WD adaptors
