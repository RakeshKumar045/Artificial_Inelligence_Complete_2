#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# get_ipython().run_line_magic('matplotlib', 'inline')

# In[2]:


cust_df = pd.read_csv("Cust_Segmentation.csv")
cust_df.head()

# In[3]:


df = cust_df.drop("Address", axis=1)

# In[4]:


df.head()

# In[5]:


from sklearn.preprocessing import StandardScaler

X = df.values[:, 1:]
X = np.nan_to_num(X)

Scaler = StandardScaler()
clust_data = Scaler.fit_transform(X)

# In[6]:


X

# In[7]:


from sklearn.cluster import KMeans

cluster_num = 3
kmeans = KMeans(init='k-means++', n_clusters=cluster_num, n_init=12)
kmeans.fit(X)
labels = kmeans.labels_
print(kmeans.labels_)

# In[8]:


df['cluster_num'] = labels

# In[9]:


k = np.arange(1, 12)
# sum squered error
# USING ELBOW CURVE DETERMING THE NO OF CLUSTERS
sse = []
for i in k:
    kmeans = KMeans(init='k-means++', n_clusters=i, n_init=12)
    kmeans.fit(X)
    sse.append(kmeans.inertia_)
plt.plot(k, sse)
plt.show()

df.head()

# In[10]:


kmeans = KMeans(init='k-means++', n_clusters=cluster_num, n_init=12)
kmeans.fit(X)

# In[11]:


# checking the centroid values
df.groupby('cluster_num').mean()

# In[12]:


cluster_center = kmeans.cluster_centers_

# In[13]:


print(cluster_center)


# In[14]:


def customer_seg(X):
    if X == 0:
        return "middle-aged and affluent"
    elif X == 2:
        return "middle-aged and middle income"
    else:
        return "young and low income "


# In[20]:


area = np.pi * (X[:, 1]) ** 2
plt.scatter(X[:, 0], X[:, 3], s=area, c=labels.astype(np.float), alpha=0.5)
plt.xlabel('age')
plt.ylabel('income')
plt.show()

# In[16]:


""""as per the group by used abovw,we can label the customer as following
0:"middle-aged and affluent"
2:"middle-aged and middle income"
1:"young and low income "
"""

# In[17]:


df['Customer_grp'] = df['cluster_num'].apply(customer_seg)

# In[18]:


df.head()

# In[ ]:


# In[ ]:
