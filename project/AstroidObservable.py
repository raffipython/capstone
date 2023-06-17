import cmd
import urllib.parse
import requests
from pprint import pprint as p

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

    def do_astroid(self, arg):
        """ Get Astroid Data"""
        try:
            print(arg)
            self.OBJECT_ID = urllib.parse.quote(arg)
            x = requests.get(self.URL + self.OBJECT_ID)
            print(x.status_code)
            p(x.content)
        except:
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










