from utils import colors

# spalvos
clr = colors.clr()

class Messages():
    def __init__(self):
        test = "test"
    def error(self, text):
        print(f"{clr.CRED}[{clr.CEND}{clr.CBOLD}ERROR{clr.CRED}]{clr.CEND} {text}")
    def used_nitro(self, text):
        print("OK")