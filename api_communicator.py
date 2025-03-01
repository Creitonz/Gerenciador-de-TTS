import requests

def get_audio_from_text(api_key, voice_id, text, output_filename="output.mp3"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/iScHbNW8K33gNo3lGgbo"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }
    data = {
        "text": text,
        "model_id": "eleven_flash_v2_5",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        with open(output_filename, "wb") as file:
            file.write(response.content)
        print(f"Áudio salvo como {output_filename}")
        return output_filename
    else:
        print("Erro ao gerar áudio:", response.status_code, response.text)
        return None
