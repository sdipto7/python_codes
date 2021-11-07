#Some of the syntaxes

keyword = ["if", "while", "for", "do", "else", "try", "catch", "import", "else if", "final", "int", "double", "float",
           "String", "char", "static", "switch", "case", "return", "continue", "goto", "break"]
mathOperator = ["+", "-", "*", "/", "%"]
logicalOperator = ["<", ">", "=", ">=", "<=", "&&", "||"]
other = [",", ";", "(", ")", "{", "}", "[", "]"]

#output values will be stored in these sets

output_keyword = set([])
output_mathOperator = set([])
output_logicalOperator = set([])
output_other = set([])
output_numericalValue = set([])
output_identifier = set([])

#Necessary method

def is_numeric(string):
    try:
        float(string)
        return True
    except:
        return False

#code starts

try:
    file = open("input.txt","r")
except:
    print("something wrong with the file. Please check")


info = file.read()
word = ""

for a in info:
    word = info.split()

for i in word:
    if i in keyword:
        output_keyword.add(i)
    elif i in mathOperator:
        output_mathOperator.add(i)
    elif i in logicalOperator:
        output_logicalOperator.add(i)
    elif i in other:
        output_other.add(i)
    elif is_numeric(i) is True:
        output_numericalValue.add(i)
    else:
        output_identifier.add(i)


print("Keywords: ", output_keyword)
print("Math Operators: ", output_mathOperator)
print("Logical Operators: ", output_logicalOperator)
print("Numerical Values: ", output_numericalValue)
print("Identifiers: ", output_identifier)
print("Others: ", output_other)
