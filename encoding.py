# 15 ville max
def decimalToBinary(n): 
    if n > 15:
        print("error, nombre trop grand")
    else:
        binary =  bin(n).replace("0b", "")
        if len(binary) < 4:
            binary = "0" * (4 - len(binary)) + binary

        return binary


def pathToVector(path):
    print(len(path))
