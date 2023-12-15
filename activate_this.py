import random


def generate_chastokol_key():
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    key = list(alphabet)
    random.shuffle(key)
    return dict(zip(alphabet, key))


def chastokol_encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            encrypted_text += key[char]
        else:
            encrypted_text += char
    return encrypted_text


def chastokol_decrypt(ciphertext, key):
    reversed_key = {v: k for k, v in key.items()}
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted_text += reversed_key[char]
        else:
            decrypted_text += char
    return decrypted_text


def main():
    user_input = input("Введіть слово для шифрування: ")


    if not all(
            char.isalpha() and char.islower() and char in "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя" for char in user_input):
        print("Будь ласка, переключіть мову на українську.")
        return

    key = generate_chastokol_key()

    encrypted_text = chastokol_encrypt(user_input, key)

    print(f"Ваше слово: {user_input}")
    print(f"Зашифроване слово: {encrypted_text}")


if __name__ == "__main__":
    main()
