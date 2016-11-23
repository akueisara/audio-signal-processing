### Question 1. Perform natural sounding transformations of a speech sound
##### Use the HPS model with the sound speech-female.wav, available in the sounds directory of sms-tools, to first analyze and then obtain a natural sounding transformation of the sound. The synthesized sound should sound as different as possible to the original sound while sounding natural. By natural we mean that it should sound like speech, that it could have been possible to be produced by a human, and by listening we should consider it as a speech sound, even though we might not be able to understand it. You should first make sure that you start from a good analysis, then you can do time and/or frequency scaling transformations. The transformation should be done with a single pass, no mixing of sounds coming from different transformations. Since you used the same sound in A7, use that experience to get a good analysis, but consider that the analysis, given that we now want to use it for applying a very strong transformation, might be done differently than what you did in A7. 
</br>
##### Write a short paragraph for every transformation, explaining what you wanted to obtain and explaining the transformations you did, giving both the analysis and transformation parameter values (sufficiently detailed for the evaluator to be able to reproduce the analysis and transformation). 
</br>
Analysis parameters:
window = blackman
M = 1650 (6*44000/160 (f0 is around 160Hz on average))
N = 4096 (zero padding)
t = -100 (will have a lot of harmonics)
minSineDur = 0.1
nH = 100
minf0 = 100
maxf0 = 300
f0et = 7
harmDevSlope = 0.01
stocf = 0.4

Transformation 1:
frequency scaling = [0, 3]
frequency stretching = [0, 1]
time scaling = [0, 0, 1, 3.146]
timbre preservation = 1

The transformation increased the pitch and slowed it down.

Transformation 2:
frequency scaling = [0, .25]
frequency stretching = [0, 1]
time scaling = [0, 0, 1, 3.146]
timbre preservation = 1

slow and low 

Transformation 3:
frequency scaling = [0, .25]
frequency stretching = [0, 1]
time scaling = [0, 0, 5, 3.146]
timbre preservation = 1

fast and low

##### After the parameter explanation, upload a maximum of three transformed sounds (e.g., speech-transformed-1.wav, speech-transformed-2.wav, speech-transformed-3.wav). You should compress them into one zip file which you upload.
[speech-hpsModel.wav](https://github.com/akueisara/audio-signal-processing/tree/master/week%208/A8/speech-hpsModel.wav) </br>
[speech-transformed-1.wav](https://github.com/akueisara/audio-signal-processing/tree/master/week%208/A8/speech-transformed-1.wav) </br>
[speech-transformed-2.wav](https://github.com/akueisara/audio-signal-processing/tree/master/week%208/A8/speech-transformed-2.wav) </br>
[speech-transformed-3.wav](https://github.com/akueisara/audio-signal-processing/tree/master/week%208/A8/speech-transformed-3.wav) </br>

### Question 2. Perform creative transformations with a sound of your choice
##### Pick any natural and harmonic sound from freesound.org and use the HPS model to do the most creative and interesting transformation you can come up with. Sounding as different as possible from the original sound.
</br>
##### It is essential that you start with a natural harmonic sound. Examples include (but not limited to) any acoustic harmonic instrument, speech, harmonic sound from nature, etc. As long as they have a harmonic structure, you can use it. You can even reuse the sound you used in A7-Part2 or upload your own sound to freesound and then use it.
</br>
##### The sound from freesound to use could be in any format, but to use the sms-tools software you will have to first convert it to be a monophonic file (one channel), sampling rate of 44100, and 16bits samples.
</br>
##### You can do any interesting transformation with a single pass. It is not allowed to mix sounds obtained from different transformations. The transformed sound need not sound natural. So, time to show some creativity!
</br>
##### Write a short paragraph for every transformation, explaining what you wanted to obtain and explaining the transformations you did, giving both the analysis and transformation parameter values (sufficiently detailed for the evaluator to be able to reproduce the analysis and transformation).
</br>
http://freesound.org/people/smart61/sounds/256506/

Analysis parameters:
window = blackman
M = 1200 (6*44000/220 (f0 is around 220Hz on average))
N = 4096 (zero padding)
t = -100 (will have a lot of harmonics)
minSineDur = 0.1
nH = 100
minf0 = 170
maxf0 = 270
f0et = 7
harmDevSlope = 0.01
stocf = 0.4

Transformation 1:
frequency scaling = [0, 1.2, 2.01, 1.2, 2.679, .7, 3.146, .7]
frequency stretching = [0, 1, 2.01, 1, 2.679, 1.5, 3.146, 1.5]
time scaling = [0, 0, 2.138, 2.138-1.0, 3.146, 3.146]
timbre preservation = 1

Transformation 2:
frequency scaling = [0, .3]
frequency stretching = [0, 1]
time scaling = [0, 0, 2, 3]
timbre preservation = 1

the pitch changed and the speed became slower

Transformation 3:
frequency scaling = [0, 3]
frequency stretching = [0, 1]
time scaling = [0, 0, 1, .5]
timbre preservation = 1

##### Upload a maximum of three transformed sounds (name them a8p2-transformed-1.wav, a8p2-transformed-2.wav, ...). You should compress them into one zip file which you upload. Your peers will choose the "most interesting" among those submitted for evaluation.
[a8p2.wav](https://github.com/akueisara/audio-signal-processing/tree/master/week%208/A8/a8p2.wav) </br>
[a8p2-transformed-1.wav](https://github.com/akueisara/audio-signal-processing/tree/master/week%208/A8/a8p2-transformed-1.wav) </br>
[a8p2-transformed-2.wav](https://github.com/akueisara/audio-signal-processing/tree/master/week%208/A8/a8p2-transformed-2.wav) </br>
[a8p2-transformed-3.wav](https://github.com/akueisara/audio-signal-processing/tree/master/week%208/A8/a8p2-transformed-3.wav) </br>