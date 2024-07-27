import asyncio
import ipaddress

async def tcp_scan(ip, port):
    """Scan a given IP address and port using TCP."""
    conn = asyncio.open_connection(ip, port)
    try:
        reader, writer = await asyncio.wait_for(conn, timeout=1)
        writer.close()
        await writer.wait_closed()
        print(f"{ip} has port {port} open")
        return True
    except:
        return False

async def scan_subnet(subnet, port):
    """Scan a given subnet for active devices on a specific port."""
    tasks = []
    for ip in ipaddress.ip_network(subnet).hosts():
        tasks.append(tcp_scan(str(ip), port))
    await asyncio.gather(*tasks)

def main():
    # Replace with your subnet and port
    subnet = '192.168.0.0/24'
    port = 80  # Commonly open port (HTTP)
    print(f"Scanning subnet: {subnet} on port {port}")
    asyncio.run(scan_subnet(subnet, port))

if __name__ == "__main__":
    main()
