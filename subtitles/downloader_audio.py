#скачиваем аудио
import yt_dlp


def download_audio(url):
# Настройки для скачивания аудио в MP3
    ydl_opts = {
       'format': 'bestaudio/best',       # Лучшее качество аудио
       'extract_audio': True,            # Извлечь аудио
       'audio_format': 'mp3',            # Конвертировать в MP3
       'outtmpl': '%(title)s.%(ext)s',   # Название файла как у видео
       'quiet': False,                   # Показывать прогресс
       'no_warnings': False,             # Не скрывать предупреждения
      }

# Скачивание
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Аудио успешно скачано!")
    except Exception as e:
        print(f"Ошибка: {e}")

#download_video('https://vkvideo.ru/video5220238_171100332')