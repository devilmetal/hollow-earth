import uuid
import world.Level as Level
import world.Weapon as Weapon
import world.Armor as Armor
import world.Item as Item

class Map:
	def __init__(self):
		self.id=uuid.uuid4()
		self.levels=[]
		
	def createMap(self):
		description = 'It is a windy forest with very high trees. You are in the middle of a crossing and you can choose to go in any directions.'
		directions=['n','e','w','s'] # north east west south
		level = Level.Level(description,directions)
		level.weapons.append(Weapon.Weapon('Wooden sword',1,'This is an useless sword'))
		level.armors.append(Armor.Armor('Grass skirt',0,'This is an useless armor'))
		level.items.append(Item.Item('item1',[],[],'item 1 test'))
		level.items.append(Item.Item('item2',[],[],'item 2 test'))
		level.items.append(Item.Item('item3',[],[],'item 3 test'))
		level.items.append(Item.Item('item4',[],[],'item 4 test'))
		self.levels.append(level)
		return level
