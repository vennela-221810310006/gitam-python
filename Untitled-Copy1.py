#!/usr/bin/env python
# coding: utf-8

# In[1]:


4+5


# # Markdown Basics
# ## Markdown Basics
# ### Markdowm Bascis
# #### Markdowm Bascis
# ##### Markdowm Bascis
# ###### Markdowm Bascis
# ###### #Markdowm Bascis
# 
# 
#   
# 

# **point 1**
# 
# *point 1*
# 
# ***point 1***

# # Python Basics
# - Python version 3.7
# - functional programming
# - object orented programming
# - Scripting programming
# 

# In[2]:


print("hello")


# In[3]:


print("Gitam")
print("Hyderbad")


# In[6]:


print("hello,GITAM","|||",end ="")
print("HYDERBAD","|||",end ="")
print("Python Programming")


# In[7]:


n1=100
print(n1)


# In[8]:


n1=100
a=b=c=20
print(n1)
print(a,b,c)
print(a1,b1,c1)


# In[9]:


n1=100
a = b = c =20
a1,b1,c1=111,222,333
print(n1)
print(a,b,c)
print(a1,b1,c1)


# # Data Types
# - int
# - float
# - string

# In[10]:


a =100;
s1 ="Python"
s2 ='p'
f1 =10.2
print(a,s1,s2)
print(type(a),type(s1),type(s2),type(f1))


# In[12]:


print("Hello world!\nHello world!") 


# In[14]:


i = 100
print(type(i))
s1 = str(i)
print(type(s1))
f1 = float(i)
print(type(f1))


# In[15]:


s1 = "100"
print(type(s1))
a=int(s1)
print(type(a))
f = 1.5
a1 = int(f)
print(type(a1))
print(a1)


# In[18]:


# a number is given 1234 -
# Digi count
a1 = 1234
x=0
for i in str(a1):
    x=x+1
print("len=",x)


# In[ ]:


a1=1234
print(len(str(a1)))


# In[21]:


s1 = input("Enter your name")
print(s1)
print(type(s1))
print(len(s1))


# # reading the value -- input function
#  - input("message")-- string
#  - upper one is the solution

# In[23]:


# want a number as input 
n1=int(input("enter a number"))
print(n1,type(n1))


# In[25]:


n1=1234
print(n1+10)
print(n1-10)
print(n1*10)
print(n1/10)
print(n1%10)
print(n1//10) 
print(n1**10)


# ### Precedence of the arth operator
# - parenthesis
# - power
# - multiplaction
# - addition

# In[29]:


x = 1 + 2 ** 3/ 4 + 5
print(x)


# In[28]:


x = 1 + 2 ** 3/ 4 * 5 
print(x)


# ### Relational operators
# - ==
# - !=
# - Greater(>)
# - less than(<)
# - less than or equal to(<=)
# - greater then or equal to(>=) 
# 

# In[31]:


x = 10
a1 = x > 15
print(a1)


# # logical operators
# - used to combinemore than single condiction
# - and
# - or
# - not

# In[34]:


i = 100
a1 =(i>15) and (i<800)
a2 =(i>15) and (i>800)
print(a1)
print(a2)


# ### Control flow statements
# - Conditional statments
# - looping statment
# ### if - else statment
#  ** syntax
#  - If bollen_condition:
#  - statments
#  - else
#  - statments

# In[37]:


# to check given number is even or odd
n = int(input("enter a number"))
if n%2 == 0:
    print("even")
else:
    print("odd")


# In[41]:


# given number is perfectly multipe of 3 and 5
n = int(input("enter a number"))
if n%3==0 and n%5==0:
    print("yes")
else:
    print("no")
    


# In[ ]:




