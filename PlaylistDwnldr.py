import os
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def download_youtube_playlist(playlist_url, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        messagebox.showinfo("Success", "Playlist downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def choose_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

def start_download():
    playlist_url = url_entry.get()
    output_dir = directory_entry.get()

    if not playlist_url or not output_dir:
        messagebox.showwarning("Input Error", "Please enter both the playlist URL and the directory.")
        return

    download_youtube_playlist(playlist_url, output_dir)

# Set up the Tkinter window
root = tk.Tk()
root.title("YouTube Playlist to MP3 Downloader")

# Playlist URL input
tk.Label(root, text="YouTube Playlist URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Directory selection
tk.Label(root, text="Download Directory:").grid(row=1, column=0, padx=10, pady=10)
directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=choose_directory).grid(row=1, column=2, padx=10, pady=10)

# Download button
tk.Button(root, text="Download Playlist", command=start_download).grid(row=2, column=1, padx=10, pady=20)

# Run the Tkinter main loop
root.mainloop()
