import os
import logging
from faster_whisper import WhisperModel
from dotenv import load_dotenv
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Your code that uses OpenMP or calls libraries using OpenMP



log = logging.getLogger(__name__)
detected_lang = 'English'
def generate_transcript(filepath):

    global detected_lang
    filepath = filepath.translate(str.maketrans({'?': None, '|': None}))
    print("Looking for", filepath)
    
    filename = filepath
    with open(filename,'rb') as file:
        uploaded_file = file.read()
    
    model_size="large-v3"
    model=WhisperModel(model_size, device="cuda", compute_type="float16")
    transcription,info=model.transcribe("temp/Pursuit Of Happyness Iconic Speech.mp3",beam_size=5)
    print(transcription.text)
    for transcript in transcription:
        print("[%.2fs -> %.2fs] %s" % (transcript.start, transcript.end, transcript.text))
    result = transcription
    print(result)

    log.debug("Working Folder:", os.path.split(os.path.dirname(__file__))[-1])
    print("Working Folder:", os.path.split(os.path.dirname(__file__))[-1])

    detected_lang = result['language'].capitalize()
    print(detected_lang)
    transcript = result['text']

    output_path = f"temp/{filename}.txt"
    print(transcript)
    try:
        os.remove('temp'+filepath)
    except:
        log.warning("Could not remove audio")
    
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(transcript)

        return transcript
    
    except:
        return transcript
        
# To Update Model to latest version :
# pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

import os
print(os.listdir('temp'))
generate_transcript("temp/Pursuit Of Happyness Iconic Speech.mp3")