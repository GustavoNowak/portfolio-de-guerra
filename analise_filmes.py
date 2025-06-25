# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analisar_dados_filmes(caminho_arquivo):
    """
    Função principal que carrega, limpa e analisa os dados de filmes,
    gerando gráficos para responder às perguntas de negócio.
    """
    # --- 1. Carregamento e Limpeza dos Dados ---
    
    print("Iniciando a análise do dataset de filmes...")
    
    # Verifica se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        print("Por favor, certifique-se de que o script está na mesma pasta que o arquivo CSV.")
        return

    # Carrega o dataset
    df = pd.read_csv(caminho_arquivo, encoding='utf-8')
    
    print("Realizando limpeza e preparação dos dados...")
    
    # Limpa e converte a coluna 'Year' para numérico
    df['Year'] = df['Year'].astype(str).str.extract(r'(\d{4})').astype(float)
    
    # Limpa e converte a coluna 'Duration' para numérico
    df['Duration'] = df['Duration'].astype(str).str.replace(' min', '', regex=False).astype(float)
    
    # Remove linhas com dados essenciais ausentes para a análise
    colunas_essenciais = ['Genre', 'Duration', 'Rating', 'Year', 'Actor 1']
    df.dropna(subset=colunas_essenciais, inplace=True)

    print("Dados limpos. Iniciando a geração dos gráficos...")

    # --- 2. Pergunta 1: Análise de Gênero ---
    
    # Separa os gêneros que estão em uma única string
    genres = df['Genre'].str.split(', ', expand=True).stack()
    top_10_genres = genres.value_counts().nlargest(10)
    
    plt.figure(figsize=(12, 7))
    sns.barplot(x=top_10_genres.values, y=top_10_genres.index, hue=top_10_genres.index, palette='viridis', orient='h', legend=False)
    plt.title('Top 10 Gêneros de Filmes Mais Comuns', fontsize=16)
    plt.xlabel('Número de Filmes', fontsize=12)
    plt.ylabel('Gênero', fontsize=12)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('grafico_top_10_generos.png')
    plt.close()
    print("Gráfico 1 (Top 10 Gêneros) salvo como 'grafico_top_10_generos.png'")

    # --- 3. Pergunta 2: Análise de Performance (Duração vs. Nota) ---
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Duration', y='Rating', alpha=0.5)
    sns.regplot(data=df, x='Duration', y='Rating', scatter=False, color='red') # Adiciona linha de regressão
    plt.title('Correlação entre Duração do Filme e Nota do Público', fontsize=16)
    plt.xlabel('Duração (minutos)', fontsize=12)
    plt.ylabel('Nota (Rating)', fontsize=12)
    plt.tight_layout()
    plt.savefig('grafico_duracao_vs_nota.png')
    plt.close()
    print("Gráfico 2 (Duração vs. Nota) salvo como 'grafico_duracao_vs_nota.png'")

    # --- 4. Pergunta 3: Análise Temporal (Nota Média por Ano) ---
    
    average_rating_by_year = df.groupby('Year')['Rating'].mean().reset_index()
    
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=average_rating_by_year, x='Year', y='Rating', marker='o')
    plt.title('Evolução da Nota Média dos Filmes por Ano', fontsize=16)
    plt.xlabel('Ano de Lançamento', fontsize=12)
    plt.ylabel('Nota Média', fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.savefig('grafico_nota_media_por_ano.png')
    plt.close()
    print("Gráfico 3 (Nota Média por Ano) salvo como 'grafico_nota_media_por_ano.png'")

    # --- 5. Pergunta 4: Análise de Atores ---
    
    # Une as colunas de atores em uma única Série (pandas Series)
    # Garante que os atores das 3 colunas sejam contados
    actors = pd.concat([df['Actor 1'], df['Actor 2'], df['Actor 3']]).dropna()
    top_10_actors = actors.value_counts().nlargest(10)

    plt.figure(figsize=(12, 7))
    sns.barplot(x=top_10_actors.values, y=top_10_actors.index, hue=top_10_actors.index, palette='plasma', orient='h', legend=False)
    plt.title('Top 10 Atores com Mais Aparições em Filmes', fontsize=16)
    plt.xlabel('Número de Filmes', fontsize=12)
    plt.ylabel('Ator', fontsize=12)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('grafico_top_10_atores.png')
    plt.close()
    print("Gráfico 4 (Top 10 Atores) salvo como 'grafico_top_10_atores.png'")
    
    print("\nAnálise concluída com sucesso! Os 4 gráficos foram salvos na pasta atual.")


# --- Execução do Programa ---
if __name__ == "__main__":
    # Define o nome do arquivo CSV a ser analisado
    nome_do_arquivo = 'IMDb Movies India.csv'
    analisar_dados_filmes(nome_do_arquivo)