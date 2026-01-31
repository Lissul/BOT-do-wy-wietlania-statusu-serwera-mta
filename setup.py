# save as setup.py
CONFIG = """
DISCORD_TOKEN=TOKEN_BOTA_DISCORD
VOICE_CHANNEL_ID=ID_KANAŁU_GŁOSOWEGO
API_KEY=API_KEY_SERWERA_SERVERPROJECT
"""

with open('.env', 'w') as f:
    f.write(CONFIG)

print("✅ Utworzono .env - uzupełnij token, ID kanału i API_KEY!")