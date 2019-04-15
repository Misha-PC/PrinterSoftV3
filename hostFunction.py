
def readFile(fileName):
    file = open(fileName)
    context = file.read()
    file.close()
    return(context)
