class PartyAnimal:
	x = 0
	def __init__(self):
		print "I am constructed"
	def party(self) :
		self.x = self.x + 1
		print "So far",self.x
	def __del__(self):
		print "I am destructed", self.x
an = PartyAnimal()
an.party()
an.party()
an.party()
print "I'm done."


#I am constructed
#So far 1
#So far 2
#So far 3
#I'm done.
#I am destructed 3
