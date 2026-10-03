import pytest
from audio_cutter.core import parse_timestamp_to_seconds


def test_parse_seconds_only():
    """Test parsing simple seconds input."""
    assert parse_timestamp_to_seconds("45") == 45.0
    assert parse_timestamp_to_seconds("12.5") == 12.5


def test_parse_minutes_and_seconds():
    """Test parsing MM:SS format."""
    assert parse_timestamp_to_seconds("01:30") == 90.0
    assert parse_timestamp_to_seconds("00:15") == 15.0
    assert parse_timestamp_to_seconds("10:00") == 600.0


def test_parse_hours_minutes_and_seconds():
    """Test parsing HH:MM:SS format."""
    # 1 hour (3600) + 2 minutes (120) + 30 seconds = 3750
    assert parse_timestamp_to_seconds("01:02:30") == 3750.0


def test_invalid_format_raises_error():
    """Test that invalid formats raise ValueError."""
    with pytest.raises(ValueError):
        parse_timestamp_to_seconds("1:2:3:4")