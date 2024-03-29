#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Regular Expression Practice

Name:- Sourabh Solanki
Batch:- DS2403
# In[ ]:





# In[ ]:





# In[ ]:


import re


# In[7]:


print(help(re))


# # Question 1-  Write a RegEx pattern in python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

# In[43]:


import re
string = 'MynameisRamandmynumberis0798845577427572557%$%&&*%%'
pattern = ('^[a-zA-Z0-9_]*')

result = re.search(pattern, string)
print(result)


# In[118]:


txt = "The rain in Spain"
x = re.search("^[a-z A-Z 0-9]*", txt)
print(x.string)


# In[ ]:





# In[14]:


import re

def check_string:
    s = 'Ram123795'
    pattern = (r'^[a-zA-Z0-9]*$')
    
result = re.fullmatch(pattern, s)
        
    
print(check_string(result))


# In[54]:


import re

def check_allstring(f):
    pattern = '^[a-zA-Z0-9]*$'
    if re.match(pattern, f):
        return True
    else:
        return False
print(check_allstring("My self 123"))

# it was False beacuse in print there is space between "my self 123" but in pattern there is no space between a-zA-Z0-9


# In[55]:


import re

def check_allstring(f):
    pattern = '^[a-z A-Z 0-9]*$'
    if re.match(pattern, f):
        return True
    else:
        return False
print(check_allstring("My self 123"))
# if can can changing the pattern like this "a-z A-Z 0-9" it will give us True output
#because its have a space between "My self 123"


# # Question 2- Write a RegEx pattern that matches a string that has an a followed by zero or more b's
# 
# 

# In[36]:


import re


string = 'hello bs bs bs bs '
pattern = ("[bs]*")
result = re.findall(pattern, string)
print(result)


# # -  Write a RegEx pattern that matches a string that has an a followed by one or more b's

# In[25]:


import re

txt = 'abs finghjim bs vbs hbsf jbsv'
pattern = ('[bs]+')
result = re.findall(pattern, txt)
print(result)


# # Write a RegEx pattern that matches a string that has an a followed by zero or one 'b'.

# In[40]:


import re 

txt = 'hello b i am very habpy to expressb'
pattern = ("[b]?+")
result = re.findall(pattern, txt)
print(result)


# # Question 5- Write a RegEx pattern in python program that matches a string that has an a followed by three 'b'.

# In[109]:


import re

txt = "ram is going to b the place and it was play b time. it was hungry b. it helps some b people"
pattern = r"\b(b
result = re.findall(pattern, txt,)
print(result)


# # Question 6- Write a RegEx pattern in python program that matches a string that has an a followed by two to three 'b'.

# In[46]:


import re
txt = 'ethyl borate B (OC2H5)3 and methyl borate B (OCH 3) 3 are obtained'
pattern = 'B {2}'
match = re.findall(pattern, txt)
print(match)


# In[ ]:





# # Question 7- Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# In[6]:


import re
txt = 'alok is a good alphabetical learner '
pattern = 'a[a-zA-Z0-9]+b'
output = re.findall(pattern,txt)
print(output)


# In[ ]:





# # Question 8- Write a RegEx pattern in python program that matches a word at the beginning of a string

# In[22]:


import re
txt = 'He was going to like the clothes she bought for the trip.'
pattern = '^\A\w+'
match = re.findall(pattern, txt)
print(match)


# In[ ]:





# # Question 9- Write a RegEx pattern in python program that matches a word at the end of a string.

# In[24]:


import re
txt = 'He was going to like the clothes she bought for the trip'
pattern = '\w+$'
match = re.findall(pattern, txt)
print(match)


# In[ ]:





# # Question 10- Write a RegEx pattern in python program to find all words that are 4 digits long in a string.
# Sample text- '01 0132 231875 1458 301 2725.'
# Expected output- ['0132', '1458', '2725']
# 

# In[89]:


import re

txt = "01 0132 231875 1458 301 2725"
pattern = r"\b\d{4}\b"

result = re.findall(pattern, txt)
print(result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




