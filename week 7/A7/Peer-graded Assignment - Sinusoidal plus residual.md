### Part 1.1
##### Analyze the sound with the STFT using the models GUI, or with any other analysis tool you might wish, and describe the characteristics of the sound that might be relevant to perform the HPS analysis. Specially important characteristics for the analysis include pitch range and maximum number of harmonics. Write no more than a paragraph for this description.

* The pitch range of f0: 130-250 Hz
* The maximum number of harmonics: 110 (1/2*fs/f0)
* The harmony length: 0.2 sec

##### Evaluation of Part 1.1: Description of the speech-female sound
A good description of the speech sound (speech-female.wav) should include details about the pitch range, number of harmonics and timbre characteristics of the sound. The fundamental frequency range in this speech excerpt is between 120 Hz and 260 Hz. The number harmonics clearly visible from the spectrogram can reach 60 in the bright vowels. Some parts of the sound are non harmonic, such as the sound corresponding to the pronunciation of the letter S (1.02-1.14 seconds). There are no quick pitch transitions in the voiced regions. The expected answer is a short paragraph describing these aspects of the sound. The maximum score you can assign to this part is 2. The description of the sound given above is only a broad guideline for evaluation.

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

##### Evaluation of Part 1.2: Analysis with HPS model
The most crucial analysis parameters for HPS analysis are window type, window size, mininum f0, maximum f0, number of harmonics, error threshold in f0 detection, and stochastic decimation factor. For the sound 'speech-female.wav' values of these analysis parameters that results in satisfactory performance can be as follows:

* Window type: Hamming
* Window size: 901 (a window size smaller than this can not resolve the partials)
* FFT Size: 2048
* minimum f0: 120 ( this is below the lowest f0 present)
* maximum f0: 260 ( this is above the higher f0 present)
* Error threshold in f0 detection: 8
* Number of harmonics: 80 (even though there are fewer good harmonics by putting this we get a better residual)
* Stochastic decimation factor: .2 (the smallest value that sounds OK)

The answer should include a short explanation the choice of these parameters (one sentence per parameter is OK), and three output sounds. The maximum score you can assign to this part is 3. The parameter values given above are only a broad guideline for evaluation. Your evaluation should be more based on listening to the output sounds, with lesser weight to the choice of parameters.

[speech-harmonic.wav](https://github.com/akueisara/audio-signal-processing/tree/quiz/week%207/A7/speech-harmonic.wav) </br>
[speech-stochastic.wav](https://github.com/akueisara/audio-signal-processing/tree/quiz/week%207/A7/speech-stochastic.wav) </br>
[speech-reconstructed.wav](https://github.com/akueisara/audio-signal-processing/tree/quiz/week%207/A7/speech-reconstructed.wav) </br>

### Part 2.1
##### Choose a sound from freesound to be analyzed. It should be a short monophonic musical fragment of a harmonic sound, not longer than 5 seconds. Put the freesound link of the sound selected and write a brief explanation of why you chose this sound. You can even use a specific sound of your own for this question. Just upload it to freesound and provide a link.

* [Nom_D_02](https://www.freesound.org/people/PaulMorek/sounds/172139/): The sound is not complex to be analyzed and it's a cool sound effect for a hungry dinosaur in a video game. 

##### Evaluation of Part 2.1: Choosing the sound from freesound
The selected sound should be monophonic and harmonic. There should be a Freesound link to the sound and a brief explanation of the reason for choosing it. The duration of the chosen sound should be less than 5 seconds.

### Part 2.2
##### Analyze the chosen sound with the STFT, or with any other analysis or tool you might wish, and describe the characteristics of the sound that will be relevant to perform the harmonic plus stochastic analysis. Important characteristics for the analysis include the pitch range and the maximum number of harmonics. Write no more than a paragraph.

* The pitch range of f0: 100-200 Hz
* The maximum number of harmonics: 170 (1/2*fs/f0)
* The harmony length: 0.5 sec

##### Evaluation of Part 2.2: Description of the chosen sound
The description of the sound should elaborate the timbre characteristics such as brightness of the sound, which mainly relates to the energy distribution among harmonics and total number of salient harmonics. It should specify if the sound has sharp attacks, for example an hammered instrument like piano would have sharp attacks compared to a singing voice. The description should also include a tight range of the fundamental frequency of the melodic source. In addition, you can apply what you learnt from Part 1.1 to evaluate Part 2.2.

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

##### Evaluation of Part 2.3: Analysis with HPS model
1.Download and listen to the sound used for the analysis from freesound </br>
2.Extract the residual component of this sound using HPR model with the same set of analysis parameters mentioned in the submission. Listen to the residual. If the analysis parameters are good, the residual component should not contain any harmonics of the sound. You will not be able to clearly perceive a pitch or see the harmonics if you visualize its spectrogram.</br>
3.Listen to the harmonic component that was uploaded in the submission. The harmonic component should be as continuous and smooth as possible with minimal distortion and musical noise. The pitch of this harmonic component should closely correspond to the pitch of the input sound, without any abrupt changes.</br>
4.Finally, listen to the stochastic component that was uploaded in the submission. It should sound smooth and quite close to the residual.</br>
In addition, you can independently perform an analysis of the downloaded input sound using the HPS model. If you achieve a better analysis (the points mentioned above) compared to the submission, that implies that the analysis parameters in the submission could have been better. You can consider this aspect as well in the evaluation.

[a7p2-harmonic.wav](https://github.com/akueisara/audio-signal-processing/tree/quiz/week%207/A7/a7p2-harmonic.wav) </br>
[a7p2-stochastic.wav](https://github.com/akueisara/audio-signal-processing/tree/quiz/week%207/A7/a7p2-stochastic.wav) </br>
[a7p2-reconstructed.wav](https://github.com/akueisara/audio-signal-processing/tree/quiz/week%207/A7/a7p2-reconstructed.wav) </br>