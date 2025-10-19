import os
import urllib.request
import zipfile
from pyspark.sql import SparkSession

# Baixar e descompactar o arquivo CSV se ele não existir
csv_path = 'imdb-reviews-pt-br.csv'
zip_url = 'https://raw.githubusercontent.com/N-CPUninter/Big_Data/main/data/imdb-reviews-pt-br.zip'
zip_path = 'imdb-reviews-pt-br.zip'

if not os.path.exists(csv_path):
    print("Baixando o arquivo zip...")
    urllib.request.urlretrieve(zip_url, zip_path)
    print("Extraindo o arquivo zip...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall('.')
    os.remove(zip_path)
    print("Arquivo CSV pronto!")

# Iniciar SparkSession
appName = "PySpark Trabalho de Big Data"
master = "local"
spark = SparkSession.builder.appName(appName).master(master).getOrCreate()

imdb_df = spark.read.csv(csv_path,
                         header=True,
                         quote="\"",
                         escape="\"",
                         encoding="UTF-8")

print("SparkSession iniciada e dados carregados com sucesso.")


# -------- Questão 01 ---------

identificacao_4746517 = "OK"

def map1(x):
    try:
        sentiment = x['sentiment']
        id_val = int(x['id']) if x['id'] else 0
    except:
        id_val = 0
        sentiment = None
    return (sentiment, id_val)

def reduceByKey1(x, y):
    return x + y

resultado_q1 = imdb_df.rdd.map(map1).reduceByKey(reduceByKey1).collect()

print("\n--- RESULTADO QUESTÃO 01 ---")
print("RU: 4746517")

soma_neg_q1 = 0
for sentiment, soma in resultado_q1:
    if sentiment == 'neg':
        soma_neg_q1 = soma

print(f"Soma total dos IDs onde sentiment == 'neg': {soma_neg_q1}")


# -------- Questão 02 ---------

import re

identificacao_4746517 = "OK"

def contar_palavras(texto):
    if texto is None:
        return 0
    palavras = re.split(r'\s+', texto.strip())
    return len([p for p in palavras if p])

def map2(x):
    sentiment = x['sentiment']
    text_en = x['text_en']
    text_pt = x['text_pt']
    return (sentiment, (contar_palavras(text_en), contar_palavras(text_pt)))

def reduceByKey2(a, b):
    return (a[0] + b[0], a[1] + b[1])

resultado_q2 = imdb_df.rdd.map(map2).reduceByKey(reduceByKey2).collect()

print("\n--- RESULTADO QUESTÃO 02 ---")
print("RU: 4746517")

diferenca_palavras = 0
for sentiment, (total_en, total_pt) in resultado_q2:
    if sentiment == 'neg':
        diferenca_palavras = total_pt - total_en
        print(f"Total de palavras em português (neg): {total_pt}")
        print(f"Total de palavras em inglês (neg): {total_en}")

print(f"Diferença (português - inglês): {diferenca_palavras}")
