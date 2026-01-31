import aiohttp
import asyncio
import sys
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")


async def test_endpoint(url):
    headers = {'Authorization': f'Bearer {API_KEY}'}
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=10) as resp:
                print(f"\n🔗 {url}")
                print(f"📊 Status: {resp.status}")
                
                if resp.status == 200:
                    data = await resp.text()
                    print(f"✅ Success! Data: {data[:200]}...")
                    return True
                else:
                    error = await resp.text()
                    print(f"❌ Error: {error}")
                    return False
    except Exception as e:
        print(f"❌ Connection failed: {type(e).__name__}")
        return False

async def main():
    print("🔍 Testing ServerProject API endpoints...")
    
    endpoints = [
        f"https://serverproject.net/panel/api/public/service/{API_KEY}/query"
    ]
    
    for url in endpoints:
        await test_endpoint(url)

if __name__ == "__main__":
    asyncio.run(main())