import requests
import json


class Team(object):
    """
    docstring
    """

    firstName = ""
    lastName = ""
    ownerId = ""
    id = ""
    teamName = ""
    teamAbbrv = ""

    def __init__(self, firstName, lastName, ownerId) -> None:
        super().__init__()
        self.firstName = firstName
        self.lastName = lastName
        self.ownerId = ownerId

    def __repr__(self) -> str:
        return json.dumps(self.__dict__)


# will need to get these from a user
league_id = 78899641

# needed cookies:
espn_s2 = "AECce3s7BMGqBmM5MdDkNRMAUO2gMmDFMkmX%2F5tPMnWyl1hanIbX4DBIJkLksVm5egJ90XWz%2B8F0dm7y4oQrHhMaNHZfm%2Fij6gmF6v57YCaDDtnd%2FwMIxmy8CkbtuLnSg3K3rIu8hAwskwwvkShpy%2BDHHf9ziHCMSOeCJktBn%2F%2Fm5KGnqokZxwRLTbj80KjHZBgSe1OiJGq9yEvQpqqBzriS7J8i5Vknyo5ilWrhvBzjNtTJWxBKA0YC2THJWwjJQsB2i6OYFjI0CHA4iNqM3ywHVNmqvM92j6bRtpZHeLb8qYJmRA8YCdLnkCh4tGH9ok4%3D"
swid = "{8EDF6DA7-8D5B-48E5-B926-E2E003D0A870}"
cookies = {"espn_s2": espn_s2, "swid": swid}

# could be retrieved for current year
current_year = 2021


base_url = f"https://fantasy.espn.com/apis/v3/games/fba/seasons/{current_year}/segments/0/leagues/{league_id}?"


def getTeamMap():
    """
    docstring
    """
    req_url = base_url + "view=mNav"
    r = requests.get(req_url, cookies=cookies).json()
    members = r["members"]
    teams = r["teams"]
    teamList = []
    ownerIdsToTeamObj = {}
    for member in members:
        team = Team(member["firstName"], member["lastName"], member["id"])
        ownerIdsToTeamObj[member["id"]] = team

    for team in teams:
        ownerId = team["owners"][0]
        id = team["id"]
        teamObj = ownerIdsToTeamObj[ownerId]
        teamObj.teamAbbrv = team["abbrev"]
        teamObj.teamName = team["location"] + team["nickname"]
        teamObj.id = id
        teamList.append(teamObj)

    return teamList


for team in getTeamMap():
    print(team)
