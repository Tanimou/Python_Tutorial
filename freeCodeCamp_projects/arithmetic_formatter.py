import re

"""
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. 
The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.
    
Rules:
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
?If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.

?The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. 
?Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.

?Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.

?Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.

If the user supplied the correct format of problems, the conversion you return will follow these rules:
*There should be a single space between the operator and the longest of the two operands, 
*the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.

*Numbers should be right-aligned.

*There should be four spaces between each problem.

*There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually.

!HINT: the trick for the formatting part is to have all the first operands of operations aligned in a single line( concatenate them and stored them in a single variable as string)
!and to have the same thing for the operator(+/-) and the second operand stored in a single string variable
!and same thing for the result of the operation
!you should use rjust() function to properly align all of them
"""

##variables that will be used for concatenation
first = ''
second = ''
sumx = ''
lines = ""

def formatter(problems, problem, first_operand, operator, second_operand):
    # sourcery skip: use-fstring-for-concatenation
    global first, second, sumx, lines

    if operator == "+":
            summ = str(int(first_operand) + int(second_operand))
    else:
            summ = str(int(first_operand) - int(second_operand))

    ##formatting part
    # *because we have to have a space between operator and the longest operand,
    # *the length of the operation will be the length of the longest operand +2
    length = max(len(first_operand), len(second_operand)) + 2

    ##the rjust() will adjust the operand to the right
    ##it retuns a right-justified string of length width
    top = str(first_operand).rjust(length)

    ##because the operator will take one place, we do length-1
    bottom = operator + str(second_operand).rjust(length - 1)

    res = summ.rjust(length)
    line = "".join("-" for _ in range(length))

    ## if we don't reach the end of the list
    if problem != problems[-1]:
        ## then we add 4 spaces between each operation

        first += top + '    '# *first = first + top + "    ", we concatenate for each iteration the first operand in a single string,
                             # *then at the end we end up with all the first operands of list in a single string    
        second += bottom + '    '# *same thing for all the operators and second operands in a single string
        lines += line + '    '  # *same thing for lines in a single string
        sumx += res + '    '
    ## if we reached the end of the list,then we d'ont need to add anymore spaces
    else:
        first += top
        second += bottom
        lines += line
        sumx += res

    """at the end of the iteration we have:
            -all the first operands of list in first variable
            -all the operators and second operands of list in second variable
            -the lines for each operation
            -all result of operation in sumx variable
    """

def handling_errors(problems, true_false):
    global first, second,sumx,lines
    if len(problems) > 5:
        return "Error: Too many problems."
    ##we loop through each problem in order to concatenate
    for problem in problems:
        probleme = problem.split()
        try:
            int(probleme[0])
            int(probleme[2])
        except Exception:
            return "Error: Numbers must only contain digits."

        probleme = problem.rstrip()

        first_operand = re.findall('([0-9].*) \S+ [0-9].*', probleme)[0]

        operator = re.findall('[0-9].* (\S+) [0-9].*', probleme)[0]

        second_operand = re.findall('[0-9].* \S+ ([0-9].*)', probleme)[0]

        if int(first_operand) > 9999 or int(second_operand) > 9999:
            return "Error: Numbers cannot be more than four digits."
        if operator in ["/", "*"]:
            return "Error: Operator must be '+' or '-'."

        formatter(problems, problem, first_operand,operator, second_operand)

    return (first+"\n"+second+"\n"+lines+"\n"+sumx if true_false is True else first+"\n"+second+"\n"+lines)


def arithmetic_arranger(problems, true_false=False):

    return handling_errors(problems, true_false)


#print(arithmetic_arranger(["3333 + 8", "1 + 3801", "9999 + 9999", "5235 + 49", "523 + 34"],True))
print(arithmetic_arranger(['3801 - 2', '123 + 49'],True))
#print(arithmetic_arranger(['1 + 2', '1 - 9380'],True))
#print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
#print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
