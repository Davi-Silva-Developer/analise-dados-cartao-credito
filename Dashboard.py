import pandas as pd

caminho = 'Data/default_of_credit_card_clients__courseware_version_1_21_19.xls'
df = pd.read_excel(caminho)

#Exibe as 5 primeiras linhas do DataFrame
print(df.head())
print("\n")


# ? Saber quantas colunas os dados contêm. (Podem ser de características, resposta ou metadados).
print("Mostrando quantas colunas: ", df.shape[1])


# ? Saber quantas linhas os dados contêm. (Podem ser de características, resposta ou metadados).
print("Mostrando quantas linhas: ", df.shape[0])
print("\n")



df.info()
print("\n")



# ? O describe() gera um resumo estatístico das colunas numéricas
print(df.describe())
print("\n")


# ? Isso é importante para entender a quantidade de dados faltantes em cada coluna
print(df.isnull().sum())
print("\n")




# ? Como verificar colunas categoricas e numericas
#criar as listas vazias
colunas_categoricas = []
colunas_numericas = []



# Isso faz o Python olhar cada coluna da tabela
for coluna in df.columns:
    if df[coluna].nunique()<15:
        # Se tiver menos de 15 valores diferentes, é Categórica (classes).
        colunas_categoricas.append(coluna)
    else:
        colunas_numericas.append(coluna)


print("Características Categóricas (Classes discretas):")
print(colunas_categoricas)

print("\nCaracterísticas Numéricas (Escala contínua):")
print(colunas_numericas)
print("\n")
print("\n")
print("\n")





# ==========================================
# RESPOSTA DA QUESTÃO 2: APARÊNCIA DOS DADOS
# ==========================================

print("\n--- 1. INTERVALO DAS CARACTERÍSTICAS NUMÉRICAS ---")
# O comando describe() mostra o intervalo (mínimo, máximo, média) das colunas contínuas
resumo_numerico = df[colunas_numericas].describe()
print(resumo_numerico)

print("\n--- 2. FREQUÊNCIA DAS CARACTERÍSTICAS CATEGÓRICAS ---")
# Vamos fazer um 'for' para imprimir a frequência de cada coluna categórica da nossa lista
for coluna in colunas_categoricas:
    print(f"\nFrequência da característica: {coluna}")
    # O value_counts() mostra quantas vezes cada classe aparece (sim, não, 1, 2) 
    print(df[coluna].value_counts())
















