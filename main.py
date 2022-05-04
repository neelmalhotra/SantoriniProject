from sqlalchemy import true
from SantoriniFramework import Game

class SantoriniCLI:
	def __init__(self):
		self.game = Game()
		self.play_game()
	
	def play_game(self):
		"""
			Main game loop that terminates when the game is over
		"""

		while (not (winner := self.game.check_if_game_over())) and self.game.check_move_available() and self.game.check_build_available(): # TODO: Check if game is over
			self.game.print_game_state()
			worker = self.__prompt_worker_select()
			move_direction = self.__prompt_move_direction()
			build_direction = self.__prompt_build_direction()
			self.game.move_worker(worker, move_direction, build_direction)
		
		print(f"{winner} has won")

	def __prompt_worker_select(self):
		"""
			Prompts the user to select a worker
		"""

		print("Select a worker to move")
		worker = input()
		worker = worker.upper()
		# Check if worker is a character
		if worker.isalpha():
			if (worker not in ['A', 'B', 'Y', 'Z']):
				print("Not a valid worker")
				return self.__prompt_worker_select()
			if(worker not in self.game.current_player.workers):
				print("That is not your worker")
				return self.__prompt_worker_select()
		else:
			print("Please enter a valid worker character")
		return worker

	def __prompt_move_direction(self):
		"""
			Prompts the user to select a move direction
		"""

		print("Select a direction to move (n, ne, e, se, s, sw, w, nw)")
		direction = input()
		dest_x, dest_y = self.game.convert_direction_to_coordinates(direction, self.game.row, self.game.col)
		if not direction.isalpha() or direction.lower() not in ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']:
			print("Not a valid direction")
			return self.__prompt_move_direction()
		if not self.game.is_move_valid(dest_x, dest_y, self.game.row, self.game.col):
			print("Cannot move", direction)
			return self.__prompt_move_direction()
		return direction
	
	def __prompt_build_direction(self):
		"""
			Prompts the user to select a build direction
		"""

		print("Select a direction to build (n, ne, e, se, s, sw, w, nw)")
		direction = input()
		dest_x, dest_y = self.game.convert_direction_to_coordinates(direction, self.game.row, self.game.col)
		if not direction.isalpha() or direction.lower() not in ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']:
			print("Not a valid direction")
			return self.__prompt_move_direction()
		if not self.game.build_is_valid_space(dest_x, dest_y):
			print("Cannot build", direction)
			return self.__prompt_build_direction()
		return direction

		

if __name__ == "__main__":
	game = SantoriniCLI()