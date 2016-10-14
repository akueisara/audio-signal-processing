# Fourier Properties

## 1. The linearity property of the DFT means that
* the scaled sum of two signals corresponds to the same scaled sum of their spectra

## 2. Shifting a signal in the time domain corresponds to
* multiplying its spectrum by a complex exponential

## 3. The spectrum of a real signal has the following symmetry
* even magnitude spectrum and odd phase spectrum

## 4. If we multiply two signals in the time domain, in the frequency domain this operation corresponds to
* the convolution of their spectra

## 5.The operation to express the magnitude spectrum of a signal in decibels is
* 20*log10(abs(X))

## 6. Phase unwrapping is a way to represent the phase spectrum so that
* we obtain a smooth function not bounded to the range 0 to 2pi

## 7. Zero-padding the input signal of the DFT permits to
* obtain an interpolated spectrum that is easier to study

## 8. The FFT algorithm is an implementation of the DFT equation that
* optimizes calculations by taking advantage of symmetries in the DFT equation

## 9. Zero-phase windowing a signal permits to obtain a spectrum in which
* there is no phase offset because the signal is centered around zero

## 10. If we take the DFT of a real signal and then the IDFT of the resulting spectrum, the resulting signal
* will be identical to the input signal