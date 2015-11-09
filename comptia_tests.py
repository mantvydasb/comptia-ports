import random
__author__ = 'mantvydas'

PORTS = [
        ("FTP data", 20),
        ("FTP control", 21),
        ("SFTP", 22),
        ("SCP", 22),
        ("SSH", 22),
        ("Telnet", 23),
        ("SMTP", 25),
        ("TACACs+", 49),
        ("DNS name queries", "u53"),
        ("DNS zone transfers", "53"),
        ("TFTP", "u69"),
        ("HTTP", 80),
        ("Kerberos", "u88"),
        ("POP3", 110),
        ("SNMP (Simple network management protocol)", "u161"),
        ("SNMP trap (Simple network management protocol)", "u162"),
        ("NetBios", "137-139"),
        ("IMAP4", 143),
        ("LDAP", 389),
        ("HTTPS", 443),
        ("SMTP (SSL/TLS)", 465),
        ("IPSec", "u500"),
        ("LDAP (SSL/TLS)", 636),
        ("IMAP (SSL/TLS)", 993),
        ("POP (SSL/TLS)", 995),
        ("L2TP", "u1701"),
        ("PP2P", 1723),
        ("RDP", 3389),
        ("MS SQL", 1433),
    ]


def askNextPort(randomIndex):
    print(str(PORTS[randomIndex][0]) + " port?")


def capturePort():
    return input()


def getActualPort(randomIndex):
    return str(PORTS[randomIndex][1])


while True:
    randomIndex = random.randint(0, PORTS.__len__() - 1)
    askNextPort(randomIndex)
    portUser = capturePort()
    portActual = getActualPort(randomIndex)

    if portUser == portActual:
        print("Correct!")
    else:
        print("Incorrect! " + portActual)
    print()

