#!/usr/bin/env python
# coding: utf-8

# # Scraping Data from Real Website + Pandas

# 
# https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'


# In[3]:


page=requests.get(url)


# In[7]:


soup=BeautifulSoup(page.text,'html')


# In[8]:


print(soup)


# In[11]:


soup.find_all('table')[1]


# In[14]:


Table=soup.find('table', class_='wikitable sortable')
print(Table)


# In[19]:


World_Title=Table.find_all('th')
print(World_Title)


# In[20]:


World_table_titles= [title.text.strip() for title in World_Title]
print(World_table_titles)


# In[21]:


import pandas as pd


# In[22]:


df=pd.DataFrame(columns=World_table_titles)
df


# In[27]:


column_data=Table.find_all('tr')


# In[40]:


for row in column_data[1:]:
    row_data=row.find_all('td')
    Indiviual_Data=[data.text.strip() for data in row_data]
   
    length=len(df)
    df.loc[length]=Indiviual_Data
        


# In[41]:


df


# In[ ]:




