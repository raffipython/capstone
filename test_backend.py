"""Testing for backend.py"""
import json

import pytest
import backend
import datetime as dt
import requests


test_determine_threat_testdata = [(0.081, "Extremely low"),
                                  (0.061, "Low"),
                                  (0.041, "Moderate, monitor closely"),
                                  (0.021, "High, plan to intercept"),
                                  (0.01, "Impact imminent"),
                                  (1, "Negligible")]


@pytest.mark.parametrize("test_input,expected", test_determine_threat_testdata)
def test_determine_threat(test_input, expected):
    assert backend.determine_threat(test_input) == expected


test_impact_date_calculator_expected_date = dt.datetime.now() + dt.timedelta(hours=10)
test_impact_date_calculator_expected_date = test_impact_date_calculator_expected_date.strftime("%Y-%b-%d %H:%M")
test_impact_date_calculator_testdata = [([10, 100], test_impact_date_calculator_expected_date)]


@pytest.mark.parametrize("test_input,expected", test_impact_date_calculator_testdata)
def test_impact_date_calculator(test_input, expected):
    assert backend.impact_date_calculator(test_input[0], test_input[1]) == expected


test_neos_approaching_testdata = [(1, True)]


@pytest.mark.parametrize("test_input,expected", test_neos_approaching_testdata)
def test_neos_approaching(test_input, expected):
    assert isinstance(backend.neos_approaching(test_input), requests.models.Response) == expected


test_asteroid_testdata_dictionary = json.loads('{"signature":{"source":"NASA/JPL SBDB Close Approach Data API",'
                                               '"version":"1.5"},"count":3,'
                                               '"fields":["des","orbit_id","jd","cd","dist","dist_min","dist_max",'
                                               '"v_rel","v_inf","t_sigma_f","h","diameter","diameter_sigma"],'
                                               '"data":[["2023 NY","2","2460141.313861245","2023-Jul-15 19:32",'
                                               '"0.0295819034655131","0.0294634624299963","0.0297003060566119",'
                                               '"2.11053770573858","2.06742034574653","00:43","27.034",null,null],'
                                               '["My_Asteroid","1","2460141.606257795","2023-Jul-16 02:33",'
                                               '"0.0401919186595426","0.0398010538236474","0.0405827800223621",'
                                               '"17.0751454226213","17.0712625013106","00:02","25.135",null,null],'
                                               '["2023 MG6","5","2460142.400871311","2023-Jul-16 21:37",'
                                               '"0.0243278302080612","0.0239987089652305","0.024656938873722",'
                                               '"12.3784096625372","12.3695585181074","00:01","20.442",null,null]]}')
test_asteroid_closest_date = "2023-Jul-16 02:33"
test_asteroid_impact_date = backend.impact_date_calculator(17.0751454226213 * 2236.94, 0.0398010538236474 * 92955807.3)
test_asteroid_testdata_expected = ["My_Asteroid",
                                   "0.040",
                                   "3699739.09",
                                   "Negligible",
                                   "38196.08 MPH",
                                   test_asteroid_closest_date,
                                   test_asteroid_impact_date]
test_asteroid_testdata = [([test_asteroid_testdata_dictionary, "My_Asteroid", 3], test_asteroid_testdata_expected)]


@pytest.mark.parametrize("test_input,expected", test_asteroid_testdata)
def test_asteroid(test_input, expected):
    assert backend.asteroid(test_asteroid_testdata[0][0][0], test_asteroid_testdata[0][0][1],
                            test_asteroid_testdata[0][0][2]) == expected
