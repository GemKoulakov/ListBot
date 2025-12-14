import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
from myQueue import Queue
import datetime
import random

load_dotenv()

#setting intents
intents = discord.Intents.default()
intents.message_content = True

#dev server
GUILD_ID = discord.Object(id=os.getenv('DEV_SERVER'))

#queue
q = Queue()

class Client(commands.Bot):
    async def on_ready(self):
        #loads queue
        print(q.load_json())

        #notifys terminal bot is running
        print(f'Logged on as {self.user}!')

        #attempts to sync with dev server
        try:
            synced= await self.tree.sync(guild=GUILD_ID)
            print(f'Synced {len(synced)} commands to guild {GUILD_ID.id}')

        except Exception as e:
            print(f'Error syncing commands: {e}')


client = Client(command_prefix="!", intents=intents)

#Commands

#check if the bot is working
@client.tree.command(name='ping', description='Check if the bot is working', guild=GUILD_ID)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong!")

#Returns n elements in queue
@client.tree.command(name='list', description='Returns n elements in queue', guild=GUILD_ID)
async def list(interaction: discord.Interaction, n: int = 0):
    if q.isEmpty():
        await interaction.response.send_message(f"The list is Empty")
    else:
        if n == 0:
            n = q.size()
        r = "```text\n"
        for i, x in enumerate(q.displayQueue(n)):
            title = f"\"{x["title"]}\""
            r += f"{i+1:>2}.  {title:<25}  added by {x["user"]:<10}  on {x["time"]}\n"
        r += "```"
        await interaction.response.send_message(f"**your first {n} elements are:**\n{r}")

#Returns size of queue
@client.tree.command(name='size', description='Returns size of queue', guild=GUILD_ID)
async def size(interaction: discord.Interaction):
    await interaction.response.send_message(f"queue is now at {q.size()} elements!")

#adds new element to queue
@client.tree.command(name='queue', description='Adds new element to queue', guild=GUILD_ID)
async def queue(interaction: discord.Interaction, item: str):
    q.enqueue({"title":item,
               "user":interaction.user.nick,
               "time":str(datetime.datetime.now())[:10]})
    q.save_json()
    await interaction.response.send_message(f"added {item} to queue!")

#randomizes order of elements
@client.tree.command(name='shuffle', description='Randomizes order of elements', guild=GUILD_ID)
async def shuffle(interaction: discord.Interaction):
    q.shuffle()
    q.save_json()
    await interaction.response.send_message(f"shuffled!")

#Returns next element in queue
@client.tree.command(name='next', description='Returns next element in queue', guild=GUILD_ID)
async def next(interaction: discord.Interaction):
    n = q.get(0)
    await interaction.response.send_message(f'the next item is queue is: "{n["title"]}"" added by {n["user"]} on {n["time"]}!')

#Returns random element in queue
@client.tree.command(name='pick', description='Returns random element in queue', guild=GUILD_ID)
async def pick(interaction: discord.Interaction):
    n= q.get(random.randint(0,q.size()-1))
    print(n)
    await interaction.response.send_message(f'randomly picked: "{n["title"]}"" added by {n["user"]} on {n["time"]}!')

#removes element from queue
@client.tree.command(name='remove', description='Removes element from queue', guild=GUILD_ID)
async def remove(interaction: discord.Interaction, item: str):
    q.remove(item)
    q.save_json()
    await interaction.response.send_message(f"removed {item} from queue!")


client.run(os.getenv('DISCORD_TOKEN'))