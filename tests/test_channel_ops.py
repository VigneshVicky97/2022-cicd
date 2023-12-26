from functools import partial

import pytest

# from ..functions.operations import ChannelNotFoundError, get_channel  # This line causes import error during pytest
from functions.operations import ChannelNotFoundError, get_channel

# Location of Mock Channles Database
MOCK_DB = "tests/mock_channels.db"
get_channel_mock = partial(get_channel, db_path=MOCK_DB)


# Test Channel Success
def test_get_channel_success() -> None:
    channel = get_channel_mock("arjancodes")
    assert channel["name"] == "ArjanCodes"


#Test Channel Failure
def test_get_channel_fail() -> None:
    with pytest.raises(ChannelNotFoundError):
        get_channel_mock("arjancodes123")
