"""Testing for frontend.py"""
import frontend


def test_asteroid_data_handler():
    """ Tests asteroid_data_handler function in frontend.py
    Checks for:
        Function ran correctly and returned nothing
    """
    assert frontend.asteroid_data_handler() is None
