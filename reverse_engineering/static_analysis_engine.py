import os

class StaticAnalyzer:
    def __init__(self):
        self.target_dir = "."

    def scan_project_structure(self):
        print(f"[Analyzer] Scanning directory: {os.path.abspath(self.target_dir)}")
        report = []
        for root, dirs, files in os.walk(self.target_dir):
            level = root.replace(self.target_dir, '').count(os.sep)
            indent = ' ' * 4 * (level)
            report.append(f"{indent}[{os.path.basename(root)}/]")
            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                report.append(f"{sub_indent}- {f}")
        return "\n".join(report)

    def get_file_stats(self):
        py_files = [f for f in os.listdir('.') if f.endswith('.py')]
        return f"Found {len(py_files)} Python files in root."

if __name__ == "__main__":
    analyzer = StaticAnalyzer()
    print(analyzer.scan_project_structure())
    print(analyzer.get_stats())
