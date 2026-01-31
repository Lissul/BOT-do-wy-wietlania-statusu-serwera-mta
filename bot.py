### Autor: Lissu
### Prosty bot Discord do wyświetlania liczby graczy na serwerze MTA za pomocą ServerProject API.





import discord
from discord.ext import tasks
import aiohttp
import asyncio
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

class SimpleSafeBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        
        self.API_KEY = os.getenv("API_KEY")  # Twój ServerProject API Key
        self.CHANNEL_ID = int(os.getenv("VOICE_CHANNEL_ID"))  # Twój channel ID
        
        self.last_count = -1
        self.last_update = 0
        
    async def on_ready(self):
        print(f'✅ {self.user} - Bot uruchomiony')
        print('⏰ Aktualizacja co 10 minut (bezpieczny limit)')
        self.update.start()
    
    async def get_player_count(self):
        try:
            url = f"https://serverproject.net/panel/api/public/service/{self.API_KEY}/query"
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=10) as r:
                    if r.status == 200:
                        data = await r.json()
                        if 'error' not in data:
                            return int(data.get('gq_numplayers', 0))
        except:
            pass
        return -1
    
    @tasks.loop(minutes=10)  # CO 10 MINUT - bezpieczny limit Discord!
    async def update(self):
        players = await self.get_player_count()
        
        if players == -1:
            name = "🔴 Serwer offline"
        elif players != self.last_count:
            name = f"👥 Online: {players}"
            
            if players == 0:
                name = "🟡 " + name
            elif players < 10:
                name = "🟢 " + name
            elif players < 15:
                name = "🔵 " + name
            else:
                name = "🔥 " + name
            
            channel = self.get_channel(self.CHANNEL_ID)
            if channel:
                try:
                    await channel.edit(name=name)
                    self.last_count = players
                    print(f"📝 {datetime.now().strftime('%H:%M')} - {name}")
                except:
                    print("⚠️ Nie udało się zaktualizować")
    
    @update.before_loop
    async def before_update(self):
        await self.wait_until_ready()

# Uruchomienie
bot = SimpleSafeBot()

bot.run(os.getenv("DISCORD_TOKEN"))