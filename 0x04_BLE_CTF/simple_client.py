import asyncio
from bleak import *

address = "30:AE:A4:97:90:26"

# Idiomatic way of creating a GATT client 
# This prevents the following exception from appearing randomly:
#    raise BleakDBusError(reply.error_name, reply.body)
# bleak.exc.BleakDBusError: [org.bluez.Error.Failed] Software caused connection abort
async def main(address=address):
    target_device = await BleakScanner.find_device_by_address(address)
    async with BleakClient(target_device) as client:
        gatt_service_collection: BleakGATTServiceCollection =  client.services
        print(gatt_service_collection.services.keys())

asyncio.run(main())
