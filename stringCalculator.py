# import pytest
# from calculator import add
# import re

def test():
# Empty string
 assert add("") == 0,"Empty string should return 0"

# For Numbers
 assert add("1") == 1,"String \"1\" single number as input"
 assert add("1,1") == 2,"String \"1,1\" add 2 numbers in a comma seperated string"
 assert add("2,10") == 12,"String \"2,10\" add 2 numbers in a comma seperated string"
 assert add("1,3,8") == 12,"String \"1,3,8\" add 3 numbers in a comma seperated string"
 assert add("1,2,3") == 6,"String \"1,2,3\" add 3 numbers in a comma seperated string"
 assert add("1,2,3,4") == 10,"String \"1,2,3,4\" unknown amount of numbers in a comma seperated string"
 assert add("5,6,7,8") == 26,"String \"5,6,7,8\" unknown amount of numbers in a comma seperated string"

#For New Lines
 assert add("1\n2") == 3,"String \"1\n2\" use new lines as delimiters"
 assert add("3\n4") == 7,"String \"3\n4\" use new lines as delimiters"

#For different delimiter for 1 char
 assert add("//;\n1;2;3") == 6,"String \"//;\n1;2;3\" can handle different delimiters"
 assert add("//-\n1-2-3") == 6,"String \"//-\n1-2-3\" can handle different delimiters"

#For different delimiter for multiple chars
 assert add("//---\n1---2---3") == 6,"String \"//---\n1---2---3\" can handle multiple delimiters"
 assert add("//[*][%]\n1*2%3") == 6,"String \"//[*][%]\n1*2%3\" can handle multiple delimiters"
 assert add("//-!;o-\n1-!;o-2-!;o-3") == 6,"String \"//-!;o-\n1-!;o-2-!;o-3\" can handle multiple delimiters"
 
#For custom 
 assert add("//abc\n1abc2abc3"), "String \"//abc\n1abc2abc3\" can handle custom delimiters in a string"

#For Negative Numbers
#  assert raises(ValueError, add, "-1")
#  assert raises(ValueError, add, "1,-2")

#For Negative numbers
#  with pytest.raises(Exception, match = r'negatives not allowed \[-1, -2, -3\]'):
# 		assert add("-1, -2, -3, 1, 2, 3")

 print ("Test cases passed")

def add(numberString):
    if len(numberString) ==  0:
        return 0
    elif len(numberString) == 1:
        return int(numberString)
    elif numberString[0] == "/":
        result = 0
        lines = numberString.split("\n")
        for char in range(2,len(lines[0])):
            delims = delims + lines[0][char]
        numbers = lines[1].split(delims)
        return multipleNumbers(numbers)
        
    else:
        result = 0
        delims = ","
        if numberString[1] != ",":
            delims = "\n"
        numbers = numberString.split(delims)
        return multipleNumbers(numbers)

def multipleNumbers(numbers):
        result = 0
        for num in numbers:
         result += int(num)
        return result 

# def validateNumbers(numbers):      
#  if any(num < 0 for num in numbers  ):
#      raise ValueError    
test ()
