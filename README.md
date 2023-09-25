# NetworkScanner
A user-friendly Python script powered by Scapy for scanning and exploring networks effortlessly.

# Features
* Discover devices on a network by sending ARP requests
* Save captured packets to a pcap file for further analysis

## Installation
```
# if you have python3
# pip3 install scapy

git clone https://github.com/ozXsasson/NetworkScanner
cd NetworkScanner
```

## Usage
```
Usage: networkScanner.py [options]

Options:
  -h, --help            show this help message and exit
  -i TARGET, --target TARGET
                        Target IP / IP range
      
```

## Example
```
sudo python3 networkScanner.py --target IP_ADDRESS.1/24
