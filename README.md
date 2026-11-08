# causal-ml-benchmarks

Stratified backdoor adjustment under measured confounding.

## Scope

A small, inspectable, reproducible **v0.1 reference implementation**. The project is not presented as a production system or peer-reviewed research result.

## Requirements

Python 3.12

## Setup

```bash
python -m pip install pytest
```

## Run example / experiment

From the repository root:

```bash
python -m experiments.confounding_study
```

## Test

```bash
python -m pytest -q
```

## Reproducibility

Experiments use deterministic inputs or explicitly seeded generators. See the experiment sources for assumptions and input sizes. CI exercises both tests and the example; check the Actions tab for actual run results. No empirical results are claimed without executed measurements.

## Limitations

Identification assumes consistency, exchangeability conditional on the measured stratum, and positivity. Synthetic data do not establish performance on observational datasets.

## License

MIT. Contributions should include a focused regression test and an explanation of changed assumptions.
