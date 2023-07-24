import numpy as np
import matplotlib.pyplot as plt

resolution = 6
offset     = 8192
amplitude  = 8190

# Compute number of sample
nsample     = int(360/resolution)
alpha       = np.linspace(0, (360-resolution), nsample)
sin_uint14  = np.round( ((np.sin(alpha*np.pi/180) * amplitude) + offset), 0 )

# Print output
print('Angle array')
print(alpha)
print('Sine samples (14-bit, unsigned)')
print(sin_uint14)
for k in range(nsample):
    h = '{:04}'.format(int(sin_uint14[k]))
    print(h + ', ', end='')
    if ((k+1)%4 == 0):
        print()
# Plot wavetable
fig = plt.figure(1)
fig.clf()
plt.title('Sine wavetable')
plt.xlabel('Alpha')
plt.ylabel('#')
plt.plot(alpha, sin_uint14, 'ro')
plt.xlim(0,360)
plt.xticks(np.arange(0, 360 +1, step=30))
plt.ylim(0,16383)
plt.yticks(np.arange(0, 16383 +1, step=256))
plt.grid(True)
plt.show()