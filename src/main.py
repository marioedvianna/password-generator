import random
import string

def gerar_senha(num_caracteres):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_gerada = "".join(random.choice(caracteres) for i in range(num_caracteres))
    return senha_gerada

if __name__ == "__main__":
    try:
        num_caracteres = int(input("Digite o número de caracteres para a senha: "))
        nova_senha = gerar_senha(num_caracteres)
        print(f"Sua nova senha é: {nova_senha}")
        
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")