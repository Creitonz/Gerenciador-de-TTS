import os
import re
import tkinter as tk
from tkinter import messagebox
import pygame  
from api_communicator import get_audio_from_text
from audio_manager import save_audio_entry, load_audio_list, delete_audio_from_json
from PIL import Image, ImageTk  

ICON_PATH = "logo.ico"
PLAY_ICON_PATH = "play_icon.png"  
DELETE_ICON_PATH = "delete_icon.png"  

API_KEY = "API_KEY_AQUI" 
voice_id = "eVXYtPVYB9wDoz9NVTIy" 

pygame.mixer.init()

def play_audio(file):
    if pygame.mixer.get_init():
        if pygame.mixer.music.get_busy():  # Verifica se o áudio está tocando
            pygame.mixer.music.stop()  # Para o áudio se ele estiver tocando
        else:
            pygame.mixer.music.load(file)  # Carrega o áudio
            pygame.mixer.music.play()  # Toca o áudio

def delete_audio(file, listbox_frame):
    result = messagebox.askyesno("Confirmar Exclusão", f"Você tem certeza que deseja excluir o áudio {file}?")
    if result:
        try:
            # Para a música e fecha o mixer para liberar o arquivo
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                pygame.mixer.init()  # Reinicializa o mixer para uso futuro
            
            # Remove o arquivo de áudio
            os.remove(file)
            delete_audio_from_json(file)  
            messagebox.showinfo("Sucesso", f"Áudio {file} excluído com sucesso!")

            # Atualiza a interface: remove o item da lista
            for widget in listbox_frame.winfo_children():
                if isinstance(widget, tk.Frame):
                    audio_label = widget.winfo_children()[0]
                    if audio_label.cget("text") == file:
                        widget.destroy()  
                        break

            populate_audio_list()

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao excluir o áudio: {e}")

def generate_and_save_audio():
    text = text_entry.get("1.0", "end-1c")
    file_name = name_entry.get()
    new_file_name = f"audios/{file_name}.mp3"
    
    if not text or not file_name:
        messagebox.showwarning("Aviso", "Por favor, insira o texto e o nome do arquivo!")
        return
    
    if re.search(r'[<>:"/\\|?*]', file_name):
        messagebox.showwarning("Aviso", "O nome do arquivo contém caracteres inválidos. Remova os seguintes caracteres: <>:\"/\\|?*")
        return
    
    if os.path.exists(new_file_name):
        messagebox.showwarning("Aviso", "Já existe um arquivo com esse nome!")
        return
    
    audio_file = get_audio_from_text(API_KEY, voice_id, text)
    if audio_file:
        os.rename(audio_file, new_file_name)
        save_audio_entry(new_file_name)
        populate_audio_list()
        messagebox.showinfo("Sucesso", f"Áudio gerado e salvo como {new_file_name}")
        text_entry.delete("1.0", tk.END)
        name_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Falha na geração do áudio.")

def populate_audio_list():
    for widget in listbox_frame.winfo_children():
        widget.destroy()

    audio_list = load_audio_list()
    for audio in audio_list:
        frame = tk.Frame(listbox_frame, bg="#333333", bd=0)
        frame.pack(fill=tk.X, padx=10, pady=5)

        audio_name = os.path.basename(audio)  

        audio_label = tk.Label(frame, text=audio_name, fg="white", bg="#333333", font=("Helvetica", 12), anchor="w", width=40)
        audio_label.pack(side=tk.LEFT, padx=10, pady=5)

        button_frame = tk.Frame(frame, bg="#333333")
        button_frame.pack(side=tk.RIGHT, padx=20, anchor="e")

        play_icon = Image.open(PLAY_ICON_PATH).resize((24, 24))  
        play_icon = ImageTk.PhotoImage(play_icon)

        delete_icon = Image.open(DELETE_ICON_PATH).resize((24, 24))  
        delete_icon = ImageTk.PhotoImage(delete_icon)

        play_button = tk.Button(button_frame, image=play_icon, bg="#333333", relief="flat", bd=0, command=lambda a=audio: play_audio(a))
        play_button.image = play_icon 
        play_button.pack(side=tk.LEFT, padx=10)

        delete_button = tk.Button(button_frame, image=delete_icon, bg="#333333", relief="flat", bd=0, command=lambda a=audio: delete_audio(a, listbox_frame))
        delete_button.image = delete_icon  
        delete_button.pack(side=tk.LEFT, padx=10)

    listbox_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Gerenciador de Áudio")
root.geometry("600x650")  
root.resizable(False, False)  
root.configure(bg="#121212")

icon_image = Image.open(ICON_PATH)
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon_photo)

header_frame = tk.Frame(root, bg="#1c1c1c", height=50)
header_frame.pack(fill=tk.X, padx=20, pady=10)

title_label = tk.Label(header_frame, text="Gerenciador de Áudios", font=("Helvetica", 18, "bold"), fg="#ffffff", bg="#1c1c1c")
title_label.pack(pady=10)

input_frame = tk.Frame(root, bg="#1c1c1c", bd=2, relief="flat")
input_frame.pack(fill=tk.X, padx=20, pady=15)

text_entry_label = tk.Label(input_frame, text="Digite o texto:", fg="white", bg="#1c1c1c", font=("Helvetica", 12))
text_entry_label.pack(padx=10, pady=5)

text_entry = tk.Text(input_frame, width=40, height=5, bg="#333333", fg="white", wrap="word", font=("Helvetica", 12))
text_entry.pack(padx=10, pady=5)

name_entry_label = tk.Label(input_frame, text="Nome do arquivo:", fg="white", bg="#1c1c1c", font=("Helvetica", 12))
name_entry_label.pack(padx=10, pady=5)

name_entry = tk.Entry(input_frame, width=40, bg="#333333", fg="white", font=("Helvetica", 12))
name_entry.pack(padx=10, pady=5)

generate_button = tk.Button(input_frame, text="Gerar Áudio", bg="#4CAF50", fg="white", font=("Helvetica", 14), command=generate_and_save_audio, relief="flat", bd=0)
generate_button.pack(pady=20)

canvas_frame = tk.Frame(root, bg="#1c1c1c", bd=2, relief="flat")
canvas_frame.pack(fill=tk.BOTH, padx=20, pady=15, expand=True)

canvas = tk.Canvas(canvas_frame, bg="#333333")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")
canvas.config(yscrollcommand=scrollbar.set)

listbox_frame = tk.Frame(canvas, bg="#333333")
canvas.create_window((0, 0), window=listbox_frame, anchor="nw")

populate_audio_list()

root.mainloop()
