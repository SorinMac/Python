import os
import discord
from discord.ext import commands
import asyncio

msg = ""

#starting the setup for the discord bot
client = discord.Client()

#login for the bot
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global msg
    if message.author == client.user:
        return
   
    #commands for the many different games
    if message.content.startswith("$Rainbow"):
      msg = await message.channel.send("@everyone Who wants to join? Add ✅ to the next message to accept")

    if message.content.startswith("$CallofDuty"):
      msg = await message.channel.send("@everyone Who wants to join? Add ✅ to the next message to accept")

    if message.content.startswith("$Valorant"):
      msg = await message.channel.send("@everyone Who wants to join? Add ✅ to the next message to accept ")

    if message.content.startswith("$LeagueOfLegends"):
      msg = await message.channel.send("@everyone Who wants to join? Add ✅ to the next message to accept")

    if message.content.startswith("$PayDay"):
      msg = await message.channel.send("@everyone Who wants to join? Add ✅ to the next message to accept")

#puts all users that react with specific reaction into a list
@client.event
async def on_reaction_add(reaction, user):
  list_user = ""
  if reaction.emoji == '✅':
    list_user += user


#bot commmand for the timer
@client.commands
async def timer(ctx, minutes):
  try:
    minint = int(minutes)
    if minint > 600:
      await ctx.send("Can not go over 10 hours.")
      raise BaseException
    if minint <= 0:
      await ctx.send("Can not have a negative time.")
      raise BaseException

    message =  await ctx.send(f"Timer: {minutes}")

    while True:
      minint -= 1
      if minint == 0:
        await message.edit(content = "@everyone The countdown is over!")
        break
     
      await message.edit(content = f"Timer: {minint}")
      await asyncio.sleep(60)
      list_user = msg.reactions #getting reactions
      for i in range(len(list_user)):
        await ctx.send(f"{ctx.author.mention}, @"+ list_user[i] + "The countdown is over time to squad up!")
  except ValueError:
    await ctx.send("Enter a number!")

client.run(os.getenv("Token"))




OTI4OTkwMzAxNzA2Njc0MjE2.Ydgzow.DspXnU5UcdpJjgs36NdxDK0ksaI

Persmission Integer:
525613845568