
# coding: utf-8

# In[4]:

#Iimports and aliases each of the library I plan to use
import numpy as np
from pandas import *
import pandas as pd


# In[5]:

# Loads the RAW CSV FILE into a DataFrame
df = pd.read_csv("CompensationByState.csv")


# In[6]:

# Filters out all rows which have a null value for column IndustryClassification
df = df[pd.notnull(df['IndustryClassification'])]


# In[7]:

# Outputs head for sanity check
df.head()


# In[8]:

#"Melts" the data, unpivots all of the "year" columns
survey = pd.melt(df, id_vars=["GeoFIPS", "GeoName", "Region", "Table", "LineCode", "IndustryClassification", "Description"], var_name="Year", value_name="Comepnsation")


# In[9]:

survey


# In[10]:

#Outputs that data to a new CSV file
survey.to_csv("MeltedWagesByState.csv")


# In[ ]:



