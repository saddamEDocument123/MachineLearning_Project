# MatPlotlib Basic Coloring and SubPlots
#


import  matplotlib
import  matplotlib.pyplot as plt
fig = plt.figure()

# change the color of the background
rect = fig.patch
rect.set_facecolor('green')

x=[3,7,8,13]
y=[5,13,2,8]

# change grape color

grape1 = fig.add_subplot(1,1,1,axisbg='blue')
# change line color

grape1.plot(x,y,'red',linewidth='4.0')
plt.show()