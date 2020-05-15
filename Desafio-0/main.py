import hashlib
import cryptography as c
import data_management as d


def main():
    data = d.get_data()
    d.save_data(data)
    decrypted = c.decrypt(data['cifrado'], data['numero_casas'])

    hashed = hashlib.sha1(decrypted.encode())

    data['decifrado'] = decrypted
    data['resumo_criptografico'] = hashed.hexdigest()

    d.save_data(data)
    d.post_file()


if __name__ == '__main__':
    main()
