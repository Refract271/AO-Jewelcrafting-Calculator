import orjson, copy
from collections import Counter

with open ("gemData.json", "r") as f:
    gemDict = orjson.loads(f.read())
    f.close()

with open ("reagantData.json", "r") as f:
    reagantDict = orjson.loads(f.read())
    f.close()

def existence(gem, reagant1, reagant2):

    # checks if all 3 input do exist in the database and creates an empty dict for reagant2 if it doesn't exist

    # gem : string      -> the gem you want to use
    # reagant1 : string -> the first reagant
    # reagant2 : string -> the second reagant

    # return bool, (reagant2 : dict) or just exit and print the issue

    if reagant2 not in reagantDict:
        reagant2 = ""

    if gem not in gemDict:
        print("gem does not exist")
        exit()

    elif reagant1 not in reagantDict:
        print("reagant1 does not exist")
        exit()

    elif reagantDict[reagant1].keys() == reagantDict[reagant2].keys():
        print("tried to use 2 reagants of the same type")
        exit()

    else:
        return True, reagant2

def getAffixes(gem, reagant1, reagant2):

    # gets the correct affixes for the jewel

    # reagant1 : string -> the first reagant
    # reagant2 : string -> the second reagant

    # return affixes : dict -> the dictionnary with the affixes

    if reagant2 == "":
        affixes = reagantDict[reagant1]
        reagantDict[reagant1].pop("prefix")
        affixes = {k: v * 2 if gem == "musgravite" and k != "movement_speed" else v * 1.5 if gem == "musgravite" and k == "movement_speed" else v for k, v in affixes.items()}
        
        return affixes

    else:
        secondaryAffix = list(reagantDict[reagant2])[0]
        affixes = reagantDict[reagant1] | reagantDict[reagant2]
        affixes.pop("prefix")
        affixes = {k: v * 2 if gem == "musgravite" and k != "movement_speed" else v * 1.5 if gem == "musgravite" and k == "movement_speed" else v for k, v in affixes.items()}
        affixes[secondaryAffix] /= 4

        return affixes

def makeJewel(gem, reagant1, reagant2):

    # simulates making a jewel

    # gem : string      -> the gem you want to use
    # reagant1 : string -> the first reagant
    # reagant2 : string -> the second reagant

    # return jewelName : string, jewelDict : dict  -> the jewel made; separated the name and the dict because it was easier this way later on

    exists, reagant2 = existence(gem, reagant1, reagant2)

    if exists == True:

        jewelName = name = "Perfect " + reagantDict[reagant1]["prefix"].lstrip("-") +  reagantDict[reagant2]["prefix"] + " " + gem.capitalize()
        affixes = getAffixes(gem, reagant1, reagant2)

        jewelDict = {
            "stat" : gemDict[gem],
            "affix" : affixes
        }

        return jewelName, jewelDict

    else:
        print("this should not happen")
        exit()

def reducedStatFormula(x):

    # used Lagrange Interpolation to create a formula for the way all the stats are reduced because in-game it is hardcoded (ty Vetex)

    return round(((((((2.0564611381640*10**(-7))*(x-4)-5.716887057477*10**(-7))*(x-9)-2.3294018910028*10**(-6))*(x-19)-0.0000112612)*(x-39)-0.000148754)*(x-1)+0.596257)*(x-188)+112)

def getFusedJewel(jewelDict1, jewelDict2):

    # makes the values of the stats and affixes "reduced" then sums the two dict

    # jewelDict1 : dict -> the dict of the first jewel
    # jewelDict2 : dict -> the dict of the first jewel

    # return fusedJewelDict : dict  -> the final dict basically

    for i in [jewelDict1, jewelDict2]:
        i["stat"] = {k: reducedStatFormula(v) for k, v in i["stat"].items()}
        i["affix"] = {k: round(v * 0.55, 2) for k, v in i["affix"].items()}

    fusedJewelDict = {
        "stat" : dict(Counter(jewelDict1["stat"]) + Counter(jewelDict2["stat"])),
        "affix" : dict(Counter(jewelDict1["affix"]) + Counter(jewelDict2["affix"]))
    }

    return fusedJewelDict

def fuseJewel(jewel1, jewel2):

    # fuses 2 jewels create by the makeJewel function

    # gem : string  -> the gem
    # jewel1 : dict -> the first jewel to combine
    # jewel2 : dict -> the second jewel to combine

    # return fusedJewel : dict -> the fused jewel

    jewelName1, jewelDict1 = jewel1
    jewelName2, jewelDict2 = jewel2

    if jewel1 == jewel2:
        fusedJewelName = "Perfect Empowered " + jewelName1.rsplit()[-1]

    else:
        fusedJewelName = "Perfect Empowered " + jewelName1.rsplit()[-1] + "-" + jewelName2.rsplit()[-1]
   
    fusedJewel = getFusedJewel(jewelDict1, jewelDict2)

    return fusedJewelName, fusedJewel

firstJewel = makeJewel("malachite", "arcane_salt", "bone")
secondJewel = makeJewel("lapis_lazuli", "seaweed", "toxic_seawater_bottle")

print(fuseJewel(firstJewel, secondJewel))