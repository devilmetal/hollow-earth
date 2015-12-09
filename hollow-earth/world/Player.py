import engine.bcolors as bcolors
import uuid
import engine.routines as routines
import time
import sys

class Player:
	def __init__(self):
		self.id=uuid.uuid4()
		self.level=None
		self.name=None
		self.hp=None
		self.max_hp=None
		self.inventory = None
		self.armor=None
		self.weapon=None
		
	def create(self):
		print bcolors.bcolors.WARNING  +"Welcome in the player creation" + bcolors.bcolors.ENDC
		time.sleep(2)
		routines.slow_type("We are going to help you in the difficult process of player creation")
		message="Please enter the name of your character"
		validate_message="Are you sure of this name ?"
		self.name=routines.check(message,validate_message)
		time.sleep(2)
		self.hp=10
		self.max_hp=10
		self.inventory = []
		self.armor=None
		self.weapon=None
		
	def bypass_creation(self):
		self.name='Bob'
		self.hp=10
		self.max_hp=10
		self.inventory = []
		self.armor=None
		self.weapon=None
