

import imp,SpiralMap, dtools
imp.reload(SpiralMap)
imp.reload(dtools)
# import SpiralMap as sp
# import matplotlib.pyplot as plt
# import numpy as np
# import os
# import putil
# import imp,SpiralMap
# imp.reload(SpiralMap)

# import matplotlib.pyplot as plt
# import numpy as np
from SpiralMap import *
import SpiralMap as sp
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
		
	# correct poggio hc limits')
	print('plotting figures for primer')
	xsun=-8.277
		
	plt.close('all')
	plm=putil.Plm2(10,10,xsize=8.0,ysize=4.5,xmulti=False,ymulti=False,full=True,slabelx=0.7,slabely=0.07)			
	
	mylims = {}
	
	spirals = sp.main_(xsun=xsun)
	for inum,use_model in enumerate(spirals.models):		
		
		if use_model != 'Poggio_2021':
			mylims[use_model] = {}
			
			plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':False}		

			coordsys = plotattrs['coordsys']

			plm.next()
				
			spirals.getinfo(model=use_model)
			spirals.readout(plotattrs,model=use_model,arm='all')
			
			mylims[use_model]['xmin'+'_'+coordsys] = spirals.xmin
			mylims[use_model]['xmax'+'_'+coordsys] = spirals.xmax
			mylims[use_model]['ymin'+'_'+coordsys] = spirals.ymin
			mylims[use_model]['ymax'+'_'+coordsys] = spirals.ymax
	
			spirals.getinfo(model='Poggio_2021')
			spirals.readout(plotattrs,model='Poggio_2021',arm='all')
			mylims['Poggio_2021'] = {}
			mylims['Poggio_2021']['xmin'+'_'+coordsys] = spirals.xmin
			mylims['Poggio_2021']['xmax'+'_'+coordsys] = spirals.xmax
			mylims['Poggio_2021']['ymin'+'_'+coordsys] = -10
			mylims['Poggio_2021']['ymax'+'_'+coordsys] = 10
			
			plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polargrid':False}		
			coordsys = plotattrs['coordsys']
			plm.next()
				
			spirals.getinfo(model=use_model)
			spirals.readout(plotattrs,model=use_model,arm='all')
	
			mylims[use_model]['xmin'+'_'+coordsys] = spirals.xmin
			mylims[use_model]['xmax'+'_'+coordsys] = spirals.xmax
			mylims[use_model]['ymin'+'_'+coordsys] = spirals.ymin
			mylims[use_model]['ymax'+'_'+coordsys] = spirals.ymax
	
			spirals.getinfo(model='Poggio_2021')
			spirals.readout(plotattrs,model='Poggio_2021',arm='all')

			mylims['Poggio_2021']['xmin'+'_'+coordsys] = spirals.xmin
			mylims['Poggio_2021']['xmax'+'_'+coordsys] = spirals.xmax
			mylims['Poggio_2021']['ymin'+'_'+coordsys] = -10
			mylims['Poggio_2021']['ymax'+'_'+coordsys] = 10

	dtools.picklewrite(mylims,'flim',sp.dataloc)	


single_old = False
if single_old:
		
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
	# spirals.readout(plotattrs,model='Levine_2006',arm='all')
	# spirals.readout(plotattrs,model='Hou_Han_2014',arm='all')	
			

	plm.next()		
	print('style 2')
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm='all')
	# spirals.readout(plotattrs,model='Levine_2006',arm='all')
	# spirals.readout(plotattrs,model='Hou_Han_2014',arm='all')


	
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
	

mkJossfigs = False
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
	print('')
	
#------------------------------------------------------------	
############## figures for documentation ####################



single_extract_plot = False
if single_extract_plot:	
	
	#
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Drimmel_ceph_2024'
	use_arm = 'Orion'
	spirals.getinfo(model=use_model)	
	plotattrs = {'plot':False}
	spirals.readout(plotattrs,model=use_model,arm='Orion')
		
	print(list(spirals.dout.keys()))
	print('first 4 data points from the first 4 keys..')
	for ky in list(spirals.dout.keys())[:4]:
	    print(ky)
	    print(spirals.dout[ky][:4])	


	#
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Drimmel_ceph_2024'
	use_arm = 'Orion'
	spirals.getinfo(model=use_model)	

	import matplotlib.gridspec as gridspec
	
	plt.close('all')
	fig = plt.figure(figsize=(8, 3))

	fig.add_subplot(1,3,1)
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)

	fig.add_subplot(1,3,2)
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)

	fig.add_subplot(1,3,3)
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)
	
	fig.suptitle(use_model+'('+use_arm+')')
	fig.tight_layout()
	plt.savefig(figdir_primer+'/single_model_single_arm_demo.png')


single_model = True
if single_model:
		
	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Drimmel_ceph_2024'
	use_arm = 'Orion'
	spirals.getinfo(model=use_model)
				
	import matplotlib.gridspec as gridspec
	
	plt.close('all')
	fig = plt.figure(figsize=(8, 3))

	fig.add_subplot(1,3,1)
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)
	spirals.readout(plotattrs,model='Poggio_2021')
	
	fig.add_subplot(1,3,2)
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':False}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)
	spirals.readout(plotattrs,model='Poggio_2021')

	fig.add_subplot(1,3,3)
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)
	spirals.readout(plotattrs,model='Poggio_2021')
	
	fig.suptitle(use_model+'('+use_arm+')')
	fig.tight_layout()
	plt.savefig(figdir_primer+'/single_all_arms_demo.png')
	

single_model_polar = False
if single_model_polar:

	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Poggio_2021'#'Hou_Han_2014'
	spirals.getinfo(model=use_model)
				
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':False,'polargrid':False,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm='all')
	spirals.readout(plotattrs,model='Taylor_Cordes_1992',arm='all')


	ax.set_rticks([3., 6.,9.,12,15.,20.])
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)

	plt.title(use_model)
	# ax.set_xlim([np.radians(100),np.radians(260)])
	# ax.set_ylim([0.,8])

	plt.savefig(figdir_primer+'/polar_grid_overplotted.png')


checkpolar = True
if checkpolar:

	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Drimmel_NIR_2000'


	spirals.getinfo(model=use_model)
				
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	plotattrs = {'plot':True,'markersize':15,'polarproj':True}	
	spirals.readout(plotattrs,model=use_model,arm='all')	
	# spirals.readout(plotattrs,model='Taylor_Cordes_1992',arm='all')	
	# spirals.readout(plotattrs,model='Levine_2006',arm='all')	

	ax.set_rticks([3., 6.,9.,12,15.])
	ax.set_thetagrids(list(np.arange(0.,360.,30)))
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)

	plt.title(use_model)
	# ax.set_xlim([np.radians(100),np.radians(260)])
	ax.set_ylim([0.,15])

	plt.savefig(figdir_primer+'/polar_grid_overplotted1_gc.png')
	
	
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	plotattrs = {'plot':True,'markersize':15,'polarproj_hc':True}	
	spirals.readout(plotattrs,model=use_model,arm='all')	

	ax.set_rticks([3., 6.,9.,12,15.])
	ax.set_thetagrids(list(np.arange(0.,360.,30)))
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)

	plt.title(use_model)
	# ax.set_xlim([np.radians(100),np.radians(260)])
	ax.set_ylim([0.,15])

	plt.savefig(figdir_primer+'/polar_grid_overplotted1.png')

	use_model = 'Drimmel_ceph_2024'
	plt.close('all') 	
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	plotattrs = {'plot':True,'markersize':15,'polarproj_hc':True}	
	spirals.readout(plotattrs,model=use_model,arm='Sag-Car')	

	ax.set_rticks([3., 6.,9.,12,15.])
	ax.set_thetagrids(list(np.arange(0.,360.,30)))
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)

	plt.title(use_model)
	# ax.set_xlim([np.radians(100),np.radians(260)])
	ax.set_ylim([0.,15])

	plt.savefig(figdir_primer+'/polar_grid_overplotted2.png')



