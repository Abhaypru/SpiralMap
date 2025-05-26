

from SpiralMap import *
import SpiralMap as sp
import matplotlib  as mpl
Rsun= 8.277

# import imp,SpiralMap, dtools
# # imp.reload(SpiralMap)
# imp.reload(dtools)
# import putil


figdir_primer = 'figdir_primer'
os.system('rm -rf '+figdir_primer); os.system('mkdir '+figdir_primer)
plt.ion()
	


params = {'font.size':12,
		  'text.usetex':False,
		  'ytick.labelsize': 'medium',
		  'legend.fontsize': 'large',
		  'axes.linewidth': 1.0,
		  'xtick.labelsize': 'medium',
		  'font.family': 'sans-serif',
		  'axes.labelsize': 'medium'}
mpl.rcParams.update(params)

#------------------------------------------------------------	
############## figures/code for documentation ####################

initialise_ = False
if initialise_:
	
	spirals = sp.main_(Rsun=Rsun)
	spirals.getinfo()
	spirals.getinfo(model='Drimmel_Ceph_2024')
	spirals.plotattrs_default


	#################
	
	spirals = sp.main_(Rsun=Rsun)	
	use_model = 'Drimmel_Ceph_2024'
	spirals.getinfo(model=use_model)
	plotattrs = {'plot':False}
	spirals.readout(plotattrs,model=use_model,arm='Sag-Car')
	

single_model_single_arm = False
if single_model_single_arm:

	Rsun=8.277
	spirals = sp.main_(Rsun=Rsun)
	use_model =  'Drimmel_Ceph_2024' 
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
		
	Rsun=8.277
	spirals = sp.main_(Rsun=Rsun)
	use_model =  'Drimmel_Ceph_2024' 
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


multiple_models_cartesian = True
if multiple_models_cartesian:

	Rsun=8.277
	spirals = sp.main_(Rsun=Rsun)
	use_model = 'Taylor_Cordes_1992'
	use_arm = 'all'
	use_model2 = 'Poggio_cont_2021'
		
	spirals.getinfo(model=use_model)				
	
	plt.close('all')	
	fig = plt.figure(figsize=(7.,6.))	
	ax = plt.subplot(221)
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)	
	plotattrs = {'plot':True,'coordsys':'HC','markersize':3,'armcolour':'red'}	
	spirals.readout(plotattrs,model=use_model2,arm='all')	
	
	#	
	ax = plt.subplot(222)
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)	
	plotattrs = {'plot':True,'coordsys':'GC','markersize':3,'armcolour':'red'}	
	spirals.readout(plotattrs,model=use_model2,arm='all')
	
	# 
	spirals = sp.main_(Rsun=Rsun)
	use_model = 'Drimmel_NIR_2000'
	use_arm = 'all'
	use_model2 = 'Poggio_cont_2021' 	
	spirals.getinfo(model=use_model)						
	ax = plt.subplot(223)
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)	
	plotattrs = {'plot':True,'coordsys':'HC','markersize':3,'armcolour':'grey'}	
	spirals.readout(plotattrs,model=use_model2,arm='all')
	

	#	
	ax = plt.subplot(224)		
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)	
	plotattrs = {'plot':True,'coordsys':'GC','markersize':3,'armcolour':'grey'}	
	spirals.readout(plotattrs,model=use_model2,arm='all')
	plt.tight_layout()

	# plt.savefig(figdir_primer+'/multiple_models_cartesian.png')


	

single_model_polar_hou = False
if single_model_polar_hou:

	Rsun=8.277
	spirals = sp.main_(Rsun=Rsun)
	use_model = 'Hou_Han_2014'
	use_arm = 'Sagittarius-Carina'
		
	spirals.getinfo(model=use_model)				
	
	plt.close('all')
	
	fig = plt.figure(figsize=(7,7.))
	
	ax = plt.subplot(221, projection='polar')
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)	
	polar_style(ax,title=use_model+' (HC)')
		
	ax = plt.subplot(222, projection='polar')
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)
	polar_style(ax,title='(GC)')
	
	ax = plt.subplot(223, projection='polar')
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm='all')
	polar_style(ax,title='(HC)')

	ax = plt.subplot(224, projection='polar')
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm='all')
	polar_style(ax,title='(GC)')
	
	plt.tight_layout()

	plt.savefig(figdir_primer+'/polar_proj_single_model.png')


multiple_models_polar = False
if multiple_models_polar:

	Rsun=8.277
	spirals = sp.main_(Rsun=Rsun)
	use_model = 'Taylor_Cordes_1992'
	use_arm = 'all'
	use_model2 = 'Poggio_cont_2021'
		
	spirals.getinfo(model=use_model)				
	
	plt.close('all')	
	fig = plt.figure(figsize=(7.,6.))	
	# 
	ax = plt.subplot(221, projection='polar')
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)	
	plotattrs = {'plot':True,'coordsys':'HC','markersize':3,'polarproj':True,'armcolour':'red'}	
	spirals.readout(plotattrs,model=use_model2,arm='all')	
	polar_style(ax,title=use_model+' (HC)')
	ax.set_ylim([0.,8])	
	
	#	
	ax = plt.subplot(222, projection='polar')
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)	
	plotattrs = {'plot':True,'coordsys':'GC','markersize':3,'polarproj':True,'armcolour':'red'}	
	spirals.readout(plotattrs,model=use_model2,arm='all')
	polar_style(ax,title='(GC)')
	ax.set_ylim([4.,12])	

	# 
	spirals = sp.main_(Rsun=Rsun)
	use_model = 'Drimmel_NIR_2000'
	use_arm = 'all'
	use_model2 = 'Poggio_cont_2021' 	
	spirals.getinfo(model=use_model)						
	ax = plt.subplot(223, projection='polar')
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)	
	plotattrs = {'plot':True,'coordsys':'HC','markersize':3,'polarproj':True,'armcolour':'grey'}	
	spirals.readout(plotattrs,model=use_model2,arm='all')
	
	polar_style(ax,title=use_model+' (HC)')
	ax.set_ylim([0.,8])

	#		
	ax = plt.subplot(224, projection='polar')
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)	
	plotattrs = {'plot':True,'coordsys':'GC','markersize':3,'polarproj':True,'armcolour':'grey'}	
	spirals.readout(plotattrs,model=use_model2,arm='all')
	polar_style(ax,title='(GC)')
	ax.set_ylim([4.,12])	
	plt.tight_layout()

	plt.savefig(figdir_primer+'/polar_proj_multiple_models2.png')



check_poggio = False
if check_poggio:

	print('testing gaiaPVP')
	Rsun= 8.277
	spirals = sp.main_(Rsun=Rsun)
	use_model1 = 'Poggio_cont_2021'		
	use_model2 = 'GaiaPVP_cont_2022'	
	use_model3 = 'Drimmel_NIR_2000'	
	use_model4 = 'Levine_2006'	
	use_arm = 'all'
	spirals.getinfo(model=use_model1)
				

	plt.close('all')	
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))

	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'polarproj':True}	
	spirals.readout(plotattrs,model=use_model1,arm='all')

	plt.savefig(figdir_primer+'/testgc.png')




single_model_polar_drim = False
if single_model_polar_drim:


	print('plotting figures for primer')
	Rsun=8.277
	spirals = sp.main_(Rsun=Rsun)
	use_model = 'Drimmel_NIR_2000'
	use_arm = 'all'
	use_model2 = 'Poggio_cont_2021'		
	use_model2 = 'GaiaPVP_cont_2022'		
	spirals.getinfo(model=use_model)
				
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	
	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)

	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polarproj':True} #,'armcolour':'red'}
	spirals.readout(plotattrs,model=use_model2,arm=use_arm)
	
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)

	plt.title(use_model)
	ax.grid(linewidth=1.5)	
	ax.yaxis.grid(linewidth=1.5)	
	# ax.set_xlim([np.radians(100),np.radians(260)])
	# ax.set_ylim([0.,8])

	plt.savefig(figdir_primer+'/polar_proj_single_model_single_arm_hc_hou.png')
	
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
	
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)

	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polarproj':True} #,'armcolour':'red'}
	spirals.readout(plotattrs,model=use_model2,arm=use_arm)

	ax.set_rticks([3., 6.,9.,12,15.,20.])
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)

	plt.title(use_model)
	ax.yaxis.grid(linewidth=1.5)		




	plt.savefig(figdir_primer+'/polar_proj_single_model_single_arm_gc_drim.png')

