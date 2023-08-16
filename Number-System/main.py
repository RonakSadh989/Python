O = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "10": "1010",
    "11": "1011",
    "12": "1100",
    "13": "1101",
    "14": "1110",
    "15": "1111"
}
O1 = {
    "10": "A",
    "11":"B",
    "12":"C",
    "13":"D",
    "14":"E",
    "15": "F"
}


def OctalToBinary():
    octal = []
    binary = []
    bin = ""
    inp = input("Enter Your Octal No:  ")
    for letter in inp:
        octal.append(letter)

    for i in range(len(octal)):
        for index in range(8):
            if octal[i]== str(index):
                binary.append(O[str(index)][1:])

    for i in binary:
        bin += i
    print("Your Binary Number is:", bin)


def BinaryToOctal():
    octal = []
    binary = []
    oct = ""
    inp = input("Enter Your Binary No:  ")
    for l in range(0, len(inp), 3):
        binary.append(inp[l : l + 3])

    for i in range(len(binary)):
        for index in range(8):
            if binary[i] == O[str(index)][1:]:
                octal.append(str(index))

    for i in octal:
        oct += i
    print("Your Octal Number is: ", oct)


def HexadecimalToBinary():
    hexa = []
    binary = []
    bin = ""
    inp = input("Enter Your Hexadecimal No:  ")
    for letter in inp:
        hexa.append(letter.upper())
    for i in range(len(hexa)):
        for index in range(16):
            if hexa[i]== str(index):
                binary.append(O[str(index)])
                break
            if hexa[i] not in O:
                for index_ in range(1,6):
                 if hexa[i] == O1[str(9+index_)]:
                    binary.append(O[str(9+index_)])
                break
          
              
    for i in binary:
        bin += i
    print("Your Binary Number is:", bin)

def BinaryToHexadecimal():
    bin = input("Enter your Binary No: ")
    bin_arr = []
    hexa = []
    hexadecimal = ""
    for i in range(0, len(bin), 4):
        bin_arr.append(bin[i:i+4])
    for i in range(len(bin_arr)):
        for index in range(16):
         if bin_arr[i] == O[str(index)]:
             if index>9:
                 hexa.append(O1[str(index)])
             else: hexa.append(str(index))
    for i in hexa:
        hexadecimal += i     
    print("Your Hexadecimal Number is:",hexadecimal)  
      




def BinarytoDecimal():
    bin = input("Enter Your Binary Number:  ")
    str_len = len(bin) - 1
    bin_arr = []
    dec = []
    decimal = 0
    for i in range(len(bin)):
        bin_arr.append(bin[i : i + 1])
        dec1 = (2**str_len) * (int(bin_arr[i]))
        dec.append(dec1)
        str_len = str_len - 1
        decimal += dec[i]
    print("Your Decimal Number is: ", decimal)


def DecimalToBinary():
    decimal = input("Enter your Decimal Number: ")
    binary = ""
    n = int(decimal)
    steps = 0
    for i in range(100):
        if n < (2**i):
            steps = i
            break

    for i in range(steps):
        bin = int(decimal) / 2
        bin = str(bin)
        if ".5" in bin:
            binary += "1"
        else:
            binary += "0"
        decimal = bin[0 : bin.index(".")]
    print(binary[::-1])


ques = input("From what Number system do you want to convert from?  ")
ans = input("In What Number system do you want to Convert it in?  ")


if ques.lower() == "octal" and ans.lower() == "binary":
    OctalToBinary()
if ques.lower() == "binary" and ans.lower() == "octal":
    BinaryToOctal()
if ques.lower() == "binary" and ans.lower() == "decimal":
    BinarytoDecimal()
if ques.lower() == "decimal" and ans.lower() == "binary":
    DecimalToBinary()
if ques.lower() == "hexadecimal" and ans.lower() == "binary":
    HexadecimalToBinary()
if ques.lower() == "binary" and ans.lower() == "hexadecimal":
    BinaryToHexadecimal()