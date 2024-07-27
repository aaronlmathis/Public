import asyncio
import ipaddress
import aioping

async def ping(ip):
    """Ping a given IP address."""
    try:
        await aioping.ping(ip, timeout=1)  # Ping with a 1-second timeout
        print(f"{ip} is online")
    except TimeoutError:
        pass

async def scan_subnet(subnet):
    """Scan a given subnet for active devices."""
    tasks = []
    for ip in ipaddress.ip_network(subnet).hosts():
        tasks.append(ping(str(ip)))
    await asyncio.gather(*tasks)

def main():
    # Replace with your subnet
    subnet = '192.168.0.0/24'
    print(f"Scanning subnet: {subnet}")
    asyncio.run(scan_subnet(subnet))

if __name__ == "__main__":
    main()
