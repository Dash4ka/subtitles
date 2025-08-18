from subtitles.downloader_audio import download_audio 
from utils.config import URL
from subtitles.text_loader import init_whisper, extract_audio
from subtitles.transcribe_to_json import write_json
from subtitles.converter_to_srt import run
from subtitles.translater import translate_srt
from subtitles.downloader_video import download_video
from font_video.download_font import ??????????????

def main():
    download_audio(URL)
    init_whisper()
    a = extract_audio(video_path)
    write_json(audio_path)
    run(input_path, output_name, output_directory)  ???????????????????????????????????
    translate_srt(input_file, output_file)
    download_video(URL)

    
    