import asyncio
from bless import (
        BlessServer,
        BlessGATTCharacteristic,
        GATTCharacteristicProperties,
        GATTAttributePermissions
)

def my_read_callback(uuid):
    pass

async def main(loop):
    service_name = "Basic GATT server hwh_"
    server = BlessServer(name=service_name, loop=loop)
    server.read_request = my_read_callback

    custom_service_uuid = "ca59d6f6-88fd-4902-8b87-5d97e9d81b93"
    await server.add_new_service(custom_service_uuid)

    characteristic_uuid = ""

    await server.start()
    await asyncio.sleep(120)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))