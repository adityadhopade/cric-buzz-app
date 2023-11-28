import requests
import pprint
from tabulate import tabulate


def fetch_live_score():
  url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"


  headers = {
          "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
          "X-RapidAPI-Key": "YOUR_API_KEY"  # Replace with your RapidAPI key
      }
  response = requests.get(url, headers=headers)
  # print(response.json())
  data = response.json()
  matches_data = data['typeMatches'][0]['seriesMatches'][0]['seriesAdWrapper']['matches']
  #pprint.pprint(matches_data)

  for match in matches_data:
    table = []
    table.append(["Match Description", f"{match['matchInfo']['matchDesc']} , {match['matchInfo']['team1']['teamName']} vs {match['matchInfo']['team2']['teamName']}"])
    #pprint.pprint(table)
    table.append(["Match Details are", "" ])
    table.append(["Series Name", match['matchInfo']['seriesName']])
    #pprint.pprint(table)
    table.append(["Match Format", match['matchInfo']['matchFormat']])
    table.append(["Result", match['matchInfo']['status']])
    table.append([f"{match['matchInfo']['team1']['teamName']}", f"{match['matchScore']['team1Score']['inngs1']['runs']}/{match['matchScore']['team1Score']['inngs1']['wickets']} in {match['matchScore']['team1Score']['inngs1']['overs']} overs"])
    table.append([f"{match['matchInfo']['team2']['teamName']}", f"{match['matchScore']['team2Score']['inngs1']['runs']}/{match['matchScore']['team2Score']['inngs1']['wickets']} in {match['matchScore']['team2Score']['inngs1']['overs']} overs"])
    
    headers = ["Match Details", "Match Status"]
    
    print(tabulate(table, headers=headers, tablefmt="pretty"))
    print("\n")
fetch_live_score()