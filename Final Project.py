#!/usr/bin/env python
# coding: utf-8

# In[88]:


#Brandon Barkauskas
#Datasets:
#Horizontal: a10_ct1, a05_ct1, a07_ct1
#Vertical: 33RO20130803_ct1, 33RO20131223_ct1
#Mixed: a02b_ct1, 316N20111106_ct1
#Code imports data for first ~20m of seawater for each data point, and calculates average temperature/salinity for that range.
#Longitude and latitude positions are pulled for each data point.
#Temperature is measured on the ITS-90 scale, in Celsius.
#Salinity is measured on the PSS-78 scale, a unitless salinity measurement.

import matplotlib.pyplot as plt
import numpy as np
import glob

path = 'C:/users/admin/a05_ct1/*.csv'
filenames = glob.glob(path)
wholedata = np.ndarray(shape=(112, 4))
    
i = 0

for f in filenames: 
    data = np.genfromtxt(fname=f,  delimiter=",", skip_header=20, max_rows=11)
    coords= np.genfromtxt(fname=f, delimiter="=", autostrip=True, skip_header=15, max_rows=2)
    wholedata[i,0] = np.average(data[:, 2])
    wholedata[i,1] = np.average(data[:, 4])
    wholedata[i,2] = coords[0,1]
    wholedata[i,3] = coords[1,1]
    i= i+1


# In[49]:


path = 'C:/users/admin/a10_ct1/*.csv'
filenames = glob.glob(path)
wholedata2 = np.ndarray(shape=(100, 4))

i = 0

for f in filenames: 
    data = np.genfromtxt(fname=f,  delimiter=",", skip_header=20, max_rows=11)
    coords= np.genfromtxt(fname=f, delimiter="=", autostrip=True, skip_header=15, max_rows=2)
    wholedata2[i,0] = np.average(data[:, 2])
    wholedata2[i,1] = np.average(data[:, 4])
    wholedata2[i,2] = coords[0,1]
    wholedata2[i,3] = coords[1,1]
    i= i+1


# In[53]:


path = 'C:/users/admin/a07_ct1/*.csv'
filenames = glob.glob(path)
wholedata3 = np.ndarray(shape=(120, 4))
    
i = 0

for f in filenames: 
    data = np.genfromtxt(fname=f,  delimiter=",", skip_header=20, max_rows=11)
    coords= np.genfromtxt(fname=f, delimiter="=", autostrip=True, skip_header=15, max_rows=2)
    wholedata3[i,0] = np.average(data[:, 2])
    wholedata3[i,1] = np.average(data[:, 4])
    wholedata3[i,2] = coords[0,1]
    wholedata3[i,3] = coords[1,1]
    i= i+1


# In[119]:


plt.plot(wholedata[:,3], wholedata[:,0], label='25')
plt.plot(wholedata2[:,3], wholedata2[:,0], label='-30')
plt.plot(wholedata3[:,3], wholedata3[:,0], label='-5')
plt.xlabel('Longitude')
plt.ylabel('Temperature')
plt.title('Longitude vs Temperature')
plt.legend()


# In[122]:


plt.plot(wholedata[:,3], wholedata[:,1], label='25')
plt.plot(wholedata2[:,3], wholedata2[:,1], label='-30')
plt.plot(wholedata3[:,3], wholedata3[:,1], label='-5')
plt.xlabel('Longitude')
plt.ylabel('Salinity')
plt.title('Longitude vs Salinity')
plt.legend()


# In[123]:


plt.plot(wholedata[:,1], wholedata[:,0], label='25')
plt.plot(wholedata2[:,1], wholedata2[:,0], label='-30')
plt.plot(wholedata3[:,1], wholedata3[:,0], label='-5')
plt.xlabel('Salinity')
plt.ylabel('Temperature')
plt.title('Salinity vs Temperature')
plt.legend()


# In[82]:


path = 'C:/users/admin/33RO20130803_ct1/*.csv'
filenames = glob.glob(path)
wholedata4 = np.ndarray(shape=(145, 4))
    
i = 0

for f in filenames: 
    data = np.genfromtxt(fname=f,  delimiter=",", skip_header=18, max_rows=17)
    coords= np.genfromtxt(fname=f, delimiter="=", autostrip=True, skip_header=13, max_rows=2)
    wholedata4[i,0] = np.average(data[:, 2])
    wholedata4[i,1] = np.average(data[:, 4])
    wholedata4[i,2] = coords[0,1]
    wholedata4[i,3] = coords[1,1]
    i= i+1


# In[71]:


path = 'C:/users/admin/33RO20131223_ct1/*.csv'
filenames = glob.glob(path)
wholedata5 = np.ndarray(shape=(113, 4))

i = 0

for f in filenames: 
    data = np.genfromtxt(fname=f,  delimiter=",", skip_header=53, max_rows=17)
    coords= np.genfromtxt(fname=f, delimiter="=", skip_header=48, max_rows=2)
    wholedata5[i,0] = np.average(data[:, 2])
    wholedata5[i,1] = np.average(data[:, 4])
    wholedata5[i,2] = coords[0,1]
    wholedata5[i,3] = coords[1,1]
    i= i+1


# In[100]:


plt.plot(wholedata4[:,2], wholedata4[:,0])
plt.plot(wholedata5[:,2], wholedata5[:,0])
plt.xlabel('Latitude')
plt.ylabel('Temperature')


# In[107]:


plt.plot(wholedata4[:,2], wholedata4[:,1])
plt.plot(wholedata5[:,2], wholedata5[:,1])
plt.xlabel('Latitude')
plt.ylabel('Salinity')


# In[109]:


plt.plot(wholedata4[:,1], wholedata4[:,0])
plt.plot(wholedata5[:,1], wholedata5[:,0])
plt.xlabel('Salinity')
plt.ylabel('Temperature')


# In[104]:


path = 'C:/users/admin/a02b_ct1/*.csv'
filenames = glob.glob(path)
wholedata6 = np.ndarray(shape=(79, 4))
    
i = 0

for f in filenames: 
    data = np.genfromtxt(fname=f,  delimiter=",", skip_header=20, max_rows=10)
    coords= np.genfromtxt(fname=f, delimiter="=", skip_header=15, max_rows=2)
    wholedata6[i,0] = np.average(data[:, 2])
    wholedata6[i,1] = np.average(data[:, 4])
    wholedata6[i,2] = coords[0,1]
    wholedata6[i,3] = coords[1,1]
    i= i+1


# In[79]:


path = 'C:/users/admin/316N20111106_ct1/*.csv'
filenames = glob.glob(path)
wholedata7 = np.ndarray(shape=(65, 4))
    
i = 0

for f in filenames: 
    data = np.genfromtxt(fname=f,  delimiter=",", skip_header=15, max_rows=17)
    coords= np.genfromtxt(fname=f, delimiter="=", skip_header=9, max_rows=2)
    wholedata7[i,0] = np.average(data[:, 2])
    wholedata7[i,1] = np.average(data[:, 4])
    wholedata7[i,2] = coords[0,1]
    wholedata7[i,3] = coords[1,1]
    i= i+1


# In[105]:


plt.plot(wholedata6[:,2], wholedata6[:,0])
plt.plot(wholedata7[:,2], wholedata7[:,0])
plt.xlabel('Latitude')
plt.ylabel('Temperature')


# In[106]:


plt.plot(wholedata6[:,3], wholedata6[:,0])
plt.plot(wholedata7[:,3], wholedata7[:,0])
plt.xlabel('Longitude')
plt.ylabel('Temperature')


# In[108]:


plt.plot(wholedata6[:,1], wholedata6[:,0])
plt.plot(wholedata7[:,1], wholedata7[:,0])
plt.xlabel('Salinity')
plt.ylabel('Temperature')


# In[ ]:




