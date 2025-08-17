import yt_dlp 


ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # лучший качество
    'outtmpl': 'video.mp4',  # имя файла
    'quiet': False,  # показывать прогресс
}

def download_video(URL):
# Скачивание
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])

    print("Видео скачано как 'video.mp4'")