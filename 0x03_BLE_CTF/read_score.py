import asyncio
from bleak import BleakClient

address = "30:c6:f7:2f:ef:06"
MODEL_NBR_UUID = "0000ff01-0000-1000-8000-00805f9b34fb"
MODEL_NBR_UUID = 0x002a

async def read_score(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(int(MODEL_NBR_UUID)-1)
        print("Score: {0}".format("".join(map(chr, model_number))))

if __name__ == "__main__":
    asyncio.run(read_score(address))