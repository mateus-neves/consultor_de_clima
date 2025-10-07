import requests
from config import API_KEY, BASE_URL


class ConsultorClima:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL

    def buscar_clima(self, cidade):
        """Busca informaçoes climaticas sobre uma cidade"""
        params = {
            'q': cidade,
            'appid': self.api_key,
            'units': 'metric', """temperatura em Celsius"""
            'lang': 'pt_br' """descriçao do clima em portugues"""
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.rise_for_status()
            return response.jason()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar dados do clima: {e}")
            return None

    def formatar_dados(self, dados):
        """formata os dados climaticos para exibiçao"""
        if not dados or 'main' not in dados:
            return None

        temperatura = dados['main']['temp']
        sensacao = dados['main']['feels_like']
        umidade = dados['main']['humidity']
        descricao = dados['weather'][0]['description'].tittle()
        cidade = dados['name']
        pais = dados['sys']['country']

        return {
            'cidade': cidade,
            'pais': pais,
            'temperatura': temperatura,
            'sensacao': sensacao,
            'umidade': umidade,
            'descricao': descricao
        }

    def exibir_clima(self, dados_formatados):
        """exibe os dados formatados de forma amigavel"""
        if not dados_formatados:
            print("não foi possivel obter os dados climaticos")
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
