from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='fr')
    filename = text + '.mp3'
    tts.save(filename)
    # os.system(f"vlc {filename}")


word_list = ["guitare",
        "dessus",
        "bientôt",
        "poule",
        "manger",
        "petit",
        "rapide"
        ]

if __name__ == "__main__":
    for word in word_list:
        text_to_speech(word)
