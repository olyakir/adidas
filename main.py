import requests

text = requests.get('https://www.maximonline.ru/entertainment/luchshie-shutki-o-chake-norrise-id877956/').text
print(text)