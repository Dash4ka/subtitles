#жестко делаем формат srt
import sys
import whisper
from whisper.utils import get_writer
output_name = "sub.json"

def run(input_path: str, output_name: str = "", output_directory: str = "./") -> None:

    model = whisper.load_model("medium")
    result = model.transcribe(input_path)

    writer = get_writer("srt", str(output_directory))
    writer(result, output_name)

run(
input_path="/content/Песенка Чебурашки.m4a",
output_name = 'чебурашка',
output_directory="."
)