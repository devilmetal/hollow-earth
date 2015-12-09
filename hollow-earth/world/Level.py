import world.Weapon as Weapon
import world.Armor as Armor
import world.Item as Item
import uuid

class Level:
	def __init__(self):
		self.id=uuid.uuid4()
		self.description=None
		self.directions=None
		self.items=[]
		self.weapons=[]
		self.monsters=[]
		self.armors=[]
		self.x=None;
		self.y=None;
