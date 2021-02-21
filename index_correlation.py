import matplotlib.pyplot as plt 
import numpy as np 
import rsg
import correlation as cor

harmonics_count = 8
frequency = 1500
N = 1024

signal,_ = rsg.generateSignal(harmonics_count,frequency,N)
signal_copy,_ = rsg.generateSignal(harmonics_count,frequency,N)

fig1, ax1 = plt.subplots()
fig1.set_size_inches(10,4)

ax1.plot(list(range(N)), signal, c = 'b', label="signal")
ax1.plot(list(range(int(N/2))), cor.autocorrelation(signal),
         linewidth=3, label="correlation", alpha=0.5)

ax1.set_xlim(0, int(N/10))
ax1.set(ylabel='correlation', xlabel='τ',
        title='Autocorrelation')

########## 
fig2, ax2 = plt.subplots()
fig2.set_size_inches(10,4)


ax2.plot(list(range(N)), signal, c = 'b', label="signal")
ax2.plot(list(range(N)), signal_copy, c = 'g', label="signal")
ax2.plot(list(range(int(N/2))), cor.correlation(signal,signal_copy),
         linewidth=3, label="correlation", alpha=0.5)

ax2.set_xlim(0, int(N/10))
ax2.set(ylabel='correlation', xlabel='τ',
        title='Cross-correlation')    

fig1.savefig("autocorrelation.png")
fig2.savefig("crosscorrelation.png")
plt.show()
