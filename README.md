# Assistente Pessoal

<!--- See https://shields.io --->
![GitHub repo size](https://img.shields.io/github/repo-size/giovana-morais/assistente?style=plastic)
![GitHub stars](https://img.shields.io/github/stars/giovana-morais/assistente?style=plastic)
![Twitter Follow](https://img.shields.io/twitter/follow/ohshitgi?style=social)

O `assistente` é um assistente pessoal por comando de voz. Ele tem algumas
funções já definidas e nenhuma inteligência embutida (ainda), então dê uma
olhada no script `assistente.py` pra ver exatamente o que ele faz. :heart:

## Pré-requisitos

Antes de começar, você precisa lidar com algumas dependências do projeto:

* Ter a última versão do Python instalada (ou alguma versão >= 3.7) ou um
ambiente virtual que tenha a última versão instalada

* Ter o `espeak` instalado caso sua máquina seja Linux e a _engine_ que você
deseja usar para converter o texto em fala é a `pyttsx3`.
	* **ATENÇÃO**: Esse projeto não foi validado para outros sistemas operacionais.

* Conexão com a internet, uma vez que o reconhecimento de voz com a API do
Google não funciona offline

## Instalação

É recomendado instalar as dependências do projeto em um ambiente virtual,
o [virtualenv][venv], para que não haja nenhum conflito com a versão do
Python do seu sistema.

```
git clone https://github.com/giovana-morais/assistente.git

cd assistente/

# criando um ambiente virtual. pule esse e o próximo passo caso não deseje um.
virtualenv -p python3 venv

# ativando o ambiente virtual
source venv/bin/activate

pip install -r requirements.txt

```

Para desativar o seu ambiente virtual, basta digitar `deactivate`.

## Usando assistente

### Credenciais do Google
O assistente usa a API de Calendário do Google pra fazer a checagem e pra
adicionar eventos. Por causa disso, você precisa habilitar a API do
Calendário por meio [deste link](https://developers.google.com/calendar/quickstart/python).

Vá até a opção "Habilite a API do Google Agenda" (_Enable the Google Calendar API_)
e salve o arquivo `credentials.json` ao clicar no botão "Faça o Download da Configuração
de Cliente" (_Download Client Configuration_).

A primeira vez que você rodar o programa, uma janela deverá abrir pedindo a sua
permissão para que o programa acesse seus dados de agenda. Lembrando que
**nenhum dado da sua agenda é salvo ou compartilhado com qualquer pessoa**.
Esse projeto é só uma brincadeirinha e não pretendo roubar dado de ninguém.

### `config.ini`
O arquivo `config.ini` é o arquivo responsável pra você escolher o nome do
seu assistente e escolher qual a _engine_ responsável pelo texto-para-fala
(_text-to-speech_).

O `gTTS` é a _engine_ do Google e a voz é idêntica ao do Google Tradutor.
Já o `pyttsx` é uma _engine_ que usa o sistema de fala do seu sistema
operacional. Fique à vontade para mudar o arquivo de configuração e brincar com
seus testes.

### Agora sim, vamos rodar!

API com suas devidas credenciais, podemos rodar

```
python main.py
```

e, se todas as bibliotecas foram instaladas corretamente, você logo menos
estará falando com seu computador. :robot:

Aqui estão alguns exemplos de frases que o assistente atualmente entende

```
Faça um funk!
Me mostre os últimos três eventos
Quero adicionar um evento à minha agenda
Me conta uma piada?
Estou entendiada
Abra um vídeo no youtube
```


## Contribuindo
<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->
Para contribuir, siga os próximos passos:

1. Dê um fork no repositório.
2. Crie um branch: `git checkout -b <func/sua_funcionalidade>` caso queira
adicionar uma funcionalidade
3. Crie um branch: `git checkout -b <bug/sua_correcao> caso queira corrigir
um bug
4. Faça suas mudanças/adições e dê um commit: `git commit -m "sua mensagem explicativa de commit"`
5. Faça o push para seu branch original: `git push origin <assistente>/<seu_branch>`
7. Por fim, faça o [pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

**OBSERVAÇÕES IMPORTANTES**: O código que você subir deve estar **TODO** em
português, caso contrário será refutado imediatamente. Comentários, da
mesma maneira, devem seguir esse padrão.

## Contato

Se você quiser entrar em contato, pode me encontrar em <giovana.vmorais@gmail.com> ou entrar em contato com as PyLadies Sorocaba em <sorocaba@pyladies.com>.


## Licença

Esse projeto usa a [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)
como licença, o que significa que esse projeto pode ser distribuído e alterado
à vontade desde que **sempre** seja usado em projetos _open source_.
