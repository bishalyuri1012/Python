#!/usr/bin/env python
# coding: utf-8

# Datatypes are the building blocks upon which larger programs are made.

# integer

# int Yuriboyka- PASCAL CASE

# int yuriBoyka - SNAKE CASE
# 

# int yuri_boyka 

# In[1]:


4+5


# In[2]:


4-5


# In[3]:


6/6


# In[4]:


4**2


# In[12]:


print("lizaDangi"*2)


# In[13]:


5**3


# 5**3-POW

# In[15]:


4/3


# In[16]:


4%3


# 4%3-MOD

# In[17]:


(6+9)*2


# In[23]:


4\3


# In[19]:


4/3


# In[20]:


0.1+0.2-0.3


# In[21]:


yuri="crispy"


# Mutability/immutability

# In[36]:


any_word="Hello_world"
any_word[10]


# In[35]:


a="Hello_world"
a[0:5]


# In[44]:


a="Hello_world"
a[:]


# In[45]:


a="Hello_world"
a[:5]


# In[46]:


a="Hello_world"
a[1:]


# In[49]:


a="Hello_world"
a[0:11:1]


# In[50]:


a="Hello_world"
a[::-1]


# In[56]:


a="Hello_world"


# In[57]:


5**5


# In[61]:


7%4


# List
# list is an ordered sequence of elements upon which array like operations can be performed.

# In[62]:


a=[4,4.5,"hello"]


# In[63]:


a[0]


# In[64]:


a="sam"
a[0]="p"


# In[ ]:


a="pam"


# In[ ]:


a=[1,2,"hi"]


# In[65]:


a ="Hello World"


# In[66]:


a.upper()


# In[67]:


a.lower()


# In[ ]:


a ="Hello World"


# In[70]:


type(a)


# In[71]:


a.split()


# In[72]:


type(a.split())


# In[74]:


a = "HeraPheri"


# In[75]:


a.split('e')


# In[76]:


1+1


# '1'+'1'=concatination

# In[78]:


"bishal"+"yuri"


# In[79]:


a=[1,1.1,"Hello"]


# In[80]:


a="Hello\tWorld"


# In[81]:


print(a)


# In[84]:


a =[1,1.1,"Hello"]


# In[86]:


a[2]


# In[87]:


a=[1,1.1,["Hello","world"]]


# In[88]:


a[2]


# In[89]:


a[2][1]


# In[91]:


a=[3,1,5,3,4,5,10]


# In[92]:


a.sort()


# In[93]:


print(a)


# In[94]:


a=['e','f','a','b']


# In[95]:


a.sort()


# In[96]:


print(a)


# Dictinary
# unordered pair arrangement
# a={'key':'value'}

# In[98]:


a={'rollnumber': 1,'name':'Aanchal','gender':'Female'}


# In[97]:


a[0]


# In[99]:


a['rollnumber']


# In[100]:


a['name']


# In[101]:


a['gender']


# Tuple: (1,1,1,'Hello world')

# In[102]:


a=(1,1.1,'Hello world')


# In[103]:


a[0]


# In[104]:


a[2]


# In[105]:


list=[1,1.1,'hello world']


# In[106]:


tuple=[1,1.1,'hello world']


# In[107]:


list[0]


# In[110]:


tuple[0]


# In[121]:


a=[1,1.1,"hello"]


# In[122]:


a.pop(0)


# In[123]:


a.pop(1)


# In[ ]:


Set:
    should always contain unique value


# In[125]:


a=[1,2,3,1,1,2,4,5,2]


# In[126]:


set(a)


# In[127]:


a=[1,2,3]


# In[129]:


a.append(4)


# In[130]:


a


# In[ ]:


get_ipython().run_cell_magic('writefile', 'lesson.txt', 'This is my first python lesson.\nI am learning python')


# In[132]:


my_file=open('lesson.txt')


# In[133]:


my_file.read()


# In[ ]:


my_file.read()


# In[135]:


my_file.seek(0)


# In[136]:


my_file.read()


# In[138]:


my_file.seek(11)


# In[139]:


my_file.read()


# In[144]:


with open("lesson.txt")as my_file:
    my_file.seek(0)
    my_file.read()


# In[ ]:




