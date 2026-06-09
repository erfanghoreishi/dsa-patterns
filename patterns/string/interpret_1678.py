#1678. Goal Parser Interpretation
def interpret(command):
    return command.replace("()", "o").replace("(al)", "al")
