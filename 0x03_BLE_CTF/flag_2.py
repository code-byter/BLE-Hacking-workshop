import asyncio
from bleak import BleakClient
from read_score import read_score

address = "30:c6:f7:2f:ef:06"
handle = 0x002c

async def main(address):
    async with BleakClient(address) as client:
        response = await client.read_gatt_char(int(0x002e) - 1)
        print(f"Reponse: {response}")
        await client.write_gatt_char(int(handle)-1, response)
        print(f"Wrote {response} to {handle}")


asyncio.run(main(address))
asyncio.run(read_score(address))