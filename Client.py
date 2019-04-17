

class Client:
	
  name = ""
  password = ""
  # users = []
	# requests = []
	
  def __init__(self, name, password):
    self.name = name
    self.password = password
  	
	def addUser(self, newUser):
		self.users.append(newUser)
		
	def removeUser(self):
		print("teste")
		
	def checkUser(self):
		print("teste")
