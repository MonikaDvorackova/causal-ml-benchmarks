"""Backdoor-adjusted ATE for a binary treatment with discrete strata."""
from collections import defaultdict
from math import sqrt

def stratified_ate(records, treatment="treatment", outcome="outcome", stratum="stratum"):
    if not records:
        raise ValueError("empty dataset")
    groups = defaultdict(lambda: [[], []])
    for r in records:
        t = r[treatment]
        if t not in (0, 1):
            raise ValueError("treatment must be binary")
        groups[r[stratum]][t].append(float(r[outcome]))
    effect = 0.0
    for values in groups.values():
        if not values[0] or not values[1]:
            raise ValueError("positivity violation: missing treatment arm in stratum")
        effect += len(values[0] + values[1]) / len(records) * (sum(values[1])/len(values[1])-sum(values[0])/len(values[0]))
    return effect

def simulate(n=2000, seed=42, effect=2.0):
    import random
    rng = random.Random(seed)
    data = []
    for _ in range(n):
        z = rng.randrange(2)
        t = int(rng.random() < (0.8 if z else 0.2))
        y = effect*t + 4*z + rng.gauss(0, 0.5)
        data.append({"stratum": z, "treatment": t, "outcome": y})
    return data
