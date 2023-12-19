from gtts import gTTS
import os
import pandas as pd

word_list = pd.read_excel('words.ods')['mot']

def text_to_speech(text):
    tts = gTTS(text=text, lang='fr')
    filename = os.path.join('audio_files', text + '.mp3')
    tts.save(filename)


if __name__ == "__main__":
    for word in word_list:
        text_to_speech(word)
