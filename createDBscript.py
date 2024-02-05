import pandas as pd
import requests

url = 'http://127.0.0.1:8000/api/categories'
df = pd.read_csv("C:/Users/Stepan/Desktop/aluminadbinfo/categories.csv")
df = df.reset_index()

for index, row in df.iterrows():
    print(row['category_title'], row['category_name'])
    myjson = {'category_title': row['category_title'],
              'category_name': row['category_name']}
    req = requests.post(url=url, json=myjson, timeout=2.50)
    print('done')

url = 'http://127.0.0.1:8000/api/categories'
df = pd.read_csv("C:/Users/Stepan/Desktop/aluminadbinfo/categories.csv")
df = df.reset_index()

for index, row in df.iterrows():
    print(row['category_title'], row['category_name'])
    myjson = {'category_title': row['category_title'],
              'category_name': row['category_name']}
    req = requests.post(url=url, json=myjson, timeout=2.50)
    print('done')

url = 'http://127.0.0.1:8000/api/categories'
df = pd.read_csv("C:/Users/Stepan/Desktop/aluminadbinfo/categories.csv")
df = df.reset_index()

for index, row in df.iterrows():
    print(row['category_title'], row['category_name'])
    myjson = {'category_title': row['category_title'],
              'category_name': row['category_name']}
    req = requests.post(url=url, json=myjson, timeout=2.50)
    print('done')

url = 'http://127.0.0.1:8000/api/categories'
df = pd.read_csv("C:/Users/Stepan/Desktop/aluminadbinfo/categories.csv")
df = df.reset_index()

for index, row in df.iterrows():
    print(row['category_title'], row['category_name'])
    myjson = {'category_title': row['category_title'],
              'category_name': row['category_name']}
    req = requests.post(url=url, json=myjson, timeout=2.50)
    print('done')

url = 'http://127.0.0.1:8000/api/categories'
df = pd.read_csv("C:/Users/Stepan/Desktop/aluminadbinfo/categories.csv")
df = df.reset_index()

for index, row in df.iterrows():
    print(row['category_title'], row['category_name'])
    myjson = {'category_title': row['category_title'],
              'category_name': row['category_name']}
    req = requests.post(url=url, json=myjson, timeout=2.50)
    print('done')

    