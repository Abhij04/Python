marks ={
  "harry":100,
  "shubham":56,
  "rohan":23
}


# print(marks.items()) #dict_items([('harry', 100), ('shubham', 56), ('rohan', 23)])
# print(marks.keys()) #dict_keys(['harry', 'shubham', 'rohan'])
# print(marks.values()) # dict_values([100, 56, 23])

# marks.update({"harry" :99 , "renuka" : 100} )  #it will update  harry marks and it add new key named "renuka" with value 100 in dict

print(marks.get("harry2")) # none
# print(marks["harry2"]) # error
# print(marks.pop("harry"))  #it will delets harry
print(marks.popitem())
print(marks.popitem()) # last in firts out
print(marks)
