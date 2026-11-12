import json
from urllib.request import urlopen

city="Yerevan"
url=f"https://wttr.in/{city}?format=j1"
with urlopen(url, timeout=20) as response:
    status=response.status
    raw_text=response.read().decode("utf-8")
data=json.loads(raw_text)
current=data["current_condition"][0]
description=current["weatherDesc"][0]["value"]
print(f'HTTP-статус:',status)
print(f'Город:',city)
print(f'Температура:',current["temp_C"],"°C")
print(f'Ощущается как:',current["FeelsLikeC"],"°C")
print(f'Влажность:',current["humidity"],"%")
print(f'Погода:',description)