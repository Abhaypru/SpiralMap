

# import imp,SpiralMap, dtools
# imp.reload(SpiralMap)
# import SpiralMap as sp
# import matplotlib.pyplot as plt
# import numpy as np
# import os
# import putil
# import imp,SpiralMap
# imp.reload(SpiralMap)
from SpiralMap import *
import SpiralMap as sp
# import matplotlib.pyplot as plt
# import numpy as np
# import os
import putil

figdir_primer = 'figdir_primer'
os.system('rm -rf '+figdir_primer); os.system('mkdir '+figdir_primer)
plt.ion()
		


mkpaperfigs = False
if mkpaperfigs:
	
	
	print('plotting figures for primer')
	xsun=-8.277
	# plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'xmin':-10,'xmax':10,'ymin':-10,'ymax':10}
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	plt.close('all')
	plm=putil.Plm2(2,3,xsize=8.0,ysize=4.5,xmulti=False,ymulti=False,full=True,slabelx=0.7,slabely=0.07)			
	
	
	spirals = sp.main_(xsun=xsun)
	for inum,use_model in enumerate(spirals.models):		

		if use_model != 'Poggio_2021':
			

			plm.next()
			spirals.modrec = []
			spirals.getinfo(model='Poggio_2021')
			spirals.readout(plotattrs,model='Poggio_2021',arm='all')				

			spirals.getinfo(model=use_model)
			spirals.readout(plotattrs,model=use_model,arm='all')	

	
			plt.title(use_model)
	
	plm.tight_layout()
	plt.savefig(figdir_primer+'/spirals_'+plotattrs['coordsys']+'.png')
	
savelims = False
if savelims:
		
	
	print('plotting figures for primer')
	xsun=-8.277
	# plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'xmin':-10,'xmax':10,'ymin':-10,'ymax':10}
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':False}
	plt.close('all')
	plm=putil.Plm2(2,3,xsize=8.0,ysize=4.5,xmulti=False,ymulti=False,full=True,slabelx=0.7,slabely=0.07)			
	
	mylims = {}
	
	spirals = sp.main_(xsun=xsun)
	for inum,use_model in enumerate(spirals.models):		
		
		if use_model != 'Poggio_2021':
			
			

			plm.next()
				
			spirals.getinfo(model=use_model)
			spirals.readout(plotattrs,model=use_model,arm='all')
			mylims[use_model] = {}
			mylims[use_model]['xmin'] = spirals.xmin
			mylims[use_model]['xmax'] = spirals.xmax
			mylims[use_model]['ymin'] = spirals.ymin
			mylims[use_model]['ymax'] = spirals.ymax
	
			spirals.getinfo(model='Poggio_2021')
			spirals.readout(plotattrs,model='Poggio_2021',arm='all')
			mylims['Poggio_2021'] = {}
			mylims['Poggio_2021']['xmin'] = spirals.xmin
			mylims['Poggio_2021']['xmax'] = spirals.xmax
			mylims['Poggio_2021']['ymin'] = -10
			mylims['Poggio_2021']['ymax'] = 10

	dtools.picklewrite(mylims,'flim',sp.dataloc)	


single_ = False
if single_:
		
	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Drimmel_ceph_2024'
	spirals.getinfo(model=use_model)
				
	plt.close('all')
	plm=putil.Plm1(1,2,xsize=8.0,ysize=4,xmulti=False,ymulti=False,full=True,slabelx=0.7,slabely=0.07)			
		

	plm.next()		

	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':False}
	spirals.readout(plotattrs,model=use_model,arm='all')
	spirals.readout(plotattrs,model='Levine_2006',arm='all')
	spirals.readout(plotattrs,model='Hou_Han_2014',arm='all')	
			

	plm.next()		
	print('style 2')
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm='all')
	spirals.readout(plotattrs,model='Levine_2006',arm='all')
	spirals.readout(plotattrs,model='Hou_Han_2014',arm='all')


	
	# plt.xlim([-15,0.])


	plt.title(use_model)
	
	plm.tight_layout()
	plt.savefig(figdir_primer+'/polar_grid_overplotted.png')
	
polar_test = False
if polar_test:
		
	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Poggio_2021'
	spirals.getinfo(model=use_model)
				
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))


	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':False,'polargrid':False,'polarproj':True}


	# for inum,use_model in enumerate(spirals.models):
	
		# spirals.readout(plotattrs,model=use_model,arm='all')
	use_model = 'Reid_2019'
	spirals.readout(plotattrs,model=use_model,arm='all')
	use_model = 'Drimmel_ceph_2024'
	spirals.readout(plotattrs,model=use_model,arm='all')
	use_model = 'Poggio_2021'
	spirals.readout(plotattrs,model=use_model,arm='all')
	use_model = 'Hou_Han_2014'
	spirals.readout(plotattrs,model=use_model,arm='all')


	ax.set_rticks([3., 6.,9.,12,15.,20.])
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)

	# plt.title(use_model)
	ax.set_xlim([np.radians(100),np.radians(260)])
	ax.set_ylim([0.,8])

	plt.savefig(figdir_primer+'/polar_grid_overplotted.png')
	

mkJossfigs = True
if mkJossfigs:

	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model1 = 'Hou_Han_2014' 
	use_model2 = 'Poggio_2021' #'Taylor_Cordes_1992' #'Poggio_2021'
	use_model3 = 'Poggio_2021'
	spirals.getinfo(model=use_model1)


	plt.close('all')
	plm=putil.Plm2(1,3,xsize=8.0,ysize=3.,xmulti=False,ymulti=False,full=True,slabelx=0.7,slabely=0.07)			
	
	plm.next()

	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polargrid':False}

	spirals.readout(plotattrs,model=use_model1,arm='all')	
	spirals.readout(plotattrs,model=use_model2,arm='all')
	spirals.readout(plotattrs,model=use_model3,arm='all')
	plm.next()
	
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':False}

	spirals.readout(plotattrs,model=use_model1,arm='all')	
	spirals.readout(plotattrs,model=use_model2,arm='all')
	spirals.readout(plotattrs,model=use_model3,arm='all')
		
	plm.next()

	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}

	spirals.readout(plotattrs,model=use_model1,arm='all')	
	spirals.readout(plotattrs,model=use_model2,arm='all')
	spirals.readout(plotattrs,model=use_model3,arm='all')
			
	plm.tight_layout()

	plt.savefig(figdir_primer+'/JOSS_xyplot.png')	

				
	# # plt.close('all')
	# # fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))


	# # plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':False,'polargrid':False,'polarproj':True}


	# # # for inum,use_model in enumerate(spirals.models):
	
		# # # spirals.readout(plotattrs,model=use_model,arm='all')
	# # use_model = 'Reid_2019'
	# # spirals.readout(plotattrs,model=use_model,arm='all')
	# # use_model = 'Drimmel_ceph_2024'
	# # spirals.readout(plotattrs,model=use_model,arm='all')
	# # use_model = 'Poggio_2021'
	# # spirals.readout(plotattrs,model=use_model,arm='all')
	# # use_model = 'Hou_Han_2014'
	# # spirals.readout(plotattrs,model=use_model,arm='all')


	# # ax.set_rticks([3., 6.,9.,12,15.,20.])
	
	# # rlabels = ax.get_ymajorticklabels()
	# # for label in rlabels:
	    # # label.set_color('blue')
	    # # label.set_size(fontsize=10)

	# # # plt.title(use_model)
	# # ax.set_xlim([np.radians(100),np.radians(260)])
	# # ax.set_ylim([0.,8])

	# # plt.savefig(figdir_primer+'/polar_grid_overplotted.png')

	
	
	
	
