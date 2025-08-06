import json

with open('sub.json', "w", encoding="utf-8") as file:
   # file.write(transcribe_audio(audio_path: str, language: str = "ru"))
   result = transcribe_audio(audio_path, language="ru")
   file.write(result["text"])