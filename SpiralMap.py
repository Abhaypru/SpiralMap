


exec(open("./dtools.py").read()) # utilities package


root_ = os.getcwd()
dataloc = root_+'/datafiles'






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

	def output_(self,arm,color='',typ_='cartesian',xsun_=[]):	
		
		if len(xsun_) == 0:
			xsun = get_lsr()['xsun']
		else:
			xsun = xsun_[0]
		
		
		params = self.getparams(arm) ;

		
		
		if typ_ =='cartesian':

			xgc,ygc,xgc1,ygc1,xgc2,ygc2 = self.model_(params);			
			xhc = xgc - xsun
			xhc1 = xgc1 - xsun
			xhc2 = xgc2 - xsun
	
			yhc = ygc
			return xhc,yhc,xgc,ygc
		
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
			
			return 
			
		if typ_ =='polargrid':
			
			linewidth=2
			
			yhc = y
			xgc = x
			phi4 = np.degrees(np.arctan2(yhc,xgc))%360.	
			rgc = sqrtsum(ds=[x,y])

			plt.plot(np.radians(phi4),rgc,color=color,markersize=markersize,linestyle=linestyle,linewidth=linewidth,label=arm)

	

			
			return 


 

class main_(object):
	
	def __init__(self):
		
		self.tst = 'rub'
		self.listmodels()
	
	def listmodels(self):
		
		
		
		self.models = ['Drimmel_NIR_2000','DKPS_ceph_2024','reid_2019','poggio_2021','taylor_cordes_1992']
		self.models_info = []
		self.models_class = {'reid_2019':reid_spiral()}
	



	# def plot_(self,arm,color='',typ_='HC',xsun_=[],linewidth=0.8,markersize=3,linestyle = '-'):	
	def plot_(self,model='',print_=False):
		
		
		if model == '':
			 raise RuntimeError('model = blank | no model provided \n try self.models_class for list of available models')
			 
					


		spimod = self.models_class[model]
		spimod.getarmlist()

		if print_:
			print('model = '+model)
			print(spimod.arms)
		

		xhc,yhc,xgc,ygc = spimod.output_('Perseus')
				
		# return xhc,yhc,xgc,ygc
		return 



