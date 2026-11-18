from dugout_amna.loader import FantasyTeam, Player, load_player, load_team  # type: ignore

def show_pool(players):
    """Print how many players there are per franchise and per role."""
    by_franchise = {}
    by_role = {}
    for player in players.values():
        # .get(key, 0) gives 0 the first time we see a key, then we add 1
        by_franchise[player.franchise] = by_franchise.get(player.franchise, 0) + 1
        by_role[player.role] = by_role.get(player.role, 0) + 1
    print("Players by franchise:")
    for franchise in sorted(by_franchise):
        print(f"  {franchise}: {by_franchise[franchise]}")
    print("Players by role:")
    for role in sorted(by_role):
        print(f"  {role}: {by_role[role]}")

def show_team(team):
    """Print a team's players, cost and captains."""
    print(f"\nTeam {team.team_name} by {team.owner}:")
    for player in team.players:
        print(f"  {player}")
    print(f"Total credits: {team.total_credits()}")
    print(f"Captain: {team.captain.name}, Vice-captain: {team.vice_captain.name}")
 
 
# def main():
#     players = load_player("data\\players.csv")
#     show_pool(players)
#     team = load_team("data\\my_team.csv", players)
#     show_team(team)

def main():
    players = load_player("data\\players.csv")
    show_pool(players)
    teams = load_team("data\\sample_teams.csv", players)
    legal = []
    illegal = []
    for team in teams:
        show_team(team)
        errors = team.check_rules()
        if errors:
            illegal.append(team)
            print("ILLEGAL:")
            for error in errors:
                print(f"  - {error}")
        else:
            legal.append(team)
            print("LEGAL")
    print(f"\nSummary: {len(legal)} legal, {len(illegal)} illegal out of {len(teams)} teams")
    print("Legal teams:")
    for team in legal:
        print(f"  {team.team_name}")
    print("Illegal teams:")
    for team in illegal:
        print(f"  {team.team_name}")
 
 
if __name__ == "__main__":
    main()

import csv

def load_player(path):

    players = {}

    with open (path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            player = Player.from_row(row)
            players[player.player_id] = player
    return players

def team_from_row(row, players):
    team = FantasyTeam(row["team_name"], row["owner"])

    for player_id in row["players"].split(";"):
        team.add_player(players[player_id.strip()])
    
    team.set_captain(players[row["captain"]], players[row["vice_captain"]])

    return team

def load_team(path, players):

    with open (path, newline="", encoding= "utf-8") as f:
        for row in csv.DictReader(f):
            return team_from_row(row, players)
        
def load_teams(path, players):
    """Return a list of every team in a teams CSV file."""
    teams = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            teams.append(team_from_row(row, players))
    return teams