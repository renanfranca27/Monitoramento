import os
import requests
import time
import argparse

class Conectividade:
    def __init__(self, servidor, url_internet):
        self.servidor = servidor
        self.url_internet = url_internet

    def verificar_servidor(self):
        response = os.system("ping -c 1 " + self.servidor)
        if response == 0:
            print(f"Servidor {self.servidor} está ativo.")
        else:
            print(f"Servidor {self.servidor} está inativo.")

    def verificar_internet(self):
        try:
            requests.get(self.url_internet, timeout=3)
            print("Conectado à internet.")
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("Sem conexão com a internet.")

def parse_args():
    parser = argparse.ArgumentParser(description='Verifique a conectividade com um servidor e a internet.')
    parser.add_argument('--servidor', type=str, required=True, help='Endereço IP ou hostname do servidor.')
    parser.add_argument('--url', type=str, required=True, help='URL para verificar a conectividade com a internet.')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    conectividade = Conectividade(args.servidor, args.url)
    while True:
        conectividade.verificar_servidor()
        conectividade.verificar_internet()
        time.sleep(60)  # Aguarda 60 segundos antes de verificar novamente
