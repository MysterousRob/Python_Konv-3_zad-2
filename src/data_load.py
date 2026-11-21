"""Wczytywanie i walidacja ocen z pliku CSV."""

import csv
from pathlib import Path


def wczytaj_oceny(sciezka: str | Path) -> list[float]:
    """Wczytuje dokładnie 10 ocen od 1 do 6 z kolumny ``ocena``.

    Raises:
        FileNotFoundError: Gdy plik nie istnieje.
        ValueError: Gdy dane są niepoprawne lub liczba ocen jest różna od 10.
    """
    with Path(sciezka).open(encoding="utf-8-sig", newline="") as plik:
        czytnik = csv.DictReader(plik)
        if not czytnik.fieldnames or "ocena" not in czytnik.fieldnames:
            raise ValueError("Brak kolumny 'ocena' w pliku CSV")

        oceny: list[float] = []
        for numer, wiersz in enumerate(czytnik, start=2):
            wartosc = wiersz.get("ocena")
            try:
                ocena = float(wartosc)  # type: ignore[arg-type]
            except (TypeError, ValueError) as blad:
                raise ValueError(f"Nieprawidłowa ocena w wierszu {numer}") from blad
            if not 1 <= ocena <= 6:
                raise ValueError(f"Ocena poza zakresem 1–6 w wierszu {numer}")
            oceny.append(ocena)

    if len(oceny) != 10:
        raise ValueError(f"Oczekiwano 10 ocen, otrzymano {len(oceny)}")
    return oceny
