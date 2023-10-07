from bless import (
        BlessServer,
        BlessGATTCharacteristic,
        GATTCharacteristicProperties,
        GATTAttributePermissions
)

def my_read_callback(uuid):
    pass

def main():
    service_name = "Basic GATT server: hwh_"
    server = BlessServer(service_name)
    server.read_request = my_read_callback

    custom_service_uuid = ""
    server.add_new_service(custom_service_uuid)

    characteristic_uuid = ""

    server.start()

if __name__ == "__main__":
    main()