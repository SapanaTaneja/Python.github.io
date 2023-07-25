


 Scraping Data from Real Website + Pandas


https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue

from bs4 import BeautifulSoup
import requests


url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page=requests.get(url)
soup=BeautifulSoup(page.text,'html')
print(soup)
soup.find_all('table')[1]
Table=soup.find('table', class_='wikitable sortable')
print(Table)
World_Title=Table.find_all('th')
print(World_Title)
World_table_titles= [title.text.strip() for title in World_Title]
print(World_table_titles)
import pandas as pd
df=pd.DataFrame(columns=World_table_titles)
df

column_data=Table.find_all('tr')

for row in column_data[1:]:
    row_data=row.find_all('td')
    Indiviual_Data=[data.text.strip() for data in row_data]
   
    length=len(df)
    df.loc[length]=Indiviual_Data
 
df


# In[ ]:




