import datetime

class ReasoningEngine:
    def __init__(self):
        self.identity = "Niko v4.0"
        self.creator = "Master"
        self.boot_time = datetime.datetime.now()

    def analyze(self, user_text):
        user_text = user_text.lower().strip()
        
        # 1. تحليل النوايا البرمجية (Coding Intent)
        if any(word in user_text for word in ["برمج", "كود", "تطبيق", "create"]):
            return "REQUEST_CODE_GEN"
        
        # 2. تحليل الأسئلة عن الهوية (Identity)
        elif "من انت" in user_text or "identity" in user_text:
            return f"أنا {self.identity}. نظام ذكاء اصطناعي متطور ذاتياً، صممت لأكون يدك اليمنى في البرمجة وحماية الأنظمة."

        # 3. تحليل الأسئلة عن الحالة (System Status)
        elif "حالتك" in user_text or "status" in user_text:
            uptime = datetime.datetime.now() - self.boot_time
            return f"أنظمتي تعمل بكفاءة عالية. وقت التشغيل: {str(uptime).split('.')[0]}. هل هناك ملفات تريد تشفيرها؟"

        # 4. تحليل طلبات المساعدة (Help)
        elif "ماذا تفعل" in user_text or "help" in user_text:
            return "أستطيع التقاط الصور (snap)، فحص البطارية (battery)، تشفير النصوص (secure)، وتنفيذ أكواد بايثون (run code)."

        # 5. الرد الافتراضي الذكي
        else:
            return "فهمت ما تقوله.. هل تريد مني تحويل هذا الكلام إلى أمر تنفيذي، أم أضيفه لقاعدة بيانات التعلم الخاصة بي؟"

