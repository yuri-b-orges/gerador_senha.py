import random
import string

def gerar_senha(comprimento=8):
    # Define os caracteres possíveis para a senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Gera a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas!")
    comprimento = int(input("Quantos caracteres você quer na senha? "))
    senha = gerar_senha(comprimento)
    print(f"Sua senha gerada é: {senha}")

if __name__ == "__main__":
    main()