
##  ENVELOPE GENERATORS 


----

###  VIBRATO ENVELOPE 

4 phases envelope to control vibrato gain

USAGE:
  _ : *(envVibrato(b,a,s,r,t)) : _
where
  b = beginning duration (silence) in seconds
  a = attack duration in seconds
  s = sustain as a percentage of the amplitude to be modified
  r = release duration in seconds
  t = trigger signal

----

###  ASYMPT60 

Envelope generator which asymptotically approaches a target value.

USAGE:
  asympT60(value,trgt,T60,trig) : _
where
  value = starting value
  trgt = target value
  T60 = ramping time
  trig = trigger signal

##  TABLES 


----

###  CLIPPING FUNCTION 

Positive and negative clipping functions.

USAGE:
  _ : saturationPos : _
  _ : saturationNeg : _
  _ : saturationPos : saturationNeg : _

----

###  BOW TABLE 

Simple bow table.

USAGE:
  index : bow(offset,slope) : _
where
  0 <= index <= 1

----

###  REED TABLE 

Simple reed table to be used with waveguide models of clarinet, saxophone, etc.

USAGE:
  _ : reed(offset,slope) : _
where
  offset = offset between 0 and 1
  slope = slope between 0 and 1
REFERENCE:
*   [https://ccrma.stanford.edu/~jos/pasp/View_Single_Reed_Oscillation.html](https://ccrma.stanford.edu/~jos/pasp/View_Single_Reed_Oscillation.html)

##  FILTERS 


----

###  ONE POLE 


----

###  ONE POLE SWEPT 


----

###  POLE ZERO 


----

###  ONE ZEROS 

Simple One zero and One zero recursive filters

USAGE:
  _ : oneZero0(b0,b1) : _
  _ : oneZero1(b0,b1) : _
REFERENCE:
*   [https://ccrma.stanford.edu/~jos/fp2/One_Zero.html](https://ccrma.stanford.edu/~jos/fp2/One_Zero.html)

----

###  BANDPASS FILTER WITH CONSTANT UNITY PEAK GAIN BASED ON A BIQUAD 


----

###  BANDPASS FILTER BASED ON A BIQUAD 

Band pass filter using a biquad (TF2 is declared in filter.lib)

USAGE:
  _ : bandPassH(resonance,radius) : _
where
  resonance = center frequency
  radius = radius

----

###  FLUE JET NONLINEAR FUNCTION 

Jet Table: flue jet non-linear function, computed by a polynomial calculation

----

###  NON LINEAR MODULATOR 

* nonLinearModulator adapts the function allpassnn from filter.lib for using it with waveguide instruments (see the corresponding DAFx paper: [https://ccrma.stanford.edu/~rmichon/publications/doc/DAFx11-Faust-STK.pdf](https://ccrma.stanford.edu/~rmichon/publications/doc/DAFx11-Faust-STK.pdf) (Faust-STK: a Set of Linear and Nonlinear Physical Models for the Faust Programming Language) for more details).

USAGE:
  _ : nonLinearModulator(nonlinearity,env,freq,typeMod,freqMod,order) : _
where
  nonlinearity = nonlinearity coefficient between 0 and 1
  env = input to connect any kind of envelope
  freq = current tone frequency
  typeMod = if 0: theta is modulated by the incoming signal;
  freqMod = frequency of the sine wave modulation
  order = order of the filter

##  TOOLS 


----

###  STEREOIZER 

This function takes a mono input signal and spacialize it in stereo
in function of the period duration of the tone being played.

USAGE:
  _ : stereo(periodDuration) : _,_
where
  periodDuration = period duration of the tone being played in number of samples
REFERENCE:
*   [https://ccrma.stanford.edu/realsimple/faust_strings/](https://ccrma.stanford.edu/realsimple/faust_strings/)

----

###  INSTRREVERB 

GUI for zita_rev1_stereo from reverbs.lib

USAGE:
 _,_ : instrRerveb
