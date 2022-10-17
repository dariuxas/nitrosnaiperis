import colorama
from termcolor import *

colorama.init()

class Messages:
    def __init__(self):
        self.x = 10
        # spalvos
        self.CEND      = '\33[0m'
        self.CBOLD     = '\33[1m'
        self.CITALIC   = '\33[3m'
        self.CURL      = '\33[4m'
        self.CBLINK    = '\33[5m'
        self.CBLINK2   = '\33[6m'
        self.CSELECTED = '\33[7m'
        self.CBLACK  = '\33[30m'
        self.CRED    = '\33[31m'
        self.CGREEN  = '\33[32m'
        self.CYELLOW = '\33[33m'
        self.CBLUE   = '\33[34m'
        self.CVIOLET = '\33[35m'
        self.CBEIGE  = '\33[36m'
        self.CWHITE  = '\33[37m'
        self.CBLACKBG  = '\33[40m'
        self.CREDBG    = '\33[41m'
        self.CGREENBG  = '\33[42m'
        self.CYELLOWBG = '\33[43m'
        self.CBLUEBG   = '\33[44m'
        self.CVIOLETBG = '\33[45m'
        self.CBEIGEBG  = '\33[46m'
        self.CWHITEBG  = '\33[47m'
        self.CGREY    = '\33[90m'
        self.CRED2    = '\33[91m'
        self.CGREEN2  = '\33[92m'
        self.CYELLOW2 = '\33[93m'
        self.CBLUE2   = '\33[94m'
        self.CVIOLET2 = '\33[95m'
        self.CBEIGE2  = '\33[96m'
        self.CWHITE2  = '\33[97m'
    def code_found(self, invite, message):
        print(f"[{self.CBLUE}{invite}{self.CEND}] {message}")
    def uknown_code(self, invite, message):
        print(f"[{self.CRED}{invite}{self.CEND}] {message}")
    def already_redeemed(self, invite, message):
        print(f"[{self.CYELLOW}{invite}{self.CEND}] {message}")
    def need_payment(self, invite, message):
        print(f"[{self.CRED2}{invite}{self.CEND}] {message}")