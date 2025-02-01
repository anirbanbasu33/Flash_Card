import pandas as pd, random

def random_words():
    df = pd.read_csv('french_words.csv')
    # french2eng = df.set_index('French')['English'].to_dict()


    # This code converts a Pandas DataFrame (df) into a list of dictionaries, where each dictionary represents a row in the DataFrame.
    french2eng = df.to_dict(orient="records")

    current_card = random.choice(french2eng)

    print(french2eng)
    print("\n\n")
    print(current_card)


random_words()