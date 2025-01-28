

import imp,SpiralMap
imp.reload(SpiralMap)
import SpiralMap as sp
import matplotlib.pyplot as plt
plt.ion()

plotattrs = {'plot':True,'coordsys':'GC'}
spirals = sp.main_()
spirals.getinfo(model='Reid_2019')
spirals.readout(plotattrs,model='Reid_2019',arm='Outer')



