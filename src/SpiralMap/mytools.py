#######################################################################
# Helper functions
#######################################################################

import os, sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from tabulate import tabulate
from astropy.table import Table
from scipy.interpolate import CubicSpline

def sqrtsum(ds=[],prnt=False):	

	if prnt:
		print(len(ds))	
	mysum = 0
	for i in range(len(ds)):		
		tmp = ds[i]**2.
		mysum+=tmp	
	resval = np.sqrt(mysum)	
	return resval

def fcount(floc,flist=False,nlist=False,prnt=True):
	cnt = []	
	for fl in os.listdir(floc):
		cnt.append(fl)		
	cnt = np.array(cnt)		
	if prnt:
		print(str(cnt.size)+' files in total')	
	if flist:		
		return cnt
	elif nlist:
		return cnt.size	
	else:
		os.system('ls -lh '+floc)	
		return 

def xyz2lbr(x,y,z):
    rc2=x*x+y*y
    return [np.degrees(np.arctan2(y,x)),np.degrees(np.arctan(z/np.sqrt(rc2))),np.sqrt(rc2+z*z)]

def fitsread(filename,ext=1):
	
	from astropy.io import fits    
	
	data1=np.array(fits.getdata(filename,ext))
	# data1=(fits.getdata(filename,ext))
	data={}
	for x in data1.dtype.names:
		data[x.lower()]=data1[x]
		
	return data

def picklewrite(data,nam,loc,prnt=True):
	# # '''
	# # write files using pickle
	# # '''	
	import pickle	
	pickle.dump(data,open(loc+'/'+nam+'.pkl','wb'))	
	if prnt:
		print(nam+' .pkl written to '+loc)	
		
	return 

def pickleread(file1):	
	# # '''
	# # read pickle files
	# # input: fileloc+'/'+filename	
	# # '''
	import pickle	
	data = pickle.load(open(file1,'rb'))	
	
	
	return data

def add_polargrid(plotattrs,rlevels=12,xmin=-10,xmax=10,ymin=-10,ymax=10,modrec=[],armrec=[],xorig = 0.,rmin = 3):
	coordsys = plotattrs['coordsys']

	if ((plotattrs['plot']==True)&(plotattrs['polarproj']==False)&(plotattrs['polargrid'])):
		

		if armrec == []:						
			flim = pickleread(plotattrs['dataloc']+'/flim_all.pkl')	
			xmins = [flim[model]['xmin'+'_'+coordsys] for model in modrec]
			xmaxs = [flim[model]['xmax'+'_'+coordsys] for model in modrec]
			ymins = [flim[model]['ymin'+'_'+coordsys] for model in modrec]
			ymaxs = [flim[model]['ymax'+'_'+coordsys] for model in modrec]
		else:
			arm = armrec[0]
			flim = pickleread(plotattrs['dataloc']+'/flim.pkl')	
			xmins = [flim[model][arm]['xmin'+'_'+coordsys] for model in modrec]
			xmaxs = [flim[model][arm]['xmax'+'_'+coordsys] for model in modrec]
			ymins = [flim[model][arm]['ymin'+'_'+coordsys] for model in modrec]
			ymaxs = [flim[model][arm]['ymax'+'_'+coordsys] for model in modrec]
			
		try:
			xmin1 = np.nanmin(xmins)
			xmax1 = np.nanmax(xmaxs)
			ymin1 = np.nanmin(ymins)
			ymax1 = np.nanmax(ymaxs)
		except ValueError:
			xmin1 = xmins
			xmax1 = xmaxs
			ymin1 = ymins
			ymax1 = ymaxs				

		rvals = np.array([rmin + rmin*i for i in range(rlevels)])
		for r in rvals:
			ang = np.radians(np.linspace(0.,360.,100))
			x = r*np.cos(ang)
			y = r*np.sin(ang)	
			indg = np.where((x>xmin)&(x<xmax)&(y>ymin)&(y<ymax))[0]				
			plt.plot(x + xorig,y,color='grey',linewidth=0.5)		

		rvals = np.array([0 + i for i in range(rlevels*10)])			
		for l in np.arange(0.,360.,30):		
			l=np.radians(l)				
			x = np.array([r*np.cos(l) for r in rvals])
			y = np.array([r*np.sin(l) for r in rvals])								
			plt.plot(x + xorig,y,color='grey',linewidth=0.5)		
		plt.axis([xmin1,xmax1,ymin1,ymax1])

def _polarproj(spimod,plotattrs):		
	
	useclr = plotattrs['armcolour']
	if plotattrs['armcolour'] == '':
		useclr = 'grey'
			
	if plotattrs['plot'] and plotattrs['polarproj'] and plotattrs['coordsys'].lower()=='gc':	
													
		plt.plot(0.,0.,marker='*',markersize=plotattrs['markersize'],color='black')		
		plt.plot(np.radians(180.),abs(spimod.xsun),marker=r'$\odot$',markersize=plotattrs['markersize'],color='black')				

		if plotattrs['linestyle'] == '-': 
			plt.plot(np.radians(spimod.dout['phi4']),spimod.dout['rgc'],plotattrs['linestyle'],linewidth=plotattrs['linewidth'],color=useclr)	
		if plotattrs['linestyle'] == '.': 
			plt.plot(np.radians(spimod.dout['phi4']),spimod.dout['rgc'],plotattrs['linestyle'],markersize=plotattrs['markersize'],color=useclr)			

		try:
			plt.plot(np.radians(spimod.dout['phi4_ex']),spimod.dout['rgc_ex'],'.',color=useclr)	
		except KeyError:
			pass
	if plotattrs['plot'] and plotattrs['polarproj'] and plotattrs['coordsys'].lower()=='hc':
		plt.plot(np.radians(0.),abs(spimod.xsun),marker='*',markersize=plotattrs['markersize'],color='black')
		plt.plot(0.,0.,marker=r'$\odot$',markersize=plotattrs['markersize'],color='black')																

		if plotattrs['linestyle'] == '-': 
			plt.plot(np.radians(spimod.dout['glon4']),spimod.dout['dhelio'],plotattrs['linestyle'],linewidth=plotattrs['linewidth'],color=useclr)	
		if plotattrs['linestyle'] == '.': 
			plt.plot(np.radians(spimod.dout['glon4']),spimod.dout['dhelio'],plotattrs['linestyle'],markersize=plotattrs['markersize'],color=useclr)	
			
		try:
			plt.plot(np.radians(spimod.dout['glon4_ex']),spimod.dout['dhelio_ex'],'--',color=useclr)				
		except KeyError:
			pass
	
def getangular(spimod):

	spimod.dout['rgc'] = sqrtsum(ds=[spimod.dout['xgc'],spimod.dout['ygc']])						
	spimod.dout['phi1'] = np.arctan2(spimod.dout['yhc'],-spimod.dout['xgc'])
	spimod.dout['phi4'] = np.degrees(np.arctan2(spimod.dout['yhc'],spimod.dout['xgc']))%360.	
	spimod.dout['glon4'] = np.degrees(np.arctan2(spimod.dout['yhc'],spimod.dout['xhc']))%360.	
	spimod.dout['glon'],spimod.dout['glat'],spimod.dout['dhelio'] = xyz2lbr(spimod.dout['xhc'],spimod.dout['yhc'],0)

	
	if 'xhc_ex' in 	spimod.dout.keys():			

		spimod.dout['rgc_ex'] = sqrtsum(ds=[spimod.dout['xgc_ex'],spimod.dout['ygc_ex']])						
		spimod.dout['phi1_ex'] = np.arctan2(spimod.dout['yhc_ex'],-spimod.dout['xgc_ex'])
		spimod.dout['phi4_ex'] = np.degrees(np.arctan2(spimod.dout['yhc_ex'],spimod.dout['xgc_ex']))%360.	
		spimod.dout['glon4_ex'] = np.degrees(np.arctan2(spimod.dout['yhc_ex'],spimod.dout['xhc_ex']))%360.	
		spimod.dout['glon_ex'],spimod.dout['glat_ex'],spimod.dout['dhelio_ex'] = xyz2lbr(spimod.dout['xhc_ex'],spimod.dout['yhc_ex'],0)

def png2movie(readdir,savdir,flname='movie',fmt='gif',duration=1.):
	####
	# Note: works with the older version of imageio (2.27)
	# Purpose: make a gif from set of images
	# readdir = directory where set of images are
	# savdir = directory where to save the final movie
	# flname = filename	
	#dtools.png2movie(desktop+'/snaps/',desktop)	
	####
	
	from PIL import Image as image
	import imageio	
	print(imageio.__version__)
	import natsort
	from natsort import natsorted, ns
	
	images = [] 
	filenames = os.listdir(readdir)
	filenames = natsorted(filenames)
	filenames = np.array(filenames)
	
	fps = 1./duration
	
	for filename in filenames:
		filename = readdir+'/'+filename 
		images.append(imageio.imread(filename))
		
	if fmt == 'gif':	
		imageio.mimsave(savdir+'/'+flname+'.gif', images,duration=duration)	

	elif fmt == 'mp4':
		imageio.mimsave(savdir+'/'+flname+'.mp4', images,fps=fps)	
	
	
	return

def polar_style(ax,title='',rticks=[3., 6.,9.,12,15.,20.]):
	
	ax.set_rticks(rticks)	
	rlabels = ax.get_ymajorticklabels()
	for label in rlabels:
	    label.set_color('blue')
	    label.set_size(fontsize=10)
	ax.yaxis.grid(linewidth=1.5)	    
	plt.title(title)
	return



