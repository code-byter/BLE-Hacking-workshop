import asyncio
from bleak import BleakClient
from read_score import read_score

address = "30:c6:f7:2f:ef:06"
handle = 0x002c
challenge_addr = 0x003e
async def main(address):
    async with BleakClient(address) as client:

        for i in range(1000):
            response = await client.read_gatt_char(int(challenge_addr) - 1)
            print(f"Reponse: {response}")

            if not 'Read me' in str(response):
                await client.write_gatt_char(int(handle) - 1, response)
                print(f"Wrote {response} to {handle}")
                break


asyncio.run(main(address))
asyncio.run(read_score(address))