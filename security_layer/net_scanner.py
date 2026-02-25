import scapy.all as scapy

class NetScanner:
    def __init__(self):
        # النطاق الافتراضي للشبكة (يمكن تغييره حسب راوترك)
        self.target_ip = "192.168.1.1/24"

    def scan(self):
        print(f"\n[Niko] Scanning network for devices...")
        # إنشاء حزمة ARP لمعرفة الأجهزة المتصلة
        arp_request = scapy.ARP(pdst=self.target_ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        
        # إرسال واستقبال النتائج بمهلة ثانية واحدة
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        
        clients = []
        for element in answered_list:
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            clients.append(client_dict)
        return clients
