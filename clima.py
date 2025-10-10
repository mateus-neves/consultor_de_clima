import requests
from config import BASE_URL, API_KEY


class ConsultorClima:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
        self.historico = []

    def buscar_clima(self, cidade):
        """Busca informações climáticas para uma cidade"""
        params = {
            'q': cidade,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'pt_br'
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            dados = response.json()

            # Adiciona ao histórico
            self._adicionar_historico(cidade, dados)

            return dados

        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                print("❌ Erro de autenticação. Verifique sua API Key.")
            elif response.status_code == 404:
                print("❌ Cidade não encontrada. Tente outro nome.")
            else:
                print(f"❌ Erro HTTP: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro de conexão: {e}")
            return None

    def _adicionar_historico(self, cidade, dados):
        """Adiciona consulta ao histórico"""
        from datetime import datetime

        if dados and 'main' in dados:
            self.historico.append({
                'cidade': cidade,
                'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M"),
                'temperatura': dados['main']['temp'],
                'descricao': dados['weather'][0]['description']
            })

            # Mantém apenas as últimas 10 consultas
            if len(self.historico) > 10:
                self.historico.pop(0)

    def exibir_historico(self):
        """Exibe o histórico de consultas"""
        if not self.historico:
            print("\n📝 Nenhuma consulta no histórico.")
            return

        print("\n📝 HISTÓRICO DE CONSULTAS")
        print("=" * 40)
        for i, consulta in enumerate(self.historico[-5:], 1):  # Últimas 5
            print(
                f"{i}. {consulta['cidade']} - {consulta['temperatura']:.1f}°C")
            print(f"   ⏰ {consulta['timestamp']} | ☁️ {consulta['descricao']}")
        print("=" * 40)

    def formatar_dados(self, dados):
        """Formata os dados climáticos para exibição"""
        if not dados or 'main' not in dados:
            return None

        main = dados['main']
        weather = dados['weather'][0]

        # Emojis baseados nas condições climáticas
        emoji_clima = self._obter_emoji_clima(weather['main'])

        return {
            'cidade': dados['name'],
            'pais': dados['sys']['country'],
            'temperatura': main['temp'],
            'sensacao': main['feels_like'],
            'humidade': main['humidity'],
            'pressao': main.get('pressure', 'N/A'),
            'descricao': weather['description'].title(),
            'emoji': emoji_clima
        }

    def _obter_emoji_clima(self, condicao):
        """Retorna emoji baseado na condição climática"""
        emojis = {
            'Clear': '☀️',
            'Clouds': '☁️',
            'Rain': '🌧️',
            'Drizzle': '🌦️',
            'Thunderstorm': '⛈️',
            'Snow': '❄️',
            'Mist': '🌫️',
            'Fog': '🌫️'
        }
        return emojis.get(condicao, '🌤️')

    def exibir_clima(self, dados_formatados):
        """Exibe os dados climáticos de forma amigável"""
        if not dados_formatados:
            print("❌ Não foi possível obter os dados climáticos.")
            return

        emoji = dados_formatados['emoji']

        print(f"\n{emoji} " + "="*48)
        print(
            f"🌍 CLIMA EM {dados_formatados['cidade'].upper()}, {dados_formatados['pais']}")
        print("="*50)
        print(f"🌡️  Temperatura: {dados_formatados['temperatura']:.1f}°C")
        print(f"🤔 Sensação Térmica: {dados_formatados['sensacao']:.1f}°C")
        print(f"💧 Humidade: {dados_formatados['humidade']}%")
        print(f"📊 Pressão: {dados_formatados['pressao']} hPa")
        print(
            f"☁️  Condições: {dados_formatados['descricao']} {dados_formatados['emoji']}")
        print("="*50)
