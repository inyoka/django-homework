input = ['Hello','Hi','Heeololeo']

# Attempt 1
# def stringBits(mystr):
#     new_str = ""
#     seq = (number for number in range(len(mystr)) if not number%2)
#     for position in seq:
#         new_str += mystr[position]
#     return new_str
#
# for item in input:
#     print(stringBits(item))

# Attempt 2
def stringBits(mystr):
    new_str = ""
    dict_one = zip(range(len(mystr)), mystr)
    for key, item in dict_one:

        print(f"{key} : {item}")
        if not key % 2:
            new_str += item
# Final attempt

# def stringBits(mystr):
#     new_str = ''.join([item for key, item in zip(range(len(mystr)), mystr) if not key % 2])
#     return new_str

for item in input:
    print(stringBits(item))
