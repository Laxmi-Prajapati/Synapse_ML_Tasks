import random

class ChessPlayer:  # Class containing the information of chess players
    tournament_score = 0.0 
    def __init__(self,name, age, elo, tenacity, isBoring):
        self.name = name
        self.age = age
        self.elo = elo
        self.tenacity = tenacity
        self.isBoring = isBoring


def stimulateMatch(self,opponent):  # Function for stimulating the match
    elo_diff = abs(self.elo - opponent.elo)
    
    if (self.isBoring == True or opponent.isBoring == True) and elo_diff <100: # If the characters are Boring and the difference between their ELO Rating is less than 100 then the match ends in a draw
        self.tournament_score += 0.5
        opponent.tournament_score += 0.5

    elif elo_diff >100: # For ELO Rating difference >100 person with higher ElO Rating wins
        if self.elo > opponent.elo:
            self.tournament_score += 1
        else:
            opponent.tournament_score += 1
    
    elif elo_diff < 100 and elo_diff > 50: # If difference is between 50 and 100 then the person having the lower ElO has a chance to win
        lower_elo_player = self if self.elo < opponent.elo else opponent
        higher_elo_player = self if self.elo > opponent.elo else opponent

        random_factor = random.randint(1,11) 
        product = random_factor*lower_elo_player.tenacity # Multiplying the tenacity by random factor between 1 to 10

        if product > higher_elo_player.elo:
            lower_elo_player.tournament_score += 1
        else:
            higher_elo_player.tournament_score += 1

    else:
        if self.tenacity > opponent.tenacity: # Else the person having higher tenacity wins
            self.tournament_score += 1
        else:
            opponent.tournament_score += 1


players = [
    ChessPlayer("Courage the Cowardly Dog",25,1000.39,1000,False),
    ChessPlayer("Princess Peach",23,945.65,1000,True),
    ChessPlayer("Walter White",50,1650.73,750,False),
    ChessPlayer("Rory Gilmore", 16, 1700.87,500,False),
    ChessPlayer("Anthony Fantano",37,1400.45,400,True),
    ChessPlayer("Beth Harmon",20,2500.34,150,False),
]

num_players = len(players)
for i in range(num_players):
    for j in range(num_players):
        if i != j:
            stimulateMatch(players[i], players[j]) # Function calling
            

print("Results:")
for player in players:
    print(player.name,":",player.tournament_score,"points")



    
    

    