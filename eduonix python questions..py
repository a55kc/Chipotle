#!/usr/bin/env python
# coding: utf-8

# # Python

# 1.Write a program using list comprehension to find primes 
# in range 2 to 100.

# In[1]:


print([x for x in range(2, 100) if all(x % y for y in range(2, x//2))])


# 2.Write a function to reverse a string

# string='reverse a string'

# In[2]:


string = 'reverse a string'


# In[3]:


string = string[::-1]


# In[4]:


print(string)


# 3.Write a program to extract the words from the given list which have their first character in uppercase. Days = ['Monday', 'tuesday','friday', 'Sunday', 'Saturday']
# 
# Output: ['Monday', 'Sunday', 'Saturday'

# In[5]:


Days = ['Monday', 'tuesday','friday', 'Sunday', 'Saturday']


# In[6]:


for i in Days:
    if i[0].isupper():
        print(i)


# 4.Write a program to extract the year part from the dates in 
# the given list.
# 
# Batch = ['15-06-1997','15-06-2011','15-06-1993','15-06-2020']
# 
# Output: ['1997','2011','1993','2020']

# In[7]:


Batch = ['15-06-1997','15-06-2011','15-06-1993','15-06-2020']


# In[8]:


print(Batch)


# In[9]:


for i in Batch:
    year = i.split('-')[2]
    print(year)


# 5.Write a program swap the keys to values and values to keys of the given dictionary. 
# 
# Module = {'Data Science':1,'Machine Learning':2, 'SQL':3, 'Big Data':4} 
# 
# Output: {1:'Data Science',2:'Machine Learning', 3:'SQL', 4:'Big Data'}

# In[10]:


Module = {'Data Science':1,'Machine Learning':2, 'SQL':3, 'Big Data':4}
print(Module)


# In[11]:


swap = {value:key for key, value in Module.items()}
print(swap)


# 6.Write a program to count the number of elements in the string (given by the user) that are not present in the 'my_string'. 
# 
# Do not count the white spaces.
# 
# my_string = 'Data Science'

# In[16]:


my_string = 'Data Science'
string = input("Enter a string: ")
count = 0
for i in string:
    if i not in my_string and i != '  ':
        count += 1
print("The number of elements in the string that are not present in 'my_string' is:", count)


# In[ ]:





# In[ ]:





# 7.Define a function to check whether a number is in a range (1000,10000) or not.

# In[17]:


def RangeChecker (num): 
    
    return 1000 <= num <= 10000
    


# In[18]:


RangeChecker(6985)


# In[19]:


RangeChecker(458785)


# 8.Write a program to calculate the sum of all elements in the list.
# 
# test_score = [10, 32, 23, 14, 25]

# In[20]:


test_score = [10, 32, 23, 14, 25]
test_score


# In[21]:


test_score = [10, 32, 23, 14, 25]
sum_of_scores = sum(test_score)
print("The sum of all elements in the list is:", sum_of_scores)


# 9.Replace all even numbers in the array with -1.
# 
# Use the array given below num_array = np.array([0, 21, 32, 13, 44, 45, 26, 28, 38, 34, 65, 48, 76])

# In[22]:


import numpy as np

num_array = np.array([0, 21, 32, 13, 44, 45, 26, 28, 38, 34, 65, 48, 76])

num_array[num_array % 2 == 0] = -1

print(num_array)


# 10.Find the minimum value along each of the rows. 
# 
# Create a 2D Numpy array from list of lists 
# 
# Score = np.array([[210, 402, 383], [140, 375, 106], [140, 125, 217], [292, 240, 295]])

# In[23]:


import numpy as np

Score = np.array([[210, 402, 383], [140, 375, 106], [140, 125, 217], [292, 240, 295]])


# In[24]:


print(Score)


# In[25]:


min_score = np.min(Score, axis=1)

print(min_score)


# In[ ]:





# In[ ]:





# In[ ]:




