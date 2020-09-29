def arithmetic_arranger(problems, show_answer = False):
    """
    Created for Free Code Camp project.
    
    https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
    """

    ### INPUT VALIDATION ###
    # Check for more than five problems
    if len(problems) > 5:
        return "Error: Too many problems."
    # Check for '+' and '-' in each problem
    for prob in problems:
       # Check for '+' and '-' in each problem
        if '+' not in prob and '-' not in prob:
            return "Error: Operator must be '+' or '-'."
        for n in prob.split():
          # Check that numbers are four digits or less
            if len(n) > 4:
                return "Error: Numbers cannot be more than four digits." 
            # Check there are only digits
            if n.isdecimal() == False and n not in ['+','-']:
                return "Error: Numbers must only contain digits."

    ### SOLVING PROBLEM ###
    # Set up variable for each whole line
    all_line_one = ""
    all_line_two = ""
    all_line_three = ""
    all_line_four = ""
    
    # Iterate through each problem
    for prob in problems:
        # Split each problem/list into individual pieces
        split = prob.split()
        # Find the length the problem will use
        length = len(max(split, key = len)) + 2
        
        # Parse through split to get information for each line
        line_one = " "*(length-len(split[0])) + split[0] + " "*4
        line_two = split[1] + " "*(length-len(split[2])-1) + split[2] + " "*4
        line_three = "-"*length + " "*4
        
        # Line four needs to actually solve the problem
        if split[1] == '+':
            answer = str(int(split[0]) + int(split[2]))
        else:
            answer = str(int(split[0]) - int(split[2]))
        line_four = " "*(length-len(answer)) + answer + " "*4      
            
        # Add each individual problem to the whole line variable
        all_line_one += line_one
        all_line_two += line_two
        all_line_three += line_three
        all_line_four += line_four
        
    # Add all lines to final answer, removing last four empty spaces. Each line separated by a break
    show_answer_t = all_line_one[:-4] + '\n' + all_line_two[:-4] + '\n' + all_line_three[:-4] + '\n' + all_line_four[:-4]
    show_answer_f = all_line_one[:-4] + '\n' + all_line_two[:-4] + '\n' + all_line_three[:-4]
        
    # Return solution, depending whether answer are to be shown or not
    if show_answer == True:
        return show_answer_t
    else:
        return show_answer_f
    
# Testing
# print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
# print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],True))