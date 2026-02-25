class Sandbox:
    def __init__(self):
        self.is_isolated = True

    def safe_run(self, code_snippet):
        print(f"[Sandbox] Testing code snippet safety...")
        try:
            # هنا نضع منطق الفحص الأمني مستقبلاً
            return True
        except Exception as e:
            print(f"[Sandbox] Warning: Unsafe code detected! Error: {e}")
            return False

if __name__ == "__main__":
    sb = Sandbox()
    sb.safe_run("print('Hello World')")
