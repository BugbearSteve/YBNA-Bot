# ybnabot.py
#d6 functionality

import os
from random import randint

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def ybna6_faces(x):
    return{
        1: 'No, And...',
        2: 'No...',
        3: 'No, But...',
        4: 'Yes, But...',
        5: 'Yes...',
        6: 'Yes, And...'
        }[x]

def danger6_faces(x):
        return{
        1: 'Blank',
        2: 'Blank',
        3: 'Blank',
        4: 'Blank',
        5: ':skull:',
        6: ':skull: :skull:'
        }[x]

def ybna10_faces(x):
	return{
	1: 'No, And...',
	2: 'No, And, But...',
	3: 'No...',
	4: 'Not, But...',
	5: 'No, But, And...',
	6: 'Yes, But, And...',
        7: 'Yes, But...',
        8: 'Yes...',
        9: 'Yes, And, But...',
        10: 'Yes, And...'
	}[x]

def danger10_faces(x):
        return{
                1: 'Blank',
                2: 'Blank',
                3: 'Blank',
                4: 'Blank',
                5: ':skull',
                6: ':skull: :skull',
                7: 'Blank',
                8: 'Blank',
                9: ':skull:',
                10: ':skull: :skull:'
                }[x]

@client.event
async def on_ready():
    global sides
    sides = 6
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    global sides
    if message.author == client.user:
        return

#Send Help DM
    if message.content.startswith('!y help'):
        await message.author.send('YBNA Bot Help!')
        await message.author.send('Commands:')
        await message.author.send('!y X Z - Roll X number of YBNA dice and Z Danger dice (Danger die can be omitted)')
        await message.author.send('!y d6 - Choose six sided dice')
        await message.author.send('!y d10 - Choose 10 sided dice')
        await message.author.send('!y dice - Displays which dice are selected (d6 or d10)')
        await message.author.send('!y help - This message!')
        await message.author.send('The "Yes, but... No, And..." system was created and developed by txutfz73.')
        await message.author.send('https://www.reddit.com/user/txutfz73/')
        await message.author.send('Bot GitHub: https://github.com/BugbearSteve/YBNA-Bot')
        return


#Check die used
    if message.content.startswith('!y dice'):
        response = 'Using ' + str(sides) + ' sided dice!'
        await message.channel.send(response)
        return

#Choose d6 or d10
    if message.content.startswith('!y d6'):
        sides = 6
        await message.channel.send('Now using d6!')
        return

    if message.content.startswith('!y d10'):
        sides = 10
        response = 'Now using d10!'
        await message.channel.send(response)
        return




#Roll d6
    if sides == 6:
        if message.content.startswith('!y'):
            if int(message.content[2])>int(0):
                z = int(message.content[2])
                for x in range(z):
                    y = randint(1,6)
                    response = 'Roll ' + str(x+1) + ': ' + ybna6_faces(y)
                    await message.channel.send(response)

        if len(message.content)>=4:
            if int(message.content[4])>int(0):
                z = int(message.content[4])
                for x in range(z):
                    y=randint(1,6)
                    response = 'Danger ' + str(x+1) + ': ' + danger6_faces(y)
                    await message.channel.send(response)

#Roll d10
    else:
        if message.content.startswith('!y'):
            if int(message.content[2])>int(0):
                z = int(message.content[2])
                for x in range(z):
                    y = randint(1,10)
                    response = 'Roll ' + str(x+1) + ': ' + ybna10_faces(y)
                    await message.channel.send(response)

        if len(message.content)>=4:
            if int(message.content[4])>int(0):
                z = int(message.content[4])
                for x in range(z):
                    y=randint(1,10)
                    response = 'Danger ' + str(x+1) + ': ' + danger10_faces(y)
                    await message.channel.send(response)


client.run(TOKEN)
