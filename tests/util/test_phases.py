import pytest
from utilities.phases import phase_finder


def test_phase_finder():
    assert phase_finder('hydrogen', 88) == 'gas'
    assert phase_finder('OXYgen', 0) == 'gas'

    with pytest.raises(Exception):
        assert phase_finder('hydrsssssoge', 88)