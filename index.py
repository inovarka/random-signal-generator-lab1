import matplotlib.pyplot as plt 
import numpy as np 
import rsg

harmonics_count = 8
frequency = 1500
N = 1024

signals = rsg.generateSignal(harmonics_count,frequency,N)

print("Expected value: ", np.mean(signals))
print("Dispersion: ", np.std(signals))

fig, ax1 = plt.subplots()
fig.set_size_inches(12,3)

ax1.plot(signals)
ax1.set(xlabel='Time', ylabel='Signal(t)',
        title='Random generated signals')

fig.savefig("plot.png")
plt.show()
