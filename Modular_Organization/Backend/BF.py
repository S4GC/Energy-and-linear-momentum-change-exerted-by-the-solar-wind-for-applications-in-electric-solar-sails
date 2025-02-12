from libraries.py import BF
BF()


# Define a function to apply a Butterworth filter
def butterworth_filter(signal, time, cutoff_freq, order=10):
    
    # Butterworth filter parameters
    sampl_freq = len(signal) / (np.max(time) - np.min(time))
    nyquist = 0.5 * sampl_freq  # Nyquist frequency
    normal_cutoff = cutoff_freq / nyquist  # Normalize the cutoff frequency
    
    # Create the Butterworth filter
    b, a = butter(order, normal_cutoff, btype='lowpass', analog=False) #digital

    # Apply the filter to the raw data
    butter_filtered = filtfilt(b, a, signal)
    
    # Store the filtered result in the dataframe
    #data_sheet[f"{column} Butterworth"] = butter_filtered
    
    # Guardar la gráfica como archivo PNG
    #filename_error = f'butterworth_filter_NS_{year}.png'
    #plt.savefig(filename_error, format='png', dpi=300)
    #print(f"Gráfica guardada como {filename_error}")

    # Conversion in Z-domain 
    b2, a2 = signal.butter(order, 2*(np.pi)*cutoff_freq, 'lowpass', True)# Perform an analog butter filter
    z2, p2 = signal.bilinear(b2, a2, sampl_freq) #cambia del dominio de s al domino de z, z: numerador p:demonimador fs:frecuencia de muestreo
    w2, h2 = signal.freqz(z2, p2, 512) # w is the freq in z-domain & h is the magnitude in z-domain
    z2, p2, k2 = signal.tf2zpk(z2,p2)

    return nyquist, normal_cutoff, 2*np.pi*cutoff_freq, b, a, z2, p2, k2, w2, h2

