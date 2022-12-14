#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('employee_filter.csv', index_col=0)
df.columns


# In[ ]:





# In[3]:


# percentage of gender

round(df['gender'].value_counts()/df['gender'].count()*100,2)


# In[4]:


# percentage of country

round(df['country'].value_counts()/df['country'].count()*100,2)


# In[5]:


# How many people of any age are there?

df['age'].value_counts()


# In[6]:


# Find Sheryl Itzakson

df[df['full_name'].str.contains('Sheryl Itzakson')]


# In[7]:


# Find female employee who is working with amazon and from poland

df[(df.gender.str.contains('F')) & (df.country.str.contains('Poland')) & (df.company.str.contains('Amazon'))]


# In[ ]:





# In[8]:


# Find paula tulley's country, job and company

df[df['full_name'].str.contains('Paula Tulley', case=True)][['full_name','country','job_title','company']]


# In[9]:


# I just want to paula's university name

df[df['full_name'].str.contains('Paula Tulley')]['university']


# In[ ]:





# In[ ]:





# In[10]:


# Find a project manager who must be older than 30 

df[(df['job_title']=='Project Manager') & (df.age >= 30)]


# In[11]:


# How many specialist are in this dataset ?

len(df[df['job_title'].str.contains('Specialist')])


# In[12]:


# Highest paid specialist

df[df['job_title'].str.contains('Specialist')].sort_values(by='salary', ascending=False).head(5)


# In[13]:


# find scientist

len(df[df.job_title.str.contains('Scientist')])


# In[14]:


# find software related

len(df[df.job_title.str.contains('Software')])


# In[15]:


# Find analyst

len(df[df.job_title.str.contains('Analyst')])


# In[16]:


# Find who working with data

len(df[df.job_title.str.contains('Data')])


# In[17]:


# Find who working with database

len(df[df.job_title.str.contains('Database')])


# In[18]:


# find engineer's

len(df[df.job_title.str.contains('Engineer')])


# In[19]:


# find professor's

len(df[df.job_title.str.contains('Professor')])


# In[20]:


# find project manager 

len(df[df.job_title.str.contains('Project Manager')])


# In[ ]:





# In[21]:


# Find the person who get highest salary. Find his name, salary, company and country

df[df['salary'].max()==df['salary']][['full_name','salary','company','country']]


# In[22]:


# How many people's have salary and balance more than 50000

len(df[(df['salary']>50000) & (df['balance']>50000)])


# In[ ]:





# In[ ]:





# In[23]:


# Count Google employee from every country 

df[df['company']=='Google']['country'].value_counts()


# In[24]:


# How many people from each country are working in the giant (Google,Apple etc) company?

df[(df['company']=='Google') + (df['company']=='Amazon') + (df['company']=='Apple') +
  (df['company']=='Microsoft') + (df['company']=='Facebook')]['country'].value_counts()


# In[ ]:





# In[ ]:





# In[25]:


# Find 5 person visa credit-card user who get the minimum salary

df[df['credit_card']=='visa'].sort_values(by='salary').head(5)


# In[26]:


# How many people use mastercard

df['credit_card'].value_counts()['mastercard']


# In[27]:


# How many people's use every credit_card in poland

df.query("country=='Poland'")['credit_card'].value_counts()


# In[ ]:





# ### The employee with the longest length of name

# In[28]:


# Find the person whose name length is bigger than anyone

def get_max_len(lst):
    return max(enumerate(lst), key=lambda x: len(x[1]))

print(get_max_len(df['full_name']))


# In[29]:


df[df['full_name']=='Merrill Le Breton De La Vieuville']


# In[30]:


# Another way to find this 

df[df.full_name.apply(lambda x: len(x) > 30)]


# ### how many leap year in employee's birth year

# In[31]:


# Find leap year employee's birth year

leap_year = []

for i in df['year']:
    if i % 4 == 0:
        leap_year.append(i)
    elif i % 4 != 0:
        leap_year.append('Not leap year')


# In[32]:


df['leap_year'] = leap_year


# In[33]:


df['leap_year'].value_counts()


# In[34]:


df.drop('leap_year', axis=1, inplace=True)


# In[ ]:





# In[ ]:





# In[ ]:





# ### using gropby

# In[35]:


# get group visa

df.groupby('credit_card').get_group('visa').head(5)


# In[36]:


# How many visa credit cards does each country use?

df.groupby('credit_card').get_group('visa')['country'].value_counts()


# In[37]:


# if you want to be more specific

df.groupby('credit_card').get_group('visa')['country'].value_counts()['Bangladesh']


# In[38]:


# groupby based on gender

df.groupby('gender')[['salary','balance']].agg({'mean', 'sum'})


# In[39]:


df.groupby(['vehicle'])['salary'].mean().sort_values(ascending=False).head(5)


# In[40]:


df.groupby('continent')['gender'].count()


# In[41]:


# continent wise min and max

df.groupby('continent')[['salary', 'balance']].agg(['min', 'max'])


# In[42]:


# age wise min and max

df.groupby('age')[['salary', 'balance']].agg(['min', 'max']).head(5)


# In[ ]:





# ### Pivot

# In[44]:



df.pivot_table(df, index=['country']).head(10)


# ### Crosstab

# In[50]:



pd.crosstab(df.continent, df.year)


# In[56]:


pd.crosstab(df.gender, df.age)


# In[57]:


pd.crosstab(df.gender, df.year)


# In[ ]:




