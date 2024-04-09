#!/usr/bin/env python
# coding: utf-8

# In[2]:


from IPython.display import display, HTML
display(HTML('<style>.container {width: 90% !important}.</style>'))


# In[3]:


import numpy


# # **Create an Array of Zeros**
# 
# To create a numpy array containing zeros, write: **np.zeros(size)**
# 
# To create an array of size 9 write: np.zeros(9)
# 
# Here is how this array is stored in memory:

# ![Screenshot%202024-04-09%20at%206.56.04%E2%80%AFPM.png](attachment:Screenshot%202024-04-09%20at%206.56.04%E2%80%AFPM.png)

# In[6]:


Z = np.zeros(19)
print(Z)


# # Create an Array of Ones
# 
# To create a numpy array containing ones, write: **np.ones(size).**
# 
# To create an array of size 9 write: np.ones(9)
# 
# Here is how this array is stored in memory:

# In[9]:


Z = np.ones(9)
print(Z)


# # Create an Array of 0’s and 1’s
# 
# To create an array of zeros and ones, use **np.array([1,0,0,0,0,0,1,0]):**
# 
# Here is how the array is stored in memory:

# ![Screenshot%202024-04-09%20at%207.06.46%E2%80%AFPM.png](attachment:Screenshot%202024-04-09%20at%207.06.46%E2%80%AFPM.png)

# In[11]:


z = np.array([1,0,0,0,0,0,1,0])
z


# # Create an Array of 2’s

# To create an array of 2’s write: **2*np.ones(size).**
# 
# To create an array of 2’s of size 9 write: **2*np.ones(9).**
# 
# Here is how the array is stored in memory:

# ![Screenshot%202024-04-09%20at%207.09.47%E2%80%AFPM.png](attachment:Screenshot%202024-04-09%20at%207.09.47%E2%80%AFPM.png)

# In[12]:


Z = 2*np.ones(9)
print(Z)


# # Create a NumPy Array of any Length
# 
# To create an array of any length write: **np.arange(size).**
# 
# To create an array of size 9 write : np.arange(9).

# In[13]:


import numpy as np
Z = np.arange(9)
print(Z)


# # Reshape a NumPy Array into a Column Vector
# 
# To reshape a numpy array,write: **np.arange(size).reshape(size,1).**
# 
# To reshape a numpy array into 9 rows and 1 column ,write: np.arange(9).reshape(9,1).
# 
# Here is how the array is stored is stored in memory:

# ![Screenshot%202024-04-09%20at%207.57.36%E2%80%AFPM.png](attachment:Screenshot%202024-04-09%20at%207.57.36%E2%80%AFPM.png)

# In[14]:


import numpy as np  
Z = np.arange(9).reshape(9,1)
print(Z)


# # Generate Array of Random Numbers and in Grid Format
# 
# To generate an array of random size, write: **np.random.randint(0,size,(x_dimension,y_dimension)).**
# 
# To generate an array of random numbers from 0 to 9 and x dimension 3 and y dimension 3, write: np.random.randint(0,9,(3,3)).
# 
# Here is how the array is stored in memory:

# ![Screenshot%202024-04-09%20at%208.01.41%E2%80%AFPM.png](attachment:Screenshot%202024-04-09%20at%208.01.41%E2%80%AFPM.png)

# In[16]:


np.random.randint(0,9,(3,3))


# In[23]:


np.random.randint(0,9)


# In[25]:


np.random.randint(5)


# # Create a Linspace
# 
# To create **evenly spaced numbers over a specified interval**
# 
# write : **np.linspace(start, stop, size)**

# In[27]:


Z = np.linspace(0, 1, 5)
Z


# ### Create a null vector of size 10 but the fifth value which is 1?

# In[29]:


import numpy as np
Z=np.zeros(10)
Z[4]=1
Z


# ### Create a 3x3 matrix with values ranging from 0 to 8?

# In[34]:


np.arange(9).reshape(3,3)

