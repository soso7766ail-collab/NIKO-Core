import subprocess

class ExplorerAgent:
    def __init__(self):
        self.name = "Seeker"

    def check_battery(self):
        try:
            # محاولة قراءة حالة البطارية من نظام الأندرويد
            result = subprocess.check_output("termux-battery-status", shell=True)
            return f"Battery Report: {result.decode('utf-8')}"
        except:
            return "Error: Termux-API not installed. Please run 'pkg install termux-api'."

    def get_storage_info(self):
        # فحص المساحة المتوفرة
        df = subprocess.check_output("df -h /data", shell=True)
        return f"Storage Report:\n{df.decode('utf-8')}"

if __name__ == "__main__":
    seeker = ExplorerAgent()
    print(seeker.check_battery())
