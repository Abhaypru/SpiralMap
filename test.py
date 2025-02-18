

import imp,SpiralMap, dtools
imp.reload(SpiralMap)
import SpiralMap as sp
import matplotlib.pyplot as plt
import os

figdir = '/figdir'
os.system('rm -rf figdir')
os.system('mkdir figdir')
plt.ion()

plt.close('all')
plt.figure(figsize=(6,6))
plotattrs = {'plot':True,'coordsys':'GC','markSunGC':True,'xmin':-16,'xmax':8,'ymin':-12,'ymax':12}
spirals = sp.main_()
spirals.getinfo(model='Drimmel_NIR_2000')
spirals.readout(plotattrs,model='Drimmel_NIR_2000',arm='all')


# plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'xmin':-20,'xmax':10,'ymin':-15,'ymax':15}
# # models = ['Levine_2006', 'Reid_2019','Drimmel_NIR_2000','Drimmel_ceph_2024','Poggio_2021','Hou_Han_2014', 'Levine_2006']
# # # # models = ['Hou_Han_2014', 'Levine_2006']
# models = ['Taylor_Cordes_1992']
# xsun=-8.277
# models = ['Poggio_2021']

# spirals = sp.main_(xsun=xsun)
# for inum,use_model in enumerate(models):		
	# plt.close('all')
	# plt.figure(figsize=(6,6))

	# spirals.getinfo(model=use_model)
	# spirals.readout(plotattrs,model=use_model,arm='all')
	
	# plt.tight_layout()
	# plt.savefig('figdir/test_'+str(inum)+'.png')



# plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'xmin':-20,'xmax':10,'ymin':-15,'ymax':15}
# xsun=-8.277
# spirals = sp.main_(xsun=xsun)
# for inum,use_model in enumerate(spirals.models):		
	# plt.close('all')
	# plt.figure(figsize=(6,6))
	
	# if 'pogg' in use_model:    
		# plotattrs['coordsys'] = 'HC'
	
	# spirals.getinfo(model=use_model)
	# spirals.readout(plotattrs,model=use_model,arm='all')
	
	# plt.tight_layout()
	# plt.savefig('figdir/test_'+str(inum)+'.png')

# plt.close('all')
# plt.close()
# plt.figure(figsize=(7,7))
# for inum,use_model in enumerate(models):	


	# spirals.getinfo(model=use_model)
	# spirals.readout(plotattrs,model=use_model,arm='all')


	
# plt.tight_layout()
# plt.savefig('figdir/test_'+str(inum)+'.png')

# spiral = sp.TaylorCordesSpiral()
# spiral.info()
# param = spiral.getparams()







