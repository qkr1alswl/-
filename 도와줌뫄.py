import discord
import asyncio
import random

client = discord.Client()

token = "ODQ1MzA2NTgzMjk0Mjc5NzAx.YKfDGg.RcduL2YPAks84Le9kv73h9PhZTA"

@client.event
async def on_ready():

    print(client.user.name)
    print("성공적으로 봇이 시작되었습니다.")
    game = discord.Game('뫄 아니예용 뫄가 만든 봇이예용')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    if message.content == '50%뽑기':
        ran = random.randint(0,1)
        if ran == 0:
            d = '꽝'
        if ran == 1:
            d = '당첨'
        await message.channel.send(d)

    if message.content.startswith('골라줘'):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, choiceresult)
    
    if message.content == '뫄':
        await message.channel.send('멋쟁이ㅎ')

client.run(token)