import random
import math
from time import perf_counter
 

def generateSignal(harmonics_count,frequency,N):
    signal = [0] * N
    harmonics_time =  []

    for i in range (harmonics_count):
        start_time = perf_counter()

        W = (frequency / harmonics_count) * (i+1)
        Amplitude = random.random()
        Phase = random.random()

        for t in range(N):
            signal[t] += (Amplitude * math.sin(W * t + Phase))

        harmonic_time = perf_counter() - start_time 
        harmonics_time.append(harmonic_time)

    return signal, harmonics_time