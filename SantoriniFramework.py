from ast import Constant
from math import sqrt

COORDINATE_LIST = [(i,j) for i in range(5) for j in range(5)]


class Game:
    def __init__(self):
        self.board = Board()
        self.row = 0 
        self.col = 0
        self.winner = None
        self.end = False
        self.turn = 0 #Turn number
        self.sub_turn = 'P' # action within a turn: place (P), select (S), move (M), or build (B)
        self.player_one = Player('white', ['A', 'B'])
        self.player_two = Player('blue', ['Y', 'Z'])
        self.current_player = self.player_one
    
    def is_valid_num(num):
        """Checks if x or y exists within the confines of the board
        num: int
        row or column value (should be between 0 and 4 (inclusive)"""
        return -1 < num < 5
    
    def distance_between_two_points(x0, y0, x1, y1):
        
        """Calculates distance between two points (x0, y0) and (x1, y1)

        Args:
            x0 (int): x-coordinate of first point
            y0 (int): y-coordinate of first point
            x1 (int): x-coordinate of second point
            y1 (int): y-coordinate of second point
        """
        return sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
        
    def place_worker(self, color, x, y):
        """Place worker for that color player (B/W) - places two pieces of a given color on the board

        Args:
            color (char): B/W
            x (int): X-coordinate
            y (int): y-coordinate
        """
        if self.board[x][y]['occupant'] != 'O': #Checking condition
            pass
        else:
            self.board[x][y]['occupant'] = color
            return True
        return False
        
    def select_worker(self, color, x, y):
        """Chooses piece to move

        Args:
            color (char): B/W
            x (int): x-coordinate of spot on board
            y (int): y-coordinate of spot on board
        """
        if self.board[x][y]['occupant'] != color:
            pass
        else:
            self.col = x
            self.row = y
            self.make_choice_active(x, y) #Make the x,y coordinates active for the worker
            self.sub_turn = 'move' #Move to this coordinate
            return True
        return False
    
    def convert_direction_to_coordinates(self, direction, x, y):
        if direction == 'n': return x, y - 1
        if direction == 's': return x, y + 1
        if direction == 'e': return x + 1, y
        if direction == 'w': return x - 1, y
        if direction == 'ne': return x + 1, y - 1
        if direction == 'nw': return x - 1, y - 1
        if direction == 'se': return x + 1, y + 1
        if direction == 'sw': return x - 1, y + 1
    
    def move_worker(self, move_direction, x, y):
        """Moves piece to a new spot on board, checks if the deisred new spot is not the same as current spot

        Args:
            x (int): x-coordinate of new spot
            y (int): y-coordinate of new spot
        """
        self.convert_direction_to_coordinates(move_direction, x,y)
        
    def get_height_score(self, color):
        """Generates a numeric score to the game - used in the building of the AI to find the optimal position
        
        color : char (B/W) - which player is playing
        """
        score = 0
        for i, j in COORDINATE_LIST:
            space = self.board[i][j]
            if space['occupant'] == color:
                score += 2 * space['level'] + 1
        return score
    
    def get_adjacent(x,y):
        """Obtain a list of all spaces adjacent to the current one

        Args:
            x (int): x-coordinate
            y (int): y-coordinate
        """
        adjacent_list = [(x-1, y-1), (x-1, y), (x-1,y+1), 
                         (x, y-1), (x,y+1),
                         (x+1, y-1), (x+1, y), (x+1,y+1)]
        filtered_list = iter(list(filter(
            lambda x: x[0] >= 0 and x[0] <= 4 and x[1] >= 0 and x[1] <= 4, adjacent_list
        )))
        return adjacent_list
    
    def get_possible_moving_spaces(self, game, curr_x, curr_y):
        array = []
        height = game.board[curr_x][curr_y]['level']
        for crd in self.get_adjacent(curr_x, curr_y):
            x_adj, y_adj = crd
            if (game.board[x_adj][y_adj]['occupant'] == 'O' and (game.board[x_adj][y_adj]['level'] - height) <= 1):
                array.append((x_adj, y_adj))
                
        return array
                        
    def undo(self):
        """Undo most recent action"""
        self.sub_turn = 'select'
        self.make_color_active()        


    def space_is_within_bounds(self, x, y):
        """Checks if the space is within the board's bounds"""
        return x >= 0 and x <= 4 and y >= 0 and y <= 4
    
        
    def is_move_valid(self, dest_x, dest_y, current_x, current_y):
        """Checks if the move is a valid move

        Args:
            x (int): x-coordinate of the move
            y (int): y-coordinate of the move
        
        Returns: bool
        Checks if the action is valid or not, returns True if it is, else, returns False
        """
        dest_space = self.board.state[dest_x][dest_y]
        current_space = self.board.state[current_x][current_y]
        return (not dest_space['occupied']) and self.space_is_within_bounds(dest_x, dest_y) and dest_space != current_space and dest_space['level'] - current_space['level'] <= 1
        
        
    def build_is_valid_space(self, x, y):
        """Checks if the user can build on chosen space

        Args:
            x (int): x-coordinate of the chosen space
            y (int): y-coordinate of the chosen space
        
        Returns: bool
        Checks if the user can build on the chosen space, returns True if possible, else Returns False.
        """
        space_list = self.get_adjacent(x, y)
        for i, j in space_list:
            if (self.s_valid_num(i) and self.is_valid_num(j) and
                    self.board[i][j]['occupant'] == 'O'):
                return True
        print("Cannot build {}")
        return False
        
    def make_player_color_occupied(self):
        """ Mark pieces as occupied. For a given player color, mark all the spaces with that player color as occupied
        """
        for i, j in COORDINATE_LIST:
            if self.board[i][j]['occupant'] == self.color and len(self.get_possible_moving_spaces(self, (i, j), False)) > 0:
                self.board[i][j]['active'] = True
            else:
                self.board[i][j]['active'] = False
                        
    def make_choice_occupied(self):
        """Marks the piece a player has chosen as occupied"""
        
        
    def check_move_available(self):
        """Check if there is a move available for the player, if not, End Game
        """
        for i, j in COORDINATE_LIST:
            if (self.board.state[j][i]['occupant'] == self.color and self.is_move_valid(j, i)): return True
            
        self.end_game(True)  
        False 
        
        
    def check_build_available(self):
        """Checks if there is a build available for the player, if not, End Game"""
        for i, j in COORDINATE_LIST:
            if (self.board.state[j][i]['occupant'] == self.color and self.build_is_valid_space(j, i)): return True
            
        self.end_game(True)  
        return False  
        
    def end_game(self, switchColor = False):
        """Ends game and prevents further moves - Declare the winner and make all spaces inoccupied and inaccessible
        ---------
        switch_color : bool, optional - switches to the opponent's color before declaring winner in case of secondary win condition
        """
        self.end = True
        if switchColor:
            if self.color == 'W':
                self.color = 'G'
            else:
                self.color = 'W'
        self.make_all_spaces_inactive()
        self.sub_turn = 'end'
    
    def print_game_state(self):
        self.board.print_board()
        print(f"Turn: {self.turn}, {self.current_player.color} {'(A, B)' if self.current_player.color == 'white' else '(Y, Z)'}")
    
    def check_if_game_over(self):
        """Checks if the game is over, if so, end the game"""
        # self.check_move_available()
        # self.check_build_available()
        for row in self.board.state:
            for space in row:
                if space['level'] == 3 and space['occupied'] == True:
                    return space['occupant']
                else: 
                    return False 
    
    def check_adjacent_spaces(self, moves, space):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                if self.is_move_valid(space['x'] + x, space['y'] + y, space['x'], space['y']):
                    moves.append({
                        'x': space['x'] + x,
                        'y': space['y'] + y,
                        'worker': space['occupant']
                    }) 

    def make_all_spaces_inactive(self):
        for i, j in COORDINATE_LIST:
            self.board[i][j]['active'] = False #Make all coordinates Inactive
            
            
    def enumerate_player_moves(self, player):
        """Enumerates all the possible moves for the player"""
        moves = []
        for row in self.board.state:
            for space in row:
                if space['occupied'] == True and space['occupant'] in player.workers:
                    # Check all the spaces around the worker
                    self.check_adjacent_spaces(moves, space)




class Board:

    initial_occupied_spaces = [
        {
            'coordinates': (1, 1),
            'occupant': 'Y',
            'level': '0',
            'color': 'blue'
        },
        {
            'coordinates': (1, 3),
            'occupant': 'B',
            'level': '0',
            'color': 'white'
        },
        {
            'coordinates': (2, 1),
            'occupant': 'A',
            'level': '0',
            'color': 'white'
        },
        {
            'coordinates': (3, 1),
            'occupant': ' ',
            'level': '1',
            'color': ""
        },
        {
            'coordinates': (3, 3),
            'occupant': 'Z',
            'level': '0',
            'color': 'blue'
        },
    ]


    def __construct_space_string(self, x, y):
        """
            Constructs a string representation of a space on the board
            Args:
                x (int): x-coordinate of the space
                y (int): y-coordinate of the space
            Returns:
                string: string representation of the space
        """
        return f"|{str(self.state[x][y]['level'])}{repr(self.state[x][y]['occupant']) if self.state[x][y]['occupant'] else ' '}"

    def __place_initial_pieces(self):
        """
            Place initial pieces on the board
        """

        for space in self.initial_occupied_spaces:
            self.state[space['coordinates'][0]][space['coordinates'][1]]['occupant'] = Worker(space['color'], space['coordinates'], space['level'], space['occupant'])
            self.state[space['coordinates'][0]][space['coordinates'][1]]['occupied'] = True
            self.state[space['coordinates'][0]][space['coordinates'][1]]['level'] = space['level']
    

    def __init__(self):
        self.state = [[{'level': 0, 'occupant': None, 'occupied': False}
                for i in range(5)] for j in range(5)] # Initial setup as empty board   
        self.__place_initial_pieces()

    def print_board(self):
        """
            Prints the board
        """

        for i in range(5):
            print("+--+--+--+--+--+")
            for j in range(5):
                print(self.__construct_space_string(i, j), end='')
            print("|")
        print("+--+--+--+--+--+")

class Worker:
    def __init__(self, color, coordinates, level, label):
        self.color = color
        self.coordinates = coordinates
        self.level = level
        self.moves = []
        self.label = label
    
    def __repr__(self):
        return f"{self.label}"

class Player:
    def __init__(self, color, workers):
        self.workers = workers
        self.color = color

        

    
    
        
        
        
        