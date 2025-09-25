import requests

# Lista repozytoriów do sprawdzenia
repos = [
    "python/cpython",
    "django/django",
    "pallets/flask"
]

for repo in repos:
    url = f"https://api.github.com/repos/{repo}"
    response = requests.get(url)
    data = response.json()
    
    stars = data.get("stargazers_count", 0)
    if stars > 20000:
        action = "Mega popularne repo! 😎"
    else:
        action = "Nie tak popularne, można sprawdzić coś innego."
    
    print(f"Repo: {data.get('name')}, Gwiazdki: {stars}, Decyzja agenta: {action}")