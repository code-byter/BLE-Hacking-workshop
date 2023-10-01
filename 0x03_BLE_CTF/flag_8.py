import asyncio
from bleak import BleakClient
from read_score import read_score

address = "30:c6:f7:2f:ef:06"
handle = 0x002c
challenge_addr = 0x0038
async def main(address):
    async with BleakClient(address) as client:

        data = b'\xC9'
        write_addr = 0x003a
        await client.write_gatt_char(int(write_addr) - 1, data)
        print(f"Wrote {data} to {hex(write_addr)}")
        response = await client.read_gatt_char(int(challenge_addr) - 1)
        print(f"Reponse: {response}")
        
        await client.write_gatt_char(int(handle)-1, response)
        print(f"Wrote {response} to {handle}")


asyncio.run(main(address))
asyncio.run(read_score(address))