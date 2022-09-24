import discord, random, time, os
from dotenv import load_dotenv

load_dotenv()

class MyClient(discord.Client):
    def __init__(self, intents=discord.Intents.all()):
        super().__init__(intents=discord.Intents.all())
        
        with open("badday.txt", "r") as f:
            self.badday = f.readlines()
        
        with open("wisdom.txt", "r") as f:
            self.wisdom = f.readlines()
    
    async def on_ready(self):
        print('logged in as ', self.user)
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.lower() == 'ciao':
            time.sleep(1)
            await message.channel.send('cya ..!')
        
        if message.content.lower() == 'ping':
            time.sleep(1)
            await message.channel.send('rocket pong !')
        
        if ('meh' in  message.content.lower()) or ('fuck' in message.content.lower()) or ('roast' in message.content.lower()):
            await message.channel.send('gfu...')
            time.sleep(2)
            await message.channel.send(self.badday[random.randint(1,15)])
        
        if ('quote' in  message.content.lower()) or ('wisdom' in message.content.lower()) or ('help' in message.content.lower()):
            await message.channel.send('here u go...')
            time.sleep(2)
            await message.channel.send(self.wisdom[random.randint(1,8)])



client = MyClient()

client.run(os.getenv('TOKEN'))
