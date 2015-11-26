import world.Weapon as Weapon
import world.Armor as Armor
import world.Item as Item
import uuid

class Level:
	def __init__(self,description,directions,first='nope'):
		self.id=uuid.uuid4()
		self.description=description
		self.directions=directions
		self.items=[]
		self.weapons=[]
		self.monsters=[]
		self.armors=[]
