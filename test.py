

import imp,SpiralMap
imp.reload(SpiralMap)
import SpiralMap as sp
import matplotlib.pyplot as plt
plt.ion()

plt.close('all')
plotattrs = {'plot':True,'coordsys':'HC','xmin':-5,'xmax':0,'ymin':-1,'ymax':4}
# plotattrs = {'plot':True,'coordsys':'GC'}
spirals = sp.main_()
spirals.getinfo(model='Reid_2019')
# spirals.readout(plotattrs,model='Reid_2019',arm='Sct-Cen')
spirals.readout(plotattrs,model='Reid_2019',arm='all')



