#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.options.display.width = None


# In[3]:


train_df = pd.read_excel('Data_Train.xlsx')
train_df.head()


# In[4]:


test_df = pd.read_excel('Test_set.xlsx')
test_df.head()


# In[5]:


final_df = train_df.append(test_df)
final_df.head()


# In[6]:


final_df['Date'] = final_df['Date_of_Journey'].apply(lambda x: x.split('/')[0])
final_df['Month'] = final_df['Date_of_Journey'].apply(lambda x: x.split('/')[1])
final_df['Year'] = final_df['Date_of_Journey'].apply(lambda x: x.split('/')[2])


# In[7]:


final_df['Date'] = final_df['Date'].astype(int)
final_df['Date'] = final_df['Month'].astype(int)
final_df['Date'] = final_df['Year'].astype(int)


# In[8]:


final_df.drop(['Date_of_Journey'], axis=1, inplace=True)


# In[9]:


final_df.head()


# In[10]:


final_df['Arrival_Time'] = final_df['Arrival_Time'].str.split(" ").str[0]


# In[11]:


final_df['Arrival_Hour'] = final_df['Arrival_Time'].str.split(':').str[0]
final_df['Arrival_Min'] = final_df['Arrival_Time'].str.split(':').str[1]


# In[12]:


final_df['Arrival_Hour'] = final_df['Arrival_Hour'].astype(int)
final_df['Arrival_Min'] = final_df['Arrival_Min'].astype(int)


# In[13]:


final_df.info()


# In[14]:


final_df.head(5)


# In[15]:


final_df.drop(['Arrival_Time'], axis=1, inplace =True)


# In[16]:


final_df['Dep_Hour'] = final_df['Dep_Time'].apply(lambda x:x.split(':')[0])
final_df['Dep_Min'] = final_df['Dep_Time'].apply(lambda x:x.split(':')[1])


# In[17]:


final_df['Dep_Hour'] = final_df['Dep_Hour'].astype(int)
final_df['Dep_Min'] = final_df['Dep_Min'].astype(int)


# In[18]:


final_df['Total_Stops'].unique()


# In[19]:


final_df['Total_Stops'] = final_df['Total_Stops'].map({'non-stop':0, '2 stops':2, '1 stop':1, '3 stops':3,'4 stops':4})


# In[20]:


final_df['Total_Stops']=final_df['Total_Stops'].fillna(final_df['Total_Stops'].mode()[0])


# In[21]:


final_df['Total_Stops']


# In[22]:


final_df.info()


# In[23]:


final_df.drop(['Route'], axis=1, inplace=True)


# In[24]:


final_df['Duration_Hour'] = final_df['Duration'].str.split(" ").str[0].str.split("h").str[0]


# In[25]:


final_df[final_df['Duration_Hour']=='5m']


# In[26]:


final_df.drop(6474,axis=0, inplace=True)


# In[27]:


final_df.drop(2660,axis=0, inplace=True)


# In[28]:


final_df['Duration_Hour']=final_df['Duration_Hour'].astype(int)


# In[29]:


final_df.drop(['Duration'], axis=1, inplace=True)


# In[30]:


final_df.info()


# In[31]:


final_df.head(1)


# In[32]:


final_df['Additional_Info'].unique()


# In[33]:


from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()


# In[34]:


final_df['Airline']=labelencoder.fit_transform(final_df['Airline'])
final_df['Source']=labelencoder.fit_transform(final_df['Source'])
final_df['Destination']=labelencoder.fit_transform(final_df['Destination'])
final_df['Additional_Info']=labelencoder.fit_transform(final_df['Additional_Info'])


# In[35]:


final_df.head(5)


# In[45]:


pd.get_dummies(final_df, columns=['Airline','Source','Destination','Additional_Info'],drop_first=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




