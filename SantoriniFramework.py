from ast import Constant


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
    
    def distance_between_two_points(x0, y0, x1, y1):
        """Calculates distance between two points (x0, y0) and (x1, y1)

        Args:
            x0 (int): x-coordinate of first point
            y0 (int): y-coordinate of first point
            x1 (int): x-coordinate of second point
            y1 (int): y-coordinate of second point
        """
        
    def place_worker(self, color, x, y):
        """Place worker for that color player (B/W) - places two pieces of a given color on the board

        Args:
            color (char): B/W
            x (int): X-coordinate
            y (int): y-coordinate
        """
        
    def select_worker(self, color, x, y):
        """Chooses piece to movee

        Args:
            color (char): B/W
            x (int): x-coordinate of spot on board
            y (int): y-coordinate of spot on board
        """
        
    def move_worker(self, x, y):
        """Moves piece to a new spot on board, checks if the deisred new spot is not the same as current spot

        Args:
            x (int): x-coordinate of new spot
            y (int): y-coordinate of new spot
        """
        
        
    def get_height_score(self, color):
        """Generates a numeric score to the game - used in the building of the AI to find the optimal position
        
        color : char (B/W) - which player is playing
        """
        
    def undo(self):
        """Undo most recent action"""
        
    def move_is_valid_space(self, x, y):
        """Checks if the move is a valid move

        Args:
            x (int): x-coordinate of the move
            y (int): y-coordinate of the move
        
        Returns: bool
        Checks if the action is valid or not, returns True if it is, else, returns False
        """
        
        
    def build_is_valid_space(self, x, y):
        """Checks if the user can build on chosen space

        Args:
            x (int): x-coordinate of the chosen space
            y (int): y-coordinate of the chosen space
        
        Returns: bool
        Checks if the user can build on the chosen space, returns True if possible, else Returns False.
        """
        
    def make_player_color_occupied(self):
        """ Mark pieces as occupied. For a given player color, mark all the spaces with that player color as occupied
        """
        
    def make_choice_occupied(self):
        """Marks the piece a player has chosen as occupied"""
        
    def check_move_available(self):
        """Check if there is a move available for the player, if not, End Game
        """
        
    def check_build_available(self):
        """Checks if there is a build available for the player, if not, End Game"""
        
    def end_game(self):
        """Ends game and prevents further moves - Declare the winner and make all spaces inoccupied and inaccessible"""
    
    def print_game_state(self):
        self.board.print_board()
        print(f"Turn: {self.turn}, {self.current_player.color} {'(A, B)' if self.current_player.color == 'white' else '(Y, Z)'}")


class Board:

    initial_occupied_spaces = [
        {
            'coordinates': (1, 1),
            'occupant': 'Y',
            'level': '0'
        },
        {
            'coordinates': (1, 3),
            'occupant': 'B',
            'level': '0'
        },
        {
            'coordinates': (2, 1),
            'occupant': 'A',
            'level': '0'
        },
        {
            'coordinates': (3, 1),
            'occupant': ' ',
            'level': '1'
        },
        {
            'coordinates': (3, 3),
            'occupant': 'Z',
            'level': '0'
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
        return f"|{str(self.state[x][y]['level'])}{str(self.state[x][y]['occupant'])}"

    def __place_initial_pieces(self):
        """
            Place initial pieces on the board
        """

        for space in self.initial_occupied_spaces:
            self.state[space['coordinates'][0]][space['coordinates'][1]]['occupant'] = space['occupant']
            self.state[space['coordinates'][0]][space['coordinates'][1]]['occupied'] = True
            self.state[space['coordinates'][0]][space['coordinates'][1]]['level'] = space['level']
    

    def __init__(self):
        self.state = [[{'level': 0, 'occupant': ' ', 'occupied': False}
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

class Player:
    def __init__(self, color, workers):
        self.workers = workers
        self.color = color

        

    
    
        
        
        
        