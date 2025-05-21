import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Datenanalyse/Sonnenzeiten_München_2025.csv')
df['Sonnenaufgang'] = pd.to_datetime(df['Sonnenaufgang'], format='%H:%M').dt.time
df['Sonnenuntergang'] = pd.to_datetime(df['Sonnenuntergang'], format='%H:%M').dt.time

df['Datum'] = pd.to_datetime(df['Datum'])

df['Aufgang_min'] = df['Sonnenaufgang'].apply(lambda t: t.hour * 60 + t.minute)
df['Untergang_min'] = df['Sonnenuntergang'].apply(lambda t: t.hour * 60 + t.minute)

plt.figure(figsize=(14, 6))
plt.plot(df['Datum'], df['Aufgang_min'], label='Sonnenaufgang', color='orange')
plt.plot(df['Datum'], df['Untergang_min'], label='Sonnenuntergang', color='purple')
plt.title('Sonnenaufgang und Sonnenuntergang in München – 2025')
plt.xlabel('Datum')
plt.ylabel('Tageszeit (Minuten nach Mitternacht)')
plt.legend()
plt.grid(True)

plt.yticks(
    ticks=range(300, 1321, 60),
    labels=[f'{h:02d}:00' for h in range(5, 23)]
)

plt.tight_layout()
plt.savefig('zeiten.jpg')
