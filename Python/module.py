#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(*n):
    s = 0
    for i in n:
        s +=i
    return s


# In[2]:


def multip(*n):
    m = 1
    for i in n:
        m *=i
    return m


# In[3]:


def check(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


# In[ ]:




