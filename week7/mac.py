'''mac'''
def checker(address):
    """check"""
    if len(address) not in [17, 14]:
        return "ERROR"
    valid_chars = set("ABCDEFabcdef0123456789.:-")
    if not all(char in valid_chars for char in address):
        return "ERROR"
    if not (address.count(":") == 5 or address.count(".") == 2 or address.count("-") == 5):
        return "ERROR"
    if all(address[i] == "-" for i in [2, 5, 8, 11, 14]):
        return "VALID 1"
    if all(address[i] == ":" for i in [2, 5, 8, 11, 14]):
        return "VALID 2"
    if (address[4] == "." and address[9] == "." and
          address[:4].isalnum() and address[5:9].isalnum() and address[10:].isalnum()):
        return "VALID 3"
    return "ERROR"
def main():
    """aaa"""
    address = input()
    result = checker(address)
    print(result)
main()
