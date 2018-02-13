def fileRDR(filename):
    with open(filename, 'r') as myTextFileIn:
        myTextIn = myTextFileIn.read()

        myTextFileIn.close()

    return myTextIn