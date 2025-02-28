affirm = input("Do you want to encode or decode a caeser cipher?: ")
affirm = affirm.lower()
if affirm != 'encode' and affirm != 'decode' and affirm != "quit":
    print("Invalid Answer")
    affirm = input("Do you want to encode or decode a caeser cipher?: ")
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

while affirm == "encode" or affirm == "decode":
    encodedmsg = []
    shiftvalue = int(input("How much positions do you want to shift by?: "))
    if affirm == "encode":
        shiftvalue = shiftvalue * -1
        cipher = input("Enter desired message to encode: ")
        cipher = cipher.lower()
        characters = list(cipher)
        for x in characters:
            if x.isalpha():
                position = alphabets.index(x)
                position = position + shiftvalue
                word = alphabets[position]
                encodedmsg.append(word)
            else:
                encodedmsg.append(x)
        print("".join(encodedmsg))

    if affirm == "decode":
        cipher = input("Enter desired message to decode: ")
        cipher = cipher.lower()
        characters = list(cipher)
        for x in characters:
            if x.isalpha():
                position = alphabets.index(x)
                position = position + shiftvalue
                word = alphabets[position]
                encodedmsg.append(word)
            else:
                encodedmsg.append(x)
        print("".join(encodedmsg))

    affirm = input("Do you want to encode or decode a caeser cipher? (Enter 'quit' to exit): ")
    affirm = affirm.lower()
    if affirm != 'encode' and affirm != 'decode' and affirm != "quit":
        print("Invalid Answer")
        affirm = input("Do you want to encode or decode a caeser cipher?: ")
else:
    print("Thank you for using this program!")