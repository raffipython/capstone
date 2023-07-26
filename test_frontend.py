"""Testing for frontend.py

authors: Bryan Wynes, Jacob Scanlan, and Raffi Jubrael
date: 2023/07/27
version: 0.0.3
"""
import frontend


def test_asteroid_data_handler():
    """ Tests asteroid_data_handler function in frontend.py
    Checks for:
        Function ran correctly and returned nothing
    """
    assert frontend.asteroid_data_handler() is None
