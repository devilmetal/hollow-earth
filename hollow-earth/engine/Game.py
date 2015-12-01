import uuid
import world.Player as Player
import world.Level as Level
import world.Map as Map
import engine.bcolors as bcolors
import time
import engine.routines as routines
import engine.actions as actions
import random

class Game:
	def __init__(self):
		self.id=uuid.uuid4()
		self.description=None
		self.directions=None
		self.console=None
		
	def welcome(self):
		routines.clear()
		print bcolors.bcolors.HEADER + bcolors.bcolors.BOLD + bcolors.bcolors.UNDERLINE +"Welcome in this game" + bcolors.bcolors.ENDC
		time.sleep(3)
	
	def newplayer(self):
		self.player = Player.Player()
		self.player.create()
		
	def intro(self):
		routines.clear()
		routines.slow_type("Well... That was not very hard...")
		routines.slow_type("Until now ....") 
		routines.slow_type("Hahahahahaha    (-:C")
		time.sleep(2)
		routines.clear()
		print ''
		print bcolors.bcolors.HEADER + bcolors.bcolors.BOLD + bcolors.bcolors.UNDERLINE +"\tYour story, your adventure ..." + bcolors.bcolors.ENDC
		print ''
		routines.slow_type_delete('A long time ago in a realm of fairies and princess...')
		routines.slow_type('No... You know what ?')
		routines.slow_type('You were expecting some classical console-based RPG ?')
		routines.slow_type('You were expecting something boring and easy to beat ?')
		routines.slow_type('Screw that shit ! You are going to be suprized !')
		time.sleep(2)
		routines.clear()
		print ''
		print bcolors.bcolors.FAIL + bcolors.bcolors.BOLD + bcolors.bcolors.UNDERLINE +"\tYour story, your adventure, your death ..." + bcolors.bcolors.ENDC
		print ''
		routines.slow_type('You feel with your hands a smooth sensation of grass.')
		routines.slow_type('You suffer from a really bad headache and you barly manage to open your eyes.')
		routines.slow_type('The sun seems to be already quite high in the sky.')
		routines.slow_type('All around you can see very high trees. The kind of three you never saw before.')
		routines.slow_type('What did happend to you ? Who are you ?')
		routines.slow_type('Those questions act like echos in your painfull head.')
		routines.slow_type('Your breath does not seem to smell like alcohol and your pockets are empty.')
		routines.slow_type('It is all up to you now ....')
		time.sleep(2)
		
	def update_interface(self):
		routines.instant_clear()
		print ''
		print "\t"+bcolors.bcolors.UNDERLINE+"Description"+bcolors.bcolors.ENDC
		print self.player.level.description
		print "\t"+bcolors.bcolors.UNDERLINE+"Directions"+bcolors.bcolors.ENDC
		print self.player.level.directions
		print ''
		print ''	
		print self.console
		
	
	def newmap(self):
		self.map = Map.Map()
		self.map.createMap()
		self.player.level = self.map.firstLevel()
		
	def run(self):
		flag = True
		while flag:
			self.update_interface()
			input = raw_input("Enter an action : ")
			self.console=actions.decode_action(input,self.player)
		
