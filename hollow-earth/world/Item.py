import uuid
class Item:
	def __init__(self,name,react_list,react_list_actions,examine):
		self.id=uuid.uuid4()
		self.name = name
		self.react_list=react_list
		self.react_list_actions=react_list_actions
		self.examine=examine
		
	def use_action(action):
		if action in react_list:
			a=0
			# get index of action
			# do action
			# display
		else:
			print "You tried to "+action+" "+self.name+"."
			print "Nothing append"
