"""Podsumowanie wyników — część do wykonania przez studenta."""
from src.utils import oblicz_srednia


def przygotuj_podsumowanie(oceny: list[float]) -> dict[str, float | int]:
    """Zwraca liczbę ocen, ich sumę i średnią.

    Zwracany słownik zawiera klucze: liczba_ocen, suma_ocen, srednia.
    Dla pustej listy powinien zostać zgłoszony ValueError.
    """
    # TODO (zadanie 1): wykorzystaj oblicz_srednia i zwróć słownik.
    if not oceny:
        raise ValueError("nie można przygotować podsumowania z pustej listy ocen")
    return {
        "liczba_ocen": len(oceny),
        "suma_ocen": sum(oceny),
        "srednia": oblicz_srednia(oceny),
    }