import asyncio
from bleak import BleakClient
from read_score import read_score

address = "30:c6:f7:2f:ef:06"
handle = 0x002c
challenge_addr = 0x0040





async def main(address):
    async with BleakClient(address) as client:

        def callback(sender, data):
            print(f"{sender}: {data}")

        print(f"Client connection: {client.is_connected}")
        await client.start_notify(
            '0000ff0f-0000-1000-8000-00805f9b34fb', callback,
        )

        print("Listening for notifications")
        # await client.write_gatt_char(int(challenge_addr) - 1, b'0100')

        # await asyncio.sleep(20)
        # await client.stop_notify('0000ff0f-0000-1000-8000-00805f9b34fb')

        # for i in range(1000):
        #     response = await client.read_gatt_char(int(challenge_addr) - 1)
        #     print(f"Reponse: {response}")
        #
        #     if not 'Read me' in str(response):
        #         await client.write_gatt_char(int(handle) - 1, response)
        #         print(f"Wrote {response} to {handle}")
        #         break


asyncio.run(main(address))
# asyncio.run(read_score(address))
