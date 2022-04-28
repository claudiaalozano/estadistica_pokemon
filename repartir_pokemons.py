
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#función que analice Pokemon.csv y los reparta entre coach_1_pokemons.csv y coach_2_pokemons.csv
def repartir_pokemons():
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
    df['Ataque'] = random.randint(1,10)
    df.to_csv('coach_1_pokemons.csv', index=False)
    df.to_csv('coach_2_pokemons.csv', index=False)
repartir_pokemons()
 
