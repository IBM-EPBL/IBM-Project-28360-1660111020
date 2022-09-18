#!/usr/bin/env python
# coding: utf-8

# In[1]:


s="hi there sam"


# In[2]:


Words=s.split()
print(Words)


# In[3]:


planet = "Earth"
diameter = 12742


# In[4]:


print( 'The diameter of {} is {} kilometers.' .format(planet,diameter));


# In[5]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[6]:


print(d['k1'][3]["tricky"][3]['target'][3])


# In[7]:


import numpy as np


# In[8]:


array=np.zeros(10)
print(array)


# In[9]:


array=np.ones(10)*5
print(array)


# In[10]:


np.arange(20,36)


# In[11]:


x =  np.arange(0, 9).reshape(3,3)
print(x)


# In[12]:


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.concatenate((a,b))


# In[13]:


import pandas as pd


# In[14]:


data = [['Meera', 40], ['Steve', 70], ['Elena', 35]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
df


# In[15]:


p = pd.date_range(start ='1-1-2023', 
         end ='10-02-2023') 
for val in p:
    print(val)


# In[16]:


lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]


# In[17]:


df = pd.DataFrame(lists, columns =['No','Name', 'Age'])
print(df)


# In[ ]:




