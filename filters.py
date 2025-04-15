import re

SPAM_KEYWORDS = ["obuna bo‘ling", "reklama", "follow", "subscribe"]
SPAM_LINK_PATTERNS = [r"https?://", r"t\.me/"]

def is_spam(text):
    lower_text = text.lower()
    for keyword in SPAM_KEYWORDS:
        if keyword in lower_text:
            return True
    for pattern in SPAM_LINK_PATTERNS:
        if re.search(pattern, lower_text):
            return True
    return False
