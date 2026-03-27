import ffmpeg
from pathlib import Path

class VideoSubtitler:
    """Класс для добавления субтитров к видео с помощью ffmpeg-python"""
    
    def __init__(self, input_video, font_name="Noto Sans CJK JP"):
        self.input_video = Path(input_video)
        self.font_name = font_name
        
        if not self.input_video.exists():
            raise FileNotFoundError(f"Видеофайл не найден: {input_video}")
    
    def add_subtitles(self, subtitle_file, output_video):
        """Добавляет субтитры к видео"""
        subtitle_path = Path(subtitle_file)
        
        if not subtitle_path.exists():
            raise FileNotFoundError(f"Файл субтитров не найден: {subtitle_file}")
        
        # Создаем поток с субтитрами
        stream = ffmpeg.input(str(self.input_video))
        
        # Добавляем фильтр субтитров с кастомным шрифтом
        stream = ffmpeg.filter(
            stream,
            'subtitles',
            str(subtitle_path),
            force_style=f'FontName={self.font_name}'
        )
        
        # Копируем аудио без изменений
        stream = ffmpeg.output(stream, str(output_video), acodec='copy')
        
        # Выполняем
        ffmpeg.run(stream, overwrite_output=True)
        print(f"✓ Субтитры добавлены: {output_video}")
    
    def add_all_languages(self, languages_config):
        """Добавляет субтитры для всех указанных языков"""
        results = {}
        
        for lang, config in languages_config.items():
            try:
                print(f"\nОбработка {lang.upper()}...")
                self.add_subtitles(config['subtitle'], config['output'])
                results[lang] = True
            except Exception as e:
                print(f"✗ Ошибка для {lang.upper()}: {e}")
                results[lang] = False
        
        return results

# Использование
if __name__ == "__main__":
    # Создаем экземпляр класса
    subtitler = VideoSubtitler("video.mp4")
    
    # Конфигурация языков
    languages = {
        "ja": {"subtitle": "subs_ja.srt", "output": "output_ja.mp4"},
        "zh": {"subtitle": "subs_zh.srt", "output": "output_zh.mp4"},
        "ko": {"subtitle": "subs_ko.srt", "output": "output_ko.mp4"},
    }
    
    # Добавляем все субтитры
    results = subtitler.add_all_languages(languages)
    
    # Выводим итоговый отчет
    print("\n" + "="*50)
    print("ИТОГОВЫЙ ОТЧЕТ:")
    print("="*50)
    for lang, success in results.items():
        status = "✓ Успешно" if success else "✗ Ошибка"
        print(f"{lang.upper()}: {status}")