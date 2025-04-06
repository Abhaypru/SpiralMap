

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
	
single_ = True

if single_:
		
	print('plotting figures for primer')
	xsun=-8.277
	# plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'xmin':-10,'xmax':10,'ymin':-10,'ymax':10}
	plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':True}
	plt.close('all')
	plm=putil.Plm1(1,1,xsize=8.0,ysize=8,xmulti=False,ymulti=False,full=True,slabelx=0.7,slabely=0.07)			
	
	
	spirals = sp.main_(xsun=xsun)

	use_model = 'Drimmel_ceph_2024'		

	plm.next()
		
	spirals.getinfo(model=use_model)
	spirals.readout(plotattrs,model=use_model,arm='all')

	if plotattrs['polargrid']:
		dtools.add_polargrid(xsun=xsun,typ='gc')#xmin=spirals.xmin,xmax=spirals.xmax,ymin=spirals.ymin,ymax=spirals.ymax)


	plt.title(use_model)
	
	plm.tight_layout()
	plt.savefig(figdir_primer+'/test.png')
	
	




