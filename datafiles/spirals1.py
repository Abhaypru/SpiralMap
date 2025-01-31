

class reid_spiral(object):


	def __init__(self,kcor=False):
		print('')
		
		self.kcor = kcor
		self.getarmlist()
	
	def getarmlist(self):
		
		# self.arms = np.array(['3-kpc','Norma','Sct-Cen','Sgt-Car','Local','Perseus','Outer'])
		self.arms = np.array(['3-kpc','Norma','Sct-Cen','Sgr-Car','Local','Perseus','Outer'])
		
	def getparams(self,arm):
		
		if arm == '3-kpc':
			params = {'name':arm,'beta_kink':15,'pitch_low':-4.2,'pitch_high':-4.2,'R_kink':3.52,'beta_min':15,'beta_max':18,'width':0.18}
		if arm == 'Norma':
			params = {'name':arm,'beta_kink':18,'pitch_low':-1.,'pitch_high':19.5,'R_kink':4.46,'beta_min':5,'beta_max':54,'width':0.14}
		if arm == 'Sct-Cen':
			params = {'name':arm,'beta_kink':23,'pitch_low':14.1,'pitch_high':12.1,'R_kink':4.91,'beta_min':0,'beta_max':104,'width':0.23}
		if arm == 'Sgr-Car': #'Sgr-Car'
			params = {'name':arm,'beta_kink':24,'pitch_low':17.1,'pitch_high':1,'R_kink':6.04,'beta_min':2,'beta_max':97,'width':0.27}
		if arm == 'Local':
			params = {'name':arm,'beta_kink':9,'pitch_low':11.4,'pitch_high':11.4,'R_kink':8.26,'beta_min':-8,'beta_max':34,'width':0.31}
		if arm == 'Perseus':
			params = {'name':arm,'beta_kink':40,'pitch_low':10.3,'pitch_high':8.7,'R_kink':8.87,'beta_min':-23,'beta_max':115,'width':0.35}
		if arm == 'Outer':
			params = {'name':arm,'beta_kink':18,'pitch_low':3,'pitch_high':9.4,'R_kink':12.24,'beta_min':-16,'beta_max':71,'width':0.65}
		
		
		if self.kcor:
			Rreid = 8.15
			diffval = params['R_kink'] - Rreid
			xsun = get_lsr()['xsun']
			if diffval < 0:
				 params['R_kink'] = (-xsun) + diffval
			else:
				 params['R_kink'] = (-xsun) + diffval
					
		
		return params


	def model_(self,params):
		'''
		X and Y are flipped in Reid et al. 2019
		I flip it back to sensible orientation here
		
		'''
		
		beta_kink = np.radians(params['beta_kink'])
		pitch_low = np.radians(params['pitch_low'])
		pitch_high = np.radians(params['pitch_high'])
		R_kink = params['R_kink']
		beta_min = params['beta_min']
		beta_max = params['beta_max']
		width = params['width']
		
		
		# beta = np.linspace(beta_min-180,beta_max,100)
		beta = np.linspace(beta_min,beta_max,1000)


		beta_min = np.radians(beta_min)
		beta_max = np.radians(beta_max)
		beta = np.radians(beta)	
		
		
		pitch = np.zeros(beta.size) + np.nan
		indl = np.where(beta<beta_kink)[0]; pitch[indl] = pitch_low
		indr = np.where(beta>beta_kink)[0]; pitch[indr] = pitch_high
		
		tmp1 = (beta - beta_kink)*(np.tan(pitch))
		tmp2 = np.exp(-tmp1)
				
		R = R_kink*tmp2
		x = -R*(np.cos(beta))
		y = R*(np.sin(beta))

		##3 testing 
		R2 = (R_kink+(width*0.5))*tmp2
		x2 = -R2*(np.cos(beta))
		y2 = R2*(np.sin(beta))

		R1 = (R_kink-(width*0.5))*tmp2
		x1 = -R1*(np.cos(beta))
		y1 = R1*(np.sin(beta))
		
		
		
		return x,y, x1,y1,x2,y2
		
	def plot_(self,arm,color='',typ_='HC',xsun_=[],linewidth=0.8,markersize=3,linestyle = '-'):	
		
		if len(xsun_) == 0:
			xsun = get_lsr()['xsun']
		else:
			xsun = xsun_[0]
		
		
		params = self.getparams(arm) ;
		x,y, x1,y1,x2,y2 = self.model_(params);
		if color == '':
			color = 'black'
			
		if typ_ == 'GC':	
			plt.plot(x,y,color,label=params['name'],linestyle='--',linewidth=linewidth)
			plt.plot(x2,y2,color,linestyle='dotted',linewidth=linewidth)
			plt.plot(x1,y1,color,linestyle='dotted',linewidth=linewidth)
			plt.axvline(xsun,linewidth=1,linestyle='--')			
			plt.axhline(0,linewidth=1,linestyle='--')			
			# plt.xlabel('X$_{GC}$')
			# plt.ylabel('Y$_{GC}$')
			plt.plot(0.,0.,marker='+',markersize=10,color='black')
			plt.plot(xsun,0.,marker='o',markersize=10,color='black')
		if typ_ == 'HC':	
			print('..')
			print('using linewidth = '+str(linewidth))
			print('..')
			xhc = x - xsun
			xhc1 = x1 - xsun
			xhc2 = x2 - xsun
			plt.plot(xhc,y,color,label=params['name'],linestyle='-',linewidth=linewidth)
			plt.plot(xhc1,y,color,linestyle='dotted',linewidth=linewidth)
			plt.plot(xhc2,y,color,linestyle='dotted',linewidth=linewidth)
			plt.plot(0.,0.,marker='o',markersize=markersize,color='black')
			plt.plot(-xsun,0.,marker='+',markersize=markersize,color='black')		
			# plt.xlabel('X$_{HC}$')
			# plt.ylabel('Y$_{HC}$')			
			# plt.xlabel('X [kpc]')
			# plt.ylabel('Y [kpc]')			
		
		# plt.legend() 
		
		if typ_ =='polar':
			
			xhc = x - xsun
			xhc1 = x1 - xsun
			xhc2 = x2 - xsun
			
			rgc = sqrtsum(ds=[x,y])
			phi1 = np.arctan2(y,-x)
			phi2 = np.degrees(np.arctan(y/-x))
			phi3 = np.degrees(np.arctan2(y,x))%180.	
			
			# phi3 = 180.-np.degrees(phi1)
			
			# phi1 = (np.arctan2(yhc,xgc))	
			# plt.plot(phi1,rgc,color,linestyle='-',linewidth=linewidth)
			plt.plot(phi1,rgc,'.',color=color,markersize=markersize)
			
			
		if typ_ =='polargrid':
			
			linewidth=2
			
			yhc = y
			xgc = x
			phi4 = np.degrees(np.arctan2(yhc,xgc))%360.	
			rgc = sqrtsum(ds=[x,y])

			plt.plot(np.radians(phi4),rgc,color=color,markersize=markersize,linestyle=linestyle,linewidth=linewidth,label=arm)

	

			
		return 


def spiral_eloisa():

	'''
	plot contours of OB star spirals from Poggio 2021	
	'''	

	pdocdir = getdirec('pdocdir')
	dloc = pdocdir+'/science_verification/DR3/data'
	# #read overdensity contours
	xvalues_overdens=np.load(dloc+'/Eloisa_contours/xvalues_dens.npy')
	yvalues_overdens=np.load(dloc+'/Eloisa_contours/yvalues_dens.npy')
	over_dens_grid=np.load(dloc+'/Eloisa_contours/over_dens_grid_threshold_0_003_dens.npy')
	
	phi1_dens = np.arctan2(yvalues_overdens,-xvalues_overdens)
	Rvalues_dens = sqrtsum(ds=[xvalues_overdens,yvalues_overdens])
	
	# # #------------------ overplot spiral arms in overdens ------------------
	iniz_overdens=0 #.1
	fin_overdens=1.5 #.1
	N_levels_overdens=2
	levels_overdens=np.linspace(iniz_overdens,fin_overdens,N_levels_overdens)
	cset1 = plt.contourf(xvalues_overdens, yvalues_overdens,over_dens_grid.T, levels=levels_overdens,alpha=0.2,cmap='Greys')
	# cset1 = plt.contourf(phi1_dens, Rvalues_dens,over_dens_grid.T, levels=levels_overdens,alpha=0.2,cmap='Greys')
	
	iniz_overdens=0. #.1
	fin_overdens=1.5 #.1
	N_levels_overdens=4#7
	levels_overdens=np.linspace(iniz_overdens,fin_overdens,N_levels_overdens)
	cset1 = plt.contour(xvalues_overdens, yvalues_overdens,over_dens_grid.T, levels=levels_overdens,colors='black',linewidths=0.7)	
	# cset1 = plt.contour(phi1_dens, Rvalues_dens,over_dens_grid.T, levels=levels_overdens,colors='black',linewidths=0.7)	
	
	


class spiral_drimmel(object):
	'''
	
	February 22, 2022
	
	Usage: 
	spi = spiral_drimmel()
	spi.plot_(arm='1',color='b',typ_='HC')
	spi.plot_(arm='2',color='b',typ_='HC')
	spi.plot_(arm='all',color='b',typ_='HC')
	
	'''

	def __init__(self):
		
		
		# self.loc = '/net/huygens/data/users/khanna/Documents/pdoc_work/science_verification/DR3/data/Drimmel_spiral'
		self.loc = getdirec('pdocdir')+'/science_verification/DR3/data/Drimmel_spiral'
		self.fname = 'Drimmel2armspiral.fits'
		self.xsun = get_lsr()['xsun']
		self.getdata(xsun_=[self.xsun])

	def getdata(self,xsun_=[]):
		'''
		
		'''

		dt = tabpy.read(self.loc+'/'+self.fname)
		self.data0 = dt.copy()
		if len(xsun_) == 0:
			xsun = self.xsun
		else:
			xsun = xsun_[0]	
		# rescaling to |xsun|
		qnts = ['rgc1','xhc1','yhc1','rgc2','xhc2','yhc2']
		for qnt in qnts:
			dt[qnt] = dt[qnt]*abs(xsun)		
		
		
		
		#----- add phase-shifted arms as `3` and `4`
		
	
	
		dloc = self.loc+'/phase_shifted'
		for inum in [3,4]:
			dt['xhc'+str(inum)] = np.load(dloc+'/Arm'+str(inum)+'_X_hel.npy')
			dt['yhc'+str(inum)] = np.load(dloc+'/Arm'+str(inum)+'_Y_hel.npy')
			dt['rgc'+str(inum)] = np.sqrt( ((dt['xhc'+str(inum)] + xsun)**2.) + ((dt['yhc'+str(inum)])**2.) )
		
		
		#------------------
		
		
		
		self.data = dt.copy()

		return 
		
	def plot_(self,color='',typ_='HC',xsun_=[],linewidth=0.8,arm='all',markersize=3):	

		if len(xsun_) == 0:
			xsun = get_lsr()['xsun']
		else:
			xsun = xsun_[0]

		self.getdata(xsun_=[xsun])
		dt = self.data.copy()
		# print(list(dt.keys()))
		
		if color == '':
			color = 'black'
					
		numbs = [arm]
		if arm == 'all':
			numbs = ['1','2','4']
			# numbs = ['2','3','4']
		elif arm == 'main':
			numbs = ['1','2']
			# numbs = ['1','4']

		
		
		self.dused = {}
		self.dused['rgc'] = []
		self.dused['xgc'] = []
		self.dused['yhc'] = []
		self.dused['phi1'] = []
		self.dused['phi4'] = []
		
		
		for numb in numbs:
			
			linestyle = '-'
			if float(numb) > 2:
				linestyle = '--'
			
			xhc = dt['xhc'+numb]
			yhc = dt['yhc'+numb]
			rgc = dt['rgc'+numb]
			
			xgc = xhc + xsun
			
			if typ_ == 'HC':	
				
				
				# plt.plot(xhc,yhc,color,label=arm,linestyle=linestyle,linewidth=linewidth,markersize=2)
				plt.plot(xhc,yhc,color,linestyle=linestyle,linewidth=linewidth,markersize=2)
				plt.plot(0.,0.,marker='o',markersize=markersize,color='black')
				plt.plot(-xsun,0.,marker='+',markersize=markersize,color='black')

				# plt.xlabel('X$_{HC}$')
				# plt.ylabel('Y$_{HC}$')			


			
			if typ_ == 'GC':	
				
				# plt.plot(xgc,yhc,color,label=arm,linestyle=linestyle,linewidth=linewidth)
				plt.plot(xgc,yhc,color,linestyle=linestyle,linewidth=linewidth)
				plt.axvline(xsun,linewidth=1,linestyle='--')			
				plt.axhline(0,linewidth=1,linestyle='--')			
				# plt.xlabel('X$_{GC}$')
				# plt.ylabel('Y$_{GC}$')
				plt.plot(0.,0.,marker='+',markersize=10,color='black')
				plt.plot(xsun,0.,marker='o',markersize=10,color='black')
				self.dused['xgc'].append(xgc)
				self.dused['yhc'].append(yhc)
		

			if typ_ =='polar':
				

				phi1 = np.arctan2(yhc,-xgc)
				
				phi2 = np.degrees(np.arctan(yhc/-xgc))
				phi3 = np.degrees(np.arctan2(yhc,xgc))%180.	
				phi4 = np.degrees(np.arctan2(yhc,xgc))%360.	
				
				# phi3 = 180.-np.degrees(phi1)
				
				# phi1 = (np.arctan2(yhc,xgc))	
				# plt.plot(np.degrees(phi1),rgc,color,linestyle='--',linewidth=linewidth)
				# plt.plot(np.degrees(phi1),rgc,'.',color='blue')
				plt.plot(phi1,rgc,color=color,markersize=markersize,linestyle=linestyle,linewidth=linewidth)

				self.dused['rgc'].append(rgc)
				self.dused['xgc'].append(xgc)
				self.dused['yhc'].append(yhc)
				self.dused['phi1'].append(phi1)
				self.dused['phi4'].append(phi4)
				
				
			if typ_ =='polargrid':
				

				phi1 = np.arctan2(yhc,-xgc)
				
				phi2 = np.degrees(np.arctan(yhc/-xgc))
				phi3 = np.degrees(np.arctan2(yhc,xgc))%180.	
				phi4 = np.degrees(np.arctan2(yhc,xgc))%360.	
				
				# phi3 = 180.-np.degrees(phi1)


				if numb == numbs[0]:
					plt.plot(np.radians(phi4),rgc,color=color,markersize=markersize,linestyle=linestyle,linewidth=linewidth,label='NIR')

				else:
					plt.plot(np.radians(phi4),rgc,color=color,markersize=markersize,linestyle=linestyle,linewidth=linewidth)
					



				self.dused['rgc'].append(rgc)
				self.dused['xgc'].append(xgc)
				self.dused['yhc'].append(yhc)
				self.dused['phi1'].append(phi1)
				self.dused['phi4'].append(phi4)
				
				
				# plt.plot(xgc,yhc,'.',color=color)
		
		# plt.legend() 
		return 

	

class spiral_cepheids(object):
	'''
	
	June 28, 2024
	
	Usage: 
	spi = spiral_drimmel()
	spi.plot_(arm='1',color='b',typ_='HC')
	spi.plot_(arm='2',color='b',typ_='HC')
	spi.plot_(arm='all',color='b',typ_='HC')
	
	'''

	def __init__(self):
	
		
		# where the data is
		
		self.pdocdir = getdirec('pdocdir')		
		self.cephloc = self.pdocdir+'/science/dr3/data/cepheids'	
		self.spiral_loc = self.cephloc+'/spiral_model'
			
		
		self.fname = 'ArmAttributes_dyoungW1_bw025.pkl'

		self.spirals = pickleread(self.spiral_loc+'/'+self.fname)
	
		self.armlist = list(self.spirals['0']['arm_attributes'].keys())
		
		self.xsun = get_lsr()['xsun'] 
		self.rsun = get_lsr()['Rsun'] 

		
	def plotit_(self,armplt='',typ_='GC',markersize=4,linewidth=2,linestyle2='--'):
		
		from time import sleep
		from scipy.signal import find_peaks
		import numpy as np
		import astropy
		import astropy.table as tb
		import pandas as pd
		import os
		import matplotlib as mpl
		import matplotlib.pyplot as plt
		import imp 
		import dtools
		import autil 
		import tabpy
		params = {'font.size':12,
		      'text.usetex':False,
		      'ytick.labelsize': 'medium',
		      'legend.fontsize': 'large',
		      'axes.linewidth': 1.0,
		      'figure.dpi': 150.0,
		      'xtick.labelsize': 'medium',
		      'font.family': 'sans-serif',
		      'axes.labelsize': 'medium'}
		mpl.rcParams.update(params)
		
		imp.reload(dtools)
		

		
		spirals = self.spirals
		
		# arms and plotting colors for the arms
		colors = ['C3','C0','C1','C2']
		arms = np.array(['Scutum','Sag-Car','Orion','Perseus'])
		
		figtyp = 'png'
		
		# XY positions
		rsun = self.rsun  # Might want to put these in a configuration file
		xsun = self.xsun  # Might want to put these in a configuration file
		lnrsun = np.log(rsun) 
		
		
		# best phi range:
		phi_range = np.deg2rad(np.sort(spirals['1']['phi_range'].copy()))
		maxphi_range = np.deg2rad([60,-120]) 
		
		
		# arms and plotting colors for the arms
		colors = ['C3','C0','C1','C2']
		arms = np.array(self.armlist)
		
		arm_clr = {'Scutum':'C3','Sag-Car':'C0','Orion':'C1','Perseus':'C2'}
		self.arm_clr = arm_clr
		
		dt = {}
		
		
		for armi in np.arange(arms.size):
			
			arm = arms[armi]
			pang = (spirals['1']['arm_attributes'][arm]['arm_pang_strength']+spirals['1']['arm_attributes'][arm]['arm_pang_prom'])/2.
			lnr0 = (spirals['1']['arm_attributes'][arm]['arm_lgr0_strength']+spirals['1']['arm_attributes'][arm]['arm_lgr0_prom'])/2.
			
						
			
			# plot the arms
			
			
			phi=(np.arange(51)/50.)*np.diff(phi_range)[0] + phi_range[0]  
			lgrarm = lnr0 - np.tan(np.deg2rad(pang))*phi 
			
			
			xgc = -np.exp(lgrarm)*np.cos(phi); xhc = xgc - xsun
			ygc = np.exp(lgrarm)*np.sin(phi) ;  yhc = ygc
			
							
			# extrapolate the arms
			phi=(np.arange(101)/100.)*np.diff(maxphi_range)[0] + maxphi_range[0]  
			lgrarm = lnr0 - np.tan(np.deg2rad(pang))*phi 
			
			xgc_ex = -np.exp(lgrarm)*np.cos(phi);  xhc_ex = xgc_ex - xsun
			ygc_ex = np.exp(lgrarm)*np.sin(phi); yhc_ex = ygc_ex
			lonarm = np.arctan((np.exp(lgrarm)*np.sin(phi))/(rsun - np.exp(lgrarm)*np.cos(phi))) 
			
			dt[arm] = {}
			dt[arm]['xgc'] = xgc
			dt[arm]['xhc'] = xhc
			dt[arm]['ygc'] = ygc
			dt[arm]['yhc'] = yhc
						
			dt[arm]['xgc_ex'] = xgc_ex
			dt[arm]['xhc_ex'] = xhc_ex
			dt[arm]['ygc_ex'] = ygc_ex
			dt[arm]['yhc_ex'] = yhc_ex
						


		self.dused = {}
		self.dused['rgc'] = []
		self.dused['xgc'] = []
		self.dused['yhc'] = []
		self.dused['phi1'] = []
		self.dused['phi4'] = []
		


		# for armi in dt.keys():
		for armi in armplt:
			# print(armplt)
						
			xgc = dt[armi]['xgc']
			ygc = dt[armi]['ygc']
			xhc = dt[armi]['xhc']
			yhc = dt[armi]['yhc']
			
			xgc_ex = dt[armi]['xgc_ex']
			ygc_ex = dt[armi]['ygc_ex']
			xhc_ex = dt[armi]['xhc_ex']
			yhc_ex = dt[armi]['yhc_ex']			


			rgc = np.sqrt(xgc**2. + ygc**2.)
			rgc_ex = np.sqrt(xgc_ex**2. + ygc_ex**2.)



			if typ_ == 'GC':
				

				
				plt.plot(xgc,ygc,'-',color=arm_clr[armi])				
				plt.plot(xgc_ex,ygc_ex,linestyle=linestyle2,color=arm_clr[armi])
				
				plt.axvline(xsun,linewidth=1,linestyle='--')			
				plt.axhline(0,linewidth=1,linestyle='--')			
				
	
				plt.plot(0.,0.,marker='+',markersize=10,color='black')
				plt.plot(xsun,0.,marker='o',markersize=10,color='black')				
	
				plt.xlabel('X$_{GC}$')
				plt.ylabel('Y$_{GC}$')
				    
				
				
				
				# # labels
				# plt.text(-2,-5,'Scutum',fontsize=14,fontweight='bold',color=colors[0])
				# plt.text(-2,-10,'Sgr-Car',fontsize=14,fontweight='bold',color=colors[1])
				# plt.text(-3,-13,'Local',fontsize=14,fontweight='bold',color=colors[2])
				# plt.text(-9,-14,'Perseus',fontsize=14,fontweight='bold',color=colors[3])		
	    
	    
			if typ_ == 'HC':	
				
				
		
			
				
				# plt.plot(xhc,yhc,color,label=arm,linestyle=linestyle,linewidth=linewidth,markersize=2)
				# plt.plot(xhc,yhc,color,linestyle=linestyle,linewidth=linewidth,markersize=2)
				
				
				plt.plot(xhc,yhc,'-',color=arm_clr[armi])				
				plt.plot(xhc_ex,yhc_ex,linestyle=linestyle2,color=arm_clr[armi])
	
				plt.plot(0.,0.,marker='o',markersize=markersize,color='black')
				plt.plot(-xsun,0.,marker='+',markersize=markersize,color='black')						
								
	
				
				plt.xlabel('X$_{HC}$')
				plt.ylabel('Y$_{HC}$')			
	
	
	
	
			if typ_ =='polar':
							
				
				phi1 = np.arctan2(yhc,-xgc)
				phi1_ex = np.arctan2(ygc_ex,-xgc_ex)
				
				phi2 = np.degrees(np.arctan(yhc/-xgc))
				phi3 = np.degrees(np.arctan2(yhc,xgc))%180.	
				phi4 = np.degrees(np.arctan2(yhc,xgc))%360.	
				
				plt.plot(phi1,rgc,'-',color=arm_clr[armi],markersize=markersize)
				plt.plot(phi1_ex,rgc_ex,linestyle=linestyle2,color=arm_clr[armi],markersize=markersize)
			
						    
				self.dused['rgc'].append(rgc)
				self.dused['xgc'].append(xgc)
				self.dused['yhc'].append(yhc)
				self.dused['phi1'].append(phi1)
				self.dused['phi4'].append(phi4)


			if typ_ =='polargrid':
				
				linewidth=2
				linestyle = '-'
				phi4 = np.degrees(np.arctan2(yhc,xgc))%360.	
				phi4_ex = np.degrees(np.arctan2(ygc_ex,xgc_ex))%360.	

				phi1 = np.arctan2(yhc,-xgc)
				phi1_ex = np.arctan2(ygc_ex,-xgc_ex)
	

				# plt.plot(np.radians(phi4),rgc,color=arm_clr[armi],markersize=markersize,linestyle=linestyle,linewidth=linewidth)

				# plt.plot(phi1,rgc,color=arm_clr[armi],markersize=markersize,linestyle=linestyle,linewidth=linewidth)
				# plt.plot(phi1_ex,rgc_ex,color=arm_clr[armi],markersize=markersize,linestyle='--',linewidth=linewidth)
				
				plt.plot(np.radians(phi4),rgc,color=arm_clr[armi],markersize=markersize,linestyle=linestyle,linewidth=linewidth)
				
				plt.plot(np.radians(phi4_ex),rgc_ex,color=arm_clr[armi],markersize=markersize,linestyle=linestyle2,linewidth=linewidth)
				# plt.plot(np.radians(phi4_ex),rgc_ex,color=arm_clr[armi],markersize=markersize,linestyle='--',linewidth=linewidth)

	
				self.dused['rgc'].append(rgc)
				self.dused['xgc'].append(xgc)
				self.dused['yhc'].append(yhc)
				self.dused['phi4'].append(phi4)
				



class LevineSpiral:



    def __init__(self, R0=8.5):
        """Initialize spiral parameters from Levine et al. 2006"""
        self.R0 = R0  # Solar Galactocentric radius (kpc)
        self.arms = {
            'Arm1': {'pitch': 24, 'phi0': 56},   # Pitch angle and Solar crossing angle
            'Arm2': {'pitch': 24, 'phi0': 135},
            'Arm3': {'pitch': 25, 'phi0': 189},
            'Arm4': {'pitch': 21, 'phi0': 234}
        }
        
    def generate_arm(self, arm_name, R_max=25, n_points=1000):
        """Generate spiral arm coordinates using logarithmic spiral formula"""
        params = self.arms[arm_name]
        pitch_rad = np.radians(params['pitch'])
        phi0_rad = np.radians(params['phi0'])
        
        # Calculate maximum phi to reach R_max
        phi_max = phi0_rad + (np.log(R_max/self.R0)/np.tan(pitch_rad))
        
        # Generate angular range
        phi = np.linspace(phi0_rad, phi_max, n_points) #n_
        
        # Logarithmic spiral equation
        R = self.R0 * np.exp((phi - phi0_rad) * np.tan(pitch_rad))
        
        # Convert to Cartesian coordinates
        x_gc = R * np.cos(phi)
        y_gc = R * np.sin(phi)
        
        # Convert to Heliocentric coordinates
        x_hc = x_gc + self.R0  # Sun at (-R0, 0) in GC
        
        return x_gc, y_gc, x_hc, y_gc
    
    def plot_arms(self, coord_system='HC', R_max=25, show_sun=True):
        """Plot spiral arms in specified coordinate system"""
        plt.figure(figsize=(10, 10))
        colors = plt.cm.viridis(np.linspace(0, 1, len(self.arms)))
        
        for arm, color in zip(self.arms.keys(), colors):
            x_gc, y_gc, x_hc, y_hc = self.generate_arm(arm, R_max)
            
            if coord_system.upper() == 'GC':
                plt.plot(x_gc, y_gc, color=color, label=arm)
                plt.plot(-self.R0, 0, 'o', markersize=8, color='orange', label='Sun') if show_sun else None
                plt.xlabel('X (GC) [kpc]')
                plt.ylabel('Y (GC) [kpc]')
            elif coord_system.upper() == 'HC':
                plt.plot(x_hc, y_hc, color=color, label=arm)
                plt.plot(0, 0, 'o', markersize=8, color='orange', label='Sun') if show_sun else None
                plt.xlabel('X (HC) [kpc]')
                plt.ylabel('Y (HC) [kpc]')
            else:
                raise ValueError("Coordinate system must be 'GC' or 'HC'")


		

	    """""""""""""""""""""""""""""""""""""""'
     
        plt.axhline(0, color='gray', ls='--', lw=0.5)
        plt.axvline(0, color='gray', ls='--', lw=0.5)
        plt.legend(loc='upper right')
        plt.grid(alpha=0.3)
        plt.axis('equal')
        plt.title(f"Levine et al. HI Spiral Arms ({coord_system} Coordinates)")
        plt.show()

# Usage Example
if __name__ == "__main__":
    spiral_model = LevineSpiral(R0=8.5)
    
    # Plot in Heliocentric coordinates (default)
    spiral_model.plot_arms(coord_system='HC', R_max=25)
    
    # Plot in Galactocentric coordinates
    spiral_model.plot_arms(coord_system='GC', R_max=25)







    
"""""""""""""""""""""""""""""""""""""""""""""""





class HouHanSpiral:
    def __init__(self, R0=8.3, Θ0=239):
        """
        Initialize spiral parameters from Hou & Han 2014.
        """
        self.R0 = R0  # Solar Galactocentric radius (kpc)
        #self.s0 = Θ0  # Circular velocity at Sun (km/s)

        # Taken value from the table 4 from Hou & Han (2014)
        self.arms = {
            'Norma': {'a': 1.1668, 'b': 0.1198, 'c': 0.002557, 'd': 0.0, 'θ_start': 40, 'θ_end': 250},
            'Scutum-Centaurus': {'a': 5.8002, 'b': -1.8188, 'c': 0.2352, 'd': -0.008999, 'θ_start': 275, 'θ_end': 620},
            'Sagittarius-Carina': {'a': 4.2300, 'b': -1.1505, 'c': 0.1561, 'd': -0.005898, 'θ_start': 275, 'θ_end': 570},
            'Perseus': {'a': 0.9744, 'b': 0.1405, 'c': 0.003995, 'd': 0.0, 'θ_start': 280, 'θ_end': 500},
            'Local': {'a': 0.9887, 'b': 0.1714, 'c': 0.004358, 'd': 0.0, 'θ_start': 280, 'θ_end': 475},
            'Outer': {'a': 3.3846, 'b': -0.6554, 'c': 0.08170, 'd': 0.0, 'θ_start': 280, 'θ_end': 355}
        }

    def polynomial_log_spiral(self, θ, a, b, c, d):
        """Polynomial-logarithmic spiral model."""
        return np.exp(a + b*np.radians(θ) + c*np.radians(θ)**2 + d*np.radians(θ)**3)

    def generate_arm(self, arm_name, n_points=500):
        """Generate spiral arm coordinates based on the polynomial-logarithmic model."""
        params = self.arms[arm_name]
        θ = np.linspace(params['θ_start'], params['θ_end'], n_points)
        R = self.polynomial_log_spiral(θ, params['a'], params['b'], params['c'], params['d'])
        
        # Convert to Cartesian coordinates (Galactocentric)
        x_gc = R * np.cos(np.radians(θ))
        y_gc = R * np.sin(np.radians(θ))
        
        # Convert to Heliocentric coordinates
        x_hc = x_gc + self.R0
        return x_gc, y_gc, x_hc, y_gc

    def plot_arms(self, coord_system='GC'):
        """Plot spiral arms in Galactocentric (GC) or Heliocentric (HC) coordinates."""
        plt.figure(figsize=(12, 12))
        colors = plt.cm.viridis(np.linspace(0, 1, len(self.arms)))

        for (arm, color) in zip(self.arms.keys(), colors):
            x_gc, y_gc, x_hc, y_hc = self.generate_arm(arm)
            
            if coord_system.upper() == 'GC':
                plt.plot(x_gc, y_gc, color=color, label=arm)
                plt.plot(-self.R0, 0, 'o', markersize=8, color='orange', label='Sun')
            elif coord_system.upper() == 'HC':
                plt.plot(x_hc, y_hc, color=color, label=arm)
                plt.plot(0, 0, 'o', markersize=8, color='orange', label='Sun')

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	    
	plt.gca().set_aspect('equal')
        plt.xlabel(f'X ({coord_system}) [kpc]')
        plt.ylabel(f'Y ({coord_system}) [kpc]')
        plt.legend()
        plt.title("Hou & Han (2014) Spiral Arm Model (PL Spiral)")
        plt.grid(alpha=0.3)
        plt.show()

    def fit_polynomial_spiral(self, θ_data, R_data, degree=3):
        """Fit polynomial-logarithmic spiral to arm segments."""
        log_R_data = np.log(R_data)
        
        # Fit polynomial: ln(R) = a + bθ + cθ^2 + dθ^3
        coeffs = np.polyfit(np.radians(θ_data), log_R_data, degree)
        
        return coeffs

# Example usage
if __name__ == "__main__":
    spiral_model = HouHanSpiral()
    
    # Plot in Heliocentric coordinates
    spiral_model.plot_arms(coord_system='HC')
    
    # Plot in Galactocentric coordinates
    spiral_model.plot_arms(coord_system='GC')


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""







  
# kinematics
def get_lsr(typ='schonrich',show=False):
	'''
	Comment: using 8.275 kpc following ESO-grav 2021
			 # was using 8.2 kpc following ESO-grav 2018
			 
	typ =='schonrich':
	from schonrich 2011
	 
		
		
	typ == 'gravity':	       
	# values used in Drimmel 2022 (based on Gravity)  
	
	
	typ == 'galaxia':
	for use with galaxia kinematics		
		
	'''
	
	# print(typ)
	
	LSR = {}
	if typ =='schonrich':
		LSR = {'xsun':-8.275,
		       'zsun':0.027,
		       'usun':11.1,
		       'wsun':7.25,
		       'omega_sun':30.24}
	elif typ == 'gravity':	       
		# values used in Drimmel 2022 (based on Gravity)       
		LSR = {'xsun':-8.277,
		       'zsun':0.,
		       'usun':9.3,
		       # 'omega_sun':6.39*4.74}
		       'omega_sun':6.411*4.74}
     
		LSR['wsun'] = 0.219*4.74*LSR['xsun']*-1
     		       

	elif typ == 'galaxia':
		LSR = {'xsun':-8.,
		       'zsun':0.0,
		       'usun':11.1,
		       'wsun':7.25,
		       'omega_sun':239.08/8.}
				       
	LSR['vsun'] = -LSR['omega_sun']*LSR['xsun']
	LSR['Rsun'] = -LSR['xsun']
	
	if show:

		print('')
		print(typ+' LSR: ')	
		for k, v in LSR.iteritems():		
			print ("{:<15} :{:<15}".format(k,v))
	
	return LSR
	
	
