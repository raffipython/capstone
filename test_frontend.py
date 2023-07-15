"""Testing for frontend.py"""
import frontend


def test_asteroid_data_handler():
    assert frontend.asteroid_data_handler() is None
