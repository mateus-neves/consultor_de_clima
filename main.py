from clima import ConsultorClima


def main():
    consultor = ConsultorClima()

    print("🌤️  CONSULTOR DEe CLIMA AVANÇADO")
    print("=" * 40)

    # Verifica se a API key está configurada
    if not consultor.api_key or consultor.api_key == 'sua_chave_aqui':
        print("❌ ERRO: API Key não configurada!")
        print("👉 Obtenha uma chave gratuita em: https://openweathermap.org/api")
        print("👉 Configure no arquivo config.py")
        return

    while True:
        print("\n📋 Opções:")
        print("1 - Consultar clima por cidade")
        print("2 - Ver histórico de consultas")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção (1-3): ").strip()

        if opcao == '1':
            cidade = input("\n🏙️  Digite o nome da cidade: ").strip()

            if cidade:
                print(f"\n🔍 Buscando clima para '{cidade}'...")
                dados = consultor.buscar_clima(cidade)

                if dados:
                    dados_formatados = consultor.formatar_dados(dados)
                    if dados_formatados:
                        consultor.exibir_clima(dados_formatados)
                    else:
                        print("❌ Não foi possível formatar os dados recebidos.")
                else:
                    print("❌ Cidade não encontrada ou erro na consulta.")
            else:
                print("❌ Por favor, digite o nome de uma cidade.")

        elif opcao == '2':
            consultor.exibir_historico()

        elif opcao == '3':
            print("\n👋 Obrigado por usar o Consultor de Clima! Até logo! 🌈")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
