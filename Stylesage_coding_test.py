#!/usr/bin/env python
# coding: utf-8



import requests
import json
import pandas as pd




response = requests.get("https://api.artic.edu/api/v1/agents/search")



response.json()


# In[ ]:





# In[3]:


response_artist_1= requests.get("https://api.artic.edu/api/v1/agents/1963")
response_artist_1.status_code


# In[4]:


response_artist_1.json()


# In[ ]:





# In[5]:


response_artist_2= requests.get("https://api.artic.edu/api/v1/agents/1974")
print(response_artist_2.status_code)


# In[6]:


response_artist_2.json()


# In[ ]:





# In[7]:


response_artist_3= requests.get("https://api.artic.edu/api/v1/agents/1992")
print(response_artist_3.status_code)


# In[8]:


response_artist_3.json()


# In[ ]:





# In[9]:


response_artist_4= requests.get("https://api.artic.edu/api/v1/agents/1998")
print(response_artist_4.status_code)


# In[10]:


response_artist_4.json()


# In[ ]:





# In[11]:


response_artist_5= requests.get("https://api.artic.edu/api/v1/agents/2006")
print(response_artist_5.status_code)


# In[12]:


response_artist_5.json()


# In[ ]:





# In[ ]:





# In[13]:


Jan_Abrahamsz_artwork= requests.get("https://api.artic.edu/api/v1/artworks/83640")
print(Jan_Abrahamsz_artwork.status_code)


# In[14]:


Jan_Abrahamsz_artwork.json()


# In[ ]:





# In[ ]:





# In[15]:


Sara_Begody_artwork= requests.get("https://api.artic.edu/api/v1/artworks/61009")
print(Sara_Begody_artwork.status_code)


# In[16]:


Sara_Begody_artwork.json()


# In[ ]:





# In[ ]:





# In[17]:


Peter_Behrens_artwork= requests.get("https://api.artic.edu/api/v1/artworks/29114")
print(Peter_Behrens_artwork.status_code)


# In[18]:


Peter_Behrens_artwork.json()


# In[ ]:





# In[ ]:





# In[19]:


Sadiqi_artwork= requests.get("https://api.artic.edu/api/v1/artworks/70594")
print(Sadiqi_artwork.status_code)


# In[20]:


Sadiqi_artwork.json()


# In[ ]:





# In[ ]:





# In[21]:


Janice_Bell_artwork= requests.get("https://api.artic.edu/api/v1/artworks/54548")
print(Janice_Bell_artwork.status_code)


# In[22]:


Janice_Bell_artwork.json()


# In[ ]:





# In[23]:


lista = [response_artist_1.json(),response_artist_2.json(),response_artist_3.json(),response_artist_4.json(),response_artist_5.json()]


# In[24]:


print(lista)


# In[ ]:





# In[25]:


data = pd.DataFrame(lista)
data


# In[26]:


from pandas import json_normalize


# In[27]:


artist_data=json_normalize(lista)
artist_data


# In[28]:


artist_data.info()


# In[29]:


artist_data=artist_data.drop(['data.suggest_autocomplete_all.contexts.groupings'],axis=1)
artist_data=artist_data.drop(['data.suggest_autocomplete_all.weight'],axis=1)
artist_data=artist_data.drop(['data.suggest_autocomplete_all.input'],axis=1)
artist_data=artist_data.drop(['config.website_url'],axis=1)
artist_data=artist_data.drop(['config.iiif_url'],axis=1)
artist_data=artist_data.drop(['info.version'],axis=1)
artist_data=artist_data.drop(['info.license_links'],axis=1)
artist_data=artist_data.drop(['info.license_text'],axis=1)
artist_data=artist_data.drop(['data.timestamp'],axis=1)
artist_data=artist_data.drop(['data.last_updated'],axis=1)
artist_data=artist_data.drop(['data.last_updated_source'],axis=1)
artist_data=artist_data.drop(['data.site_ids'],axis=1)
artist_data=artist_data.drop(['data.is_licensing_restricted'],axis=1)
artist_data=artist_data.drop(['data.description'],axis=1)
artist_data=artist_data.drop(['data.death_place'],axis=1)
artist_data=artist_data.drop(['data.birth_place'],axis=1)
artist_data=artist_data.drop(['data.alt_titles'],axis=1)
artist_data=artist_data.drop(['data.api_link'],axis=1)
artist_data=artist_data.drop(['data.api_model'],axis=1)
artist_data=artist_data.drop(['data.agent_type_id'],axis=1)


# In[30]:


artist_data=artist_data.rename(columns={'data.title': 'artist_title'})
artist_data=artist_data.rename(columns={'data.id': 'artist_id'})
artist_data=artist_data.rename(columns={'data.artwork_ids': 'number_of_artworks_and_ids'})


# In[31]:


artist_data


# In[ ]:





# In[ ]:





# In[32]:


lista_2=[Jan_Abrahamsz_artwork.json(),Sara_Begody_artwork.json(),Peter_Behrens_artwork.json(),Sadiqi_artwork.json(),Janice_Bell_artwork.json()]
print(lista)


# In[33]:


artwork_data=json_normalize(lista_2)
artwork_data


# In[34]:


artwork_data.columns


# In[35]:


artwork_data=artwork_data.rename(columns={'data.id': 'random_artwork_id'})
artwork_data=artwork_data.rename(columns={'data.title': 'title'})
artwork_data=artwork_data.rename(columns={'data.place_of_origin': 'place_of_origin'})
artwork_data=artwork_data.rename(columns={'data.material_titles': 'material_titles'})
artwork_data=artwork_data.rename(columns={'data.dimensions': 'dimensions'})
artwork_data=artwork_data.rename(columns={'data.artist_title': 'artist_title'})


# In[36]:


main_artwork_data=artwork_data[['random_artwork_id','artist_title','title','place_of_origin','material_titles','dimensions']]
main_artwork_data


# In[37]:


main_artwork_data.info()


# In[38]:


artists_and_artworks=artist_data.merge(main_artwork_data,how="left", on=['artist_title'])
artists_and_artworks


# In[ ]:


artists_and_artworks.to_csv('artists_and_artworks.csv')


# In[ ]:




