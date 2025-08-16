#загружаем модель и выводим текст из видео
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
from config import HF_TOKEN


# Выбираем девайс: графический либо центральный процессор
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
# Выбираем модель Whisper из хаба HuggingFace
model_id = 'openai/whisper-medium'
# Загружаем модель и отправляем ее на девайс
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)
# Процессор - это "токенизатор" для аудио-моделей
processor = AutoProcessor.from_pretrained(model_id)
# Пайплайн - это сборка для распознавания речи
pipe = pipeline(
    "automatic-speech-recognition", # Тип задачи
    model=model, # Модель
    tokenizer=processor.tokenizer, # Токенизатор
    feature_extractor=processor.feature_extractor, # Извлечение признаков из спектрограмм
    torch_dtype=torch_dtype, # Тип тензоров для обработки данных
    device=device, # Девайс
    return_timestamps=True, # Временные метки
)
result = pipe(
    audio_path(download_video),
    generate_kwargs={
         "language": "ru",
         "task": "transcribe"
    }
 )
#result = pipe('/content/Песенка Чебурашки.m4a',  generate_kwargs={
       # "language": "ru",
       # "task": "transcribe"
# Явно указываем язык вывода
 # Явно указываем транскрипцию (не перевод)
  #  })

def extract_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    video.audio.write_audiofile(audio_path)
    return audio_path