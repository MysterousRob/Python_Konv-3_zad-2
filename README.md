# Zadanie 1 — Średnia ocen z matematyki (Python)

Repozytorium szkic do samodzielnej pracy na laboratorium. 

## Cel

Napisz program, który wczytuje **dokładnie 10 ocen jednego ucznia z matematyki**, oblicza ich **zwykłą średnią arytmetyczną (bez wag)** i wyświetla wynik z dokładnością do dwóch miejsc po przecinku.

Ćwiczysz: listy, pętle, funkcje, adnotacje typów, docstringi, pracę z CSV, podział projektu na moduły, testy jednostkowe i PEP 8.

## Szybki start

Wymagany Python **3.10+**. Polecenia wykonuj w katalogu głównym projektu.

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python -m src.main --plik data/oceny.csv
```

**Ważne:** przed wykonaniem zadania część testów celowo nie przechodzi, a program zgłasza `NotImplementedError`. To oczekiwane — funkcje z `TODO` są do napisania.

## Pliki

```text
zadanie_1_srednia_ocen/
├── README.md                 # start i polecenia
├── docs/
│   ├── ZADANIE_1.md          # szczegółowe wymagania i kryteria
│   └── WSKAZOWKI.md          # pomoc bez gotowego rozwiązania
├── data/oceny.csv            # 10 przykładowych ocen
├── src/
│   ├── __init__.py
│   ├── main.py               # uruchamianie z terminala
│   ├── data_load.py          # wczytywanie danych CSV
│   ├── utils.py              # TODO: obliczanie średniej
│   └── metryki.py            # TODO: podsumowanie
├── tests/                    # testy pytest
├── .github/workflows/tests.yml
├── .gitignore
├── pyproject.toml
└── requirements.txt
```

## Uruchamianie

```bash
python -m pytest -q
python -m src.main --plik data/oceny.csv
```

Możesz podmienić plik CSV, zachowując kolumnę `ocena` i dokładnie 10 wierszy danych.

## Warunki poprawności

- Średnia = suma ocen / liczba ocen.
- Nie stosuj wag ani zaokrąglania podczas obliczeń; zaokrąglij dopiero przy prezentacji wyniku.
- Pusta lista w `oblicz_srednia` powoduje `ValueError`.
- Plik zawierający inną liczbę ocen niż 10, oceny spoza zakresu 1–6 albo niepoprawne wartości powoduje `ValueError`.
- Działający projekt przechodzi testy `python -m pytest -q`.

Pełne polecenie: [docs/ZADANIE_1.md](docs/ZADANIE_1.md).
