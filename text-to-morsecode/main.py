

MAPPING_MORSE = {
   "A": ".-",
   "B": "-...",
   "C": "-.-.",
   "D": "-..",
   "E": ".",
   "F": "..-.",
   "G": "--.",
   "H": "....",
   "I": "..",
   "J": ".---",
   "K": "-.-",
   "L": ".-..",
   "M": "--",
   "N": "-.",
   "O": "---",
   "P": ".--.",
   "Q": "--.-",
   "R": ".-.",
   "S": "...",
   "T": "-",
   "U": "..-",
   "W": ".--",
   "X": "-..-",
   "Y": "-.--",
   "Z": "--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
    ".":".-.-.-",
    ",":"--..--",
    "?":"..--..",
    "'":".----.",
    "!":"-.-.--",
    "/":"-..-.",
    "(":"-.--.",
    ")":"-.--.-",
    "&":".-...",
    ":":"---...",
    ";":"-.-.-.",
    "=":"-...-",
    "+":".-.-.",
    "-":"-....-",
    "_":"..--.-",
    """""":".-..-.",
    "$":"...-..-",
    "@":".--.-.",
    " ":".-.-."
}
def convert_to_morse(text: str):
    # split_str = text.split("")
    converter_string = [MAPPING_MORSE[a.upper()] for a in text]
    return "".join(converter_string)


def main():
    while(1):
        input_text = input("Enter a string to convert to morse:")
        input_text = convert_to_morse(input_text)
        print(f"The converted string is {input_text}")
        choice = input("Do you want to continue? (Y/N)")
        if choice.lower()=='n':
            break
    return


if __name__=='__main__':
    main()