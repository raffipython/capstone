"""Backend of Near Earth Object Viewer program to conduct
the methods to obtain the data and do calculations on them.
To determine, the speed and distances of the asteroids as
well as print data to specific asteroids.

authors: Bryan Wynes, Jacob Scanlan, and Raffi Jubrael
date: 2023/08/04
version: 1.0.0
"""

import requests
import datetime as dt


def determine_threat(au_distance):
    """ Determines threat level based on distance.

    :param au_distance: Distance of NEO in AU
    :type au_distance: float
    :return: Message about threat level
    """
    if 0.08 < au_distance <= 0.09:
        return "Extremely low"
    elif 0.06 < au_distance <= 0.07:
        return "Low"
    elif 0.04 < au_distance <= 0.05:
        return "Moderate, monitor closely"
    elif 0.02 < au_distance <= 0.03:
        return "High, plan to intercept"
    elif au_distance <= 0.01:
        return "Impact imminent"
    else:
        return "Negligible"


def impact_date_calculator(velocity, distance_miles):
    """ Calculates date of impact given current velocity and distance.

    :param velocity: velocity of NEO in MPH
    :type velocity: float
    :param distance_miles: distance of NEO in miles
    :type distance_miles: float
    :return: date string
    """
    current_date = dt.datetime.now()
    delta = dt.timedelta(hours=distance_miles / velocity)
    impact_date = current_date + delta
    impact_date = impact_date.strftime("%Y-%b-%d %H:%M")
    return impact_date


def neos_approaching(days):
    """ NEOs approaching Earth within given days. It makes the API call to NASA's website for the data about NEOs.

    :param days: range of days for approaching NEOs
    :type days: int
    :return: dictionary of NEOs approaching Earth within given days
    """
    try:
        data = requests.get(f"https://ssd-api.jpl.nasa.gov/cad.api?date-max=%2B{days}&diameter=1")
        if data.status_code == 200:
            return data
        else:
            print("Error: Could not fetch data from the API.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


def asteroid(database, asteroid_name, count):
    """ Queries database dictionary for a given asteroid name. It returns a list with asteroid data if a match is found
    otherwise, it returns Asteroid not found message.

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
