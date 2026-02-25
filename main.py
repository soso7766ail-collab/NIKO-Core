import os, sys, time, subprocess
import google.generativeai as genai
from openai import OpenAI

class NikoUltimate:
    def __init__(self):
        self.version = "40.0 [FINAL]"
        self.master = "بشير"
        self.key = "Fox776696"
        
        # --- الترسانة المفعلة بمفاتيحك ---
        self.gemini_key = "AIzaSyBbV0VAulRrV_vLYPu9yKcWBbaTcWVEbEY"
        self.openai_key = "Sk-proj-iBUATBNX2F1V_MXXBVxhCUEJmoGF1CdaFcYbS0ewqcx6Y6Y2BvPS76JOOFYCOa1nd5EaJhVoOFT3BlbkFJiH1S0_KJAY_p9J20BYmY9YSr6dKom9_2SXW0ghuJfO6_oG2IB6OZ-foUoiUgbAkf0obpddL1QA"

        # تشغيل العقول الذكية
        try:
            genai.configure(api_key=self.gemini_key)
            self.gemini = genai.GenerativeModel('gemini-pro')
            self.openai = OpenAI(api_key=self.openai_key)
            self.ai_active = True
        except Exception as e:
            print(f"تنبيه: فشل ربط العقول. السبب: {e}")
            self.ai_active = False

    def execute_sys(self, cmd):
        """تنفيذ أوامر النظام تلقائياً"""
        try:
            return subprocess.getoutput(cmd)
        except:
            return "فشل تنفيذ الأمر."

    def ask(self, prompt, brain="gemini"):
        """استشارة الذكاء الاصطناعي"""
        try:
            if brain == "openai":
                res = self.openai.chat.completions.create(model="gpt-4", messages=[{"role":"user","content":prompt}])
                return res.choices[0].message.content
            return self.gemini.generate_content(prompt).text
        except:
            return "عذراً سيدي، واجهت مشكلة في الاتصال بعقلي السحابي."

def start():
    niko = NikoUltimate()
    os.system("clear")
    print("💎" * 15)
    print(f"   NIKO v{niko.version} | MASTER: {niko.master}")
    print("   STATUS: READY & ARMED ✅")
    print("💎" * 15)

    if input(f"مرحباً يا سيدي {niko.master}. أدخل رمز السيادة: ") != niko.key:
        print("الرمز خاطئ. إغلاق النظام.")
        return

    os.system("termux-tts-speak 'النظام جاهز للخدمة'")

    while True:
        cmd = input(f"\n{niko.master}@Niko_Core >> ").lower()

        if cmd == "exit": 
            break
        
        elif cmd.startswith("ask "): # ذكاء Gemini
            print("\n[Niko (Gemini)]: " + niko.ask(cmd.replace("ask ", "")))

        elif cmd.startswith("deep "): # ذكاء OpenAI للبرمجة
            print("\n[Niko (GPT-4)]: " + niko.ask(cmd.replace("deep ", ""), "openai"))

        elif cmd == "fix": # إصلاح الأخطاء التي ظهرت في الصور
            print("[+] جاري إصلاح المستودعات وتثبيت الأدوات...")
            os.system("pkg update -y && pkg install root-repo -y && pkg install nmap sqlmap -y")
            print("[+] تم الإصلاح بنجاح.")

        elif cmd == "status":
            print(f"العقول: نشطة ✅\nالمالك: {niko.master}\nالاصدار: {niko.version}")

        elif cmd == "clear": 
            os.system("clear")

if __name__ == "__main__":
    start()

