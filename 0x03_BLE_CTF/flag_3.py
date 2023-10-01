import asyncio
from bleak import BleakClient
from read_score import read_score
import hashlib


address = "30:c6:f7:2f:ef:06"
handle = 0x002c
hash = hashlib.md5(b'BLECTF').digest().hex()
async def main(address):
    async with BleakClient(address) as client:
        await client.write_gatt_char(int(handle)-1, hash.encode()[:20])
        print(f"Wrote {hash[:20]} to {handle}")


asyncio.run(main(address))
asyncio.run(read_score(address))