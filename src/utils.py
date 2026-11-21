"""Podstawowe funkcje statystyczne — część do wykonania przez studenta."""


def oblicz_srednia(oceny: list[float]) -> float:
    """Zwraca średnią arytmetyczną ocen.

    Args:
        oceny: Lista liczb reprezentujących oceny.

    Returns:
        Średnia arytmetyczna jako float.

    Raises:
        ValueError: Gdy lista jest pusta.
    """
    if not oceny:
        raise ValueError("nie można obliczyć średniej z pustej listy ocen")
    return sum(oceny) / len(oceny)