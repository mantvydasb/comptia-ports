import random
__author__ = 'mantvydas'

class Colours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

PROGRAMS = [
        # scanning
        ("Angry IP Scanner", "[scanning] similar to nmap"),
        ("SNScan", "[scanning] Scans network for devices with SNMP"),
        ("zenmap", "[scanning] nmap with UI"),
        ("NetScan Tools", "[scanning] multipurpose"),
        ("hping", "[scanning] packet crafter. Custom scans."),
        ("NBTScan", "[scanning, enumeration] NetBios scans"),
        ("Zanti", "[scanning] mobile security assesment"),
        ("p0f", "[fingerprinting] passive OS fingerprinting"),

        # enumeration
        ("DumpSec", "[enumeration] reveal users, groups, printers, etc"),
        ("SuperScan", "[enumeration] Windows Enumeration"),
        ("Netcat", "multipurpose, can do enumeration"),
        ("cryptcat", "netcat with encryption. Good for evading IDS"),
        ("showmount", "linux enum, show mounts"),
        ("finger", "linux enum, user info"),
        ("rpcinfo/rpcclient", "linux enum"),
        ("OpUtils 5", "SNMP enumeration"),
        ("IP Network Browser", "SNMP enumeration"),
        
        # passwords
        ("L0pthCrack", "[cracking] windows password cracking, auditing"),
        ("Ophcrack", "[cracking] windows password cracking, auditing"),
        ("Hydra", "[cracking] brute-forcing"),
        ("Medusa", "[cracking] brute-forcing"),
        ("Rainbow Crack", "[cracking] generates rainbow tables to be used in password cracking"),
        ("TRK (Trinity Rescue Kit)", "Passwor resets on local computer"),
        ("Brutus", "Old school brute force"),
        ("Cain & Abel", "Sniffing, password cracking, MAC spoofing"),
        ("ScoopLM", "password cracker, windows authentication traffic sniffer"),
        ("KerbCrack", "looks for kerberos traffic for password cracking"),
        ("Legion", "password cracking"),
        
        # sniffers
        ("Kismet (Wireless)", "Wireless sniffing and detection tool"),
        ("Ntop", "sniffer for unix"),
        ("Network Miner", "sniffer, forensically accepted"),
        ("EtherApe", "sniffer"),
        ("OmniPeek", "sniffer"),
        ("Etherflood", "MAC flooding"),
        ("Macof", "MAC flooding"),
        ("SMAC", "MAC spoofing"),
        ("Arpspoof", "Arp spoofing"),
        ("WINARPAttacker", "Arp spoofing"),
        ("Ufasoft", "Arp spoofing"),
        ("Dsniff", "Arp spoofing, sniffing"),
        ("ADMutate", "create scripts hard for IDS to understand"),
        ("NIDSBench", "fragmentation to bypass IDS"),
        ("PaketETH", "Packet generator"),
        ("Ferret & Hamster", "Sniffing, sidejacking attack, stealing cookies with sessions"),

        # wifi
        ("inSSIDer", "[wireless] network detection and location"),
        ("Reaver", "[wireless] WPS brute-force"),
        ("NetStumbler", "[wireless] Network detection and location, rogue device detection"),
        ("WaveStumbler", "[wireless] Network detection and location"),
        ("Bluesnarfer", "[wireless] A Bluetooth bluesnarfing Utility"),
        ("aircrack-ng", "[wireless] monitoring, replay, deauth attacks, fake APs, testing, cracking"),
        ("AirMagnet", "[wireless] wifi traffic analysis"),
        ("WifiPilot", "[wireless] wifi traffic sniffing/analysis"),
        ("CommView", "[wireless] wifi traffic analysis"),
        ("Bluepot", "[bluetooth] bluetooth honeypot"),
        ("Bluesniff", "[bluetooth] discovery"),
        ("BlueScanner", "[bluetooth] discovery"),
        ("Bt (bluetooth) Browser", "[bluetooth] discovery"),
        ("Bt Crawler", "[bluetooth] discovery"),
        ("Super Bluetooth", "[bluetooth] pentesting"),
        ("BlueBugger, BlueDiver", "[bluetooth] pentesting"),
        ("JiWire", "[wireless] traffic analysis"),
        ("OpenSignal", "[wireless] traffic analysis"),
        ("ChopChop", "WEP cracking"),
        ("SkyHook", "[wireless] traffic analysis"),
        ("Wigle", "[wireless] network detection, location"),
        ("WinDump", "[wireless] network sniffing, analysis"),
        ("Silica", "[wireless] network sniffing, vulnerabilities"),
        ("AirCheck", "[wireless] network sniffing, vulnerabilities"),

        # tunnelling
        ("AckCMD", "Ack tunnelling. Command prompt over ACK."),
        ("Loki", "ICMP tunneling. Exploiting covert channels"),
        ("007Shell", "tunneling, packet crafting"),
        ("NCovert", "tunneling, packet crafting"),

        # android
        ("DroidSQLi", "[mobile] Android automated sqli tool"),
        ("sqlmapchik", "[mobile] sqlmap GUI for mobile"),
        ("SQLite Editor", "[mobile] test sqli in web apps"),
        ("HTTP Injector", "[mobile] send modified http requests"),
        ("HTTP Tool", "send modified http requests"),
        ("Psiphon", "[mobile] VPN for tunnelling traffic"),
        ("Wifite", "[mobile] automated wireless cracking"),
        ("SuperOneClick", "root android"),
        ("Superboot", "root android"),
        ("AirMon", "[mobile] monitoring, sensing wifi"),
        ("WifiKill", "[mobile] scan network and terminate wireless hosts it discovers"),
        ("Kismet [android port]", "wifi scanning, detection, sniffing"),
        ("KisMAC", "wifi scanning, detection, sniffing, password cracking. Works on MAC."),
        ("dSploit Scripts", "[mobile] pentesting suite - map networks, fingerprint hosts, crack logons, sniffing, mitm, etc. Combined with zANTI"),
        ("zANTI", "[mobile] network diagnostics and pentests at the push of a button"),
        ("Hackode", "[mobile] pentesting suite on mobile"),
        ("AppScanner", "[mobile] application vulnerability scanner"),
        ("LanDroid", "[mobile] network info collection"),
        ("Network Handbook", "[mobile] network troubleshooting"),
        ("Fing", "[mobile] network security evaluation, host detection"),
        ("Mobile NM", "[mobile] nmap mobile port"),
        ("Shares Finder", "[mobile] a real app"),
        ("Packet Generator", "[mobile] a real app"),
        ("Packet Capture", "[mobile] a real app"),
        ("PacketShark", "[mobile] a real app"),
        ("Network Discovery", "[mobile] a real app"),
        ("PacketShark", "[mobile] a real app"),
        ("DroidSheep", "[mobile] session hijack. root required"),
        ("FaceNiff", "[mobile] session sniffing/hijack"),
        ("SSLstrip", "[mobile] session sniffing/hijack"),
        ("AnDOSid", "[mobile] real app"),
        ("Easy Packet Blaster", "[mobile] DOS, real app"),
        ("WPScan", "[mobile] WP vulnerability scanner"),
        ("CCTV Scanner", "[mobile] locate CCTV cameras"),
        ("NetCut", "[mobile] test security of firewalls"),
        ("UPNP Scanner", "[mobile] find plug'n'play devices on the network"),

        # hardware
        ("MiniPwner", "[hardware] sniffing wired/wireless, AP, wifi attacks"),
        ("USB RubberyDuck", "[hardware] runs script on the system when plugged (game over)"),
        ("Wifi pineapple", "[hardware] wifi honeypot, reconnaissance, MITM, tracking, logging, reporting"),
        ("LAN Turtle", "[hardware] sniffing, remote accessing"),
        ("AirPCAP", "[hardware] USB dongle for deep wifi packet sniffing/analysis"),
        ("UberTooth One", "[hardware] bluetooh detection and analysis"),
        ("PwnPad & PwnPhone", "[hardware] tablet/phone for pentesting"),
        ("KeyGrabber", "[hardware] usb keylogger"),
        
        # logs
        ("LogParserLizard", "Log analyser"),
        ("ALog reader", "Android Log analyser"),
        ("Syslog", "Logs for mobile also"),

        # SQLi
        ("SQLPing", "Finds databases on the newtork. Can crack passwords"),
        ("SQLReconn", "Finds databases on the newtork"),
        ("SQL Brute", "sql injection automation"),
        ("Pangolin", "sql injection automation"),
        ("Havij", "sql injection automation"),
        ("Absinthe", "sql injection automation"),
        ("Bobcat", "sql injection automation"),
        ("SQLninja", "sql injection automation"),


        # other
        ("Orbot", "Proxy from TOR project"),
        ("Orweb", "Browser working with Orbot"),
        ("EliteWrap", "A trojan packer"),
        ("Saran Wrap", "A trojan packer for BackOrifice"),
        ("Stealth Tool", "Allows hiding trojans"),
        ("Firekiller 2000", "A trojan packer"),
        ("Restorator", "A trojan packer"),
        ("Teflon Oil Patch", "A trojan packer"),
        ("Trojan Man", "A trojan packer"),
        ("Intellius", "People search utility"),
        ("ZabaSearch", "People search utility"),
        ("LexisNexis", "[reconn] competitive data search"),
        ("Spokeo", "[reconn] people search utility"),
        ("Wink", "[reconn] people search utility"),
        ("JXplorer", "LDAP searching"),
        ("PDQDeploy", "Deploy stuff, plant backdoors"),
        ("PhoneSweep from Niksun", "Wardialing"),
        ("THC-SCAN", "Wardialing"),
        ("ToneLoc", "Wardialing"),
        ("TeleSweep", "Wardialing"),
        ("WarVox", "Wardialing"),
        ("SFind", "NTFS Stream finder"),
        ("LNS", "NTFS Stream finder"),
        ("Tripwire", "File chande detector, NTFS Stream finder"),
        ("FakeGINA", "Keylogger"),
        ("Spector Pro", "Keylogger"),
        ("Ghost Keylogger", "Real app, keylogger"),
        ("IKS Software Keylogger", "Real app, keylogger"),
        ("WhoReadMe", "Tracks emails, provides OS info"),
        ("Firesheep", "session hijacking. Cookies inspection"),
        ("CANVAS", "Similar to metasploit"),
        ("Coret Impact", "Similar to metasploit, pentest automation"),
        ("PDQ deploy / dameware / remote exec", "Remote code execution, deployment"),
        ("WinZapper", "covering tracks"),
        ("Evidence Eliminator", "covering tracks"),
        ("elsave", "covering tracks"),
        
        # site rippers
        ("BlackWidow", "Site ripper"),
        ("HTTrack", "Site ripper"),
        ("WebRipper", "Site ripper"),
        ("Teleport Pro", "Site ripper"),
        ("GNU Wget", "Site ripper"),
        ("Backstreet Browser", "Site ripper"),
        
        # Trojan Creation Tools
        ("Let me rule", "[trojan creation]"),
        ("RECUB", "[trojan creation]"),
        ("Phatbot", "[trojan creation]"),
        ("Amitis", "[trojan creation]"),
        ("Zombam.B", "[trojan creation]"),
        ("Beast", "[trojan creation]"),
        ("Hard-disk killer", "[trojan creation]"),
        
        # cloud
        ("SOASTA Cloud Test", "[cloud] functional and performance testing"),
        ("Load Storm", "[cloud] web/mobile load testing"),
        ("BlazeMeter", "[cloud] load testing"),
        ("Nexpose", "[cloud] vulnerability scanning"),     
        ("AppThwack", "[cloud] simulator for testing android, ios, web apps on actual devices"),

        # bots & ddos
        ("BotPlug", "[DOS] Botnet creation"),
        ("Shark", "[DOS] Botnet creation"),
        ("PoisonIvy", "[DOS] Botnet creation"),
        ("LOIC", "[DDOS] Botnet creation. Anonymous group uses it."),
        ("Trinoo", "UDP DDOS, can target multiple IPs"),
        ("TNF2k (Tribe Network Flood)", "[DDOS] icmp/syn/udp/smurf attacks"),
        ("Stacheldraht", "[DDOS] icmp/syn/udp/smurf attacks"),
        ("Jolt2", "[DOS] , IP fragmentation attack"),
        ("DoSHTTP", "[DOS] Real app. Can target URL"),
        ("UDPFlood", "[DOS] Real app"),
        ("Targa", "[DOS] Many attacks in one: land, nuke, teardrop, etc"),
    ]


def askNext(randomIndex):
    print(Colours.OKGREEN + "\n\n" + str(PROGRAMS[randomIndex][0]) + Colours.ENDC)


def captureAnswer():
    return input()


def getRealAnswer(randomIndex):
    print(str(PROGRAMS[randomIndex][1]) + "\n\n\n----------------------------------------------------")


while True:
    randomIndex = random.randint(0, PROGRAMS.__len__() - 1)
    askNext(randomIndex)
    answer = captureAnswer()
    getRealAnswer(randomIndex)
