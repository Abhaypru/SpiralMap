

import os, sys
import numpy as np
from astropy.table import Table
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

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



def fitsread(filename,ext=1):
	
	from astropy.io import fits    
	
	data1=np.array(fits.getdata(filename,ext))
	# data1=(fits.getdata(filename,ext))
	data={}
	for x in data1.dtype.names:
		data[x.lower()]=data1[x]
		
	return data

def pickleread(file1):
	
	'''
	read pickle files
	input: fileloc+'/'+filename
	
	'''
	import pickle	
	data = pickle.load(open(file1,'rb'))	
	
	
	return data

def sqrtsum(ds=[],prnt=False):
	'''
	handy function to sum up the squares and return the square-root
	'''
	
	if prnt:
		print(len(ds))
	
	mysum = 0
	for i in range(len(ds)):
		
		
		tmp = ds[i]**2.
		mysum+=tmp
	
	
	resval = np.sqrt(mysum)
	
	
	return resval

