def main():
    while True:
        print("Bem-vindo ao simulador de corrida Mahindra Formula E!")
        print("Vamos determinar as melhores configurações para sua corrida.")
        print("-----------------------------------------")

        # Lista de pilotos da equipe Mahindra atualizada.
        pilotos = ["Edoardo Mortara", "Nyck de Vries"]
        # Lista de tipos de pneus.
        pneus = ["Seco", "Molhado", "Intermediário"]
        # Lista de condições climáticas.
        clima = ["Ensolarado", "Chuvoso", "Nublado"]

        # Perguntas que serão feitas ao usuário.
        questoes = [
            "Qual é a previsão do tempo para a corrida (ensolarado/chuvoso/nublado)? ",
            "Qual piloto você deseja que corra (Edoardo Mortara/Nyck de Vries)? "
        ]

        # Respostas esperadas para cada configuração.
        resps_clima = {
            "ensolarado": "Seco",
            "chuvoso": "Molhado",
            "nublado": "Intermediário"
        }

        # Dicionário para armazenar as escolhas do usuário.
        escolhas_usuario = {}

        # Loop para fazer as perguntas e coletar as respostas.
        for i, questao in enumerate(questoes):
            while True:
                resp = input(questao).lower()
                if i == 0:  # Verifica se é a primeira pergunta sobre o clima
                    if resp in [c.lower() for c in clima]:
                        escolhas_usuario["pneu"] = resps_clima[resp]
                        break
                    else:
                        print("Resposta inválida. Por favor, escolha entre ensolarado, chuvoso ou nublado.")
                elif i == 1:  # Verifica se é a segunda pergunta sobre o piloto
                    if resp in [p.lower() for p in pilotos]:
                        escolhas_usuario["piloto"] = resp.title()  # Converte a resposta para começar com letra maiúscula
                        break
                    else:
                        print(f"Resposta inválida. Por favor, escolha entre {', '.join(pilotos)}.")

        # Verifica se todas as configurações foram coletadas.
        if "pneu" in escolhas_usuario and "piloto" in escolhas_usuario:
            # Mostra o resultado para o usuário.
            print("-----------------------------------------")
            print(f"Para um dia {resp}, o melhor pneu é {escolhas_usuario['pneu']} e o piloto escolhido é {escolhas_usuario['piloto']}.")
        else:
            print("Não foi possível determinar as configurações da corrida.")

        # Pergunta se o usuário quer continuar.
        cont = input("Deseja configurar outra corrida? Digite 'sim' para continuar ou 'não' para concluir: ").lower()
        
        if cont == "não":
            break

main()