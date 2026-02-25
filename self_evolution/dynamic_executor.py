import subprocess

class CodeExecutor:
    def __init__(self):
        self.temp_file = "self_evolution/temp_run.py"

    def execute_custom_code(self, code_string):
        # كتابة الكود في ملف مؤقت لتشغيله
        with open(self.temp_file, "w") as f:
            f.write(code_string)
        
        try:
            # تشغيل الكود وجلب النتيجة
            result = subprocess.check_output(f"python {self.temp_file}", shell=True, stderr=subprocess.STDOUT)
            return f"[Success] Output: {result.decode()}"
        except Exception as e:
            return f"[Error] Niko failed to run code: {e}"

if __name__ == "__main__":
    exec_tool = CodeExecutor()
    print(exec_tool.execute_custom_code("print('Niko is learning to code!')"))
