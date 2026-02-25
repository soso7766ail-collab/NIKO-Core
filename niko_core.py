# أضف هذا الجزء داخل كود نيكو الأساسي في مصفوفة المحركات

    # الجناح 11: الاتصال السحابي المطلق (Niko Cloud Bridge)
    def niko_cloud_bridge(self):
        print("\n[Niko]: جاري فحص جسر الاتصال بالسيرفر الخارجي...")
        
        # معلومات السيرفر (يتم ملؤها مرة واحدة)
        cloud_config = {
            "ip": "YOUR_SERVER_IP", # ضع هنا IP السيرفر الذي حصلت عليه
            "user": "ubuntu",
            "key_path": "~/.ssh/id_rsa"
        }

        print("[1] إنشاء نفق آمن (SSH Tunnel)...")
        print("[2] مزامنة قاعدة البيانات (Rsync Data)...")
        print("[3] تفعيل المعالجة البعيدة (Remote Execution)...")
        
        action = input("\n[Niko]: حدد نوع الارتباط السحابي: ")
        
        if action == "1":
            # فتح نفق لنقل البيانات صامتاً
            os.system(f"ssh -M -S niko-ctrl-socket -fnNT -D 1080 {cloud_config['user']}@{cloud_config['ip']}")
            print("[Niko]: النفق الآمن نشط الآن على المنفذ 1080.")
            
        elif action == "2":
            # مزامنة ملفات نيكو للسيرفر ليعمل هناك
            os.system(f"rsync -avz ./ {cloud_config['user']}@{cloud_config['ip']}:/home/ubuntu/niko_core")
            print("[Niko]: تمت المزامنة. نيكو الآن موجود في السحاب.")

        elif action == "3":
            # تنفيذ أمر على السيرفر وإرجاع النتيجة للهاتف
            cmd = input("[Niko]: أدخل الأمر لتنفيذه في السحاب: ")
            os.system(f"ssh {cloud_config['user']}@{cloud_config['ip']} '{cmd}'")

