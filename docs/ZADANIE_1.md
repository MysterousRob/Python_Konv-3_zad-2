# Zadanie 1: obliczanie średniej ocen z matematyki

## Treść zadania

Uczeń otrzymał **10 ocen z matematyki**. Napisz program, który oblicza **średnią arytmetyczną** tych ocen, bez wag. Dane znajdują się w `data/oceny.csv` (pojedyncza kolumna `ocena`).

## Co należy wykonać

1. Zapoznaj się ze strukturą repozytorium i przykładowym plikiem CSV.
2. W `src/utils.py` zaimplementuj `oblicz_srednia(oceny: list[float]) -> float`. Dla pustej listy zgłoś `ValueError`.
3. W `src/metryki.py` zaimplementuj `przygotuj_podsumowanie(oceny: list[float]) -> dict[str, float | int]`. Zwróć słownik z kluczami `liczba_ocen`, `suma_ocen`, `srednia`. Wykorzystaj `oblicz_srednia`, nie kopiuj obliczeń.
4. Uruchom `python -m pytest -q` i popraw kod tak, by wszystkie testy przechodziły.
5. Uruchom `python -m src.main --plik data/oceny.csv` i sprawdź wydrukowany rezultat.
6. Dodaj **własny test** dla kolejnej listy 10 ocen w `tests/test_utils.py`.

## Kontrakt funkcji

`oblicz_srednia([2, 4, 6])` → `4.0` (przykład działania funkcji na krótkiej liście; wymóg 10 ocen dotyczy danych programu).

`przygotuj_podsumowanie([2, 4, 6])` → `{'liczba_ocen': 3, 'suma_ocen': 12.0, 'srednia': 4.0}`.

Dane z CSV: dokładnie 10 ocen, każda liczba z zakresu od 1 do 6. Przykładowy plik zawiera wyłącznie oceny całkowite, ale parser obsługuje też oceny ułamkowe (np. `4.5`).

## Kryteria oceny (propozycja: 10 pkt)

- Poprawna funkcja średniej i obsługa pustej listy: 4 pkt.
- Poprawne podsumowanie i ponowne użycie funkcji: 2 pkt.
- Testy: wszystkie istniejące testy + jeden własny przypadek: 2 pkt.
- Czytelność, PEP 8, adnotacje typów i docstringi: 1 pkt.
- Poprawne uruchomienie modułu `src.main`: 1 pkt.

## Oddanie

Przekaż link do swojego repozytorium GitHub lub archiwum ZIP bez folderów `.venv`, `__pycache__` i `.pytest_cache`. Nie zmieniaj testów tylko po to, aby uzyskać pozytywny wynik.

## Zgodność z materiałami

Zadanie odpowiada slajdowi „ZADANIE 1 — obliczanie średniej ocen z matematyki” z przesłanej prezentacji (strona 35). Moduły oraz folder `tests` nawiązują do pokazanej w materiałach organizacji projektu.
