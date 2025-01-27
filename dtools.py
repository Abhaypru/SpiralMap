

import os, sys
import numpy as np

def fcount(floc,flist=False,nlist=False):
	
	'''
    NAME: fcount

    PURPOSE: counts the number of files in a given directory


    INPUT: file location 

    OUTPUT: number count 
       
    HISTORY: October 27, 2022 (INAF Torino)
    	
	'''
	
	
	cnt = []
	
	for fl in os.listdir(floc):
		cnt.append(fl)
		
	cnt = np.array(cnt)	
	
	
	print(str(cnt.size)+' files in total')
	
	if flist:
		# os.system('ls -lh '+floc)	
		return cnt
	elif nlist:
		return cnt.size	
	else:
		os.system('ls -lh '+floc)	
		return 

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
	
	




