import yt_dlp

# Ссылка на видео VK
url = 'https://vkvideo.ru/video5220238_171100332'

# Настройки
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # лучший качество
    'outtmpl': 'video.mp4',  # имя файла
    'quiet': False,  # показывать прогресс
}

# Скачивание
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Видео скачано как 'video.mp4'")