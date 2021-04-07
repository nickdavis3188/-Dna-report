import re
class Patient:
    """"
    this is a patient object
    """
    
    # this helps in initializing new Petient
    def __init__(self, Name, Age, Strand, diabetis, blue_eyes, three_eyes):
        self.name = Name
        self.age = str(Age)
        self.strand = Strand
        self.has_diabetis = diabetis
        self.has_Blue_eyes = blue_eyes
        self.has_Three_eyes = three_eyes

