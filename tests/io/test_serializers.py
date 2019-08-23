import pytest

from frater.io import frater_to_json
from ..mocks import MOCKS

mocks = [(frater, json) for frater, json in zip(MOCKS.frater.get_mocks(), MOCKS.json.get_mocks())]
mocks += [({'some': 'mock', 'data': 'test'}, {'some': 'mock', 'data': 'test'})]


@pytest.mark.parametrize("frater, json", mocks)
def test_frater_to_json(frater, json):
    assert frater_to_json(frater) == json
