import getpass
import telnetlib

HOST = "192.168.20.70"
user = input("Enter your Telnet username: ")
password = getpass.getpass()
enable_password = getpass.getpass("Enable password: ")

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(enable_password.encode('ascii') + b"\n")
tn.write(b"configure terminal\n")

tn.write(b"interface loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"exit\n")

tn.write(b"interface loopback 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"exit\n")

tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
