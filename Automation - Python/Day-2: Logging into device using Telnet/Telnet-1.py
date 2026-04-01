import telnetlib
import getpass

switch_ip = '192.168.99.30'

print(f"Logging into {switch_ip}")

username = input("Enter your username: ")
Password = getpass.getpass()

tn = telnetlib.Telnet(switch_ip)

tn.read_until(b"login:")
tn.write(username.encode('ascii') + b'\n')>
tn.read_until(b"Password:")
tn.write(Password.encode('ascii') + b'\n')
tn.write (b'show version\n')
tn.write(b'exit\n')

print(tn.read_all().decode('ascii'))

