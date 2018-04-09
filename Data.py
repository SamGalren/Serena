import discord
import asyncio
import random
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("Greetings. I am Kaliana Serena Andres, people know me as Serena")

@client.event
async def on_message(message):
    if message.author == client.user:
        pass
    elif message.content.startswith("$ping"):
        await client.send_message(message.channel, "pong")
    elif message.content.startswith("$Je t'aime"):
        await client.send_message(message.channel, "Moi aussi <3")
    elif message.content.startswith("$Serenaaa"):
        await client.send_message(message.channel, "Quoiii '-'")
    elif message.content.startswith("$C'est qui la plus belle?"):
        await client.send_message(message.channel, "C'est Zoe! :D")
    elif message.content.startswith("$Seal est mieux qu'uni"):
        await client.send_message(message.channel, "pfff n'importe quoi e_e")
    elif message.content.startswith("$Hello"):
        await client.send_message(message.channel, "Hi there!")
    elif message.content.startswith("$Its me brista"):
        await client.send_message(message.channel, "Hey brista! ;DD")
    elif message.content.startswith("$Its me Sam"):
        await client.send_message(message.channel, "oh.. you. uh. hi?")
    elif message.content.startswith("$How are you?"):
        await client.send_message(message.channel, "Im Great! What about you? ^-^")
    elif message.content.startswith("$Im good"):
        await client.send_message(message.channel, "Glad to read ;P")
    elif message.content.startswith("$Im bad"):
        await client.send_message(message.channel, "oh..im sorry to hear that ;c")
    elif message.content.startswith("$Its me Zoe"):
        await client.send_message(message.channel, "Zoee!!! :DDD *hug* I love u sooooo much ;D")
    elif message.content.startswith("$Fuck you"):
        await client.send_message(message.channel, "Watch out.. Language")
    elif message.content.startswith("$You're the worst scientist ever"):
        await client.send_message(message.channel, ":sob:")
    elif message.content.startswith("$Hey Serena"):
        await client.send_message(message.channel, random.choice(["It is certain :wink: ",
                                                                  "It is decidedly so :8ball:",
                                                                  "Without a doubt :8ball",
                                                                  "You may rely on it :8ball:",
                                                                  "As I see it, yes :8ball:",
                                                                  "Most likely :8ball:",
                                                                  "Outlook good :8ball:",
                                                                  "Yes :8ball:",
                                                                  "Signs point to yes :8ball",
                                                                  "Reply hazy try again :8ball",
                                                                  "Ask again later :8ball:",
                                                                  "Better not tell you now :8ball:",
                                                                  "Cannot predict now :8ball:",
                                                                  "Concentrate and ask again :8ball",
                                                                  "Don't count on it :8ball:",
                                                                  "My reply is no :8ball",
                                                                  "My sources say no :8ball:",
                                                                  "Outlook not so good :8ball:",
                                                                  "Very doubtful :8ball:",
                                                                  "You have to be kidding me.. :8ball:",
                                                                  "Eh.. go ask Zoe. Im out. >_>",
                                                                  "Heck no.. :rage: ",
                                                                  "For real.. :8ball:",
                                                                  "I know that i am a genious but.. come on.. :8ball:",]))    
  
        
client.run("NDMxOTU5MDU0ODE5MDAwMzIx.Da0_mQ.HYJheOK6jZYI94DBahQmqS-zhKQ")
