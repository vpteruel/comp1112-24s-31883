import csv
import os
import subprocess
import sys
from datetime import datetime

# Function to install required packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install required packages if not already installed

# discord.py: A modern, easy to use, feature-rich, and async ready API wrapper for Discord written in Python.
try:
    import discord
    from discord.ext import commands
except ModuleNotFoundError:
    install('discord.py')

BOT_TOKEN = ''
CHANNEL_ID = 1268591038155456574

# Initialize the bot
intents = discord.Intents.all()
intents.members = True  # Make sure to enable the members intent
bot = commands.Bot(command_prefix="!", intents=intents)

# Path to the CSV file
CSV_FILE = 'assignment-3/members.csv'

# Helper function to write to the CSV
def write_to_csv(member, join_date):
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([member.id, member.name, join_date])

# Helper function to remove from the CSV
def remove_from_csv(member):
    lines = []
    with open(CSV_FILE, 'r') as file:
        reader = csv.reader(file)
        lines = [line for line in reader if line[0] != str(member.id)]
    
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

# Helper function to print message
async def log_message(message):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(message)
    print(message)

@bot.event
async def on_ready():
    await log_message(f'Logged in as {bot.user}.')

    # Create a list in first time
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Join Date'])

    # Users already registered
    for guild in bot.guilds:
        for member in guild.members:
            if not member.bot:
                write_to_csv(member, datetime.utcnow())

@bot.event
async def on_member_join(member):
    await log_message(f'{member.name} joined the server.')

    # Register when an user joins the server 
    write_to_csv(member, datetime.utcnow())

@bot.event
async def on_member_remove(member):
    await log_message(f'{member.name} left the server.')
    
    # Register when an user joins the server 
    remove_from_csv(member)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def add(ctx, x, y):
    result = int(x) + int(y)
    await ctx.send(f'{x} + {y} = {result}')

bot.run(BOT_TOKEN)
