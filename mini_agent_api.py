import requests

url = "https://api.github.com/repos/python/cpython"
response = requests.get(url)
data = response.json()

stars = data.get("stargazers_count", 0)
if stars > 40000:
    action = "Wow! To popularne repo! 😎"
else:
    action = "Nie tak popularne, można sprawdzić coś innego."

print(f"Repo: {data.get('name')}, Gwiazdki: {stars}, Decyzja agenta: {action}")