import base64

class SecurityShield:
    def __init__(self):
        self.key = "NIKO_CORE_SECURE_KEY" # مفتاح افتراضي

    def encrypt_data(self, raw_text):
        # تشفير بسيط باستخدام Base64 (كمرحلة أولى)
        encoded_bytes = base64.b64encode(raw_text.encode("utf-8"))
        return encoded_bytes.decode("utf-8")

    def decrypt_data(self, encrypted_text):
        decoded_bytes = base64.b64decode(encrypted_text.encode("utf-8"))
        return decoded_bytes.decode("utf-8")

if __name__ == "__main__":
    shield = SecurityShield()
    test = shield.encrypt_data("System Startup Successful")
    print(f"[Security] Encrypted Test: {test}")
    print(f"[Security] Decrypted Test: {shield.decrypt_data(test)}")
