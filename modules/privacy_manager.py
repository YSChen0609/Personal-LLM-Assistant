import re

class PrivacyManager:
    def __init__(self):
        self.private_patterns = [
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email
            r'\b(?:\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b',  # Phone
            r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
            r'\b(?:\d{4}[-\s]?){3}\d{4}\b'  # Credit Card
        ]

    def is_private_info(self, text):
        for pattern in self.private_patterns:
            if re.search(pattern, text):
                return True
        return False

