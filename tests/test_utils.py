"""Testy funkcji do napisania przez studentów."""

import pytest

from src.utils import oblicz_srednia


def test_srednia_z_10_ocen():
    oceny = [4, 5, 3, 4, 6, 5, 4, 3, 5, 4]
    assert oblicz_srednia(oceny) == pytest.approx(4.3)


def test_srednia_z_krotszej_listy():
    assert oblicz_srednia([2, 4, 6]) == pytest.approx(4.0)


def test_srednia_z_pustej_listy():
    with pytest.raises(ValueError):
        oblicz_srednia([])


# TODO (student): dopisz własny test dla innej listy 10 ocen.
def test_srednia_z_innej_listy():
    oceny = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert oblicz_srednia(oceny) == pytest.approx(5.5)