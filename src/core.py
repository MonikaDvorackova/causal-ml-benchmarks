def average_treatment_effect(y0: list[float], y1: list[float]) -> float:
    """Oracle ATE for paired potential outcomes in synthetic benchmarks."""
    if not y0 or len(y0) != len(y1):
        raise ValueError("Potential outcomes must be nonempty and paired")
    return sum(b - a for a, b in zip(y0, y1)) / len(y0)
