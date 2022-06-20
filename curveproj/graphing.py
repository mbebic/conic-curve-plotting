#!/usr/bin/env python
# coding: utf-8

# In[42]:


from plotly.offline import download_plotlyjs, plot
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import pandas as pd


# In[43]:


#general canonical form for ellipse with xc = 1, yc = 1, a =2, b=1
a = 0.25
b = 0
c = 1
d = -0.5
e = -2
f = 0.25


# In[44]:


mx = np.array([[a,b/2],[b/2,c]])
print(mx)


# In[45]:


[lam1,lam2] = np.linalg.eig(mx)[0]
print(lam1, lam2)


# In[46]:


mx2 = np.array([[a,b/2,d/2],[b/2,c,e/2],[d/2,e/2,f]])
print(mx2)


# In[47]:


s = np.linalg.det(mx2)
print(s)


# In[48]:


a = np.sqrt(-s/(lam1**2*lam2))
b = np.sqrt(-s/(lam1*lam2**2))
print(a,b)


# In[49]:


xc = -d*a**2/2
yc = -e*b**2/2
print(xc,yc)


# In[66]:


theta = np.linspace(0,2*np.pi,200)
x = xc+a*np.cos(theta)
y = yc+b*np.sin(theta)


# In[70]:


fig = px.line(x=x,y=y)
fig.show()


# In[72]:


fig.update_layout(autosize=False)


# In[73]:


graph = fig.to_html(full_html=False, default_height=600, default_width=600)
f = open('graph.html', "w")
f.write(graph)
f.close()


# In[ ]:




