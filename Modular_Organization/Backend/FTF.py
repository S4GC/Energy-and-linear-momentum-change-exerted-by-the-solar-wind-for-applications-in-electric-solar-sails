import numpy as np


def FT_filter(signal, time, cutoff_frequency, pass_type):
  """
  Applies a high-pass filter in the Fourier domain to the signal.
  
  :param signal: Signal to filter.
  :param time: Time corresponding to each signal point.
  :param cutoff_frequency: Cutoff frequency in Hz.
  :param pass_type: "low" or "high
  
  :return: filtered signal, freqs, raw freqs amplitudes, filter freqs amplitudes.
  """
  
  # FFT of the signal
  fft_signal = np.fft.fft(signal)
  n = len(signal)
  freqs = np.fft.fftfreq(n, d=(np.max(time) - np.min(time)) / n)

  # Apply filter
  if pass_type == "low":
    filter_mask = np.abs(freqs) <= cutoff_frequency
  elif pass_type == "high":
    filter_mask = np.abs(freqs) >= cutoff_frequency
  else:
    print("Pass type not found: only ¨low¨ or ¨high¨. In this case, different operator is applied in filter_mask")
    filter_mask = np.abs(freqs) != cutoff_frequency

  filtered_fft_signal = fft_signal * filter_mask
  filtered_signal = np.fft.ifft(filtered_fft_signal).real  # Filtered signal in the time domain

  return filtered_signal, freqs, np.sqrt((np.abs(fft_signal)**2)), np.sqrt((np.abs(filtered_fft_signal)**2))


def amplitude_FT_filter(signal, time, cutoff_amplitude, pass_type):
  """
  Applies a high-pass filter in the amplitude Fourier domain to the signal.
  
  :param signal: Signal to filter.
  :param time: Time corresponding to each signal point.
  :param cutoff_amplitude: Cutoff amplitude.
  :param pass_type: "low" or "high
  
  :return: filtered signal, freqs, raw freqs magnitudes, filter freqs magnitudes.
  """
  
  # FFT of the signal
  fft_signal = np.fft.fft(signal)
  n = len(signal)
  freqs = np.fft.fftfreq(n, d=(np.max(time) - np.min(time)) / n)

  # Apply filter
  if pass_type == "low":
    filter_mask = np.sqrt((np.abs(fft_signal**2))) <= cutoff_amplitude
  elif pass_type == "high":
    filter_mask = np.sqrt((np.abs(fft_signal**2))) >= cutoff_amplitude
  else:
    print("Pass type not found: only ¨low¨ or ¨high¨. In this case, different operator is applied in filter_mask")
    filter_mask = np.sqrt((np.abs(fft_signal**2))) != cutoff_amplitude
  
  filtered_fft_signal = fft_signal * filter_mask
  filtered_signal = np.fft.ifft(filtered_fft_signal).real  # Filtered signal in the time domain

  return filtered_signal, freqs, np.sqrt((np.abs(fft_signal)**2)), np.sqrt((np.abs(filtered_fft_signal)**2))