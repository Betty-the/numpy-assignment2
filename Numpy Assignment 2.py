#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np

# create a vector of length 5 filled with random integers from 0 to 10
vec = np.random.randint(low=0, high=11, size=5)

print(vec)


# In[43]:


import numpy as np
 
#create a vector with values arranging from 15 to 55
vec = np.arange(15, 55)
#print(vec)

#except the first and last of vec
vec1 = (v[1:-1])
print(vec1)


# In[50]:


import numpy as np

#create a random array with 1000 elements
arr = np.random.rand(1000)
print(arr)


# In[54]:


mean = np.mean(arr)
print("average", mean)


# In[56]:


variance = np.var(arr)
print("variance", variance)


# In[59]:


st_deviation = np.std(arr)
print("Standard deviation", st_deviation)


# In[30]:


import numpy as np

#Define 3*3 array
array = np.array([[11,12,13], [14,15,16], [17,18,19]])
print("Original array:\n", array) 

#Calculate cumulative sum of the element along axis
cumu_sum_rows = np.cumsum(array, axis=1)
print("\nCumulative sum of elements along rows:\n", cumu_sum_rows)

#Calculate sum over rows for each 3 columns
sum_over_rows = np.sum(array, axis=0)
print("\nsum over rows for each colum:\n", sum_over_rows)

#Calculate sum over columns for each 2 rows
sum_over_columns = np.sum(array, axis=1)
print("\nsum over colums for each row:\n", sum_over_columns)


# In[28]:


import numpy as np

#Define the matrices
matrix = np.array([[1,0], [0,1]])
print("matrix:\n", matrix)

matrix1 = np.array([[1,2], [3,4]])
print("\nmatrix1:\n", matrix1)

#Multiple the matrices
Answer = np.dot(matrix, matrix1)
print("\nAnswer:\n", Answer)


# In[ ]:




