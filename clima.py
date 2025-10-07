import requests
from config import BASE_URL, API_KEY


class ConsultorClima:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL

    def buscar_clima(self, cidade):
        """Busca informações climáticas para uma cidade"""
        params = {
            'q': cidade,
            'appid': self.api_key,
            'units': 'metric',  # Para temperatura em Celsius
            'lang': 'pt_br'     # Para descrições em português
        }

        try:
            response = requests.get(self.base_url, params=params)

            # Debug: veja a resposta da API
            print(f"Status Code: {response.status_code}")
            print(f"Resposta: {response.text[:200]}...")

            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                print("❌ Erro de autenticação. Verifique sua API Key.")
            elif response.status_code == 404:
                print("❌ Cidade não encontrada.")
            else:
                print(f"❌ Erro HTTP: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro na requisição: {e}")
            return None

    def formatar_dados(self, dados):
        """Formata os dados climáticos para exibição com verificações de segurança"""
        if not dados:
            print("❌ Nenhum dado recebido da API")
            return None

        # Verifica se a API retornou um erro
        if 'cod' in dados and dados['cod'] != 200:
            print(
                f"❌ Erro da API: {dados.get('message', 'Erro desconhecido')}")
            return None

        # Verifica se todas as chaves necessárias existem
        try:
            temperatura = dados['main']['temp']
            sensacao = dados['main']['feels_like']
            humidade = dados['main']['humidity']
            descricao = dados['weather'][0]['description'].title()
            cidade = dados['name']
            pais = dados['sys']['country']

            return {
                'cidade': cidade,
                'pais': pais,
                'temperatura': temperatura,
                'sensacao': sensacao,
                'humidade': humidade,
                'descricao': descricao
            }

        except KeyError as e:
            print(f"❌ Chave não encontrada nos dados: {e}")
            print(f"📊 Dados recebidos: {dados}")
            return None

    def exibir_clima(self, dados_formatados):
        """Exibe os dados climáticos de forma amigável"""
        if not dados_formatados:
            print("❌ Não foi possível obter os dados climáticos.")
            return

        print("\n" + "="*50)
        print(
            f"🌍 CLIMA EM {dados_formatados['cidade'].upper()}, {dados_formatados['pais']}")
        print("="*50)
        print(f"🌡️  Temperatura: {dados_formatados['temperatura']:.1f}°C")
        print(f"🤔 Sensação Térmica: {dados_formatados['sensacao']:.1f}°C")
        print(f"💧 Humidade: {dados_formatados['humidade']}%")
        print(f"☁️  Condições: {dados_formatados['descricao']}")
        print("="*50)
