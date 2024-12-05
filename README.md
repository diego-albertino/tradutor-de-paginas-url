# 🌐 Tradutor de Páginas URL

### Descrição do Projeto 📜
Desenvolvi um sistema de tradução automatizada em Python utilizando a API do Microsoft Translator e o modelo GPT-4 hospedado no Microsoft Azure, capaz de traduzir textos do inglês para o português de forma eficiente e personalizada. O projeto implementa controle de limites de tokens e requisições, respeitando as restrições das APIs, além de realizar pré-processamento para otimizar o desempenho. Com integração direta aos endpoints dos serviços e suporte a múltiplos idiomas de destino, a solução é ideal para aplicações que demandam tradução rápida e confiável, como plataformas de comunicação e ferramentas de suporte ao cliente.

### Funcionalidades 🚀

- **Extração de Texto**: O projeto é capaz de extrair o conteúdo textual de uma página da web a partir de uma URL fornecida. Isso inclui a remoção de elementos desnecessários como scripts e estilos, resultando em um texto limpo e pronto para tradução.

- **Tradução com GPT-4**: Utilizando o modelo GPT-4 hospedado no Microsoft Azure, o projeto traduz o texto extraído para o português. Esta abordagem garante uma tradução contextualizada e fluida, aproveitando a capacidade avançada de compreensão de linguagem natural do GPT-4.

- **Tradução com Microsoft Translator**: Como alternativa, o projeto também oferece a tradução utilizando o serviço Microsoft Translator. Esta funcionalidade é útil para comparar a qualidade das traduções e garantir que o texto traduzido seja o mais preciso possível.

- **Comparação de Traduções**: Ao disponibilizar duas traduções diferentes para o mesmo texto, o projeto permite uma análise comparativa, ajudando a identificar qual abordagem oferece a melhor qualidade de tradução para diferentes tipos de conteúdo.

## Benefícios 🎉

- **🔍 Precisão**: A utilização de dois métodos de tradução distintos aumenta a precisão e a confiabilidade das traduções.
- **🌐 Flexibilidade**: O projeto pode ser facilmente adaptado para traduzir textos para outros idiomas, além do português.
- **⚡ Eficiência**: A extração e tradução de textos são realizadas de forma automatizada, economizando tempo e esforço manual.
- **📈 Qualidade**: A combinação de tecnologias avançadas de tradução garante que o texto traduzido mantenha a coerência e a fluidez do original.
  
### Como Usar 🛠️
1. Clone o repositório:
    ```bash
    git clone https://github.com/diego-albertino/tradutor-de-paginas-url.git
    ```
2. Baixe o arquivo `tradutor_de_páginas_url.ipynb` ou `tradutor.py`.
3. Crie um arquivo `.env` e adicione as chaves e endpoints do Azure:
    ```
    SUBSCRIPTION_KEY= 
    ENDPOINT=
    LOCATION=
    AZURE_ENDPOINT=
    API_KEY=
    API_VERSION=
    ```
