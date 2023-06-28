import cmd
import urllib.parse
import requests
from pprint import pprint as p # awesome module to pretty print JSONs
import json

class Astroid(cmd.Cmd):

    prompt = "[>] "
    intro = """
    ___         __             _     ______  __                               __    __   
   /   |  _____/ /__________  (_)___/ / __ \/ /_  ________  ______   ______ _/ /_  / /__ 
  / /| | / ___/ __/ ___/ __ \/ / __  / / / / __ \/ ___/ _ \/ ___/ | / / __ `/ __ \/ / _ \\
 / ___ |(__  ) /_/ /  / /_/ / / /_/ / /_/ / /_/ (__  )  __/ /   | |/ / /_/ / /_/ / /  __/
/_/  |_/____/\__/_/   \____/_/\__,_/\____/_.___/____/\___/_/    |___/\__,_/_.___/_/\___/ 
\nWelcome to Astroid Observable"""


    OBJECT_ID = None #Example 2023 HL. Run: astroid 2023 HL
    URL = "https://www.neowsapp.com/rest/v1/neo/"
    DB = {} # main database dictionary
    COUNT = 0
    TOLERANCE = 0.04 # for testing, probably want lower for real
    NAMES = {}

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
                p(self.DB['data'][self.NAMES.get(arg)][0])  # name
                p(self.DB['data'][self.NAMES.get(arg)][5])  # dist_min - minimum (3-sigma) approach distance (au)
                if float(self.DB['data'][0][5]) < self.TOLERANCE:
                    print("DANGER ZONE!!!")
            else:
                print("Astroid not found!")



        except:
            pass

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










