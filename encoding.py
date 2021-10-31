def decimalToBinary(n): 
    if n > 255:
        print("error, nombre trop grand")
    else:
        binary =  bin(n).replace("0b", "")
        if len(binary) < 8:
            binary = "0" * (8 - len(binary)) + binary

        return binary
