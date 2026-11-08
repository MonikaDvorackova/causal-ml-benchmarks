from src.core import average_treatment_effect

def test_ate():
    assert average_treatment_effect([0, 1], [2, 3]) == 2
