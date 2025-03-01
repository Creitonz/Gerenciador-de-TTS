import json
import os

AUDIO_LIST_FILE = "audios.json"
AUDIO_FOLDER = "audios"

# Cria a pasta 'audios' caso não exista
if not os.path.exists(AUDIO_FOLDER):
    os.makedirs(AUDIO_FOLDER)

def save_audio_entry(filename):
    """Adiciona um novo áudio à lista e salva no JSON"""
    audios = load_audio_list()
    if filename not in audios:
        audios.append(filename)
    with open(AUDIO_LIST_FILE, "w", encoding="utf-8") as f:
        json.dump(audios, f, ensure_ascii=False, indent=4)

def load_audio_list():
    """Carrega a lista de áudios salvos"""
    if not os.path.exists(AUDIO_LIST_FILE):
        return []
    with open(AUDIO_LIST_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def delete_audio(filename):
    """Remove um áudio da lista e do JSON"""
    audios = load_audio_list()
    if filename in audios:
        audios.remove(filename)
        if os.path.exists(os.path.join(AUDIO_FOLDER, filename)):  # Verifica se o arquivo existe
            try:
                os.remove(os.path.join(AUDIO_FOLDER, filename))  # Remove o arquivo de áudio
            except Exception as e:
                print(f"Erro ao tentar excluir o arquivo {filename}: {e}")
        with open(AUDIO_LIST_FILE, "w", encoding="utf-8") as f:
            json.dump(audios, f, ensure_ascii=False, indent=4)

def delete_audio_from_json(filename):
    """Remove um áudio da lista e do JSON"""
    audios = load_audio_list()
    if filename in audios:
        audios.remove(filename)
        with open(AUDIO_LIST_FILE, "w", encoding="utf-8") as f:
            json.dump(audios, f, ensure_ascii=False, indent=4)

    # Remover o arquivo de áudio da pasta
    file_path = os.path.join(AUDIO_FOLDER, filename)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)  # Remove o arquivo de áudio
        except Exception as e:
            print(f"Erro ao tentar excluir o arquivo {filename}: {e}")

