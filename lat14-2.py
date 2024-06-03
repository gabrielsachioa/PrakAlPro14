import re
import string
import random

def generate_random_password():
    length = random.randint(8, 8)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    txt = "Berikut adalah daftar email dan nama pengguna dari mailing list: anton@mail.com dimiliki oleh antonius budi@gmail.co.id dimiliki oleh budi anwari slamet@getnada.com dimiliki oleh slamet slumut matahari@tokopedia.com dimiliki oleh toko matahari"

    email_pattern = re.findall("[a-zA-Z0-9]+@[a-zA-Z]+\.[\w.-]+", txt)


    for i in email_pattern:
        user = i.split("@")[0]
        print(f"{i} username: {user}, password: {generate_random_password()}")

# PROGRAM UTAMA
main()