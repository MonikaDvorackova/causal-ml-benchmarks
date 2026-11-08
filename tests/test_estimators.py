import pytest
from src.estimators import ipw_ate, bootstrap_interval

def test_randomized_ate_and_interval():
    rows=[{"treatment":t,"outcome":2*t,"propensity":0.5} for _ in range(50) for t in (0,1)]
    assert ipw_ate(rows)==2.0
    lo,hi=bootstrap_interval(rows,repetitions=100,seed=1)
    assert lo<=2<=hi
    with pytest.raises(ValueError):
        ipw_ate([{"treatment":1,"outcome":2,"propensity":1}])
