from subtitles.downloader_audio import download_audio 
from utils.config import URL
from subtitles.text_loader import init_whisper, extract_audio
from subtitles.transcribe_to_json import write_json





def main():
    download_audio(URL)
    init_whisper()
    a = extract_audio(video_path)
    write_json(audio_path)
    
    