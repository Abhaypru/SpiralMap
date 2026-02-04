#####################
# testing the scripts here...




from models_ import *
import models_ as sp
import matplotlib  as mpl
Rsun= 8.277

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


impl_vallee_ = False
if impl_vallee_ :


	# spirals = sp.main_(Rsun=Rsun)
	# spirals.getinfo()
	# spirals.getinfo(model='Vallee_1995')
	# spirals.plotattrs_default


	#################
	
	spirals = sp.main_(Rsun=Rsun)	
	use_model = 'Vallee_1995'
	spirals.getinfo(model=use_model)
	plotattrs = {'plot':True,'coordsys':'GC'}
	spirals.readout(plotattrs,model=use_model,arm='all')	

	plt.savefig(figdir_primer+'/test_vallee_gc.png')	


	plt.close('all')
	plotattrs = {'plot':True,'coordsys':'HC'}
	spirals.readout(plotattrs,model=use_model,arm='all')	

	plt.savefig(figdir_primer+'/test_vallee_hc.png')	
		
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
	# use_model =  'Drimmel_Ceph_2024' 
	use_model =  'Vallee_1995' 
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

multiple_models_cartesian = False
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
	plotattrs = {'plot':True,'coordsys':'HC','markersize':2}	
	spirals.readout(plotattrs,model=use_model2,arm='all')	
	
	#	
	ax = plt.subplot(222)
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)	
	plotattrs = {'plot':True,'coordsys':'GC','markersize':2}	
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
	plotattrs = {'plot':True,'coordsys':'HC','markersize':1}	
	spirals.readout(plotattrs,model=use_model2,arm='all')
	

	#	
	ax = plt.subplot(224)		
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)	
	plotattrs = {'plot':True,'coordsys':'GC','markersize':1}	
	spirals.readout(plotattrs,model=use_model2,arm='all')
	plt.tight_layout()

	plt.savefig(figdir_primer+'/multiple_models_cartesian.png')


single_model_polar_hou = False
if single_model_polar_hou:

	Rsun=8.277
	spirals = sp.main_(Rsun=Rsun)
	use_model = 'Hou_Han_2014'
	use_arm = 'Arm2'
		
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
	plotattrs = {'plot':True,'coordsys':'HC','markersize':3,'polarproj':True}	
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


hou_han_test = False
if hou_han_test:

	Rsun=8.277
	spirals = sp.main_(Rsun=Rsun)
	use_model = 'Hou_Han_2014'
	use_model3 = 'Hou_Han_2014'
	use_arm = 'all'
	use_model2 = 'Poggio_cont_2021'

		
	spirals.getinfo(model=use_model)				
	
	plt.close('all')
	
	fig = plt.figure(figsize=(10,10.))
	
	ax = plt.subplot(121, projection='polar')		

	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polarproj':True,'linewidth':5}
	spirals.readout(plotattrs,model=use_model,arm=use_arm)	
	plotattrs = {'plot':True,'coordsys':'HC','markersize':3,'polarproj':True}	
	spirals.readout(plotattrs,model=use_model2,arm='all')	
	polar_style(ax,title=use_model+' (HC)')
	
	ax = plt.subplot(122, projection='polar')		

	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polarproj':True,'linewidth':5}
	spirals.readout(plotattrs,model=use_model3,arm=use_arm)	
	plotattrs = {'plot':True,'coordsys':'GC','markersize':3,'polarproj':True}	
	spirals.readout(plotattrs,model=use_model2,arm='all')	
	polar_style(ax,title=use_model3+' (GC)')
	
	
	plt.tight_layout()

	plt.savefig(figdir_primer+'/test_houhan.png')

makegif = True
if makegif:

	plt.close('all')

	Rsun=8.277
	spirals = sp.main_(Rsun=Rsun)
	use_model2 = 'Poggio_cont_2021' 
	use_arm = 'all'
		
	
	for inum, use_model in enumerate(spirals.models):
		
		if 'cont' not in use_model:

			plt.close('all')
			
			fig = plt.figure(figsize=(5,5.))
			
			ax = plt.subplot(111, projection='polar')
			plotattrs = {'plot':True,'coordsys':'GC','linewidth':5,'markersize':15,'markSunGC':True,'polarproj':True}
			spirals.readout(plotattrs,model=use_model,arm=use_arm)	
			plotattrs = {'plot':True,'coordsys':'GC','markersize':3,'polarproj':True}
			spirals.readout(plotattrs,model=use_model2,arm=use_arm)	
			polar_style(ax,title=use_model+' (GC)')
			ax.set_ylim([0.,15])	
			plt.legend()
			plt.savefig(figdir_primer+'/map_'+str(inum)+'png')

	import mytools
	curdir = os.getcwd()
	mytools.png2movie(figdir_primer,curdir,flname='movie_',duration=3.5,fmt='gif')
	
		

templot = False
if templot:

	# grab data	(poggio and ceph)
	plotattrs = {'plot':False,'coordsys':'GC','markersize':3,'polarproj':True,'armcolour':''}
	pg = spiral_poggio_maps()
	pg.xsun = 8.277
	pg.output_(plotattrs)	
	xvalues = pg.dout['xhc']
	yvalues = pg.dout['yhc']
	overdens_grid = pg.over_dens_grid
	

	plotattrs = {'plot':True,'coordsys':'HC','markersize':5,'linewidth':4,'linestyle':'-','polargrid':False}
	Rsun=8.277
	spirals = sp.main_(Rsun=Rsun)
	use_model2 = 'Drimmel_Ceph_2024' 
	use_arm = 'all'	
	
	plt.close('all')
	
	fgsize=(6.5,5.)
	fig = plt.figure(figsize=fgsize, dpi=150)
	
	ax = fig.gca()
	
	iniz=-1.18
	fin=1.18
	N_levels=50
	levels=np.linspace(iniz,fin,N_levels)
	cset1 = ax.contourf(xvalues, yvalues,overdens_grid.T, levels=levels, cmap='seismic',vmin=-1.18,vmax=1.18)
	
	cbar=plt.colorbar(mappable=cset1,orientation="vertical",ticks=[-1,-0.5, 0,  0.5, 1])
	
	cbar.set_label('Overdensity', fontsize=18)
	cbar.ax.tick_params(labelsize=18) 

	spirals.readout(plotattrs,model=use_model2,arm=use_arm)	
	
	ax.set_xlabel('X (kpc)', fontsize=18)
	ax.set_ylabel('Y (kpc)', fontsize=18)
	
	ax.set_xlim([-5.5,5.1])
	ax.set_ylim([-5.8,5.5])
	ax.tick_params(axis="x", labelsize=15)
	ax.tick_params(axis="y", labelsize=15)
	plt.tight_layout()
	
	# # plt.show()	
	
	
	
	
	

