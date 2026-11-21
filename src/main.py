"""Uruchamianie programu z wiersza poleceń."""

import argparse
from pathlib import Path

from src.data_load import wczytaj_oceny
from src.metryki import przygotuj_podsumowanie


def main() -> None:
    """Wczytuje 10 ocen i prezentuje podsumowanie."""
    parser = argparse.ArgumentParser(description="Średnia ocen z matematyki")
    plik_domyslny = Path(__file__).resolve().parent.parent / "data" / "oceny.csv"
    parser.add_argument("--plik", type=Path, default=plik_domyslny)
    argumenty = parser.parse_args()

    oceny = wczytaj_oceny(argumenty.plik)
    podsumowanie = przygotuj_podsumowanie(oceny)
    print("Przedmiot: matematyka")
    print(f"Liczba ocen: {podsumowanie['liczba_ocen']}")
    print(f"Suma ocen: {podsumowanie['suma_ocen']:g}")
    print(f"Średnia: {podsumowanie['srednia']:.2f}")


if __name__ == "__main__":
    main()
