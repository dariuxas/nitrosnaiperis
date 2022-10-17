# bot file
import os, sys
from discord.ext import commands
import json
from utils import colors, msgs


clr = colors.clr() #spalvos
cmsg = msgs.Messages()

def lg():
  print(f"""{clr.CYELLOW2}
       _ _                               _ 
 _ __ (_) |_ _ __ ___  ___ _ __   __   _/ |
| '_ \| | __| '__/ _ \/ __| '_ \  \ \ / / |
| | | | | |_| | | (_) \__ \ | | |  \ V /| |
|_| |_|_|\__|_|  \___/|___/_| |_|   \_(_)_|
                                           
  {clr.CEND}""")

lg()

def check():
  print(f"{clr.CYELLOW2}[INFO] Tikrinam ar viskas taip kaip turi buti....{clr.CEND}")
  if not sys.version_info.major == 3 and sys.version_info.minor >= 6:
    cmsg.error(f"Python versija privalo buti {clr.CRED}3.6{clr.CEND} arba aukstesne.")
    sys.exit()
  try:
    cfg_file = open('config.json', 'r', encoding="UTF-8").read()
    cfg = json.loads(cfg_file)
  except:
    cmsg.error(f"Nepavyko atidaryti {clr.CRED}config.json{clr.CEND} failo.")
    sys.exit()
  if not cfg["user"]["bot_token"]:
    cmsg.error(f"Patikrinkite {clr.CRED}config.json{clr.CEND} faila. Neuzpildytas {clr.CRED}bot_token{clr.CEND}")
    sys.exit()
  if not cfg["user"]["user_token"]:
    cmsg.error(f"Patikrinkite {clr.CRED}config.json{clr.CEND} faila. Neuzpildytas {clr.CRED}user_token{clr.CEND}")
    sys.exit()
  print(f"{clr.CGREEN}[INFO] Viskas ok...{clr.CEND}")
  
  

check()


bot = commands.Bot(command_prefix='@(!*@(')
cfg_file = open('config.json', 'r', encoding="UTF-8").read()
cfg = json.loads(cfg_file)

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
bot.run(cfg['user']['bot_token'])
