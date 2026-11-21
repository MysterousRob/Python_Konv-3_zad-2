"""Testy gotowego modułu wczytywania — powinny przejść od razu."""

import pytest

from src.data_load import wczytaj_oceny


def test_wczytaj_10_ocen(tmp_path):
    plik = tmp_path / "oceny.csv"
    plik.write_text("ocena\n" + "4\n" * 10, encoding="utf-8")
    assert wczytaj_oceny(plik) == [4.0] * 10


@pytest.mark.parametrize("zawartosc", [
    "ocena\n4\n5\n",  # za mało ocen
    "wynik\n" + "4\n" * 10,  # niepoprawna nazwa kolumny
    "ocena\n" + "7\n" * 10,  # niepoprawny zakres
    "ocena\n" + "abc\n" * 10,  # niepoprawny format
])
def test_niepoprawne_dane(tmp_path, zawartosc):
    plik = tmp_path / "oceny.csv"
    plik.write_text(zawartosc, encoding="utf-8")
    with pytest.raises(ValueError):
        wczytaj_oceny(plik)
