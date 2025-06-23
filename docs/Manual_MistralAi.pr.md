



# Mistral AI
  
Módulo para interagir com os modelos do Mistral AI a partir do Rocketbot.  

*Read this in other languages: [English](Manual_mistralai.md), [Português](Manual_mistralai.pr.md), [Español](Manual_mistralai.es.md)*

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  

## Como usar este módulo

Para usar este módulo, precisamos obter a chave API do MistralAI. Siga estes passos:

- Primeiro, crie uma conta Mistral ou faça login em [console.mistral.ai](https://console.mistral.ai/home).

- Em seguida, navegue até "Workspace" e "Billing" para adicionar suas informações de pagamento e ativar os pagamentos em sua conta.
- Depois disso, vá para a página "API keys" e crie uma nova chave API clicando em "Create new key". Certifique-se de copiar a chave API, armazená-la com segurança e não compartilhá-la com ninguém.
## Descrição do comando

### Conectar com Mistral
  
Estabelece conexão com Mistral AI
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|API Key|Sua chave de API do Mistral|sk-abc123...|
|Atribuir à variável|Nome da variável para armazenar a conexão|resultadoMistral|

### Obter Modelos
  
Recupera os modelos disponíveis do Mistral AI
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir à variável|Nome da variável para armazenar a lista de modelos|resultadoModelos|

### Gerar Texto
  
Gera texto usando o Mistral AI
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Prompt|Texto de entrada para gerar texto|O que é Rocketbot?|
|Modelo|ID do modelo a ser usado|mistral-tiny|
|Atribuir à variável|Nome da variável para armazenar o texto gerado|resultadoTexto|
|Temperatura (opcional)|Controla a aleatoriedade da geração de texto (0.0 a 0.7)|0.7|
|Máximo de tokens (opcional)|Número máximo de tokens a serem gerados|100|
|Sequência de parada (opcional)|Sequência opcional para parar a geração de texto|ferramenta RPA|

### OCR para Imagem/PDF
  
Processa uma imagem ou PDF com o OCR do Mistral AI
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Modelo|Nome do modelo OCR a ser usado|mistral-ocr-latest|
|Arquivo ou URL|Permite fazer o upload de um arquivo local ou entrar uma url para um arquivo online|Caminho ou URL do arquivo|
|Atribuir à variável|Nome da variável para armazenar o resultado do OCR|resultadoOCR|
