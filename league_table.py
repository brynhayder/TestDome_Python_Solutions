from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def sorted_players(self):
      sorted_on_games = sorted(
              self.standings,
              key=lambda x: self.standings[x]['games_played']
                              )
      sorted_on_score = sorted(
              sorted_on_games,
              key=lambda x: self.standings[x]['score'],
              reverse=True
            )
      return sorted_on_score
      
    def player_rank(self, rank):
        return self.sorted_players()[rank-1]

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.standings)
    print(table.sorted_players())
    print(table.player_rank(1))
