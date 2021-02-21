import matplotlib.pyplot as plt 
import numpy as np 
import rsg

harmonics_count = 8
frequency = 1500
N = 1024

signals,harmonics_time = rsg.generateSignal(harmonics_count,frequency,N)

print("Expected value: ", np.mean(signals))
print("Dispersion: ", np.std(signals))

for i in range(harmonics_count):
        print("harmonic {0} creation time: {1}s".format(i,harmonics_time[i]))


fig, ax1 = plt.subplots()
fig.set_size_inches(12,3)

ax1.plot(signals)
ax1.set(xlabel='Time', ylabel='Signal(t)',
        title='Random generated signals')

fig.savefig("plot.png")
plt.show()

