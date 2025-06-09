# 🕵️‍♀️ Esteganografia de Imagens Web

Este projeto é uma aplicação web simples que permite aos usuários ocultar mensagens secretas em imagens (esteganografia) e extrair mensagens ocultas de imagens. A plataforma utiliza a técnica LSB (Least Significant Bit) para incorporar e extrair os dados.

## 🎯 Objetivo

Desenvolver uma plataforma web funcional onde o usuário possa:
* Fazer upload de uma imagem e inserir uma mensagem secreta nela.
* Fazer upload de uma imagem possivelmente modificada e descobrir se há uma mensagem secreta embutida, e qual seria essa mensagem.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python com Flask
* **Frontend:** HTML, CSS, JavaScript
* **Processamento de Imagens:** Pillow (PIL Fork)

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e rodar a aplicação em sua máquina local:

### Pré-requisitos

Certifique-se de ter o Python 3 instalado.

### 1. Clonar o Repositório (se aplicável)

Se este projeto estiver em um repositório Git, clone-o:
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd esteganografia

Caso contrário, navegue até a pasta do projeto.

2. Criar e Ativar o Ambiente Virtual
É uma boa prática usar um ambiente virtual para isolar as dependências do projeto

Bash

python -m venv venv

No Windows:

Bash

.\venv\Scripts\activate

No macOS/Linux:

Bash

source venv/bin/activate

3. Instalar as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias:

Bash

pip install Flask Pillow

4. Executar a Aplicação Flask
Após instalar as dependências, você pode iniciar o servidor Flask:

Bash

flask run

O servidor será iniciado e você verá uma mensagem similar a esta no terminal:

 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

5. Acessar a Aplicação
Abra seu navegador web e acesse a URL: http://127.0.0.1:5000/

📋 Como Usar a Plataforma
🔐 Inserir Mensagem em Imagem
Acesse a aplicação no seu navegador.
Na seção "Selecione a imagem", clique em "Escolher arquivo" e selecione uma imagem (preferencialmente PNG, JPG ou JPEG).
No campo "Escolha a operação", selecione "Esconder Mensagem".
Um novo campo "Mensagem secreta" aparecerá. Digite a mensagem que deseja ocultar (máximo 255 caracteres).
Clique no botão "Processar Imagem".
A imagem original e a imagem processada (com a mensagem oculta) serão exibidas. Você poderá baixar a imagem processada através do link fornecido.
🔎 Ler Mensagem de Imagem
Acesse a aplicação no seu navegador.
Na seção "Selecione a imagem", clique em "Escolher arquivo" e selecione uma imagem que possa conter uma mensagem oculta.
No campo "Escolha a operação", selecione "Extrair Mensagem".
Clique no botão "Processar Imagem".
A mensagem oculta (se existir) será exibida na tela. Caso contrário, uma mensagem indicando que não foi encontrada uma mensagem ou houve um erro será mostrada.