import json

def savePopulation(population):
    with open('results.json') as f:
        list = json.load(f)['list']

    with open('results.json','w', encoding='utf-8') as f:
        average = 0
        for element in population:
            average += element[1]

        element = {average/int(len(population)) : population}
        list.append(element)
        json.dump({"list" : list}, f, ensure_ascii=False, indent=4)
