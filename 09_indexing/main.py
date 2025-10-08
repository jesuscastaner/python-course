# indexing = accesing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_card = "1234-5678-9012-3456"

# get value at index i
print(credit_card[0])  # it starts at index 0
print(credit_card[1])
print(credit_card[4])
print(credit_card[-1])  # negative index starts at last element and goes backwards

# get values up to index i
print(credit_card[:4])  # doesn't include the end element
print(credit_card[:10])

# get values starting at index i
print(credit_card[5:])  # includes the start element
print(credit_card[10:])

# get every nth value
print(credit_card[::2])
print(credit_card[::5])

# print only last 4 digits
print(f"XXXX-XXXX-XXXX-{credit_card[-4:]}")

# reverse string
print(credit_card[::-1])
