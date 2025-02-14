

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


plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'xmin':-20,'xmax':20,'ymin':-20,'ymax':20}
models = ['Levine_2006', 'Reid_2019','Drimmel_NIR_2000','Drimmel_ceph_2024','Poggio_2021','Hou_Han_2014', 'Levine_2006']
# # # models = ['Hou_Han_2014', 'Levine_2006']
# models = ['Reid_2019']
xsun=-8.277
# models = ['Poggio_2021']
plt.close('all')
plt.figure(figsize=(6,6))
spirals = sp.main_(xsun=xsun)
for use_model in models:	
	spirals.getinfo(model=use_model)
	spirals.readout(plotattrs,model=use_model,arm='all')
	
plt.tight_layout()
plt.savefig('test.png')
# spiral = sp.spiral_houhan()
# spiral.info()
# param = spiral.getparams()
