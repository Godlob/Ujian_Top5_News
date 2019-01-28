import requests

print('Selamat datang, mau tahu berita apa hari ini?')
print('[1] Berita seputar teknologi')
print('[2] Berita seputar bisnis')
print('[3] Berita seputar olahraga')
print('[4] Berita seputar kesehatan')
print('[5] Berita seputar science')
x = int(input('Ketik pilihan Anda [1/2/3/4/5]: '))

def getData(x):
    if x == 1 :
        category = 'technology'
    if x == 2:
        category = 'business'    
    if x == 3 :
        category = 'sports'
    if x ==4 :
        category = 'health'
    if x == 5 :
        category = 'science'
    apiKey = '2eaad153252a4c06b4f8bd19cc1aa604'
    url = 'https://newsapi.org/v2/top-headlines?country=id&category='+category+'&apiKey='+apiKey
    data = requests.get(url).json()
    for i in range(0,5):
        print(i+1,' - ',data['articles'][i]['title'])
getData(x)
