import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

radio = adafruit_ble.BLERadio()

class iBeacon(Advertisement):
    match_prefixes = b"\x02\x15"
    manufacturer_data = adafruit_ble.AdvertisingPacketField(
        "manufacturer_data", 0, length=23
    )

# Replace these with your UUID, major, and minor values
uuid = b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10"
major = b"\x00\x01"
minor = b"\x00\x02"
power = b"\xC5"

beacon_advertisement = iBeacon()
beacon_advertisement.manufacturer_data = b"\x4C\x00" + uuid + major + minor + power

radio.start_advertising(beacon_advertisement, interval=1.0)

while True:
    pass
# Write your code here :-)
