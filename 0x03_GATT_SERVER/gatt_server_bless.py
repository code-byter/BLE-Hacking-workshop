import asyncio
from bless import (
        BlessServer,
        BlessGATTCharacteristic,
        GATTCharacteristicProperties,
        GATTAttributePermissions
)

#This callback gets passed an object of type BlessGATTCaharateristic
#        return self.read_request_func(characteristic)
#  src: https://github.com/kevincar/bless/blob/67aacd4128186f13ea94c713a66271a7fc5e4bf2/bless/backends/server.py#L258
def my_read_callback(characteristic:BlessGATTCharacteristic):
    print(f"Returning: {characteristic.value} for uuid: {characteristic.uuid}")
    return characteristic.value

async def main(loop):
    service_name = "Basic GATT server hwh_"
    server = BlessServer(name=service_name, loop=loop)
    server.read_request_func = my_read_callback

    custom_service_uuid = "ca59d6f6-88fd-4902-8b87-5d97e9d81b93"
    await server.add_new_service(custom_service_uuid)

    characteristic_uuid = "abcf9298-6d32-4615-a365-61f074114425"
    char_properties = (GATTCharacteristicProperties.read)
    gatt_rw_perm = (GATTAttributePermissions.readable|GATTAttributePermissions.writeable)
    await server.add_new_characteristic(custom_service_uuid,
                                  characteristic_uuid,
                                  char_properties,
                                  b"a randomchar",
                                  gatt_rw_perm)

    await server.start()
    await asyncio.sleep(120)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))