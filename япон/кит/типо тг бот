import os
import requests
from aiogram import Bot, Dispatcher, types, executor
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import speech_recognition as sr
from googletrans import Translator

# Настройка бота
API_TOKEN = 'ВАШ_ТОКЕН'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
translator = Translator()

# Универсальная загрузка видео
def download_video(url, save_path="video.mp4"):


    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return save_path
    except Exception as e:
        raise Exception(f"Ошибка загрузки видео: {str(e)}")

# Генерация субтитров
def audio_to_subtitles(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="ru-RU")
    return text

# Наложение субтитров
def add_subtitles(video_path, text, output_path="output.mp4"):
    video = VideoFileClip(video_path)
    txt_clip = TextClip(text, fontsize=24, color="white", bg_color="black")
    txt_clip = txt_clip.set_position(("center", "bottom")).set_duration(video.duration)
    final_video = CompositeVideoClip([video, txt_clip])
    final_video.write_videofile(output_path)
    return output_path

# Обработчик сообщений
@dp.message_handler(content_types=[types.ContentType.TEXT])
async def handle_message(message: types.Message):
    if message.text.startswith(("http://", "https://")):
        await message.reply("⏳ Скачиваю видео...")
        try:
            video_path = download_video(message.text)

            await message.reply("🔉 Извлекаю аудио...")
            audio_path = "audio.wav"
            VideoFileClip(video_path).audio.write_audiofile(audio_path)

            await message.reply("📝 Генерирую субтитры...")
            subtitles = audio_to_subtitles(audio_path)

            await message.reply("🌍 Перевожу на английский...")
            translated = translator.translate(subtitles, dest="en").text

            await message.reply("🎬 Накладываю субтитры...")
            output_video = add_subtitles(video_path, translated)

            await message.reply_video(types.InputFile(output_video))

            # Удаляем временные файлы
            os.remove(video_path)
            os.remove(audio_path)
            os.remove(output_video)

        except Exception as e:
            await message.reply(f"❌ Ошибка: {str(e)}")
    else:
        await message.reply("Отправьте прямую ссылку на видео!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)