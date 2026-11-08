import pytest
from src.causal import stratified_ate, simulate

def test_recovers_known_effect():
    assert abs(stratified_ate(simulate()) - 2.0) < 0.15

def test_posivitity_check():
    with pytest.raises(ValueError, match="positivity"):
        stratified_ate([{"stratum":0,"treatment":0,"outcome":1}])

def test_reproducible():
    assert simulate(10) == simulate(10)
