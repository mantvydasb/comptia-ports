import random
__author__ = 'mantvydas13'

PORTS = [
        ("FTP data", 20),
        ("FTP control", 21),
        ("SFTP", 22),
        ("SCP", 22),
        ("SSH", 22),
        ("Telnet", 23),
        ("SMTP", 25),
        ("WINS", 42),
        # ("TACACs+", 49),
        ("DNS name queries", "u53"),
        ("DNS zone transfers", "53"),
        # ("TFTP", "u69"),
        ("HTTP", 80),
        ("Kerberos", "u88"),
        ("POP3", 110),
        ("Portmapper", 111),
        ("NTP (network time protocol)", 123),
        ("RPC-DCOM", 135),
        ("SNMP (Simple network management protocol)", "u161"),
        ("SNMP trap (Simple network management protocol)", "u162"),
        ("NetBios", "137-139"),
        ("IMAP4", 143),
        ("LDAP", 389),
        ("HTTPS", 443),
        ("CIFS", 445),
        # ("SMTP (SSL/TLS)", 465),
        # ("IPSec", "u500"),
        ("Syslog", 514),
        ("LDAP (SSL/TLS)", 636),
        # ("IMAP (SSL/TLS)", 993),
        # ("POP (SSL/TLS)", 995),
        ("Socks5", 1080),
        ("Nessus Server", 1241),
        # ("L2TP", "u1701"),
        ("MS SQL", 1433),
        ("Citrix management", 1494, 2598),
        ("Oracle listener", 1521),
        ("PP2P", 1723),
        ("Global catalog service", 3268),
        ("RDP", 3389),
        ("IRC", "6662-6667"),
    ]


def askForNextPort(randomIndex):
    print(str(PORTS[randomIndex][0]) + " port?")


def captureAnswer():
    return input()


def getActualPort(randomIndex):
    return str(PORTS[randomIndex][1])


while True:
    randomIndex = random.randint(0, PORTS.__len__() - 1)
    askForNextPort(randomIndex)
    answer = captureAnswer()
    portActual = getActualPort(randomIndex)

    if answer == portActual:
        print("Correct!")
    else:
        print("Incorrect! " + portActual)
    print()
