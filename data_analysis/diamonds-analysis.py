import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('data_analysis/diamonds.csv')
    df.info()
    print(df.isna().sum())
    print(df.isnull().sum())
    # Jetzt möchte ich einen Plot (Histogramm der carat-Werte) erstellen und speichern
    # Schritt 1: Pandas kann ein Histogramm erstellen
    df.hist(column='carat') # Diese Grafik ist gezeichnet auf dem plt-Objekt von matplotlib, plt ist eine leere Leinwand, die von pd.hist bemalt wird
    # plt.show()
    plt.savefig('carat_histogramm.png')


main()