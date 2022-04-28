

class Game:
    def __init__(self):
        self.board = [[{'level': 0, 'occupant': 'O', 'active': False}
                       for i in range(5)] for j in range(5)]   #5 x 5 board, each space contains level, occupant, and active bool - can be chosen as a space
        self.row = 0 
        self.col = 0
        self.winner = None
        self.end = False
        self.turn = 0 #Turn number
        self.sub_turn = 'P' # action within a turn: place (P), select (S), move (M), or build (B)
        self.color = 'W' # player color, B(Blue) or W(hite)
    
    def __str__(self):
        """Creating a CLI / ASCII representation of the 5 x 5 board
        """
        
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
        
    def make_player_color_active(self):
        """ Mark pieces as active. For a given player color, mark all the spaces with that player color as active
        """
        
    def make_choice_active(self):
        """Marks the piece a player has chosen as active"""
        
    def check_move_available(self):
        """Check if there is a move available for the player, if not, End Game
        """
        
    def check_build_available(self):
        """Checks if there is a build available for the player, if not, End Game"""
        
    def end_game(self):
        """Ends game and prevents further moves - Declare the winner and make all spaces inactive and inaccessible"""
        
        

    
    
        
        
        
        