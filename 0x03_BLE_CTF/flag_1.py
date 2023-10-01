import asyncio
from bleak import BleakClient
from read_score import read_score

address = "30:c6:f7:2f:ef:06"
handle = 0x002c
data = b"12345678901234567890"

async def main(address):
    async with BleakClient(address) as client:
        await client.write_gatt_char(int(handle)-1, data)
        print(f"Wrote {data} to {handle}")

asyncio.run(main(address))
asyncio.run(read_score(address))