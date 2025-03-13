Documentação do Código:

Gerenciador de Áudio
Este aplicativo é um gerenciador de áudios que permite gerar áudios a partir de texto usando a API ElevenLabs, salvar, listar, reproduzir e excluir arquivos de áudio localmente.

Importações:
os: Manipulação de arquivos e diretórios.
re: Utilizado para validação de caracteres no nome do arquivo.
tkinter: Interface gráfica do usuário (GUI).
pygame: Biblioteca para reprodução de áudio.
api_communicator: Módulo que se comunica com a API ElevenLabs para geração de áudio.
audio_manager: Módulo responsável por gerenciar os arquivos de áudio, como salvar e excluir.
PIL (Pillow): Para manipulação de imagens (ícones).
Constantes:
ICON_PATH: Caminho para o ícone da aplicação.
PLAY_ICON_PATH: Caminho para o ícone de reprodução de áudio.
DELETE_ICON_PATH: Caminho para o ícone de exclusão de áudio.
API_KEY: Chave de autenticação da API ElevenLabs.
voice_id: Identificador da voz na API ElevenLabs.
Funções:
play_audio(file)
Descrição: Reproduz o áudio indicado pelo parâmetro file utilizando o módulo pygame.mixer.
Parâmetros:
file (str): Caminho do arquivo de áudio a ser reproduzido.
Comportamento: Verifica se o áudio está tocando. Caso sim, interrompe a reprodução atual e começa a reprodução do novo arquivo de áudio.
delete_audio(file, listbox_frame)
Descrição: Exclui um arquivo de áudio tanto do sistema de arquivos quanto da lista exibida na interface.
Parâmetros:
file (str): Caminho do arquivo de áudio a ser excluído.
listbox_frame (tk.Frame): Frame onde a lista de áudios é exibida.
Comportamento:
Confirma com o usuário se ele deseja excluir o arquivo.
Para a reprodução do áudio, se necessário.
Remove o arquivo de áudio do sistema de arquivos e da lista de arquivos armazenados no JSON.
Atualiza a interface para refletir a exclusão.
generate_and_save_audio()
Descrição: Gera um novo arquivo de áudio a partir do texto inserido pelo usuário e o salva no sistema.
Comportamento:
Verifica se o texto e o nome do arquivo foram preenchidos.
Verifica se o nome do arquivo contém caracteres inválidos.
Verifica se já existe um arquivo com o mesmo nome.
Chama a função get_audio_from_text() para gerar o áudio a partir da API.
Salva o arquivo gerado e atualiza a lista de áudios na interface.
populate_audio_list()
Descrição: Preenche a lista de áudios na interface gráfica com os arquivos presentes na pasta audios e registrados no arquivo audios.json.
Comportamento:
Para cada áudio na lista, cria um novo item na interface com um botão de "Play" e um botão de "Delete".
Interface Gráfica (GUI):
A aplicação utiliza tkinter para criar a interface gráfica. A interface é composta por vários componentes:

Cabeçalho (header_frame):

Contém o título da aplicação.
Entrada de Texto e Nome de Arquivo (input_frame):

O usuário pode inserir um texto para gerar o áudio e um nome de arquivo.
O botão "Gerar Áudio" chama a função generate_and_save_audio().
Lista de Áudios (canvas_frame):

Exibe os áudios gerados com botões para reproduzir ou excluir cada um.
Botões:

Play: Reproduz o áudio correspondente.
Delete: Exclui o áudio selecionado.
Arquivos:
audios.json: Arquivo que contém a lista de áudios gerados.
audios/: Pasta onde os arquivos de áudio gerados são armazenados.
Módulo audio_manager:
Este módulo lida com a manipulação de arquivos de áudio no sistema.

Funções:
save_audio_entry(filename):

Adiciona um novo arquivo de áudio à lista no arquivo JSON.
load_audio_list():

Carrega a lista de áudios a partir do arquivo audios.json.
delete_audio(filename):

Exclui um áudio do sistema e da lista no JSON.
delete_audio_from_json(filename):

Exclui um áudio apenas da lista no JSON.
Módulo api_communicator:
Este módulo lida com a comunicação com a API ElevenLabs para gerar o áudio a partir do texto.

Função:
get_audio_from_text(api_key, voice_id, text, output_filename="output.mp3"):
Envia uma solicitação à API ElevenLabs para gerar um arquivo de áudio a partir do texto fornecido.
Retorna o caminho do arquivo de áudio gerado ou None em caso de erro.
Considerações Finais:
O código funciona como um gerenciador de áudios, com a capacidade de gerar áudios a partir de texto, exibi-los em uma lista e permitir que os usuários reproduzam ou excluam os arquivos gerados. Ele utiliza a API ElevenLabs para gerar os áudios, e a interface gráfica é construída com o tkinter para uma experiência de usuário intuitiva.
