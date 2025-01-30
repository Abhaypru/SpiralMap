

import imp,SpiralMap, dtools
imp.reload(SpiralMap)
import SpiralMap as sp
import matplotlib.pyplot as plt
plt.ion()

# plt.close('all')
# plt.figure(figsize=(6,6))
# # plotattrs = {'plot':True,'coordsys':'GC','markSunGC':True,'xmin':-16,'xmax':8,'ymin':-12,'ymax':12}
# plotattrs = {'plot':True,'coordsys':'GC','markSunGC':False}
# spirals = sp.main_()
# spirals.getinfo(model='Drimmel_NIR_2000')
# # spirals.readout(plotattrs,model='Reid_2019',arm='Sct-Cen')
# spirals.readout(plotattrs,model='Drimmel_NIR_2000',arm='all')


plotattrs = {'plot':True,'coordsys':'GC','markersize':5,'markSunGC':True,'xmin':-16,'xmax':8,'ymin':-12,'ymax':12}
# models = ['Levine_2006', 'Reid_2019','Drimmel_NIR_2000']
xsun=-8.277
models = ['Drimmel_ceph_2024']
plt.close('all')
plt.figure(figsize=(6,6))
for use_model in models:

	spirals = sp.main_(xsun=xsun)
	spirals.getinfo(model=use_model)
	spirals.readout(plotattrs,model=use_model,arm='all')
	
plt.tight_layout()
