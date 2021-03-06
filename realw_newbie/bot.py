import discord, ctypes, webbrowser, json, os
from discord.ext import commands

f = open('config.json', 'r', encoding="utf-8")
json_data = json.load(f)

bot = commands.Bot(command_prefix='')
bot.remove_command("help")
token = json_data['bot']['token']

cogs = [
    "newbie",
    "error",
    "ready"
]

def load_extension():
    try:
        for extension in cogs:
            bot.load_extension('realw_newbie.cogs.' + extension)
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, f"오류가 발생하였습니다.\n\n{e}", "Error", 0)
        quit()

def load_module():
    os.system('pip install -r realw_newbie/requirements.txt')
    os.system('cls')