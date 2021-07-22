# input_name = input("give me a name: ")

input_name = "dela cruz"


name_elements = input_name.split()
print(name_elements)
print(all(name.isalpha() for name in name_elements))


#
# if input_name.isalpha():
#     print("name isalpha")
# elif any(input_name.isalpha):
#     print("any of name isalpha")
# else:
#     print("nope")