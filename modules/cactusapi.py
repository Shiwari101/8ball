#############################################################################################
#                                                                                           #
#   CACTUSAPI V0.1 CREATED BY OWOQQ | API ENDPOINT: http:cactusqq.herokuapp.com/api         #
#   MODIFYING THIS CODE WITHOUT PERMISSION IS NOT PERMITTED                                 #
#                                                                                           #
#   SHARING THIS MODULE TO ANYONE ELSE WHO IS NOT GRANTED FOR THE API IS NOT PERMITTED      #
#   THIS MODULE CAN ONLY BE DOWNLOADED VIA CACTUSAPI OFFICIAL WEBSITE                       #
#   DOCUMENTATION: http:cactusqq.herokuapp.com/api.html                                     #
#                                                                                           #
#   ! Sharing your API key or password will result in deletion of your account              #
#                                                                                           #
#############################################################################################

import requests

endpoint = r"https://api-cactus.herokuapp.com/api/"
usermonthly = r"https://api-cactus.herokuapp.com/api/usermonthly"
userlevel = r"https://api-cactus.herokuapp.com/api/userlevel"
userxp = r"https://api-cactus.herokuapp.com/api/userxp"
userwarns = r"https://api-cactus.herokuapp.com/api/userwarns"
userstatus = r"https://api-cactus.herokuapp.com/api/userstatus"

class CactusAPI():
    """
    CactusAPI Connection Instance
    ------------
    All functions and subfunctions are connected to this class.
    Authenticate with your API key.
    """
    def __init__(self, key:str):
        self.key = key

    def __str__(self) -> str:
        return "CactusAPI connection instance"

    def usermonthly(self, id) -> str:
        """
        CactusAPI.usermonthly
        ----------
        Returns the Monthly XP value for the user with specified ID.
        Required Parameters: ID
        This function should be run under CactusAPI class instance

        Returns a string value.
        """
        params = {
            "key":self.key,
            "id": id
        }
        r = requests.get(url=usermonthly, params=params)
        return r.text

    def userlevel(self, id) -> str:
        """
        CactusAPI.userlevel
        ----------
        Returns the level for the user with specified ID.
        Required Parameters: ID
        This function should be run under CactusAPI class instance

        Returns a string value.
        """
        params = {
            "key":self.key,
            "id": id
        }
        r = requests.get(url=userlevel, params=params)
        return r.text

    def userxp(self, id) -> str:
        """
        CactusAPI.userxp
        ----------
        Returns the current and next level xp values for the user with specified ID.
        Required Parameters: ID
        This function should be run under CactusAPI class instance

        Returns a string value. (currentXP/nextXP)
        """
        params = {
            "key":self.key,
            "id": id
        }
        r = requests.get(url=userxp, params=params)
        return r.text

    def userwarns(self, id) -> str:
        """
        CactusAPI.userwarns
        ----------
        Returns the warn count for the user with specified ID.
        Required Parameters: ID
        This function should be run under CactusAPI class instance

        Returns a string value.
        """
        params = {
            "key":self.key,
            "id": id
        }
        r = requests.get(url=userwarns, params=params)
        return r.text

    def userstatus(self, id) -> str:
        """
        CactusAPI.userstatus
        ----------
        Returns the status for the user with specified ID.
        Required Parameters: ID
        This function should be run under CactusAPI class instance

        Returns a string value about whether the user is banned or not (from the leveling system).
        """
        params = {
            "key":self.key,
            "id": id
        }
        r = requests.get(url=userstatus, params=params)
        return r.text
