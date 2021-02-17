import numpy as np 
import math

def correlation(signal1,signal2):
    result = []

    m1 = np.mean(signal1)
    m2 = np.mean(signal2)

    d1 = np.std(signal1)
    d2 = np.std(signal2)

    l = len(signal1) // 2
    
    for tau in range(l):
        cov = 0

        for i in range(l):
            cov += (signal1[i]-m1)*(signal2[i + tau]-m2) / (l-1)

        result.append(cov / (math.sqrt(d1) * math.sqrt(d2)))    
            
    return result


def autocorrelation(signal1):
    return correlation(signal1,signal1)