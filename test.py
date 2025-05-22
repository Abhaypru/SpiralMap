

from SpiralMap import *
import SpiralMap as sp

import imp,SpiralMap, dtools
imp.reload(SpiralMap)
imp.reload(dtools)
import putil


figdir_primer = 'figdir_primer'
os.system('rm -rf '+figdir_primer); os.system('mkdir '+figdir_primer)
plt.ion()
	

savelims = False
if savelims:		

	print('saving plot limits for all models')
	xsun=-8.277

	mylims = {}
	
	spirals = sp.main_(xsun=xsun)
	for inum,use_model in enumerate(spirals.models):				
		
		plt.close('all')
		plm=putil.Plm2(10,10,xsize=8.0,ysize=4.5,xmulti=False,ymulti=False,full=True,slabelx=0.7,slabely=0.07)			

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


		plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polargrid':False}		
		coordsys = plotattrs['coordsys']
		plm.next()
			
		spirals.getinfo(model=use_model)
		spirals.readout(plotattrs,model=use_model,arm='all')
		mylims[use_model]['xmin'+'_'+coordsys] = spirals.xmin
		mylims[use_model]['xmax'+'_'+coordsys] = spirals.xmax
		mylims[use_model]['ymin'+'_'+coordsys] = spirals.ymin
		mylims[use_model]['ymax'+'_'+coordsys] = spirals.ymax

			

	dtools.picklewrite(mylims,'flim',sp.dataloc)	

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


single_model = False
if single_model:
		
	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Taylor_Cordes_1992' #'Drimmel_NIR_2000'
	use_arm = 'all' #'2_arm'
	spirals.getinfo(model=use_model)
				
	import matplotlib.gridspec as gridspec
	
	plt.close('all')
	fig = plt.figure(figsize=(8, 3))

	fig.add_subplot(1,3,1)
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)
	# spirals.readout(plotattrs,model='Poggio_2021')
	
	fig.add_subplot(1,3,2)
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':False}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)
	# spirals.readout(plotattrs,model='Poggio_2021')

	fig.add_subplot(1,3,3)
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)
	# spirals.readout(plotattrs,model='Poggio_2021')
	
	fig.suptitle(use_model+'('+use_arm+')')
	fig.tight_layout()
	plt.savefig(figdir_primer+'/single_all_arms_demo.png')
	

single_model_polar = False
if single_model_polar:

	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Hou_Han_2014'
	spirals.getinfo(model=use_model)
				
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polarproj':True}
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

check_poggio = False
if check_poggio:

	print('testing gaiaPVP')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model1 = 'Poggio_2021'	
	use_model2 = 'GaiaPVP_Poggio_2022'	
	
	spirals.getinfo(model=use_model1)
				
	plt.close('all')
	plotattrs = {'plot':True,'coordsys': 'GC','markersize':15,'polargrid':True,'colour_contour':'red'}	
	spirals.readout(plotattrs,model=use_model1,arm='all')	
	plotattrs = {'plot':True,'coordsys': 'GC','markersize':15,'polargrid':True,'colour_contour':'green'}	
	spirals.readout(plotattrs,model=use_model2,arm='all')	

	

test_polar_poggio = False
if test_polar_poggio:
	
	
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	
	fl = pickleread(dataloc+'/Poggio_2021/Poggio_2021_pproj_contours.pkl')
	# plt.plot(np.radians(fl['phi4']),fl['rgc'],'.')
	plt.plot(np.radians(fl['glon4']),fl['dhelio'],'.')

	fl = pickleread(dataloc+'/GaiaPVP_Poggio_2022/GaiaPVP_Poggio_2022_pproj_contours.pkl')
	# plt.plot(np.radians(fl['phi4']),fl['rgc'],'.')
	plt.plot(np.radians(fl['glon4']),fl['dhelio'],'.')

checkpolar = False
if checkpolar:

	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model1 = 'Poggio_2021'
	# use_model1 = 'Hou_Han_2014' #'Drimmel_NIR_2000'


	spirals.getinfo(model=use_model1)
				
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	plotattrs = {'plot':True,'coordsys': 'GC','markersize':15,'polarproj':True}	
	spirals.readout(plotattrs,model=use_model1,arm='all')	

	ax.set_rticks([3., 6.,9.,12,15.])
	ax.set_thetagrids(list(np.arange(0.,360.,30)))
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)
	ax.set_ylim([0.,15])
	
	plt.title(use_model1)


	plt.savefig(figdir_primer+'/polar_grid_overplotted1_gc.png')
	# plt.close('all')
	# fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	# plotattrs = {'plot':True,'coordsys': 'GC','armcolour':'red','markersize':15,'polarproj':True}	
	# spirals.readout(plotattrs,model=use_model1,arm='Outer')	

	# ax.set_rticks([3., 6.,9.,12,15.])
	# ax.set_thetagrids(list(np.arange(0.,360.,30)))
	
	# rlabels = ax.get_ymajorticklabels()
	# for label in rlabels:
	    # label.set_color('blue')
	    # label.set_size(fontsize=10)
	# ax.set_ylim([0.,15])
	
	# plt.title(use_model1)


	# plt.savefig(figdir_primer+'/polar_grid_overplotted1_hc.png')
		
	# plt.close('all')
	# fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	# plotattrs = {'plot':True,'coordsys': 'GC','markersize':15,'polarproj':True}	
	# spirals.readout(plotattrs,model=use_model,arm='all')	

	# ax.set_rticks([3., 6.,9.,12,15.])
	# ax.set_thetagrids(list(np.arange(0.,360.,30)))
	
	# rlabels = ax.get_ymajorticklabels()
	# for label in rlabels:
	    # label.set_color('blue')
	    # label.set_size(fontsize=10)

	# plt.title(use_model)
	# # ax.set_xlim([np.radians(100),np.radians(260)])
	# ax.set_ylim([0.,15])

	# plt.savefig(figdir_primer+'/polar_grid_overplotted1.png')

	# plt.close('all') 	
	# fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	# plotattrs = {'plot':True,'coordsys': 'GC','markersize':15,'polarproj':True}	
	# spirals.readout(plotattrs,model=use_model,arm='2_arm')	

	# ax.set_rticks([3., 6.,9.,12,15.])
	# ax.set_thetagrids(list(np.arange(0.,360.,30)))
	
	# rlabels = ax.get_ymajorticklabels()
	# for label in rlabels:
	    # label.set_color('blue')
	    # label.set_size(fontsize=10)

	# plt.title(use_model)
	# ax.set_ylim([0.,15])

	# plt.savefig(figdir_primer+'/polar_grid_overplotted2_gc.png')
	
	# plt.close('all') 	
	# # fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	# plotattrs = {'plot':True,'coordsys': 'HC','markersize':15,'polarproj':False}	
	# spirals.readout(plotattrs,model=use_model,arm='2_arm')	


	# plt.title(use_model)
	
	# plt.savefig(figdir_primer+'/polar_grid_overplotted2_hc.png')







