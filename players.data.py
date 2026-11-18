"""Session 2 checkpoint: Player and FantasyTeam, with one XI typed in by hand."""


class Player:
    """One real cricketer in the PSL player list."""

    def __init__(self, player_id, name, franchise, role, credits):
        self.player_id = player_id
        self.name = name
        self.franchise = franchise
        self.role = role
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.franchise}, {self.role}, {self.credits} cr)"


class FantasyTeam:
    """A fantasy XI picked by one person."""

    def __init__(self, team_name, owner):
        self.team_name = team_name
        self.owner = owner
        self.players = []
        self.captain = None
        self.vice_captain = None

    def add_player(self, player):
        self.players.append(player)

    def total_credits(self):
        total = 0
        for player in self.players:
            total = total + player.credits
        return total

    def count_by_role(self):
        counts = {"WK": 0, "BAT": 0, "AR": 0, "BOWL": 0}
        for player in self.players:
            counts[player.role] = counts[player.role] + 1
        return counts

    def set_captain(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain

    def __str__(self):
        size = len(self.players)
        cost = self.total_credits()
        return f"{self.team_name} (owner: {self.owner}, {size} players, {cost} cr)"


team = FantasyTeam("Dugout Demo XI", "Haroon")
saim_ayub = Player("P012", "Saim Ayub", "Hyderabad Kingsmen", "AR", 10.5)
fakhar = Player("P056", "Fakhar Zaman", "Lahore Qalandars", "BAT", 8.5)
shadab_khan = Player("P029", "Shadab Khan", "Islamabad United", "AR", 10.5)
haris_rauf = Player("P066", "Haris Rauf", "Lahore Qalandars", "BOWL", 7.5)
shaheen_shah_afridi = Player("P068", "Shaheen Shah Afridi", "Lahore Qalandars", "BOWL", 10.5)
babar_azam = Player("P089", "Babar Azam", "Peshawar Zalmi", "BAT", 10.5)
farhan_yousaf = Player("P090", "Farhan Yousaf", "Peshawar Zalmi", "BAT", 7.5)
hasan = Player("P046", "Hasan Ali", "Karachi Kings", "BOWL", 10.0)
mohammad_rizwan = Player("P122", "Mohammad Rizwan", "Rawalpindiz", "WK", 10.5)
naseem_shah = Player("P070", "Naseem Shah", "Rawalpindiz", "BOWL", 8.0)
asif = Player("P133", "Asif Afridi", "Rawalpindiz", "BOWL", 6.5)

for player in [saim_ayub, fakhar, shadab_khan, haris_rauf, shaheen_shah_afridi, babar_azam, farhan_yousaf, hasan, mohammad_rizwan, naseem_shah, asif]:
    team.add_player(player)
team.set_captain(babar_azam, mohammad_rizwan)

print(team)
print("Roles:", team.count_by_role())
print("Captain:", team.captain)
print("Vice-captain:", team.vice_captain)
