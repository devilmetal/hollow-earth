import uuid
class Weapon:
	def __init__(self,name,damage,examine):
		self.id=uuid.uuid4()
		self.name = name
		self.damage = damage
		self.examine=examine
