import pandas as pd

# ==========================================
# CARREGAMENTO DOS DADOS
# ==========================================

caminho = 'default_of_credit_card_clients__courseware_version_1_21_19.xls'

df = pd.read_excel(caminho)

# Exibindo as 5 primeiras linhas
print(df.head())

# ==========================================
# QUANTIDADE DE LINHAS E COLUNAS
# ==========================================

print("Quantidade de linhas:", df.shape[0])
print("Quantidade de colunas:", df.shape[1])



# ==========================================
# INFORMAÇÕES DO DATASET
# ==========================================

df.info()



# ==========================================
# IDENTIFICAÇÃO DE CARACTERÍSTICAS
# ==========================================

colunas_categoricas = []
colunas_numericas = []

for coluna in df.columns:
    
    if df[coluna].nunique() < 15:
        colunas_categoricas.append(coluna)
    else:
        colunas_numericas.append(coluna)

print("Características categóricas:")
print(colunas_categoricas)

print("\nCaracterísticas numéricas:")
print(colunas_numericas)


# ==========================================
# APARENCIA DOS DADOS NUMERICOS
# ==========================================

df[colunas_numericas].describe()


# ==========================================
# FREQUÊNCIA DAS VARIAVEIS CATEGORICAS
# ==========================================

for coluna in colunas_categoricas:
    print(f"\nFrequência da característica: {coluna}")
    print(df[coluna].value_counts())



# ==========================================
# VERIFICAÇÃO DE DADOS FALTANTES
# ==========================================

df.isnull().sum()



























