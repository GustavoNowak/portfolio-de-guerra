# Qual é a URL para obter todos os personagens.
# Resposta: Você pode acessar todos os personagens utilizando o link https://rickandmortyapi.com/api/character ou usando o endpoint /character.

# Como a resposta JSON é estruturada.
# Resposta: A resposta JSON é estruturada em dois objetos: info e results.
# O objeto info contém informações sobre a paginação, como o número total de personagens (count), o número de páginas (pages), O link para a próxima página (next)
# e o link para a página anterior (prev).
# O objeto results contém uma lista onde cada item é um objeto que representa um personagem, cada objeto de personagem possui vários campos que detalham suas características
# como o número de identificação (id), o nome do personagem (name), o estado atual entre vivo, morto ou desconhecido (status), a espécie (species), 
# o subtipo ou variação da espécie (type), o gênero do personagem (gender), um link com local de origem do personagem (origin), 
# um link com a última localização do personagem (location), uma imagem do personagem (image), uma lista de episódios (episode), um link com o personagem (url).
# e um campo criado pelo sistema com a data e hora da criação do personagem (created).

# Como o sistema de paginação funciona (preste atenção nos campos info e next na resposta).
# Resposta: Ao acessar https://rickandmortyapi.com/api/character, você recebe a primeira página de resultados. 
# o objeto info gerencia a paginação. Ele informa que existem, por exemplo, 826 personagens no total (count), divididos em 42 páginas (pages).
# Para obter a próxima leva de personagens, basta fazer uma nova requisição para a URL fornecida no campo next.
# Você repete esse processo, seguindo o link next de cada página, até que o valor do campo next seja null. Um valor null indica que você chegou à última página e não há mais resultados.


# Ação:
# 1. Use a biblioteca requests para fazer uma requisição GET ao endpoint dos personagens.
# 2. Parseie a resposta JSON.
# 3. Extraia os seguintes campos para cada personagem: name, status, species e o nome da localização de origem (que está em um dicionário aninhado: origin['name']).
# 4. Implemente um loop que verifica a existência da URL next no campo info da resposta. Enquanto essa URL existir (e você não tiver atingido o limite), o script deve fazer uma nova requisição para essa URL, continuando a coleta de dados.
# 5. Defina um limite para o seu loop: você vai coletar os dados das 5 primeiras páginas.
# 6. Armazene todos os dados coletados em um arquivo characters.csv, com os cabeçalhos apropriados: Nome,Status,Especie,Origem.

import requests
import pandas as pd

# Lista para acumular os dados de todas as páginas
all_characters_list = []

# URL inicial da API
current_url = "https://rickandmortyapi.com/api/character"

# 5. Defina um limite para o seu loop: você vai coletar os dados das 5 primeiras páginas.
page_limit = 5
pages_fetched = 0

# 4. Implemente um loop que verifica a existência da URL next no campo info da resposta.
while current_url and pages_fetched < page_limit:
    # 1. Use a biblioteca requests para fazer uma requisição GET ao endpoint dos personagens.
    response = requests.get(current_url)
    
    # 2. Parseie a resposta JSON.
    data = response.json()

    # 3. Extraia os seguintes campos para cada personagem.
    for character in data['results']:
        all_characters_list.append({
            'name': character['name'],
            'status': character['status'],
            'species': character['species'],
            # Extração correta do nome da origem
            'origin_name': character['origin']['name'] 
        })
    
    # Prepara a URL para a próxima iteração do loop
    current_url = data['info']['next']
    pages_fetched += 1
    print(f"Página {pages_fetched} coletada.")

# 6. Armazene todos os dados coletados em um arquivo characters.csv.
# Cria o DataFrame a partir da lista, depois que o loop terminou
df = pd.DataFrame(all_characters_list)

# Define os cabeçalhos apropriados: Nome,Status,Especie,Origem.
df.columns = ['Nome', 'Status', 'Espécie', 'Origem']

# Salva o arquivo CSV uma única vez com todos os dados
df.to_csv('characters.csv', index=False)

print(f"\nProcesso concluído. Arquivo 'characters.csv' salvo com {len(df)} registros.")