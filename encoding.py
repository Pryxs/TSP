import path

# 15 ville max
def decimalToBinary(n): 
    if n > 15:
        print("error, nombre trop grand")
    else:
        binary =  bin(n).replace("0b", "")
        if len(binary) < 4:
            binary = "0" * (4 - len(binary)) + binary

        return binary


def vectorToObject(arrayPath, cities):
    convertedPaths = []
    for i in arrayPath:
        convertedPath = []
        for element in i:
            convertedPath.append(cities[element])


        convertedPath.append(convertedPath[0])
        newCovertedPath = []
        for i in range(int(len(convertedPath) - 1)):
            # print('depart : ', convertedPath[i].name)
            # print('arrivé : ', convertedPath[i + 1].name , '\n')
            newPath = path.Path(convertedPath[i], convertedPath[i + 1])
            newCovertedPath.append(newPath)


        convertedPaths.append(newCovertedPath)

    return convertedPaths
