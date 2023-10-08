import asyncio
from bleak import *

address = "30:AE:A4:97:90:26"

async def main(address=address):
    async with BleakClient(address) as client:
        gatt_service_collection: BleakGATTServiceCollection =  client.services
        print(gatt_service_collection.services.keys())

asyncio.run(main())
