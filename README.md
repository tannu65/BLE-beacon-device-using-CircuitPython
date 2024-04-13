# BLE-beacon-device-using-CircuitPython

## Overview

A BLE (Bluetooth Low Energy) beacon is a device that uses Bluetooth technology to transmit small data packets within short distances periodically. These packets, known as 'advertising packets,' are detectable by nearby Bluetooth-enabled devices like smartphones, tablets, or dedicated receivers.

## Key Features

- **Low Energy Consumption:** BLE beacons are engineered for minimal power usage, enabling long-term operation on small batteries, such as coin cells.

- **Simple Data Broadcast:** Beacons broadcast unique identifiers and, optionally, data like URLs, sensor readings, or telemetry. These broadcasts support a variety of applications:
  - **Indoor navigation**
  - **Proximity marketing**
  - **Asset tracking**
  - **Contextual notifications**

- **Broadcast Protocols:**
  - **iBeacon:** Introduced by Apple, utilizes a UUID (universally unique identifier) along with Major and Minor values for additional context.
  - **Eddystone:** Developed by Google, capable of transmitting URLs, UID data, or telemetry (TLM).

## Use Cases

- **Retail:** Enhance shopping experiences with personalized promotions and navigational aids.
- **Museums and Parks:** Offer informational or audio tours triggered by location.
- **Healthcare:** Improve patient tracking and asset management through wayfinding solutions.
- **Smart Homes and Offices:** Automate and streamline environment interactions without manual inputs.

## Advantages

- **No Pairing Required:** Beacons transmit data detectable by any equipped device without needing a paired connection.

BLE beacons are essential in IoT (Internet of Things), praised for their simplicity, effectiveness, and the ubiquity of Bluetooth technology.

## Project Setup

This project involves developing firmware for a BLE beacon device using CircuitPython. Below are the initial steps to get started:

### Step 1: CircuitPython Environment Setup

- **Install CircuitPython:** Load CircuitPython onto a BLE-supporting board like the Adafruit Feather nRF52840. [CircuitPython Downloads](https://circuitpython.org/downloads)
- **Install Libraries:** Ensure `adafruit_ble` is installed. Available in the [Adafruit CircuitPython Library Bundle](https://circuitpython.org/libraries).

### Step 2: Eddystone Example

This section includes an example on broadcasting an Eddystone URL. The complete code is attached in the GitHub repository.

### Step 3: iBeacon Setup

For iBeacon functionality, you'll need to define UUID, Major, and Minor values. The setup details and code for this are also provided in the repository.
