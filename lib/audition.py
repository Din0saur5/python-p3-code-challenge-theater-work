class Audition:
    #all contains all instances of auditions
    all = []
    def __init__(self, role, actor, location, phone):
      self.role = role 
      self.actor = actor
      self.location = location #not validated 
      self.phone = phone #not validated 
      self.hired = False #defaults to false
      type(self).all.append(self) #adds new audition instance to all
      
      
#input validation standard for actor     
    @property
    def actor(self):
        return self._actor
    @actor.setter
    def actor(self, actor):
        if isinstance(actor, str) and 2< len(actor)<21:
            self._actor= actor
        else:
            raise Exception("Sorry, must be str and btwn 3-20 char")
    
 #input validation with internal import to avoid circular dependancy for role (Role instance)   
    @property
    def role(self):
        return self._role
    @role.setter
    def role(self, role):
        from lib.role import Role
        if isinstance(role, Role):
            self._role = role
        else:
            raise Exception('not role')

#change hired to true will affect Role methods     
    def call_back(self):
        self.hired = True
        return