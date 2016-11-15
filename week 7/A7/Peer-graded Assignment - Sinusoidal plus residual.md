### Part 1.1
##### Analyze the sound with the STFT using the models GUI, or with any other analysis tool you might wish, and describe the characteristics of the sound that might be relevant to perform the HPS analysis. Specially important characteristics for the analysis include pitch range and maximum number of harmonics. Write no more than a paragraph for this description.

* The pitch range of f0: 130-250 Hz
* The maximum number of harmonics: 110 (1/2*fs/f0)
* The harmony length: 0.2 sec

### Part 1.2
##### Select the analysis parameters that give a good reconstruction and at the same time result in the most compact representation possible, specially related to the number of harmonics and the number of stochastic coefficients. We recommend that you first perform the harmonic plus residual analysis and by listening to the residual make some decisions on the best parameters to use. You can listen to the output sounds (harmonic, residual, stochastic components) and fine tune the parameters. Save the output sounds. Explain the choices for the following parameters: window type, window size, FFT size, minimum f0, maximum f0, error threshold in f0 detection, number of harmonics, and stochastic decimation factor. In your descriptions do not use more than one sentence per parameter.

* window type: blackman
* window size: 1350
* FFT size: 2048
* minimum f0: 130
* maximum f0: 250
* error threshold in f0 detection: 5
* number of harmonics: 110
* stochastic decimation factor: 0.2

[speech-harmonic.wav](https://github.com/akueisara/audio-signal-processing/tree/quiz/week%207/A7/speech-harmonic.wav) </br>
[speech-stochastic.wav](https://github.com/akueisara/audio-signal-processing/tree/quiz/week%207/A7/speech-stochastic.wav) </br>
[speech-reconstructed.wav](https://github.com/akueisara/audio-signal-processing/tree/quiz/week%207/A7/speech-reconstructed.wav) </br>

### Part 2.1
##### Choose a sound from freesound to be analyzed. It should be a short monophonic musical fragment of a harmonic sound, not longer than 5 seconds. Put the freesound link of the sound selected and write a brief explanation of why you chose this sound. You can even use a specific sound of your own for this question. Just upload it to freesound and provide a link.

* [Nom_D_02](https://www.freesound.org/people/PaulMorek/sounds/172139/): The sound is not complex to be analyzed and it's a cool sound effect for a hungry dinosaur in a video game. 


### Part 2.2
##### Analyze the chosen sound with the STFT, or with any other analysis or tool you might wish, and describe the characteristics of the sound that will be relevant to perform the harmonic plus stochastic analysis. Important characteristics for the analysis include the pitch range and the maximum number of harmonics. Write no more than a paragraph.

* The pitch range of f0: 100-200 Hz
* The maximum number of harmonics: 170 (1/2*fs/f0)
* The harmony length: 0.5 sec

### Part 2.3
##### Select the analysis parameters that give a good reconstruction and at the same time result in to the most compact representation, specially related to the number of harmonic and the number of stochastic coefficients. We recommend that you first perform the harmonic plus residual analysis and by listening to the residual make some decisions on the best parameters to use. You can listen to the output sounds (harmonic, residual, stochastic components) and fine tune the parameters. Save the output sounds. Explain the choices for the following parameters: window type, window size, FFT size, minimum f0, maximum f0, error threshold in f0 detection, number of harmonics, and stochastic decimation factor. In your descriptions do not use more than one sentence per parameter.

* window type: blackman
* window size: 2040
* FFT size: 2048
* minimum f0: 100
* maximum f0: 200
* error threshold in f0 detection: 5
* number of harmonics: 170
* stochastic decimation factor: 0.2

[a7p2-harmonic.wav](https://github.com/akueisara/audio-signal-processing/tree/quiz/week%207/A7/a7p2-harmonic.wav) </br>
[a7p2-stochastic.wav](https://github.com/akueisara/audio-signal-processing/tree/quiz/week%207/A7/a7p2-stochastic.wav) </br>
[a7p2-reconstructed.wav](https://github.com/akueisara/audio-signal-processing/tree/quiz/week%207/A7/a7p2-reconstructed.wav) </br>