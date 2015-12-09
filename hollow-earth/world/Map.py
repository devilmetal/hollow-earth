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
		level = Level.Level()
		level.description = 'It is a windy forest with very high trees. You are in the middle of a crossing and you can choose to go in any directions.'
		level.directions=['n','e','w','s'] # north east west south
		level.weapons.append(Weapon.Weapon('Wooden sword',1,'This is an useless sword'))
		level.weapons.append(Weapon.Weapon('Wooden sword2',1,'This is an useless sword'))
		level.armors.append(Armor.Armor('Grass skirt',0,'This is an useless armor'))
		level.armors.append(Armor.Armor('Grass skirt2',0,'This is an useless armor'))
		level.items.append(Item.Item('item1',[],[],'item 1 test'))
		level.items.append(Item.Item('item2',[],[],'item 2 test'))
		level.items.append(Item.Item('item3',[],[],'item 3 test'))
		level.items.append(Item.Item('item4',[],[],'item 4 test'))
		level.items.append(Item.Item('item 5',[],[],'item 5 test'))
		level.x=0;
		level.y=0;
		self.levels.append(level)
		
	def firstLevel(self):
		items = [level for level in self.levels if (level.x == 0 and level.y == 0)]
		return items[0]
		
