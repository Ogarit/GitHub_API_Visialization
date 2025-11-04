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

    # Converte o objeto de resposta em um dicionário
    response_dict = r.json()
    print(f"Total de repositórios: {response_dict['total_count']}")
    print(f"Resultados completos: {not response_dict['incomplete_results']}")

    # Explora informações sobre os repositórios
    repo_dicts = response_dict['items']
    print(f"Repositórios retornados: {len(repo_dicts)}")

    print("\nSeleciona informações sobre cada repositório:")
    for repo_dict in repo_dicts:
        print(f"Nome: {repo_dict['name']}")
        print(f"Proprietário(a): {repo_dict['owner']['login']}")
        print(f"Estrelas: {repo_dict['stargazers_count']}")
        print(f"Repositório: {repo_dict['html_url']}")
        print(f"Criado: {repo_dict['created_at']}")
        print(f"Atualizado: {repo_dict['updated_at']}")
        print(f"Descrição: {repo_dict['description']}")
