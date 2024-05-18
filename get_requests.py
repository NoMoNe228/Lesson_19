import requests

# web = 'https://habr.com'
# result=requests.get(web)
# print(result)
# print('код ответ аот сервера:', result.status_code)

# main_url = f'{web}ru/feed'
# result = requests.get(web)
# data = result.json()
# print(data)

url_for = requests.get('https://vk.com')
print(url_for.status_code)
web = 'https://habr.com'
main_url2 = f'{web}?page_id=5/'
result= requests.post(main_url2, data = {'name' : 'Musia', 'brees': 'siam', 'age': '20'})
print(result.status_code)
print(f'{web}?page_id=5/')