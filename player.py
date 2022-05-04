import random


class PlayerFactory:
    def build_player_factory(board, ply_type, ply_num):
        if ply_type == "human":
            return Human(board, ply_num)
        if ply_type == "random":
            return Random(board, ply_num)
        if ply_type == "heuristic":
            return Heuristic(board, ply_num)
        
class Player:
    def __init__(self):
        #...#
        pass
        
    def choose_move(self):
        pass
    
    def enumerate_player_moves(self):
        #...#
        pass
        
    def try_move(self):
        # Check if move valid, and if build valid - methods in Game
        #...#
        pass
        
    #Get height get_height_score
    #Get center score

class Human(Player):
    def __init__(self, board, player_num, player_type = "human"):
        super().__init__(board, player_num, player_type)
        
    def choose_move(self):
        #...#
        pass
        
class Random:
    def __init__(self, board, player_num, player_type = "random"):
        super().__init__(board, player_num, player_type)
        
    def choose_move(self):
        moves = self.enumerate_player_moves()
        choose_random_val = random.randint(0, len(moves) - 1)
        #...#
    
    
class Heuristic:
    def __init__(self, board, player_num, player_type = "heuristic"):
        super().__init__(board, player_num, player_type)
        self.height_score = 0
        self.center_score = 0
        self.distance_score = 0
        
    def choose_move(self):
        moves = self.enumerate_player_moves()
        #Find a list of max score moves
        #Choose a random one out of them if more than 1