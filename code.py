# Write your code here :-)
import board
import adafruit_ble
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.advertising.standard import SolicitServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_ble_eddystone import uid, url, tlm

radio = adafruit_ble.BLERadio()

# Set up Eddystone-URL
eddystone_url = url.EddystoneURL('https://www.example.com')
radio.start_advertising(eddystone_url)

# Advertise indefinitely
while True:
    pass
