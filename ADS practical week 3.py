#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
pi=3.14
print(np.pi)


# In[2]:



for rad in range(2,20,2):
    A=4*np.pi*rad**2
    V=4/3*np.pi*rad**3
    print(A, V)


# In[4]:


#Write a loop, which reads three numbers from the keyboard and prints the sum and the
#average at the end.
sum =0
for i in range(3):
    num=int(input('pick number'))
    sum+=num
avg=sum/3
          
print(sum, avg)


# In[6]:


for i in range(10):
    x=int(input("print enter 10 numbers"))
    np.arange(10)= x
    print(x)


# In[24]:


# get every other row
a = np.arange(27.).reshape(9, 3)
print(a)
print(a[::2])

# get diagonal values in the 5x5 array using fancy indexing
b = np.arange(25).reshape(5, 5)
print(b)
print(b[[0, 1, 2, 3, 4],[0, 1, 2, 3, 4]])

# use Boolean array to create 1d array of selection
c = np.array([[0., 1., 2.], [2., 3., 4.]])
d = np.array([[True, False, False], [False, True, True]])
print(c[d])

# create and use the Boolean array to selectively change data
e = np.arange(9.).reshape(3, 3)
f = e>5  # select values greater than 5.0
e[f] = 10.  # make all values greater than 5.0 to 10.0
print(e)
# or you can simply do
e = np.arange(9.).reshape(3, 3)
e[e>5] = 10.0


# In[30]:


l=int(input("enter the limit"))
x=int(input("enter the numbers")
for i in range(5):
      
  


# In[10]:


import numpy as np
def get(value):
    value=int(input("enter numbers"))
    return value

arr = np.array([])
l=int(input("Enter  how many rows"))
k=int(input("Enter  how many coloums"))

for value in range(l):
    for value in range(k):
        arr = np.append(arr,get(value))
        
print(arr.reshape(l,k))

np.sort(arr.reshape(l,k))


# In[ ]:





# In[ ]:




