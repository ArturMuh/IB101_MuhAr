def encrypt_caesar(msg: str, shift: int = 3) -> str:
    temp = ''
    for char in msg:
        if 'А' <= char <= 'Я':
            new_char = chr(ord('А') + (ord(char) - ord('А') + shift) % 32)
            temp += new_char
        elif 'а' <= char <= 'я':
            new_char = chr(ord('а') + (ord(char) - ord('а') + shift) % 32)
            temp += new_char
        else:
            temp += char
    return temp

def decrypt_caesar(encrypted: str, shift: int = 3) -> str:
    return encrypt_caesar(encrypted, -shift)

msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)