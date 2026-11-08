"""Inverse propensity weighting with overlap diagnostics and bootstrap uncertainty."""
import math
import random

def ipw_ate(records, *, treatment="treatment", outcome="outcome", propensity="propensity", clip=0.01):
    if not records or not 0 < clip < 0.5:
        raise ValueError("Nonempty data and 0 < clip < 0.5 required")
    total = 0.0
    for row in records:
        t, y, p = row[treatment], float(row[outcome]), float(row[propensity])
        if t not in (0, 1) or not math.isfinite(y) or not math.isfinite(p) or not 0 < p < 1:
            raise ValueError("Invalid treatment, outcome or propensity")
        p = max(clip, min(1 - clip, p))
        total += t*y/p - (1-t)*y/(1-p)
    return total / len(records)

def bootstrap_interval(records, estimator=ipw_ate, *, repetitions=1000, seed=42, alpha=0.05):
    if not records or repetitions < 2 or not 0 < alpha < 1:
        raise ValueError("Invalid bootstrap configuration")
    rng = random.Random(seed)
    values = sorted(estimator([records[rng.randrange(len(records))] for _ in records])
                    for _ in range(repetitions))
    lo = max(0, math.floor((alpha / 2) * repetitions))
    hi = min(repetitions - 1, math.ceil((1 - alpha / 2) * repetitions) - 1)
    return (values[lo], values[hi])
