import requests
import pandas as pd
from datetime import datetime, timedelta
import io
from pandas.io.json import json_normalize

# newsapi

api_key = '20b7ba02045b4d02999affa48d7e4969'
query = 'acidente carro'
country = 'pt'

url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(query, api_key)
response = requests.get(url)

if response.status_code == 200:
    articles = response.json()['articles']

    # Create a list of dictionaries with the relevant information for each article
    data = [{'title': article['title'], 'url': article['url'], 'source': article['source']['name']} for article in articles]

    # Create a Pandas dataframe from the data
    df = pd.DataFrame(data)

    # Print the dataframe
    print(len(df))
else:
    print('An error occurred:', response.status_code)
    
# Get today date now to file name when export to csv or excel with encoding utf8
df.to_csv((datetime.now()+timedelta(hours=1)).strftime('data_sources/data_transformed/news_api-%Y-%m-%d-%H-%M-%S.csv'), encoding='utf8', index=False)