from clima import ConsultorClima

def main():
    consultor = ConsultorClima()
    print("🌤️  CONSULTOR DE CLIMA")
    print("="*30)

    while True:
        print("\nOpçoes:")
        print("1. Buscar clima por cidade")
        print("2. Sair")

        opçao = input("\nEscolha uma opçao (1 ou 2): ").strip()

        if opçao == '1':
            cidade = input("\nDijite o nome da cidede: ").strip()

            if cidade:
                print(f"\nBuscando clima para {cidade}...")
                dados = consultor.buscar_clima(cidade)

                if dados:
                    dados_formatados = consultor.formatar_dados(dados)
                    consultor.exibir_clima(dados_formatados)
                else:
                    print("cidade nao encontrado ou erro na consulta.")

            else:
                print("Por favor, dijite um nome de cidade")

        elif opçao == '2':
            print("obrigado por usar o Consultor de Clima. Ate logo!")
            break
        else:
            print("Opçao invalida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
    