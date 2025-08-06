#кит
from deep_translator import GoogleTranslator

def translate_srt(input_file, output_file, source_lang='ru', target_lang='zh-TW'):
    with open("чебурашка.srt", 'r', encoding='utf-8') as f:
        srt_content = f.read()

    # Разбиваем на блоки (каждый блок — субтитр с таймкодами)
    blocks = srt_content.strip().split('\n\n')

    translated_blocks = []
    for block in blocks:
        lines = block.split('\n')
        if len(lines) >= 3:  # Проверяем, что блок содержит номер, таймкоды и текст
            # Переводим только текст (не трогаем номер и таймкоды)
            text_to_translate = '\n'.join(lines[2:])
            translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text_to_translate)
            translated_blocks.append(f"{lines[0]}\n{lines[1]}\n{translated_text}")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(translated_blocks))

# Использование
translate_srt("чебурашка.srt", 'subs_zh.srt')