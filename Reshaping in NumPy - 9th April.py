#!/usr/bin/env python
# coding: utf-8

# As explained in the previous lesson, to create a basic NumPy array write:

# In[1]:


import numpy as np
Z = np.array([0,0,0,0,0,0,0,0,0,0,1,0])
print(Z)   


# In[2]:


np.arange(7)


# In[3]:


np.arange(0,15)


# We can **<u>reshape the array in any dimension</u>**
# 
# The basic syntax for reshaping array is:
# 
# #### Z = np.array(1D_array).reshape(x_dimension,y_dimension)

# In[4]:


np.array([0,0,5,6,7,4,3,4,5,6]).reshape(5,2)


# In[7]:


np.arange(0,24).reshape(5,5)


# In[8]:


np.arange(0,24) ## here 23 is the last because stop - 1 


# In[9]:


np.arange(0,25).reshape(5,5)


# Given an array Z. How would you reshape an array in **3 rows and 4 columns**?

# In[10]:


Z = np.array([0,0,0,0,0,0,0,0,0,0,1,0]).reshape(3,4)
Z

