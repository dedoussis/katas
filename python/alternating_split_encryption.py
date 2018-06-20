def decrypt(encrypted_text, n):
    if not encrypted_text or n < 1:
        return encrypted_text
    split = len(encrypted_text)//2
    str1, str2, text = encrypted_text[:split], encrypted_text[split:], ''
    for idx in range(len(str1)):
        text += str2[idx] + str1[idx]
    text += str2[len(str1):]
    return decrypt(text, n-1)

def encrypt(text, n):
    if not text or n < 1:
        return text
    return encrypt(text[1::2] + text[0::2], n-1)
