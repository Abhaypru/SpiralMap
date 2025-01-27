

import imp,SpiralMap
imp.reload(SpiralMap)
import SpiralMap as sp

plotattrs = {'plot':True}
spirals = sp.main_()
spirals.getinfo(model='Reid_2019')
spirals.readout(plotattrs,model='Reid_2019',arm='Perseus')
