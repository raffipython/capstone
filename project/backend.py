import requests

OBJECT_ID = None  # Example 2023 HL. Run: astroid 2023 HL
URL = "https://www.neowsapp.com/rest/v1/neo/"
DB = {}  # main database dictionary
COUNT = 0
TOLERANCE = 0.04  # for testing, probably want lower for real
NAMES = {}


def determine_threat(distance):
    """ Determines threat level based on distance

    :param distance: Distance of NEO in AU
    :type distance: float
    :return: Message about threat level
    """
    if 0.08 < distance <= 0.09:
        return "Extremely low, safe to lightly monitor."
    elif 0.06 < distance <= 0.07:
        return "Low"
    elif 0.04 < distance <= 0.05:
        return "Moderate, monitor closely for changes in trajectory."
    elif 0.02 < distance <= 0.03:
        return "High, start assessing plans of action to defend planet."
    elif distance <= 0.01:
        return "Impact imminent. Say a prayer."
    else:
        return "Negligible"


def neos_approaching(days):
    """ NEOs approaching Earth within given days

    :param days: Range of days for approaching NEOs
    :type days: int
    :return: Dictionary of NEOs approaching Earth within given days
    """

    data = None
    try:
        data = requests.get(f"https://ssd-api.jpl.nasa.gov/cad.api?date-max=%2B{days}&diameter=1")
        return data
    except data.status_code != 200:
        return data


def asteroid(database, asteroid_name, count):
    """ Queries database dictionary for a match for the asteroid

    :param database: Main data dictionary
    :type database: dict
    :param asteroid_name:
    :type asteroid_name: str
    :param count: Count of NEOs
    :type count: int
    :return: List with data from the database, or error message string
    """

    try:
        names_dictionary = {}
        for i in range(0, count):
            name = database['data'][i][0]
            names_dictionary.update({name: i})
        if asteroid_name in list(names_dictionary.keys()):
            name = database['data'][names_dictionary.get(asteroid_name)][0]
            dist_min = float(
                # dist_min - minimum (3-sigma) approach distance (au)
                database['data'][names_dictionary.get(asteroid_name)][5])
            threat = determine_threat(dist_min)
            return [name, dist_min, threat]
        else:
            return "Asteroid not found!"
    except Exception as e:
        print(f"Error: {str(e)}")
