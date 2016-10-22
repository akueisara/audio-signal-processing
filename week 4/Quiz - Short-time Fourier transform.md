# Short-time Fourier transform

## 1. The main relationship between the STFT and the DFT is that
* the STFT is the time-varying version of the DFT

## 2. The DFT of a windowed sinusoid is
* the transform of the window shifted to the frequency of the sinusoid and scaled with the amplitude of the sinusoid

## 3. The analysis windows that we use in this course are
* real and symmetric functions

## 4. The main difference between the Blackman window and the Hanning window is that
* the spectrum of the Blackman window has a wider main lobe and a lower highest side lobe level than the Hanning window

## 5. A bigger window size applied to a stable sound will result into
* better frequency resolution

## 6. The main difference between an even and an odd size window is that
* with an odd-size window we can apply perfect zero-phase windowing

## 7. Given a window-size M, if we use an FFT-size N larger than M
* we will apply zero padding to the windowed signal

## 8. For a perfect reconstruction using the STFT, the window hop-size should be chosen in a way that
* the overlapping of the windows is equal to a constant

## 9. The time-frequency compromise of the STFT refers to the fact that
* if we want to improve the frequency resolution by increasing the window size we lose time resolution

## 10. A magnitude spectrogram is
* the visualisation of the sequence of magnitude spectra obtained using the STFT