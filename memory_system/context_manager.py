class ContextManager:
    def __init__(self):
        self.history = []

    def add_event(self, event):
        self.history.append(event)
        print(f"[Memory] Event recorded: {event}")

    def get_last_event(self):
        return self.history[-1] if self.history else None

if __name__ == "__main__":
    mem = ContextManager()
    mem.add_event("Niko system started successfully")
