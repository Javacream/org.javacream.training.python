
# 🆚 Vergleich: Dask vs. Modin vs. Pandas

| Merkmal                 | 🐼 Pandas                       | ⚡ Modin                            | 🧱 Dask                          |
|-------------------------|--------------------------------|------------------------------------|----------------------------------|
| **Skalierung**          | Nur **ein CPU-Kern**           | Mehrere Kerne (lokal oder Cluster) | Skalierbar auf Cluster & verteilte Systeme |
| **API-Kompatibilität**  | Native API                     | Fast 100 % Pandas-kompatibel       | Ähnlich, aber nicht 100 % kompatibel |
| **Performance (lokal)** | Gut bei kleinen Daten          | Besser bei mittleren Datenmengen   | Gut bis sehr gut bei großen Daten |
| **Clusterfähig**        | ❌ Nicht                        | ✅ (via Ray oder Dask)             | ✅ Vollständig verteilt          |
| **Lazy Evaluation**     | ❌ Nein                         | ❌ Nein                            | ✅ Ja                            |
| **Streaming/Big Data**  | ❌ Nicht geeignet               | ⚠️ Eingeschränkt                   | ✅ Sehr gut                      |
| **Installation**        | `pip install pandas`           | `pip install modin[ray]`          | `pip install dask[dataframe]`   |
| **Lernkurve**           | Einfach                        | Sehr einfach (wie Pandas)          | Etwas höher                     |
| **Machine Learning**    | Integration via sklearn        | Integration via sklearn            | Gut mit Dask-ML                 |
| **Use Cases**           | Kleine bis mittlere Datensätze | Pandas-Ersatz mit Speedup          | Große oder verteilte Datenverarbeitung |

---

## 📌 Zusammenfassung

### ✅ **Pandas**
- Beste Wahl für **kleine bis mittlere Datenmengen**
- Einfach, stabil, sehr große Community

### ✅ **Modin**
- Ideal für Nutzer, die mehr Performance wollen ohne Pandas-Code zu ändern
- Parallele Verarbeitung mit `Ray` oder `Dask` im Backend

### ✅ **Dask**
- Beste Option für **verteilte Verarbeitung** und **Big Data**
- Ideal für Pipelines, Dashboards, Machine Learning auf großen Daten

---

## 🔧 Beispiel: Pandas → Modin

```python
# Mit Pandas
import pandas as pd
df = pd.read_csv("data.csv")

# Mit Modin (identisch!)
import modin.pandas as pd
df = pd.read_csv("data.csv")
```

---

## 🧠 Wann welches Framework?

| Datenmenge / Problem            | Empfehlung  |
|--------------------------------|-------------|
| < 1 Mio Zeilen                 | ✅ Pandas    |
| 1–10 Mio Zeilen, mehr CPUs     | ✅ Modin     |
| 10+ Mio Zeilen, verteilte Umgebung | ✅ Dask  |
| Komplexe Workflows / Pipelines | ✅ Dask      |
