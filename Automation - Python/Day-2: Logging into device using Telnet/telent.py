import telnetlib

HOST = "192.168.99.30"

print(f"Connecting to Switch-1 at {HOST} via Telnet...")

tn = telnetlib.Telnet(HOST)
tn.read_until(b'login:')
tn.write(b"admin\n")

tn.read_until(b"Password: ")
tn.write(b"Admin@eve\n")

tn.write(b"show version\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))