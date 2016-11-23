# Sound transformations

## 1. Filtering using the STFT can be performed by
* multiplying the magnitude spectrum of the filter response by the one of the sound and adding the phase spectrum of the filter response with the one of the sound

## 2. To apply a band pass filter using the STFT and to minimize any resulting distortion we should multiply the magnitude spectrum of the sound by
* a smooth function, like a hanning window

## 3. In class we implemented sound morphing using the STFT, modifying the magnitude spectrum of each frame of a sound by
* interpolating, or combining, the magnitude spectrum with the one of another

## 4. To obtain the effect of a "speaking ocean", when doing spectral morphing using the STFT and combining a speech sound with a sound of the ocean, we should generate an output spectrum in which
* the magnitude spectrum is mainly the one of the speech sound and the phase spectrum is the one of the ocean sound

## 5. With the sinusoidal model, if we want to perform a time stretching transformation
* we have to interpolate the frequencies and amplitudes of the sinusoids and generate the phases of the sinusoids from the frequency information

## 6. With the harmonic plus residual model it is not feasible, or really hard, to perform
* time stretching

## 7. With the sinusoidal plus residual model we can perform frequency transformations by
* modifying the frequencies of the sinusoidal component

## 8. The different between frequency transposition and frequency shifting in a harmonic sound is that
* in frequency transposition we preserve the harmonicity of the sound

## 9. With the harmonic plus stochastic model we can transform
* the harmonic frequencies, magnitudes and the stochastic component

## 10. With the morphing performed with the harmonic plus stochastic model we can obtain a synthesized sounds that
* can sound like going from one sound to the other progresively