

from SpiralMap import *
import SpiralMap as sp

import imp,SpiralMap, dtools
imp.reload(SpiralMap)
imp.reload(dtools)
import putil


figdir_primer = 'figdir_primer'
os.system('rm -rf '+figdir_primer); os.system('mkdir '+figdir_primer)
plt.ion()
	

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


single_model_single_arm = False
if single_model_single_arm:
		
	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model =  'Drimmel_Ceph_2024' #'Taylor_Cordes_1992'
	use_arm = 'Sag-Car' 
	spirals.getinfo(model=use_model)
				
	import matplotlib.gridspec as gridspec
	
	plt.close('all')
	fig = plt.figure(figsize=(8, 3))

	fig.add_subplot(1,3,1)
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)
		
	fig.add_subplot(1,3,2)
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)

	fig.add_subplot(1,3,3)
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)
	
	fig.suptitle(use_model+'('+use_arm+')')
	fig.tight_layout()
	plt.savefig(figdir_primer+'/single_model_single_arm.png')
	
single_model_all_arms = False
if single_model_all_arms:
		
	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model =  'Drimmel_Ceph_2024' #'Taylor_Cordes_1992'
	use_arm = 'all' 
	spirals.getinfo(model=use_model)
				
	import matplotlib.gridspec as gridspec
	
	plt.close('all')
	fig = plt.figure(figsize=(8, 3))

	fig.add_subplot(1,3,1)
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)
		
	fig.add_subplot(1,3,2)
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)

	fig.add_subplot(1,3,3)
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)
	
	fig.suptitle(use_model+'('+use_arm+')')
	fig.tight_layout()
	plt.savefig(figdir_primer+'/single_model_all_arms.png')
	

single_model_polar_hou = False
if single_model_polar_hou:

	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Hou_Han_2014'
	use_arm = 'all'
	spirals.getinfo(model=use_model)
				
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)

	ax.set_rticks([3., 6.,9.,12,15.,20.])
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)

	plt.title(use_model)
	# ax.set_xlim([np.radians(100),np.radians(260)])
	# ax.set_ylim([0.,8])

	plt.savefig(figdir_primer+'/polar_proj_single_model_single_arm_hc_hou.png')
	
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)

	ax.set_rticks([3., 6.,9.,12,15.,20.])
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)

	plt.title(use_model)
	# ax.set_xlim([np.radians(100),np.radians(260)])
	# ax.set_ylim([0.,8])

	plt.savefig(figdir_primer+'/polar_proj_single_model_single_arm_gc_hou.png')


single_model_polar_drim = False
if single_model_polar_drim:

	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Drimmel_NIR_2000'
	use_arm = 'all'		
	use_model2 = 'GaiaPVP_cont_2022'	
	spirals.getinfo(model=use_model)
				

	# plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polarproj':True}
	# spirals.readout(plotattrs,model=use_model,arm=use_arm)
	# plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'polarproj':True,'armcolour':'red'}	
	# spirals.readout(plotattrs,model=use_model2,arm='all')


	plt.close('all')	
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'polarproj':True,'armcolour':'red'}	
	spirals.readout(plotattrs,model=use_model2,arm='all')

	ax.set_rticks([3., 6.,9.,12,15.,20.])
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)

	plt.title(use_model)


	plt.savefig(figdir_primer+'/polar_proj_single_model_single_arm_hc_drim.png')
	
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)

	ax.set_rticks([3., 6.,9.,12,15.,20.])
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)

	plt.title(use_model)
	# ax.set_xlim([np.radians(100),np.radians(260)])
	# ax.set_ylim([0.,8])

	plt.savefig(figdir_primer+'/polar_proj_single_model_single_arm_gc_drim.png')





check_poggio = True
if check_poggio:

	print('testing gaiaPVP')
	xsun= -8.277
	spirals = sp.main_(xsun=xsun)
	use_model1 = 'Poggio_cont_2021'		
	use_model2 = 'GaiaPVP_cont_2022'	
	use_model3 = 'Drimmel_NIR_2000'	
	use_model4 = 'Levine_2006'	
	use_arm = 'all'
	spirals.getinfo(model=use_model1)
				
	plt.close('all')
	plotattrs = {'plot':True,'coordsys': 'GC','markersize':15,'polargrid':True}	
	spirals.readout(plotattrs,model=use_model1,arm='all')	
	plotattrs = {'plot':True,'coordsys': 'GC','markersize':15,'polargrid':True,'colour_contour':'green'}	
	spirals.readout(plotattrs,model=use_model2,arm='all')	

	plt.savefig(figdir_primer+'/test.png')


	plt.close('all')	
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	# # # plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'polarproj':True,'armcolour':'red'}	
	# # # spirals.readout(plotattrs,model=use_model1,arm=use_arm)
	# # # plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polarproj':True,'armcolour':'blue'}
	# # # spirals.readout(plotattrs,model=use_model2,arm=use_arm)
	
	# # # plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polarproj':True}
	# # # spirals.readout(plotattrs,model=use_model3,arm='1_arm')


	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polarproj':True,'armcolour':'red'}
	spirals.readout(plotattrs,model=use_model2,arm=use_arm)
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'polarproj':True}	
	spirals.readout(plotattrs,model=use_model3,arm='all')

	plt.savefig(figdir_primer+'/testgc.png')

	# # plt.close('all')	
	# # fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	# # plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'polarproj':True,'armcolour':'red'}	
	# # spirals.readout(plotattrs,model=use_model2,arm='all')
	# # spirals.readout(plotattrs,model=use_model3,arm='all')
	

	# # plt.savefig(figdir_primer+'/testhc.png')
	

	
	# # use_model1 = 'Reid_2019'	
	# # use_model2 = 'Drimmel_Ceph_2024'	


	# # plt.close('all')	
	# # fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	# # plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'polarproj':True}	
	# # spirals.readout(plotattrs,model=use_model1,arm='all')
	# # spirals.readout(plotattrs,model=use_model2,arm='all')

	# # plt.savefig(figdir_primer+'/test.png')
	
