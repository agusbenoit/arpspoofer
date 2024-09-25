# ARPSpoofer

**ARPSpoofer** is a simple ARP Spoofing tool built using Python and Scapy. It allows you to perform ARP spoofing attacks on your local network by either running in reconnaissance mode to gather MAC addresses or in attack mode to carry out the ARP poisoning.

## Features
- Reconnaissance mode to capture ARP requests and responses on the network.
- Attack mode to perform ARP spoofing between a target device and the network gateway.
- Continuous ARP poisoning with customizable intervals.
- Works on Linux and requires root privileges.

## Requirements
- Python 3
- Scapy
- Root privileges (run the tool with `sudo`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/agusbenoit/arpspoofer.git
    ```

2. Navigate to the arpspoofer directory:
   ```bash
   cd arpspoofer
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Important Note: Promiscuous Mode

For ARPSpoofer to work effectively, your network interface card (NIC) needs to be in promiscuous mode. This allows your machine to capture all traffic on the network, not just the packets addressed to it.

### How to Enable Promiscuous Mode

#### Linux
You can enable promiscuous mode using the following command:
```bash
sudo ifconfig <interface> promisc
```
Replace `<interface>` with your actual network interface name (e.g., `eth0`, `wlan0`)

### VirtualBox Users

If you are running ARPSpoofer on a virtual machine, make sure to set the network adapter to **Bridged Adapter** mode and enable **Promiscuous Mode: Allow All** in the network settings of your virtual machine.

## Usage

### Reconnaissance Mode

Run ARPSpoofer in reconnaissance mode to capture ARP requests on your network and discover IP and MAC addresses of devices:
   ```bash
   sudo python3 arpspoofer.py -r
   ```

### Attack Mode

Run ARPSpoofer in attack mode to perform ARP spoofing between a target device and the network gateway:
   ```bash
   sudo python3 arpspoofer.py -a <victim_ip> <victim_mac> <gateway_ip>  <gateway_mac>

   ```
**Example:**
   ```bash
   sudo python3 arpspoofer.py -a 192.168.1.5 aa:bb:cc:dd:ee:ff 192.168.1.1 11:22:33:44:55:66
   ```

### Options
- `-r`, `--reconisance`: Start in reconnaissance mode.
- `-a`, `--attack`: Start in attack mode and requires 4 parameters: `<victim_ip> <victim_mac> <gateway_ip> <gateway_mac>`.

## Disclaimer
> **Warning:** This tool is intended for educational purposes only. Use it only on networks that you own or have explicit permission to test. Unauthorized use on networks that you do not own is illegal and can have serious consequences. The author is not responsible for any misuse of this tool.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
