'''
Created on Jul 07, 2013
@author: Rafael Alfaro
'''
class Stringsk:
    def __init__(self,stringsk = "" , char_empty = '0'):
        self.stringsk = stringsk
        self.long = len (self.stringsk)
        self.char_empty = char_empty

    def get_length(self):
        return(self.long)

    def verify_only_num(self):
        return(self.stringsk.isdigit())

    def get_81_characters(self,size = 81):
        """
        This method gets the 81 first characters and remove the character "\n"
        """
        self.stringsk = self.stringsk[0:size]
        self.long = len (self.stringsk)
        return self.stringsk

    def print_values(self):
        """
        This merthod print the values in the object
        """
        print("String :" + self.stringsk)
        print("Length :" + str(self.long))
        print("Holes :" + self.char_empty)


    def get_zero_number(self,char):
        """
            This method get number of holes in the puzzle
        """
        return (self.stringsk.count(char))

    def verify_string_to_sudoku(self):
        """
            This method verify if the string has 81 characters and
        """
        length = self.get_length()
        if (length >= 80):
            self.stringsk = self.get_81_characters()
            if (not(self.verify_only_num())):
                self.stringsk = self.stringsk.replace('0',self.char_empty)
                self.stringsk = self.stringsk.replace('.',self.char_empty)
                self.stringsk = self.stringsk.replace('_',self.char_empty)
            return True

    def put_a_sring(self, stringsk,char_empty = '0'):
        """
        This method put a new puzle to verify
        """
        self.stringsk = stringsk
        self.long = len (self.stringsk)
        self.char_empty = char_empty

    def get_str(self):
        """
        This method get the sring of the object
        """
        return(self.stringsk)

