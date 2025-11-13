# Python f-String Cheat Sheet

## 🧱 Grundsyntax

``` python
f"{wert:format_spec}"
```

## 📐 Ausrichtung

  Code   Bedeutung
  ------ --------------
  `<`    linksbündig
  `>`    rechtsbündig
  `^`    zentriert

``` python
f"{42:<5}"   # '42   '
f"{42:>5}"   # '   42'
f"{42:^5}"   # ' 42  '
```

## 🔢 Füllzeichen

``` python
f"{42:_>5}"   # '__42'
f"{42:0>5}"   # '00042'
```

## 🔣 Zahlentypen

  Typ         Beschreibung
  ----------- --------------
  `d`         Dezimal
  `b`         Binär
  `o`         Oktal
  `x` / `X`   Hex
  `e` / `E`   Exponential
  `f`         Festkomma
  `%`         Prozent

## ➕ Vorzeichen

``` python
f"{42:+d}"  # '+42'
f"{42: d}"  # ' 42'
f"{-42: d}" # '-42'
```

## 📏 Breite & Nachkommastellen

``` python
f"{3.14159:8.2f}"   # '    3.14'
```

## 🔢 Tausendertrennzeichen

``` python
f"{1000000:,}"  # '1,000,000'
f"{1000000:_}"  # '1_000_000'
```

## 🔤 Strings formatieren

``` python
f"{'ABC':*^10}"   # '***ABC****'
```

## 🕒 Datum/Zeit

``` python
from datetime import datetime
f"{datetime.now():%Y-%m-%d %H:%M}"
```

## 🧩 Komplettes Format

    [[fill]align][sign][#][0][width][grouping][.precision][type]
