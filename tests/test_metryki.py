"""Testy funkcji podsumowującej do napisania przez studentów."""

import pytest

from src.metryki import przygotuj_podsumowanie


def test_podsumowanie():
    dane = [2, 4, 6]
    wynik = przygotuj_podsumowanie(dane)
    assert set(wynik) == {"liczba_ocen", "suma_ocen", "srednia"}
    assert wynik["liczba_ocen"] == 3
    assert wynik["suma_ocen"] == pytest.approx(12.0)
    assert wynik["srednia"] == pytest.approx(4.0)


def test_podsumowanie_pustej_listy():
    with pytest.raises(ValueError):
        przygotuj_podsumowanie([])
