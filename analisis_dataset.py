import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
#función que analice Pokemon.csv y nos devuelva una serie con los datos de cada pokemon
def analisis_dataset():
    df = pd.read_csv('Pokemon.csv')
    df = df.drop(['#'], axis=1)
    df = df.drop(['Type 2'], axis=1)
    df = df.drop(['Generation'], axis=1)
    df = df.drop(['Legendary'], axis=1)
    df = df.drop(['Name'], axis=1)
    df = df.drop(['Total'], axis=1)
    df = df.drop(['HP'], axis=1)
    df = df.drop(['Attack'], axis=1)
    df = df.drop(['Defense'], axis=1)
    df = df.drop(['Sp. Atk'], axis=1)
    df = df.drop(['Sp. Def'], axis=1)
    df = df.drop(['Speed'], axis=1)
analisis_dataset()
#función que calcule la media, varianza, desviación típica y la mediana de cada columna de Pokemon.csv
def analisis_dataset_2():
    df = pd.read_csv('Pokemon.csv')
    df = df.drop(['#'], axis=1)
    df = df.drop(['Type 2'], axis=1)
    df = df.drop(['Generation'], axis=1)
    df = df.drop(['Legendary'], axis=1)
    df = df.drop(['Name'], axis=1)
    df = df.drop(['Total'], axis=1)
    df = df.drop(['HP'], axis=1)
    df = df.drop(['Attack'], axis=1)
    df = df.drop(['Defense'], axis=1)
    df = df.drop(['Sp. Atk'], axis=1)
    df = df.drop(['Sp. Def'], axis=1)
    df = df.drop(['Speed'], axis=1)
    df.describe()
analisis_dataset_2()

#función que te calcule el 68%, el 95% y el 97% de cada columna de Pokemon.csv
def percentiles():
    df = pd.read_csv('Pokemon.csv')
    df = df.drop(['#'], axis=1)
    df = df.drop(['Type 2'], axis=1)
    df = df.drop(['Generation'], axis=1)
    df = df.drop(['Legendary'], axis=1)
    df = df.drop(['Name'], axis=1)
    df = df.drop(['Total'], axis=1)
    df = df.drop(['HP'], axis=1)
    df = df.drop(['Attack'], axis=1)
    df = df.drop(['Defense'], axis=1)
    df = df.drop(['Sp. Atk'], axis=1)
    df = df.drop(['Sp. Def'], axis=1)
    df = df.drop(['Speed'], axis=1)
    df.describe()
    df.describe(percentiles=[.68, .95, .97])
percentiles()