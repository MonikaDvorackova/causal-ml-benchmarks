"""Compare unadjusted and backdoor-adjusted ATE over seeded simulations."""
import json
from src.causal import simulate, stratified_ate

def run(seeds=range(20), n=2000, true_effect=2.0):
    rows = []
    for seed in seeds:
        data = simulate(n=n, seed=seed, effect=true_effect)
        treated = [r["outcome"] for r in data if r["treatment"]]
        control = [r["outcome"] for r in data if not r["treatment"]]
        naive = sum(treated)/len(treated)-sum(control)/len(control)
        adjusted = stratified_ate(data)
        rows.append({"seed": seed, "naive": naive, "adjusted": adjusted})
    return {"true_effect": true_effect,
            "naive_mae": sum(abs(r["naive"]-true_effect) for r in rows)/len(rows),
            "adjusted_mae": sum(abs(r["adjusted"]-true_effect) for r in rows)/len(rows),
            "replicates": rows}

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
