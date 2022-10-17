from discord.ext import commands
import discord
import requests, re
from bs4 import BeautifulSoup
import json
from msgs import Messages
from utils import colors
from datetime import date, datetime

# kintamieji
msg = Messages()
clr = colors.clr()


# bot klase
class Test_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.codes = []
        self.cfg_file = open('config.json', 'r', encoding="UTF-8").read() # nustatymu failas
        self.cfg = json.loads(self.cfg_file) # loadinam nustatymu faila
    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            DISCORD_NITRO = r"(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)"            
            regex = re.compile(DISCORD_NITRO)
            invites = regex.findall(str(message.content))
            inv = bool(invites)
            if inv:
                x = ["".join(x) for x in invites]
                invite = ''.join(x).rsplit('/', 1)[-1]
                # jeigu kodas buvo isbandytas 0 kartu
                if invite not in self.codes:
                    self.codes.append(invite)
                    print(f"[{clr.CYELLOW}INFO{clr.CEND}] rastas invite kodas {clr.CYELLOW}{invite}{clr.CEND} bandom aktyvuoti...")
                    headers = {
                        "Authorization": self.cfg['user']['user_token'],
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
                    }
                    r = requests.post(f"https://discord.com/api/v9/entitlements/gift-codes/{invite}/redeem", headers=headers)
                    response_time = int(r.elapsed.total_seconds())
                    bs = BeautifulSoup(r.content, 'html.parser')
                    y = json.loads(bs.prettify())
                    timestamp = datetime.now()
                    data = timestamp.strftime(r"%Y-%m-%d %H:%M:%S")
                    try:
                        kodas = y['code']
                    except:
                        if r.status_code == 200:
                            kodas = 69
                        elif r.status_code == 429:
                            kodas = 429
                    if kodas == 10038:
                        ats = "Kodas negaliojantis."
                        cl = f"[{clr.CRED}{invite}{clr.CEND}]"
                    elif kodas == 50050:
                        ats = "Kodas jau buvo aktyvuotas"
                        cl = f"[{clr.CRED}{invite}{clr.CEND}]"
                    elif kodas == 429:
                        ats = f"Per daug kartu bandyta aktyvuoti neteisingus kodus..."
                        cl = f"[{clr.CRED}{invite}{clr.CEND}]"
                    elif kodas == 0:
                        ats = f"Nepavyko patikrinti kodo, patikrinkite {clr.CRED}config.json{clr.CEND} faile {clr.CRED}user_token{clr.CEND}"
                        cl = f"[{clr.CRED}{invite}{clr.CEND}]"
                    elif kodas == 50070:
                        ats = "Nepridetas mokejimo metodas"
                        cl = f"[{clr.CYELLOW}{invite}{clr.CEND}]"
                    elif kodas == 69:
                        ats = "Nitro buvo sėkmingai aktyvuotas!"
                        cl = f"[{clr.CGREEN}{invite}{clr.CEND}]"
                    else:
                        ats = y['message']
                    if ats:
                        # print(f"{cl} {ats}")
                        print(r.content)
                        print(f"{data} ┃ {invite} ┃ {ats}")
                    # if kodas == 69:
                    #     scs = 1
                    #     spalva = 0x57d916
                    #     # sendinam sau msg kad zjb
                    #     usr = self.bot.get_user(int(self.cfg["user"]["admin_id"]))
                    #     await usr.send("Rastas veikiantis nitro, jis aktyvuotas xd")
                else:
                    print(f"[{clr.CRED}ANTI-BLOCK{clr.CEND}] {clr.CRED}{invite}{clr.CEND} jau buvo bandytas panaudoti.")
        except Exception as e:
            print(e)

def setup(bot): # a extension must have a setup function
    bot.add_cog(Test_Cog(bot)) # adding a cog