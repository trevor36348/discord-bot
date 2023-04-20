"""
Code by trevor36348 https://github.com/trevor36348

Description:
Discord bot built with the purpose of practicing developing. Bot has a variety of functions, such as:
-   Set which roles in your server can use certain bot commands
    -   Only Admins can use admin commands
    -   Users with a server role associated with:
        -   full can use all commands except admin ones
        -   game can only use game commands
        -   text can only use text commands

-   Text commands such as:
    -   ...
    -   ...

-   Ability to play games such as TicTacToe and Rock Paper Scissors against another person or bot
"""

import re
import discord
from botFunctions import *
from commands.textcommands import *
from discord.ext import commands, tasks
from discord.ext.commands import Bot



bot = Bot (
   command_prefix='!',
   intents=discord.Intents.all(),
   help_command=None
)

# IMPORTANT ----------------------------------------------------------------------------------------
# Stores users custom roles
# Types of roles: [0] is full, [1] is game, [2] is text
# Once an admin assigns a server role to a type of role, users with that server role can use the 
#   commands associated with the type role
# --------------------------------------------------------------------------------------------------
roles = ['', '', '']

# Upon bot loading into server send message to console
@bot.event
async def on_ready():
  print('BOT ONLINE')



"""
ADMIN Commands
"""

# Help Command
@bot.command()
@commands.has_permissions(administrator=True)
async def help(ctx):
  await ctx.send(readfile("docs/admin_help.txt"))

# Sets roles that can use bot commands
@bot.command()
@commands.has_permissions(administrator=True)
async def set_role(ctx, *, message):
# user's message will be split into "!command" and "message"
# message split further below into two parts, as input require is as follows:
#   !set_role "type_role" "server_role"
  try:
    type_role = message.split()[0]
    server_role = message.replace((type_role+" "), "", 1)
  except IndexError:
    await ctx.send('Invalid input, missing name of server role "' + type_role + '" will be assigned to.')
    return 0

  if server_role in roles:
    await ctx.send('Role: "' + server_role + '" is already added.')
  elif not re.match("^[A-Za-z0-9_-]+$", server_role):
    await ctx.send('Please enter a server role name which is alphanumeric.')
  else:
    if(setTypeRole(roles, type_role, server_role)) == False:
       await ctx.send("Invalid type of role given.")
    else:
      await ctx.send('Role: "' + server_role + '" added for "' + type_role + '"!')

# Remove Role command, using setTypeRole function (view botFunctions.py)
@bot.command()
@commands.has_permissions(administrator=True)
async def remove_role(ctx, *, type_role):
  if(setTypeRole(roles, type_role, "")) == False:
    await ctx.send('Invalid type of role given.')
  else:
    await ctx.send('Provided role for "' + type_role + '" removed!')

# List Roles Command
@bot.command()
@commands.has_permissions(administrator=True)
async def list_roles(ctx):
  await ctx.send(roles)



"""
FULL Commands
"""

# 
@bot.command()
async def help_full(ctx):
  # Check if user has a server role associated with full
  if checkUserRole(roles[0], str(ctx.message.author.roles)):
    await ctx.send(readfile("docs/full_help.txt"))
  else:
    await ctx.send('NOT ALLOWED')



"""
GAME Commands
"""

# 
@bot.command()
async def help_game(ctx):
  if (checkUserRole(roles[0], str(ctx.message.author.roles)) or checkUserRole(roles[1], str(ctx.message.author.roles))):
    await ctx.send(readfile("docs/game_help.txt"))
  else:
    await ctx.send('NOT ALLOWED')



"""
TEXT Commands
"""
#
@bot.command()
async def help_text(ctx):
  if (checkUserRole(roles[0], str(ctx.message.author.roles)) or checkUserRole(roles[2], str(ctx.message.author.roles))):
    await ctx.send(readfile("docs/text_help.txt"))
  else:
    await ctx.send('NOT ALLOWED')

# 
@bot.command()
async def modTxt(ctx, *, message):
  try:
    command_type = message.split()[0]
    target = (message.split()[1])
    text = (message.split(":")[1]).lstrip()

    if (target[-1] != ":"):
      await ctx.send('Invalid input, missing arguments!')
      return 0
    else:
      target = target[:-1]
    
  except IndexError:
    await ctx.send('Invalid input, missing arguments!')
    return 0
  
  if (checkUserRole(roles[0], str(ctx.message.author.roles)) or checkUserRole(roles[2], str(ctx.message.author.roles))):
    await ctx.send(modify_text(command_type, target, text))
  else:
    await ctx.send('NOT ALLOWED')


"""
Error Handling
"""

# MissingRequiredArgument error handling for all commands
# Active when user enters command without required arguments (such as remove_role)
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Invalid input, please enter arguments for this command.")



bot.run(readfile("n1D3jfN3.txt"))