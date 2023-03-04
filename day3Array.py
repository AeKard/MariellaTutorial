# ARRAY IN PYTHON
#
#   List - is a collection whihc is {ordered and changeable}. allows {duplicate memebrs}
#   Tuple - is a collection which is {ordered and unchangeable}. Allows {duplicate members.}
#   Set - is s a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#   Dictionary - is a collection which is ordered** and changeable. No duplicate members.

# what is variablename, what is the index of that variable that you want to replace
print("=" * 40)
ListOfNames = ["Venedict", "LordDrake", "Mariella", "Marvin"]
print(type(ListOfNames))
# variable name [index] = you want to replace
ListOfNames[1] = "Colleen"
ListOfNames.insert(0,"anothername")
# Add from backoftheline
ListOfNames.append("Lord Drake")
print(ListOfNames)
ListOfNames.sort()
print(ListOfNames)
print("BOJBOPSHJDFP")
TupleOfnames = {"VEnedict", "LOrddrake", "mariella", "marvin", "marvin"}
# TupleOfnames[1] = "Colleen"
print(type(TupleOfnames))
TupleOfnames.add("Budoy")
TupleOfnames.discard("LOrddrake")
print(TupleOfnames)

dict_students = {
    # KEY : "VARIABLE"
    1: {"name": "Lord Drake", "Gender": "Male", "GradeLevel" : "Firstyear"},
    2: {"name": "Mariella Biscarra", "Gender": "Female", "GradeLevel" : "Firstyear"}
}
print(dict_students[1]["name"])
print(dict_students.keys())



