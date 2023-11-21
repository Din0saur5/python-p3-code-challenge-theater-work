from lib.audition import Audition


class Role:
    # all class variable contains all instances of Role class
    all=[]
    def __init__(self, character_name):
        self.character_name = character_name #name of character validated input
        type(self).all.append(self) #adds each instance to all variable
    
    
#validates input of character name 
    @property
    def character_name(self):
        return self._character_name
    
    @character_name.setter
    def character_name(self, name):
        if isinstance(name, str) and len(name)>0:
            self._character_name = name
            
        else: 
            raise Exception("Sorry, must be str and more than 0 char")

#returns list of all auditions associated with the instances' role using list comp
    def auditions(self):
        return [audition for audition in Audition.all if audition.role is self]
 
#returns list of actors auditioning for the role using a set to cull repeats     
    def actors(self):
        return list({audition.actor for audition in Audition.all if audition.role is self})

#does the same as the previous fn just with location   
    def locations(self):
        return list({audition.location for audition in Audition.all if audition.role is self})        
    
# uses previous auditions() fn to show different method of list comp then conditionally pulling the first hired actor in the list if there is one       
    def lead(self):
        lst = [audition.actor for audition in self.auditions() if audition.hired]  
        if len(lst)>0:
           return lst[0]
        return 'no actor has been hired for this role'
# very similar to the prev fn except condition changes to grab the second actor in the list who is hired if there is one  
    def understudy(self):
        lst = [audition.actor for audition in self.auditions() if audition.hired] 
        if len(lst)>1:
           return lst[1]
        return 'no actor has been hired for understudy for this role'
#can be called on any instance of Role and will produce all of the roles that are not currently cast by checking for a lead    
    @classmethod
    def not_cast(cls):
        return [ role for role in cls.all if role.lead() == 'no actor has been hired for this role']
    
#lastly, to initialize an instance of Audition we must have a Role so we can initialize an audition from our Role instances,
#although this can make them harder to access without looping through Auditions.all but thats nbd unless using SQL which then you can use rows and id etc...
    def create_audition(self, actor,location,phone):
        audition = Audition(self,actor,location,phone)
        return audition