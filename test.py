

import imp,SpiralMap, dtools
imp.reload(SpiralMap)
import SpiralMap as sp
import matplotlib.pyplot as plt
import numpy as np
import os
import putil

figdir_primer = 'figdir_primer'
os.system('rm -rf '+figdir_primer); os.system('mkdir '+figdir_primer)
plt.ion()
		


mkpaperfigs = False

if mkpaperfigs:
	
	
	print('plotting figures for primer')
	xsun=-8.277
	# plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'xmin':-10,'xmax':10,'ymin':-10,'ymax':10}
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':False}
	plt.close('all')
	plm=putil.Plm2(2,3,xsize=8.0,ysize=4.5,xmulti=False,ymulti=False,full=True,slabelx=0.7,slabely=0.07)			
	
	
	spirals = sp.main_(xsun=xsun)
	for inum,use_model in enumerate(spirals.models):		

		if use_model != 'Poggio_2021':

			plm.next()
				
			spirals.getinfo(model=use_model)
			spirals.readout(plotattrs,model=use_model,arm='all')
	
	
			spirals.getinfo(model='Poggio_2021')
			spirals.readout(plotattrs,model='Poggio_2021',arm='all')
			dtools.add_polargrid()
	
	
			plt.title(use_model)
	
	plm.tight_layout()
	plt.savefig(figdir_primer+'/spirals_'+plotattrs['coordsys']+'.png')
	
single_ = False

if single_:
		
	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Drimmel_NIR_2000'
	spirals.getinfo(model=use_model)
				
	plt.close('all')
	plm=putil.Plm1(1,2,xsize=8.0,ysize=4,xmulti=False,ymulti=False,full=True,slabelx=0.7,slabely=0.07)			
		

	plm.next()		

	plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm='4_interarm')
	# spirals.readout(plotattrs,model=use_model,arm='all')

	plm.next()		

	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	spirals.readout(plotattrs,model=use_model,arm='all')



	plt.title(use_model)
	
	plm.tight_layout()
	plt.savefig(figdir_primer+'/polar_grid_overplotted.png')
	
polar_test = True

if polar_test:
		
	print('plotting figures for primer')
	xsun=-8.277
	spirals = sp.main_(xsun=xsun)
	use_model = 'Drimmel_NIR_2000'
	spirals.getinfo(model=use_model)
				
	plt.close('all')
	fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))


	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':False,'polargrid':False,'polarproj':True}
	spirals.readout(plotattrs,model=use_model,arm='all')


	ax.set_rticks([3., 6.,9.,12,15.])
	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)

	plt.title(use_model)

	plt.savefig(figdir_primer+'/polar_grid_overplotted.png')
	
	plt.close('all')

	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':False,'polarproj':False}
	spirals.readout(plotattrs,model=use_model,arm='all')

	plt.title(use_model)

	plt.savefig(figdir_primer+'/normal_overplotted.png')
	
	



