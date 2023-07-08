import requests
import datetime as dt


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


def impact_date_calculator(vel, dist):
    """ Calculates date of impact given current velocity and distance

    :param vel: velocity of NEO in MPH
    :type vel: float
    :param dist: distance of NEO in miles
    :type dist: float
    :return: date string
    """
    current_date = dt.datetime.now()
    delta = dt.timedelta(hours=dist/vel)
    impact_date = current_date + delta
    impact_date = impact_date.strftime("%Y-%b-%d %H:%S")
    return impact_date


def neos_approaching(days):
    """ NEOs approaching Earth within given days

    :param days: range of days for approaching NEOs
    :type days: int
    :return: dictionary of NEOs approaching Earth within given days
    """

    data = None
    try:
        data = requests.get(f"https://ssd-api.jpl.nasa.gov/cad.api?date-max=%2B{days}&diameter=1")
        return data
    except data.status_code != 200:
        return data


def asteroid(database, asteroid_name, count):
    """ Queries database dictionary for a match for the asteroid

    :param database: main data dictionary
    :type database: dict
    :param asteroid_name: actual NEO designator
    :type asteroid_name: str
    :param count: count of NEOs
    :type count: int
    :return: list with data from the database, or error message string
    """

    try:
        names_dictionary = {}
        for i in range(0, count):
            name = database['data'][i][0]
            names_dictionary.update({name: i})
        if asteroid_name in list(names_dictionary.keys()):
            name = database['data'][names_dictionary.get(asteroid_name)][0]
            # dist_min - minimum (3-sigma) approach distance (au)
            dist_min_au = float(database['data'][names_dictionary.get(asteroid_name)][5])
            dist_min_miles = dist_min_au * 92955807.3
            threat = determine_threat(dist_min_au)
            dist_min_formatted = "{:.3f}".format(dist_min_au)  # Format to two decimal places
            dist_min_miles_formatted = "{:.2f}".format(dist_min_miles)  # Format to two decimal places
            # v_rel - velocity relative to the approach body at close approach (km/s)
            velocity = float(database['data'][names_dictionary.get(asteroid_name)][7])
            velocity = velocity * 2236.94  # Convert km/s to mph
            impact_date = impact_date_calculator(velocity, dist_min_miles)
            velocity_format = "{:.2f}".format(velocity)
            velocity_str = f"{velocity_format} MPH"
            closest_approach_date = database['data'][names_dictionary.get(asteroid_name)][3]
            return [name, dist_min_formatted, dist_min_miles_formatted, threat, velocity_str, closest_approach_date,
                    impact_date]
        else:
            return "Asteroid not found!"
    except Exception as e:
        print(f"Error: {str(e)}")
