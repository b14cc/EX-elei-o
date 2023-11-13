import random

class Candidato:
    def __init__(self, nome):
        self.nome = nome
        self.votos = 0

candidatos = [
    Candidato("MOBA"),
    Candidato("FPS"),
    Candidato("TPS"),
    Candidato("Survival"),
    Candidato("Construção"),
    Candidato("Tycoon"),
]

def exibir_opcoes():
    print("Escolha o candidato digitando o numero correspondente:")
    for i, candidato in enumerate(candidatos, start=1):
        print(f"{i}. {candidato.nome}")

def realizar_votacao():
    while True:
        exibir_opcoes()
        try:
            print("Votação para saber qual estilo de jogo preferido das pessoas")
            voto = int(input("Digite o numero do candidato (ou 0 para encerrar): "))
            if 0 <= voto <= len(candidatos):
                if voto == 0:
                    break
                candidatos[voto - 1].votos += 1
                print(f"Voce votou em {candidatos[voto - 1].nome}.")
            else:
                print("Opcao invalida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um numero valido.")

def exibir_resultados():
    print("\nResultados da eleicao:")
    for candidato in candidatos:
        print(f"{candidato.nome}: {candidato.votos} votos")

    vencedor = max(candidatos, key=lambda x: x.votos)
    print(f"\nO vencedor é {vencedor.nome} com {vencedor.votos} votos!")

if __name__ == "__main__":
    print("Bem-vindo a eleicao dos jogos!!")
    realizar_votacao()
    exibir_resultados()
