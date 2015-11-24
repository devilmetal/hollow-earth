import uuid
class Armor:
	def __init__(self,name,protection,examine):
		self.id=uuid.uuid4()
		self.name = name
		self.damage = protection
		self.examine=examine
