"""
SDE/SDET - Take Home Test
Raquel Lippincott 6/25/19
Python 3.7.2
"""

import sys
from os import path

NUM_FRAMES = 10


def calc_score(roll_list: list) -> int:
	"""Calculates the score of an entire game of Ten-Pin Bowling.

	Args:
		roll_list: A list of all the rolls in the game. Each roll is represented by a
			list of pin numbers.

	Returns:
		The integer score that was calculated from the entire game.
	"""
	score = 0
	roll_curr = 0

	for frame in range(NUM_FRAMES):
		if is_strike(roll_list[roll_curr]):
			# Strike!
			# Add 10, plus the value of the next two rolls
			score += 10
			score += len(roll_list[roll_curr + 1])
			score += len(roll_list[roll_curr + 2])
			roll_curr += 1
		elif is_spare(roll_list[roll_curr], roll_list[roll_curr+1]):
			# Spare!
			# Add 10, plus the value of the next roll
			score += 10
			score += len(roll_list[roll_curr + 2])
			roll_curr += 2
		else:
			# Neither a Strike nor a Spare
			# Add the value of the current two roll
			score += len(roll_list[roll_curr])
			score += len(roll_list[roll_curr + 1])
			roll_curr += 2

	return score


def read_rolls_from_file(fileName: str) -> list:
	"""Reads a Ten-Pin Bowling game's list of rolls from the given file. Each line
	is a seperate roll. Gutter balls are represented by an empty line.

	Args:
		fileName: A string path for the input file.

	Returns:
		A list of rolls, where each roll is represented by a list of pin numbers.
	"""
	roll_list = []
	with open(fileName, 'r') as file:
		line = file.readline()
		while line:
			roll_list.append(line.split())
			line = file.readline()
		roll_list.append([])
	return roll_list


def is_strike(roll: list) -> bool:
	"""Determines if a given roll is a strike by checking if all pins were
	knocked over in that roll.

	Args:
		roll: A list of knocked pin numbers from the roll.

	Returns:
		A boolean value representing whether the roll was a strike.
	"""
	return len(roll) == 10


def is_spare(roll1: list, roll2: list) -> bool:
	"""Determines if the given two rolls are a spare by checking if all pins were
	knocked over within those two rolls.

	Args:
		roll1: A list of knocked pin numbers from the first roll.
		roll2: A list of knocked pin numbers from the second roll.

	Returns:
		A boolean value representing whether the rolls were a spare.
	"""
	combined_roll = roll1 + roll2
	return len(combined_roll) == 10


def main():
	if len(sys.argv) < 2:
		print("Please include a relative path for the input file.")
		return
	if not path.exists(sys.argv[1]):
		print("This file does not exist.")
		return

	roll_list = read_rolls_from_file(sys.argv[1])
	score = calc_score(roll_list)

	print("Score = " + str(score))

if __name__ == "__main__":
	main()
