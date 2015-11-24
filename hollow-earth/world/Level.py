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
		if first=='first':
			#this is the first level => be kind
			self.weapons.append(Weapon.Weapon('Wooden sword',1,'This is an useless sword'))
			self.armors.append(Armor.Armor('Grass skirt',0,'This is an useless armor'))
			self.items.append(Item.Item('item1',[],[],'item 1 test'))
			self.items.append(Item.Item('item2',[],[],'item 2 test'))
			self.items.append(Item.Item('item3',[],[],'item 3 test'))
			self.items.append(Item.Item('item4',[],[],'item 4 test'))
