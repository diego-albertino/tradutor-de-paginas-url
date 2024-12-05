import requests
from bs4 import BeautifulSoup
from langchain_openai.chat_models.azure import AzureChatOpenAI
import os

# Configurações do Azure Translator
subscription_key = os.getenv("SUBSCRIPTION_KEY")
endpoint = os.getenv("ENDPOINT")
location = os.getenv("LOCATION")
language_destination = 'pt-br'

def extract_text_from_url(url, limit= False):
  """
  Extrai e limpa o conteúdo de texto de uma URL fornecida.
  Args:
    url (str): A URL da página da web para extrair o texto.
    limit (bool, opcional): Se True, limita o texto extraído a um número máximo de caracteres. O padrão é False.
  Retorna:
    str: O texto limpo extraído da página da web. Se `limit` for True, retorna o texto limitado a um número especificado de caracteres.
    None: Se a solicitação para a URL falhar
  """

  response = requests.get(url)

  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for script_or_tyle in soup(['script', 'style']):
      script_or_tyle.decompose()
    texto = soup.get_text(separator= ' ')

    #limpar texto
    linhas = (line.strip() for line in texto.splitlines())
    parts = (phrase.strip() for line in linhas for phrase in line.split("  "))
    texto_limpo = '\n'.join(part for part in parts if part)


    if limit:
      max_characters = 200  # Ajuste conforme necessário
      texto_limpo_limit = texto_limpo[:max_characters]
      return texto_limpo_limit

    return texto_limpo
  else:
    print(f"Failed to fetch the URL. Status code: {response.status_code}")
    return None




def translate_article(text, lang):
  client = AzureChatOpenAI(
    azure_endpoint = os.getenv("AZURE_ENDPOINT"),
    api_key = os.getenv("API_KEY"),
    api_version = os.getenv("API_VERSION"),
    deployment_name= 'gpt-4o-mini',
    max_retries=0
    )
  
  messages = [
      ("system" , "Você atua como tradutor de textos"),
      ("user" , f"Traduz o {text} para o idioma {lang} e reponda em markdown")
  ]

  response = client.invoke(messages)
  print(response.content)
  return response.content


def translator_text(text, target_language):

  path = '/translate'
  constructed_url = endpoint + path
  headers = {
      'Ocp-Apim-Subscription-Key': subscription_key,
      'Ocp-Apim-Subscription-Region': location,
      'Content-type': 'application/json',
      'X-ClientTraceId': str(os.urandom(16))
  }

  body = [{
      'text': text
  }]

  params = {
      'api-version': '3.0',
      'from': 'en',
      'to': target_language
  }
  request = requests.post(constructed_url, params=params, headers=headers, json=body)
  response = request.json()
  return response[0]["translations"][0]["text"]

# UILIZA O GPT-4O-MINI PARA FAZER TRADUÇÃO
url = 'https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo'
text = extract_text_from_url(url, True)
article = translate_article(text, 'portugues')

print(article)

# UTILIZA O MICROSOFT TRANSLATE PARA TRADUZIR
url = 'https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo'
texto = extract_text_from_url(url)
artigo = translator_text(texto, 'pt-br')

print(artigo)