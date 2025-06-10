#######################################################################
# SpiralMap: a library of the Milky Way's spiral arms
# History:  	
# May 2025: Prusty (IISER Kolkata) & Shourya Khanna (INAF Torino)
#######################################################################


#--------------------------------------------
# import utilities package / set root 
import os
from os.path import dirname
root_ = dirname(__file__)
dataloc = root_+'/datafiles'
exec(open(root_+"/mytools.py").read())

#--------------------------------------------       


### TO do:
#1 consistent colours for similar arms
####################################

class spiral_poggio_maps(object):
	# """
	# Class containing spiral arm models from
		# Poggio_2021: Poggio al. 2021 (EDR3 UMS stars)
		# GaiaPVP_2022: Gaia collaboration et al. 2021 (OB stars)
					
	# HISTORY:
		# 09 May 2025: Prusty/Khanna					
	# """
	
	def __init__(self,model_='GaiaPVP_cont_2022'):		
		"""Initialize the list of available spiral arms 
		and their corresponding plot colors. """		
		self.model_ = model_
		self.loc = dataloc + '/'+model_
		self.getarmlist()	
	def getarmlist(self):
		"""Initialize the list of available spiral arms 
		and their corresponding plot colors. """
		self.arms = np.array(['all'])
		self.armcolour = {'all': 'black'}	
		self.armcolours= [self.armcolour[ky]  for ky in self.arms  ]			
	def info(self):
		"""Collate arm information """
		d = {'Arm list': self.arms, 'Colour': self.armcolours}		
		dfmodlist = pd.DataFrame(d)	
		print(tabulate(dfmodlist, headers = 'keys', tablefmt = 'psql'))		
	def output_(self,plotattrs):
		
		xsun = self.xsun
	
		flist1 = fcount(self.loc,flist=True,prnt=False)		
		func_ = lambda s: 'grid' in s
		overdens_file = list(filter(func_,flist1))[0]
		func_ = lambda s: 'xval' in s
		xval_file = list(filter(func_,flist1))[0]
		func_ = lambda s: 'yval' in s
		yval_file = list(filter(func_,flist1))[0]
		
		# # read overdensity contours
		xvalues_overdens=np.load(self.loc+'/'+xval_file)
		yvalues_overdens=np.load(self.loc+'/'+yval_file)
		over_dens_grid=np.load(self.loc+'/'+overdens_file)
		phi1_dens=np.arctan2(yvalues_overdens, -xvalues_overdens)
		Rvalues_dens=sqrtsum(ds=[xvalues_overdens, yvalues_overdens])
		Rgcvalues_dens=sqrtsum(ds=[xvalues_overdens+xsun, yvalues_overdens])
		
		fl = pickleread(self.loc+'/'+self.model_+'_pproj_contours.pkl')
		self.dout = {'xhc':xvalues_overdens,'yhc':yvalues_overdens,'xgc':xvalues_overdens+xsun,'ygc':yvalues_overdens}
		self.dout['phi4'] =fl['phi4'].copy()	
		self.dout['glon4'] =fl['glon4'].copy()	
		self.dout['rgc'] =fl['rgc'].copy()	
		self.dout['dhelio'] =fl['dhelio'].copy()	
		
		# # # # getangular(self)

		#----overplot spiral arms in overdens----#
		iniz_overdens= 0  
		fin_overdens= 1.5 
		N_levels_overdens= 2
		levels_overdens1= np.linspace(iniz_overdens,fin_overdens,N_levels_overdens)		
		
		if plotattrs['polarproj'] == False:	
			useclr = plotattrs['armcolour']					
			if plotattrs['armcolour'] == '':
				useclr = 'grey'
			cset1 = plt.contourf(self.dout['x'+plotattrs['coordsys'].lower()],self.dout['y'+plotattrs['coordsys'].lower()],over_dens_grid.T, 
								levels=levels_overdens1,alpha=0.05,cmap='Greys')	
			iniz_overdens= 0. 
			fin_overdens= 1.5 
			N_levels_overdens= 4 
			levels_overdens2= np.linspace(iniz_overdens,fin_overdens,N_levels_overdens)
			cset2 = plt.contour(self.dout['x'+plotattrs['coordsys'].lower()],self.dout['y'+plotattrs['coordsys'].lower()],over_dens_grid.T,levels=levels_overdens2,colors=useclr,linewidths=plotattrs['markersize'])
	
			self.xmin,self.xmax =plt.gca().get_xlim()[0].copy(),plt.gca().get_xlim()[1].copy()				
			self.ymin,self.ymax =plt.gca().get_ylim()[0].copy(),plt.gca().get_ylim()[1].copy()								

			plt.xlabel('X$_{'+plotattrs['coordsys']+'}$ [Kpc]')
			plt.ylabel('Y$_{'+plotattrs['coordsys']+'}$ [Kpc]')	 

			return cset1, cset2														
		else:
			plotattrs['linestyle'] = '.'
			_polarproj(self,plotattrs)	
				
			
class TaylorCordesSpiral(object):		
	"""	
	Taylor & Cordes (1993) Galactic spiral arm model,	  
	based on radio pulsar observations. The model defines four major spiral arms.		
	"""	
	def __init__(self):		
		self.getarmlist()        
	def getarmlist(self):
		"""Set arm names and colours"""
		
		self.arms = np.array(['Arm1','Arm2','Arm3','Arm4'])
		self.armcolour = {'Arm1':'yellow','Arm2':'green','Arm3':'blue','Arm4':'purple'}
		self.armcolours= [self.armcolour[ky]  for ky in self.arms  ]
	
		self.getparams()        
	def info(self):        

		d = {'Arm list': self.arms, 'Colour': self.armcolours}
		dfmodlist = pd.DataFrame(d)			
		print(tabulate(dfmodlist, headers = 'keys', tablefmt = 'psql'))									
	def getparams(self):	   
		"""Load original spiral parameters from Taylor & Cordes (1993) Table 1.
		
	   :return: self.params['Arm1','Arm2','Arm3','Arm4'], 
				nested dictionary such that, 
				self.params['Arm']['theta_deg'] -> Anchor points in galactic longitude (degrees). \
				self.params['Arm']['r_kpc'] ->Corresponding galactocentric radii (kiloparsecs). 
	   :rtype: dict
		"""		
		self.params = {	'Arm1': {'theta_deg': [164, 200, 240, 280, 290, 315, 330],
					'r_kpc': [3.53, 3.76, 4.44, 5.24, 5.36, 5.81, 5.81]},
					
					'Arm2':{'theta_deg': [63, 120, 160, 200, 220, 250, 288],
					'r_kpc': [3.76, 4.56, 4.79, 5.70, 6.49, 7.29, 8.20]},
					
					'Arm3':{'theta_deg': [52, 120, 170, 180, 200, 220, 252],
					'r_kpc': [4.90, 6.27, 6.49, 6.95, 8.20, 8.89, 9.57]},
					
					'Arm4':{'theta_deg': [20, 70, 100, 160, 180, 200, 223],
					'r_kpc': [5.92, 7.06, 7.86, 9.68, 10.37, 11.39, 12.08]}					  
								  }    
	def model_(self, arm_name):					
		"""			
		   Generate arm coordinates using cubic spline interpolation.
		
		   :param arm_name: Must be one of: 'Arm1', 'Arm2', 'Arm3', 'Arm4'.	
		   :type arm_name: String 
		   :return: (x_hc, y_hc, x_gc, y_gc)
		   :rtype: tuple 
		"""		
		
		self.getparams()
		arm_data = self.params[arm_name]
		theta = np.deg2rad(arm_data['theta_deg'])  # Convert to radians
		r = np.array(arm_data['r_kpc'])
		
		# Cubic spline interpolation for smooth curve
		cs = CubicSpline(theta, r)
		theta_fine = np.linspace(min(theta), max(theta), 300)
		r_fine = cs(theta_fine)
		
		# Convert to Cartesian coordinates (Galacto-Centric)
		
		xgc = r_fine * np.sin(theta_fine)
		ygc = -r_fine * np.cos(theta_fine)
		
		# rotate by 90 anti-clockwise to match with our convention 
		rot_ang = np.radians(90)
		x_gc = (xgc*np.cos(rot_ang)) - (ygc*np.sin(rot_ang)  )
		y_gc = (xgc*np.sin(rot_ang)) + (ygc*np.cos(rot_ang)  )
			
		# Convert to Heliocentric coordinates
		x_hc = x_gc + self.R0  # Sun at (-R0, 0) in GC
		
		return x_hc, y_gc, x_gc, y_gc		
	def output_(self,arm):			
		"""			
		   Get arm coordinates in structured format.
		
		   :param arm: Arm identifier (e.g., 'Arm1')		
		   :type arm: String 
		   :return: self.dout = {'xhc':xhc,'yhc':yhc,'xgc':xgc,'ygc':ygc}
		   :rtype: dict 
		"""				
		
		xsun = self.xsun
		self.R0 = -xsun  # Solar Galactocentric radius (kpc)					
		xhc,yhc,xgc,ygc = self.model_(arm);					
		self.dout = {'xhc':xhc,'yhc':yhc,'xgc':xgc,'ygc':ygc}							 


class spiral_houhan(object):	
	"""Hou & Han (2014) polynomial-logarithmic spiral arm model
	
	Implements the Milky Way spiral structure model from:
	"The spiral structure of the Milky Way from classical Cepheids" (Hou & Han 2014)
	using polynomial-logarithmic spiral functions. Provides 6 major arm segments.	
	"""	
	def __init__(self):			
		self.getarmlist()	
	def getarmlist(self):
		"""Set arm names and colours"""
		self.arms = np.array(['Norma','Scutum-Centaurus','Sagittarius-Carina','Perseus','Local','Outer'])
		self.armcolour = {'Norma':'black','Scutum-Centaurus':'red','Sagittarius-Carina':'green','Perseus':'blue','Local':'purple','Outer':'gold'}
		self.armcolours= [self.armcolour[ky]  for ky in self.arms  ]	
	def info(self):		
		d = {'Arm list': self.arms, 'Colour': self.armcolours}
		dfmodlist = pd.DataFrame(d)		
		print(tabulate(dfmodlist, headers = 'keys', tablefmt = 'psql'))			
		
	def getparams(self):						
		"""			
		   Load spiral parameters from Hou & Han (2014) Table 4.
		   
		   :return: params ( Nested dictionary containing for each arm).
		   
	   				a, b, c, d: Polynomial coefficients.
	   				
					θ_start: Start angle in degrees (Galactic longitude).
					
					θ_end: End angle in degrees.		   		   
		   :rtype: dict 
		"""					
		params = {
			'Norma': {'a': 1.1668, 'b': 0.1198, 'c': 0.002557, 'd': 0.0, 'θ_start': 40, 'θ_end': 250},
			'Scutum-Centaurus': {'a': 5.8002, 'b': -1.8188, 'c': 0.2352, 'd': -0.008999, 'θ_start': 275, 'θ_end': 620},
			'Sagittarius-Carina': {'a': 4.2300, 'b': -1.1505, 'c': 0.1561, 'd': -0.005898, 'θ_start': 275, 'θ_end': 570},
			'Perseus': {'a': 0.9744, 'b': 0.1405, 'c': 0.003995, 'd': 0.0, 'θ_start': 280, 'θ_end': 500},
			'Local': {'a': 0.9887, 'b': 0.1714, 'c': 0.004358, 'd': 0.0, 'θ_start': 280, 'θ_end': 475},
			'Outer': {'a': 3.3846, 'b': -0.6554, 'c': 0.08170, 'd': 0.0, 'θ_start': 280, 'θ_end': 355}
		}	
		return params		
	def polynomial_log_spiral(self, θ, a, b, c, d):		
		"""Calculate radius using polynomial-logarithmic spiral equation.
		
		Parameters
		----------
		θ : float or ndarray
			Galactic longitude angle in degrees
		a,b,c,d : float
			Polynomial coefficients from Hou & Han Table 4
			
		Returns
		-------
		float or ndarray
			Galactocentric radius in kiloparsecs
			
		Notes
		-----
		Implements equation:
		R(θ) = exp(a + bθ_rad + cθ_rad² + dθ_rad³)
		where θ_rad = np.radians(θ)
		"""	
		return np.exp(a + b*np.radians(θ) + c*np.radians(θ)**2 + d*np.radians(θ)**3)
	
	def model_(self, arm_name, n_points=500):
		
		params_ = self.getparams()
		params = params_[arm_name]
		
		
		θ = np.linspace(params['θ_start'], params['θ_end'], n_points)
		R = self.polynomial_log_spiral(θ, params['a'], params['b'], params['c'], params['d'])
		
		# Convert to Cartesian coordinates (Galactocentric)
		x_gc = R*np.cos(np.radians(θ))
		y_gc = R * np.sin(np.radians(θ))
		
		# Convert to Heliocentric coordinates
		x_hc = (x_gc + self.R0)
	
		return x_hc, y_gc, x_gc, y_gc
	
	def output_(self, arm):			
		"""			
		   Get arm coordinates in structured format.
		
		   :param arm: Arm identifier (e.g., 'Arm1')		
		   :type arm: String 
		   :return: self.dout = {'xhc':xhc,'yhc':yhc,'xgc':xgc,'ygc':ygc}
		   :rtype: dict 
		"""				
		
		xsun = self.xsun
		self.R0 = -xsun  # Solar Galactocentric radius (kpc)	
		# Generate spiral arm coordinates
		xhc, yhc, xgc, ygc = self.model_(arm)	
		self.dout = {
			'xhc': xhc,
			'yhc': yhc,
			'xgc': xgc,
			'ygc': ygc
		}


class spiral_levine(object):		
	"""	
	Levine et al (2006) logarithmic spiral arm model for the Milky Way.  				
	"""	

	def __init__(self):   
		self.getarmlist()
	
	def getarmlist(self):	
		"""Set arm names and colours"""					
		self.arms = np.array(['Arm1','Arm2','Arm3','Arm4'])
		self.armcolour = {'Arm1':'yellow','Arm2':'green','Arm3':'blue','Arm4':'purple'}
		self.getparams()
		self.armcolours= [self.armcolour[ky]  for ky in self.arms  ]
		
	def info(self):

		d = {'Arm list': self.arms, 'Colour': self.armcolours}
		dfmodlist = pd.DataFrame(d)			
		print(tabulate(dfmodlist, headers = 'keys', tablefmt = 'psql'))			
	
	def getparams(self):
		"""		
	   :return: self.params['Arm1','Arm2','Arm3','Arm4'], nested dictionary such that,
	   				 				
				self.params['Arm']['pitch'] -> pitch angle
				
				self.params['Arm']['phi0'] -> Solar crossing angle)
	   :rtype: dict
		"""		
		
		self.arms_model = {
			'Arm1': {'pitch': 24, 'phi0': 56},   
			'Arm2': {'pitch': 24, 'phi0': 135},
			'Arm3': {'pitch': 25, 'phi0': 189},
			'Arm4': {'pitch': 21, 'phi0': 234}
		}
	 
	def model_(self,arm_name, R_max=25, n_points=1000):
		
		"""Generate logarithmic spiral coordinates for specified arm.
		
		Parameters
		----------
		arm_name : str
			Name of arm to model (must be in ['Arm1', 'Arm2', 'Arm3', 'Arm4'])
		R_max : float, optional
			Maximum galactocentric radius to model (kpc), default=25
		n_points : int, optional
			Number of points to sample along the spiral, default=1000
	
		Returns
		-------
		tuple
			(x_hc, y_hc, x_gc, y_gc) coordinate arrays where:
			- x_hc, y_hc: Heliocentric coordinates (kpc)
			- x_gc, y_gc: Galactocentric coordinates (kpc)
	
		Raises
		------
		ValueError
			If invalid arm_name is provided
	
		Notes
		-----
		Implements the logarithmic spiral equation:
			R(φ) = R₀ * exp[(φ - φ₀) * tan(i)]
		where:
		- R₀ is solar galactocentric distance
		- i is pitch angle
		- φ₀ is solar crossing angle
		- φ is the angular coordinate
		"""
	
		params = self.arms_model[arm_name]
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
		x_hc = x_gc + self.R0  
	
		return x_hc, y_gc,x_gc, y_gc
		
	def output_(self, arm):		

		"""			
		   Get arm coordinates in structured format.
		
		   :param arm: Arm identifier (e.g., 'Arm1')		
		   :type arm: String 
		   :return: self.dout = {'xhc':xhc,'yhc':yhc,'xgc':xgc,'ygc':ygc}
		   :rtype: dict 
		"""		
				
		xsun = self.xsun
		self.R0 = -xsun  
		xhc, yhc, xgc, ygc = self.model_(arm)   
		self.dout = {
			'xhc': xhc,
			'yhc': yhc,
			'xgc': xgc,
			'ygc': ygc}


class spiral_drimmel_cepheids(object):
	
	def __init__(self):
		self.loc = dataloc+'/Drimmel2024_cepheids'
		self.fname = 'ArmAttributes_dyoungW1_bw025.pkl'
		self.getarmlist()
	def getarmlist(self):

		
		self.spirals = pickleread(self.loc+'/'+self.fname)
		self.arms= np.array(list(self.spirals['0']['arm_attributes'].keys()))
		self.armcolour = {'Scutum':'C3','Sag-Car':'C0',
						  'Orion':'C1','Perseus':'C2'}   
						  
		self.armcolours= [self.armcolour[ky]  for ky in self.arms  ]			  
	def info(self):		
		'''
		here goes basic info for the user about this model
		'''					
		d = {'Arm list': self.arms, 'Colour': self.armcolours}
		dfmodlist = pd.DataFrame(data=d)
		print(tabulate(dfmodlist, headers = 'keys', tablefmt = 'psql'))			        

	def output_(self,arm):		
		
		xsun = self.xsun
		rsun = -xsun	
		spirals = self.spirals
		arms = self.arms
							
		# XY positions
		lnrsun = np.log(rsun) 
			
		# best phi range:
		phi_range = np.deg2rad(np.sort(self.spirals['1']['phi_range'].copy()))
		maxphi_range = np.deg2rad([60,-120]) 
		
		pang = (spirals['1']['arm_attributes'][arm]['arm_pang_strength']+spirals['1']['arm_attributes'][arm]['arm_pang_prom'])/2.
		lnr0 = (spirals['1']['arm_attributes'][arm]['arm_lgr0_strength']+spirals['1']['arm_attributes'][arm]['arm_lgr0_prom'])/2.
						
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
		
		rgc = np.sqrt(xgc**2. + ygc**2.)
		rgc_ex = np.sqrt(xgc_ex**2. + ygc_ex**2.)
          
		self.dout = {'xhc':xhc,'yhc':yhc,'xgc':xgc,'ygc':ygc,'xhc_ex':xhc_ex,'yhc_ex':yhc_ex,'xgc_ex':xgc_ex,'ygc_ex':ygc_ex}			


class spiral_drimmel_nir(object):
	"""Drimmel (2000) Near-Infrared (NIR) spiral arm model
	
	Implements the 2-arm spiral structure model from:
	Drimmel, R. (2000) "Evidence for a two-armed spiral in the Milky Way"
	using COBE/DIRBE near-infrared data. Includes main arms and phase-shifted interarms.
	
	Attributes
	----------
	arms : ndarray
		Array of arm identifiers ['1_arm', '2_arm', '3_interarm', '4_interarm']
	armcolour : dict
		Color mapping for visualization:
		- Main arms: black
		- Interarms: red	
	"""
	def __init__(self):
		"""Initialize Drimmel NIR spiral model with default parameters"""
	 
		self.loc = dataloc+'/Drimmel_NIR'
		self.fname = 'Drimmel2armspiral.fits'
		self.getarmlist()
	def getarmlist(self):
		"""Set arm names and colours"""
		self.arms = np.array(['1_arm','2_arm','3_interarm','4_interarm'])
		self.armcolour = {'1_arm':'black','2_arm':'black','3_interarm':'red','4_interarm':'red'}		
		self.armcolours= [self.armcolour[ky]  for ky in self.arms  ]			
	def info(self):		
		# """Display basic model information and arm components."""	
		d = {'Arm list': self.arms, 'Colour': self.armcolours}
		dfmodlist = pd.DataFrame(d)			
		print(tabulate(dfmodlist, headers = 'keys', tablefmt = 'psql'))		
	        
	def getdata(self):
		"""Load and preprocess spiral arm data from FITS file.
		
		1. Loads base FITS data
		
		2. Scales coordinates using solar position
		
		3. Adds phase-shifted interarm components
		
		4. Calculates galactocentric radii
		
		Notes
		-----
		- Original data scaled by solar galactocentric distance
		- Phase-shifted arms loaded from separate numpy files
		"""
	
		dt = fitsread(self.loc+'/'+self.fname)
		self.data0 = dt.copy()
		
		xsun = self.xsun					
			
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
	def output_(self,arm):			
		"""Retrieve spiral arm coordinates in specified format.
		
		Parameters
		----------
		arm : str
			Arm identifier or selection mode:
			- '1', '2' for main arms
			- '3', '4' for interarms 
			- 'all' for all components
			- 'main' for just main arms
		typ_ : {'cartesian', 'polar', 'polargrid'}, default 'cartesian'
			Output format:
			- cartesian: Returns x,y coordinates
			- polar/polargrid: Generates polar coordinate plots
	
		Returns
		-------
		dict
			For cartesian type contains:
			- xhc, yhc: Heliocentric coordinates (kpc)
			- xgc, ygc: Galactocentric coordinates (kpc)
			
		Notes
		-----
		Polar modes create matplotlib plots directly using:
		- phi1: Angle from negative x-axis (GC frame)
		- phi4: Galactic longitude (0-360 degrees)
		"""
		xsun = self.xsun
		self.getdata()
		dt = self.data.copy()  
					
		numbs = [arm]
		if arm == 'all':
			numbs = self.arms
		elif arm == 'main':
			numbs = ['1','2']		
		
		self.dused = {}
		self.dused['rgc'] = []
		self.dused['xgc'] = []
		self.dused['yhc'] = []
		self.dused['phi1'] = []
		self.dused['phi4'] = []
	
		for numb1 in numbs:	
			numb = str(int(numb1.split('_')[0]))	            
			xhc = dt['xhc'+numb]
			yhc = dt['yhc'+numb]
			rgc = dt['rgc'+numb]            
			xgc = xhc + xsun			
			ygc = yhc                     
			self.dout = {'xhc':xhc,'yhc':yhc,'xgc':xgc,'ygc':ygc}					


class reid_spiral(object):
	"""Reid et al. (2019) kinked logarithmic spiral arm model
	
	Implements the Milky Way spiral structure model from:
	"Trigonometric Parallaxes of High Mass Star Forming Regions: The Structure and Kinematics of the Milky Way"
	using kinked logarithmic spirals with varying pitch angles. Models 7 major arm features.
	
	Attributes
	----------
	arms : ndarray
		Array of arm identifiers ['3-kpc', 'Norma', 'Sct-Cen', 'Sgr-Car', 'Local', 'Perseus', 'Outer']	
	"""
	
	def __init__(self, kcor=False):
		"""Initialize Reid et al. (2019) spiral model
		
		Parameters
		----------
		kcor : bool, optional
			Apply distance correction adjustment to R_kink parameters,
			default=False
		"""
		self.kcor = kcor
		self.getarmlist()		
	def getarmlist(self):	
		"""Set arm names and colours"""			
		self.arms = np.array(['3-kpc','Norma','Sct-Cen','Sgr-Car','Local','Perseus','Outer'])      				
		self.armcolour = {'3-kpc':'C6','Norma':'C5','Sct-Cen':'C4',
		                  'Sgr-Car':'C3','Local':'C2','Perseus':'C1',
		                  'Outer':'C0'}	
		self.armcolours= [self.armcolour[ky]  for ky in self.arms  ]			                  	  		
	def info(self):		
		d = {'Arm list': self.arms, 'Colour': self.armcolours}
		dfmodlist = pd.DataFrame(d)			
		print(tabulate(dfmodlist, headers = 'keys', tablefmt = 'psql'))				
		
	def getparams(self,arm):
		"""Load spiral parameters for specified arm from Reid et al. (2019) Table 4.
		
		Parameters
		----------
		arm : str
			Valid arm identifier from class arms list
	
		Returns
		-------
		dict
			Dictionary containing:
			- beta_kink: Kink angle position in degrees
			
			- pitch_low: Pitch angle before kink (degrees)
			
			- pitch_high: Pitch angle after kink (degrees)
			
			- R_kink: Galactocentric radius at kink (kpc)
			
			- beta_min/max: Angular range in degrees
			
			- width: Arm width parameter (kpc)
	
		Notes
		-----
		Applies correction to R_kink if kcor=True during initialization
		"""
		if arm == '3-kpc':
			params = {'name':arm,'beta_kink':15,
					  'pitch_low':-4.2,'pitch_high':-4.2,
					  'R_kink':3.52,'beta_min':15,
					  'beta_max':18,'width':0.18}
		if arm == 'Norma':
			params = {'name':arm,'beta_kink':18,'pitch_low':-1.,
			          'pitch_high':19.5,'R_kink':4.46,'beta_min':5,
			          'beta_max':54,'width':0.14}
		if arm == 'Sct-Cen':
			params = {'name':arm,'beta_kink':23,'pitch_low':14.1,
			          'pitch_high':12.1,'R_kink':4.91,'beta_min':0,
			          'beta_max':104,'width':0.23}
		if arm == 'Sgr-Car': #'Sgr-Car'
			params = {'name':arm,'beta_kink':24,'pitch_low':17.1,
			          'pitch_high':1,'R_kink':6.04,'beta_min':2,
			          'beta_max':97,'width':0.27}
		if arm == 'Local':
			params = {'name':arm,'beta_kink':9,'pitch_low':11.4,
			          'pitch_high':11.4,'R_kink':8.26,'beta_min':-8,
			          'beta_max':34,'width':0.31}
		if arm == 'Perseus':
			params = {'name':arm,'beta_kink':40,'pitch_low':10.3,
			          'pitch_high':8.7,'R_kink':8.87,'beta_min':-23,
			          'beta_max':115,'width':0.35}
		if arm == 'Outer':
			params = {'name':arm,'beta_kink':18,'pitch_low':3,
			          'pitch_high':9.4,'R_kink':12.24,'beta_min':-16,
			          'beta_max':71,'width':0.65}				
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
		"""Generate kinked logarithmic spiral coordinates.
		
		Parameters
		----------
		params : dict
			Spiral parameters dictionary from getparams()
	
		Returns
		-------
		tuple
			(x, y, x1, y1, x2, y2) coordinate arrays where:
			
			- x,y: Arm center coordinates (GC)
			
			- x1,y1: Inner arm boundary
			
			- x2,y2: Outer arm boundary
	
		Notes
		-----
		Implements modified logarithmic spiral equation with pitch angle kink:
		R(β) = R_kink * exp[-(β - β_kink) * tan(pitch)]
		where pitch changes at β_kink
		"""
		
		beta_kink = np.radians(params['beta_kink'])
		pitch_low = np.radians(params['pitch_low'])
		pitch_high = np.radians(params['pitch_high'])
		R_kink = params['R_kink']
		beta_min = params['beta_min']
		beta_max = params['beta_max']
		width = params['width']
				
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
	
		R2 = (R_kink+(width*0.5))*tmp2
		x2 = -R2*(np.cos(beta))
		y2 = R2*(np.sin(beta))
	
		R1 = (R_kink-(width*0.5))*tmp2
		x1 = -R1*(np.cos(beta))
		y1 = R1*(np.sin(beta))
						
		return x,y, x1,y1,x2,y2	
	def output_(self,arm):		
		"""			
		   Get arm coordinates in structured format.
		
		   :param arm: Arm identifier (e.g., 'Norma')		
		   :type arm: String 
		   :return: self.dout = {'xhc':xhc,'yhc':yhc,'xgc':xgc,'ygc':ygc}
		   :rtype: dict 
		"""		
		
		xsun = self.xsun
		params = self.getparams(arm)		
		
		xgc,ygc,xgc1,ygc1,xgc2,ygc2 = self.model_(params);			
		xhc = xgc - xsun
		xhc1 = xgc1 - xsun
		xhc2 = xgc2 - xsun	
		yhc = ygc			
		self.dout = {'xhc':xhc,'yhc':yhc,'xgc':xgc,'ygc':ygc}													


class main_(object):	
	"""	
	The main executor that calls the individual models to grab the spiral traces.
	It is also used to set plot preferences and make plots.		
	"""
	def __init__(self,Rsun=8.277,print_=True):  		
		"""			
		   Initialize main object.
		
		   :param Rsun: Optional - Galactocentric R(kpc) of the Sun, default=8.277.	
		   :type Rsun: float 
		   :param print\_: Optional - if set to False does not print to screen.
		   :type print\_: Boolean 
		"""		
		 		   		 	
		self.root_ = root_
		self.dataloc = dataloc        
		self.xsun = -Rsun
		self.Rsun = Rsun        
		self.listmodels()
		self.getinfo(print_=print_)	    
		
		self.modrec = []
		self.armrec = []
	def listmodels(self):  
		"""			
		   	Defines list of available models/maps
		   	Constructs dictionaries to initialise individual model classes
		"""	
		   		
		self.models = ['Taylor_Cordes_1992','Drimmel_NIR_2000',
					   'Levine_2006','Hou_Han_2014','Reid_2019',
					   'Poggio_cont_2021','GaiaPVP_cont_2022','Drimmel_Ceph_2024']        
		self.models_class = {'Reid_2019':reid_spiral(),
							 'Levine_2006':spiral_levine(),
							 'Poggio_cont_2021':spiral_poggio_maps(model_='Poggio_cont_2021'),
							 'GaiaPVP_cont_2022':spiral_poggio_maps(model_='GaiaPVP_cont_2022'),
							 'Drimmel_NIR_2000':spiral_drimmel_nir(),
							 'Taylor_Cordes_1992':TaylorCordesSpiral(),
							 'Hou_Han_2014':spiral_houhan(),
							 'Drimmel_Ceph_2024':spiral_drimmel_cepheids()}
							 
		self.models_desc = 	['HII','NIR emission',
					   'HI','HII/GMC/Masers','MASER parallax',
					   'Upper main sequence (map)','OB stars (map)','Cepheids']  			 							 
	def getinfo(self,model='',print_=True):	
		"""			
		   prints (model list, tracers) & default plot attributes are defined here.
		
		   :param model: Optional - '' by default so lists all models. otherwise provide a model (ex: Drimmel_Ceph_2024) to list out all arms and default colours.	
		   :type model: String 
		   :param print\_: Optional - if set to False does not print to screen.
		   :type print\_: Boolean 
		"""		
		
		if model == '':		
			print('try self.getinfo(model) for more details')		
			dfmodlist = pd.DataFrame(self.models,columns=['Available models & maps:'])			
			d = {'Available models & maps:': self.models, 'Description': self.models_desc}
			dfmodlist = pd.DataFrame(d)					
			
			if print_:			
				print(tabulate(dfmodlist, headers = 'keys', tablefmt = 'psql'))

		else:
			
			try:
				spimod = self.models_class[model]
				print('#####################')			
				print('Model = '+model)
				spimod.info()
			except KeyError:
				print(' ')
				print(model+' is not in the library, check name !')	
				print(' ')				
			
		self.plotattrs_default = {'plot':False,
								'markersize':3,
								'coordsys':'HC',
								'linewidth':0.5,
								'linestyle': '-',
								'armcolour':'',
								'markSunGC':True,
								'xmin':'',
								'xmax':'',
								'ymin':'',
								'ymax':'',
								'polarproj':False,       
								'polargrid':False,    
								'dataloc':dataloc}    
	def add2plot(self,plotattrs):			
		if plotattrs['coordsys'] =='HC':								
			plt.plot(0.,0.,marker=r'$\odot$',markersize=plotattrs['markersize'],color='black')
			plt.plot(-self.xsun,0.,marker='*',markersize=plotattrs['markersize'],color='black')		
		if plotattrs['coordsys'] =='GC':										
			plt.plot(0.,0.,marker='*',markersize=plotattrs['markersize'],color='black')
			plt.plot(self.xsun,0.,marker=r'$\odot$',markersize=plotattrs['markersize'],color='black')
	def xyplot(self,spimod,plotattrs_):						
		if plotattrs_['plot'] and plotattrs_['polarproj']==False :							
			plt.plot(spimod.dout['x'+plotattrs_['coordsys'].lower()],
			         spimod.dout['y'+plotattrs_['coordsys'].lower()],
			         plotattrs_['linestyle'],color=plotattrs_['armcolour'])			
			if 'xhc_ex' in 	spimod.dout.keys():
				plt.plot(spimod.dout['x'+plotattrs_['coordsys'].lower()+'_ex'],
				         spimod.dout['y'+plotattrs_['coordsys'].lower()+'_ex'],
				         '--',color=plotattrs_['armcolour'])	
				                							
			plt.xlabel('X$_{'+plotattrs_['coordsys']+'}$ [Kpc]')
			plt.ylabel('Y$_{'+plotattrs_['coordsys']+'}$ [Kpc]')	 
			if plotattrs_['xmin'] == '' or plotattrs_['xmax'] == '' or plotattrs_['ymin'] == '' or plotattrs_['ymax'] == '':
				rub=1																			
			else:
				xmin,xmax = plotattrs_['xmin'],plotattrs_['xmax']
				ymin,ymax = plotattrs_['ymin'],plotattrs_['ymax']	
				plt.xlim([xmin,xmax])	
				plt.ylim([ymin,ymax])	
			
			self.xmin,self.xmax =plt.gca().get_xlim()[0].copy(),plt.gca().get_xlim()[1].copy()				
			self.ymin,self.ymax =plt.gca().get_ylim()[0].copy(),plt.gca().get_ylim()[1].copy()			
			
			if plotattrs_['markSunGC']:
				self.add2plot(plotattrs_)	
	def readout(self,plotattrs={},model='',arm='',print_=False):	
		"""			
		   reads out individual models/ makes plots etc.
		
		   :param plotattrs: Optional - if not provided, uses default plot attributes.
		   :type plotattrs: dict 
		   :param model: (required otherwise raises exception)
		   :type model: String 
		   :param arm:  Optional - (default = '' so reads all arms)
		   :type arm:  String
		   :param print\_: Optional - if set to False does not print to screen.
		   :type print\_: Boolean 
		   :raise RuntimeError: if no model is provided.
		"""						
		if model == '':
			 raise RuntimeError('model = blank | no model provided \n try self.getino() for list of available models')			 
			
		self.modrec.append(model)		
		spimod = self.models_class[model]			
		spimod.xsun = self.xsun
		spimod.getarmlist()		
		self.armlist = spimod.arms	
		self.arm = arm
				
		# in case plot attributes are not provided, or incomplete
		for ky in self.plotattrs_default.keys():			
			if ky not in list(plotattrs.keys()):				
				plotattrs[ky] = self.plotattrs_default[ky]
		plotattrs1 = plotattrs.copy()		
		if 'cont' in model.lower():													
			spimod.output_(plotattrs1)		
			# self.xmin,self.xmax,self.ymin,self.ymax = spimod.xmin,spimod.xmax,spimod.ymin,spimod.ymax
		if (('cont' not in model.lower())&('all' not in arm)):	
			self.armrec.append(arm)					
			plotattrs1 = plotattrs.copy()													
			spimod.output_(arm)
			getangular(spimod)
			self.dout = spimod.dout.copy() 													
			if plotattrs1['armcolour'] == '':
				plotattrs1['armcolour'] = spimod.armcolour[arm]		
			self.xyplot(spimod,plotattrs1)
			_polarproj(spimod,plotattrs1)														
		if (('cont' not in model.lower())&(arm=='all'))  :														
			for arm_temp in spimod.arms:			
				plotattrs1 = plotattrs.copy()			
				spimod.output_(arm_temp)
				getangular(spimod)											
				if plotattrs1['armcolour'] == '':
					plotattrs1['armcolour'] = spimod.armcolour[arm_temp]
					self.xyplot(spimod,plotattrs1)
					_polarproj(spimod,plotattrs1)																							
		try:	
			add_polargrid(plotattrs1,xmin=self.xmin,xmax=self.xmax,ymin=self.ymin,ymax=self.ymax,modrec=self.modrec,armrec=self.armrec)	
		except AttributeError:
			pass										
									
class _make_supportfiles(object):
	"""
	was run to save supporting files
	
	"""
	
	def __init__(self):
					
		self.xsun = -8.277	
	
		# self.prep_poggio_polar()
		self.savelims_all()
		self.savelims()	
	def prep_poggio_polar(self):	
		'''
		saves the poggio contours for polarprojection
		'''
	
		xsun=self.xsun
		usemodels = ['Poggio_cont_2021','GaiaPVP_cont_2022']	
		
		for usemodel in usemodels:
			
			plt.close('all')
			plotattrs = {'plot':True,'coordsys': 'HC','markersize':15,'linewidth':1,'polarproj':False,'armcolour':'black'}	
			sp = spiral_poggio_maps(model_=usemodel)
			sp.xsun = xsun
			cset1,cset2 = sp.output_(plotattrs)
			
			# # check xy projection
			# plt.ion()
			# plt.close('all')
			# [[plt.plot(q[:,0],q[:,1], c='C%d'%c) for q in Q]  for c,Q in enumerate(cset1.allsegs)]
			# # # # plt.savefig(root_+'/test_xy.png')	
			
				
			tst = [[(q[:,0],q[:,1]) for q in Q]  for c,Q in enumerate(cset1.allsegs)]
			
			plt.ion()
			plt.close('all')
			fig, ax = plt.subplots(figsize=(7.5,7.),subplot_kw=dict(projection="polar"))
			
			dsave = {}
			dsave['glon4'] = []
			dsave['dhelio'] = []
			dsave['phi4'] = []
			dsave['rgc'] = []
			for inum,Q in enumerate(cset1.allsegs):
				xc = [q[:,0] for q in Q]
				yc = [q[:,1] for q in Q]
				
				for i in range(len(xc)):
					glon4 = np.degrees(np.arctan2(yc[i],xc[i]))%360.
					dhelio = sqrtsum(ds=[xc[i],yc[i]])
					phi4 = np.degrees(np.arctan2(yc[i],xc[i]+sp.xsun))%360.	
					rgc = sqrtsum(ds=[xc[i]+sp.xsun,yc[i]])
					# plt.plot(np.radians(phi4),rgc,'.') # gc frame
					# plt.plot(np.radians(glon4),dhelio,'.') # hc frame
					dsave['phi4'].append(phi4)
					dsave['rgc'].append(rgc)
					dsave['glon4'].append(glon4)
					dsave['dhelio'].append(dhelio)
	
			
			for ky in dsave.keys():
				dsave[ky] = np.concatenate(dsave[ky]).ravel()	
				
			dsave['ang_gc'] = dsave['phi4'].copy()	
			dsave['ang_hc'] = dsave['glon4'].copy()	
			
			dsave['rad_gc'] = dsave['rgc'].copy()	
			dsave['rad_hc'] = dsave['dhelio'].copy()	
			
			
			picklewrite(dsave,usemodel+'_pproj_contours',dataloc+'/'+usemodel)						
	def savelims_all(self):		
	
		print('saving plot limits for all models')
		xsun=self.xsun
	
		mylims = {}
		
		spirals = main_(xsun=xsun)
		for inum,use_model in enumerate(spirals.models):				
			
			plt.close('all')
		
			mylims[use_model] = {}
			
			plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':False}		
	
			coordsys = plotattrs['coordsys']
	
			spirals.getinfo(model=use_model)
			spirals.readout(plotattrs,model=use_model,arm='all')		
			mylims[use_model]['xmin'+'_'+coordsys] = spirals.xmin
			mylims[use_model]['xmax'+'_'+coordsys] = spirals.xmax
			mylims[use_model]['ymin'+'_'+coordsys] = spirals.ymin
			mylims[use_model]['ymax'+'_'+coordsys] = spirals.ymax
	
			plt.close('all')
			plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polargrid':False}		
			coordsys = plotattrs['coordsys']		
				
			spirals.getinfo(model=use_model)
			spirals.readout(plotattrs,model=use_model,arm='all')
			mylims[use_model]['xmin'+'_'+coordsys] = spirals.xmin
			mylims[use_model]['xmax'+'_'+coordsys] = spirals.xmax
			mylims[use_model]['ymin'+'_'+coordsys] = spirals.ymin
			mylims[use_model]['ymax'+'_'+coordsys] = spirals.ymax
						
		picklewrite(mylims,'flim_all',dataloc)		
	def savelims(self):		
	
		print('saving plot limits for all models')
		xsun=self.xsun
	
		mylims = {}
		
		spirals = main_(xsun=xsun)
		
		for inum,use_model in enumerate(spirals.models):	
						
				
			spimod = spirals.models_class[use_model]
			spimod.getarmlist()
		
			mylims[use_model] = {}
			
			for jnum, arm in enumerate(spimod.arms):
				
				mylims[use_model][arm] = {}

				plt.close('all')
				plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'markSunGC':True,'polargrid':False}		
		
				coordsys = plotattrs['coordsys']
		
				spirals.getinfo(model=use_model)
				spirals.readout(plotattrs,model=use_model,arm=arm)		
				mylims[use_model][arm]['xmin'+'_'+coordsys] = spirals.xmin
				mylims[use_model][arm]['xmax'+'_'+coordsys] = spirals.xmax
				mylims[use_model][arm]['ymin'+'_'+coordsys] = spirals.ymin
				mylims[use_model][arm]['ymax'+'_'+coordsys] = spirals.ymax
		
				plt.close('all')
				plotattrs = {'plot':True,'coordsys':'HC','markersize':15,'markSunGC':True,'polargrid':False}		
				coordsys = plotattrs['coordsys']		
					
				spirals.getinfo(model=use_model)
				spirals.readout(plotattrs,model=use_model,arm=arm)
				mylims[use_model][arm]['xmin'+'_'+coordsys] = spirals.xmin
				mylims[use_model][arm]['xmax'+'_'+coordsys] = spirals.xmax
				mylims[use_model][arm]['ymin'+'_'+coordsys] = spirals.ymin
				mylims[use_model][arm]['ymax'+'_'+coordsys] = spirals.ymax
						
		picklewrite(mylims,'flim',dataloc)	
	


