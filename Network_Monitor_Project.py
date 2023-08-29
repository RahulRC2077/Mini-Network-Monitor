import psutil
import netifaces

def get_network_info():
    interfaces = netifaces.interfaces()
    info = {}
    for interface in interfaces:
        if interface != 'lo':
            addrs = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addrs:
                ip = addrs[netifaces.AF_INET][0]['addr']
                info[interface] = ip
    return info

def get_network_stats():
    stats = psutil.net_io_counters()
    return stats

def main():
    network_info = get_network_info()
    network_stats = get_network_stats()

    # Display network information
    print("Network Information:")
    for interface, ip in network_info.items():
        print(f"Interface: {interface} | IP: {ip}")

    # Display network statistics for each interface
    print("\nNetwork Statistics:")
    for interface in network_info.keys():
        stats = psutil.net_io_counters(pernic=True).get(interface)
        if stats is not None:
            print(f"Interface: {interface}")
            print(f"Bytes Sent: {stats.bytes_sent}")
            print(f"Bytes Received: {stats.bytes_recv}")
            print(f"Packets Sent: {stats.packets_sent}")
            print(f"Packets Received: {stats.packets_recv}")
            print("-" * 20)

if __name__ == '__main__':
    main()

