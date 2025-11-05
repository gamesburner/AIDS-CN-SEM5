import socket

print("======DNS Lookup Program =====")

# Ask user for input
choice = input("Enter 1 for Domain to IP lookup or 2 for IP to Domain lookup: ")

if choice == '1':
    # Domain to IP lookup
    domain = input("Enter Domain Name: ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP address of {domain} is: {ip}")
    except socket.gaierror:
        print("Invalid domain name or unable to resolve DNS.")

elif choice == '2':
    # IP to Domain lookup
    ip = input("Enter IP Address: ")
    try:
        domain = socket.gethostbyaddr(ip)
        print(f"Domain name for IP {ip} is: {domain[0]}")
    except socket.herror:
        print("Unable to resolve domain for the given IP")

else:
    print("Invalid choice! Please enter 1 or 2.")