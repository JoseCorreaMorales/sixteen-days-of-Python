diccionary = {"key 1": "value 1", "key 2": "value 2", 3: 3, True: False, 3.1: 2.2}

print(diccionary)

""" List inside a diccionary """
myDiccionary = {"key 1": "value 1", 
                "key 2": [1, 2, 3, "hey"], 
                "key 3": [4, 34, 23, 4],
                "key 4": {"sub key 4-1": 2,
                                         "sub key 4-2": [1, 5, 3, 1]}
}

print(myDiccionary["key 1"])
print(myDiccionary["key 2"][3])
print(myDiccionary["key 3"][2])
print(myDiccionary["key 4"]["sub key 4-1"])
print(myDiccionary["key 4"]["sub key 4-2"][0])

dic = {'k1': ['a', 'b', 'c', 'd'],  "k2": ['e', 'f', 'g']}

print(dic["k2"][1].upper())

""" adding elemets """

dic[3] = 123
dic["k3"] = 'value 3'
print(dic)

""" overwritting """
myDiccionary["key 4"]["sub key 4-2"][0] = 0
print(f"overwritting:\t {myDiccionary}")


""" seeing structure """
print(dic.keys())
print(dic.items())
print(dic.values())