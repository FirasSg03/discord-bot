from discord.ext import commands
from dotenv import load_dotenv
import discord, time, os, typing
import google.generativeai as genai

load_dotenv()
#### COMMANDS ####
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='$')
@bot.command()
async def test(ctx, *args):
    await ctx.send(' '.join(args))

@bot.command()
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
    await ctx.send(f'{amount} bottles of {liquid} on the wall!')

#### generative AI ####
genai.configure(api_key=os.getenv('API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

def generativeai(input: str):
    response = model.generate_content(input)
    return response.text
    
#### implementation of GEMINI API
class MyClient(discord.Client):
    def __init__(self, intents=discord.Intents.all()):
        super().__init__(intents=discord.Intents.all())
    
    async def on_ready(self):
        print('logged in as ', self.user)
    
    # bot ignores his output
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.lower()[0]=="!":
            time.sleep(1)
            await message.channel.send(generativeai(message.content.lower()))
        

client = MyClient()
client.run(os.getenv('BOT_TOKEN'))
