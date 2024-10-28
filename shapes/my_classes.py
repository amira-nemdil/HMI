class Parent :
    def __init__( self ):
        self.value = "Parent value "
        
class Child (Parent):
    def __init__(self):
        #Overriding the variable from the Parent class
        self.value = "Child value "