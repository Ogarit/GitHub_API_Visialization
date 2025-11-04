import plotly.express as px
from requests.exceptions import ConnectionError
import requests

# Cria uma chamada de API e verifica a resposta
url = "https://api.github.com/search/repositories"
url += f"?q=language:python+sort:stars+stars:>{10_000}"

headers = {"Accept": "application/vnd.github.v3+json"}
try:
    r = requests.get(url, headers=headers)
except ConnectionError:
    print("Erro de conexão!!")
else:
    print(f"Código de status: {r.status_code}")

    # Processa os resultados gerais
    response_dict = r.json()
    print(f"Resultados completos: {not response_dict['incomplete_results']}")

    # Processa as informações do repositório
    repo_dicts = response_dict['items']
    repo_names, stars = [], []
    for repo_dict in repo_dicts:
        repo_names.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])

    # Cria a visualização
    fig = px.bar(x=repo_names, y=stars)
    fig.show()
