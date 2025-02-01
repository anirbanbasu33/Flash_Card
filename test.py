import pandas as pd

def random_words():
    df = pd.read_csv('french_words.csv')
    french2eng = df.set_index('French')['English'].to_dict()
    print(french2eng)

random_words()