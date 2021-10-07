#!/usr/bin/env python
# coding: utf-8



import requests
import json
import pandas as pd




response = requests.get("https://api.artic.edu/api/v1/agents/search")

response.json()


response_artist_1= requests.get("https://api.artic.edu/api/v1/agents/1963")
response_artist_1.status_code

response_artist_1.json()



response_artist_2= requests.get("https://api.artic.edu/api/v1/agents/1974")
print(response_artist_2.status_code)

response_artist_2.json()



response_artist_3= requests.get("https://api.artic.edu/api/v1/agents/1992")
print(response_artist_3.status_code)

response_artist_3.json()




response_artist_4= requests.get("https://api.artic.edu/api/v1/agents/1998")
print(response_artist_4.status_code)

response_artist_4.json()




response_artist_5= requests.get("https://api.artic.edu/api/v1/agents/2006")
print(response_artist_5.status_code)

response_artist_5.json()




Jan_Abrahamsz_artwork= requests.get("https://api.artic.edu/api/v1/artworks/83640")
print(Jan_Abrahamsz_artwork.status_code)

Jan_Abrahamsz_artwork.json()




Sara_Begody_artwork= requests.get("https://api.artic.edu/api/v1/artworks/61009")
print(Sara_Begody_artwork.status_code)

Sara_Begody_artwork.json()





Peter_Behrens_artwork= requests.get("https://api.artic.edu/api/v1/artworks/29114")
print(Peter_Behrens_artwork.status_code)

Peter_Behrens_artwork.json()





Sadiqi_artwork= requests.get("https://api.artic.edu/api/v1/artworks/70594")
print(Sadiqi_artwork.status_code)

Sadiqi_artwork.json()






Janice_Bell_artwork= requests.get("https://api.artic.edu/api/v1/artworks/54548")
print(Janice_Bell_artwork.status_code)

Janice_Bell_artwork.json()




lista = [response_artist_1.json(),response_artist_2.json(),response_artist_3.json(),response_artist_4.json(),response_artist_5.json()]

print(lista)



data = pd.DataFrame(lista)
data


from pandas import json_normalize



artist_data=json_normalize(lista)
artist_data



artist_data.info()



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



artist_data=artist_data.rename(columns={'data.title': 'artist_title'})
artist_data=artist_data.rename(columns={'data.id': 'artist_id'})
artist_data=artist_data.rename(columns={'data.artwork_ids': 'number_of_artworks_and_ids'})


artist_data








lista_2=[Jan_Abrahamsz_artwork.json(),Sara_Begody_artwork.json(),Peter_Behrens_artwork.json(),Sadiqi_artwork.json(),Janice_Bell_artwork.json()]
print(lista)





artwork_data=json_normalize(lista_2)
artwork_data



artwork_data.columns



artwork_data=artwork_data.rename(columns={'data.id': 'random_artwork_id'})
artwork_data=artwork_data.rename(columns={'data.title': 'title'})
artwork_data=artwork_data.rename(columns={'data.place_of_origin': 'place_of_origin'})
artwork_data=artwork_data.rename(columns={'data.material_titles': 'material_titles'})
artwork_data=artwork_data.rename(columns={'data.dimensions': 'dimensions'})
artwork_data=artwork_data.rename(columns={'data.artist_title': 'artist_title'})





main_artwork_data=artwork_data[['random_artwork_id','artist_title','title','place_of_origin','material_titles','dimensions']]
main_artwork_data





main_artwork_data.info()





artists_and_artworks=artist_data.merge(main_artwork_data,how="left", on=['artist_title'])
artists_and_artworks



artists_and_artworks.to_csv('artists_and_artworks.csv')







