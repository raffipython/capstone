import cmd
import urllib.parse
import requests
from pprint import pprint as p # awesome module to pretty print JSONs
import json

# ADD UI/UX
#   Collect data (give range)
#   View asteroid list
#   Choose (via number in text box)
#   Calculate
#   Option to Destroy
#       Y/N



class Astroid(cmd.Cmd):

    prompt = "[>] "
    intro = """
  _   _ _____ _____     __
 | \ | | ____/ _ \ \   / /
 |  \| |  _|| | | \ \ / / 
 | |\  | |__| |_| |\ V /  
 |_| \_|_____\___/  \_/   
\nWelcome to Near Earth Objects Viewer"""


    OBJECT_ID = None #Example 2023 HL. Run: astroid 2023 HL
    URL = "https://www.neowsapp.com/rest/v1/neo/"
    DB = {} # main database dictionary
    COUNT = 0
    TOLERANCE = 0.04 # for testing, probably want lower for real
    NAMES = {}

    def determine_threat(self, distance):
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

    def do_astroid(self, arg):
        """ Get Astroid Data"""
        try:
            #print(arg)
            #self.OBJECT_ID = urllib.parse.quote(arg)
            #x = requests.get(self.URL + self.OBJECT_ID)
            #print(x.status_code)
            #p(x.content)
            ##### Above code is for API live
            #print((list(self.NAMES.keys())[0]))
            #print(arg)
            if arg in list(self.NAMES.keys()):
                name = self.DB['data'][self.NAMES.get(arg)][0]  # name
                dist_min = float(
                    self.DB['data'][self.NAMES.get(arg)][5])  # dist_min - minimum (3-sigma) approach distance (au)
                threat = self.determine_threat(dist_min)
                print(f"Asteroid: {name}")
                print(f"Threat level: {threat}")
                print()
            else:
                print("Asteroid not found!")
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_nextyear(self, arg):
        """ Get all objects within next year and add to DB"""
        #https://ssd-api.jpl.nasa.gov/doc/cad.html
       #URL = "https://ssd-api.jpl.nasa.gov/cad.api?date-max=%2B365&diameter=1&dist-max=0.05&fullname=1&nea-comet=1&rating=1&www=1"
        URL = "https://ssd-api.jpl.nasa.gov/cad.api"
        try:
            x = requests.get(URL)
            print(x.status_code)
            #p(x.content)
            #p(json.loads(x.content))  # Good example to print data to json
            self.DB = json.loads(x.content)
            self.COUNT = self.DB['count']
            print(self.COUNT)
        except:
            pass

    def do_show(self, arg):
        """ Show all objects within next year from DB"""
        try:
            #p(self.DB)
            #p(self.DB['data'])

            # test first asteroid from list
            p(self.DB['data'][0][0]) # name
            p(self.DB['data'][0][5]) # dist_min - minimum (3-sigma) approach distance (au)

            if float(self.DB['data'][0][5]) < self.TOLERANCE:
                print("DANGER ZONE!!!")
        except:
            pass

    def do_list(self, arg):
        """ Lists all asteroids in DB"""
        for i in range(0, self.COUNT):
            name = self.DB['data'][i][0]
            self.NAMES.update({name:i})
            print(name)

    def do_threat(self, arg):
        """Lists the threat levels for the asteroids"""
        try:
            if self.COUNT > 0:
                for i in range(self.COUNT):
                    name = self.DB['data'][i][0]
                    dist_min = float(self.DB['data'][i][5])
                    threat = self.determine_threat(dist_min)
                    print(f"Asteroid: {name}")
                    print(f"Threat level: {threat}")
                    print()
            else:
                print("Asteroid doesn't exist or data is not yet found.")
        except Exception as e:
            print(f"Error, incorrect input: {str(e)}")


    def do_add(self, arg):
        """ Add an asteroid object to DB['data'] """
        # Future possibly, if we can figure it out
        pass

    def do_settings(self, arg):
        """ Get settings """
        print(f"OBJECT ID: {self.OBJECT_ID}")

    def do_exit(self, arg):
        """ Exit the server """
        exit(0)

    ###################################
    # Help messages

    def help_astroid(self):
        print("Get details of an astroid")

    def help_settings(self):
        print("Get settings")

    def help_exit(self):
            print("Exit the server")

if __name__ == '__main__':
    Astroid().cmdloop()
