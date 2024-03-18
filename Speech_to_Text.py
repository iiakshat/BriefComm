import os
import whisper
from whisper.tokenizer import LANGUAGES
import logging

log = logging.getLogger(__name__)
detected_lang = 'English'
def generate_transcript(filepath):

    global detected_lang
    filepath = filepath.translate(str.maketrans({'?': None, '|': None}))
    print("Looking for", filepath)
    
    filename = filepath[:-4]
    model = whisper.load_model("small")

    log.debug("Working Folder:", os.path.split(os.path.dirname(__file__))[-1])
    print("Working Folder:", os.path.split(os.path.dirname(__file__))[-1])

    result = model.transcribe('temp/'+filepath, verbose=True, task='translate')

    detected_lang = LANGUAGES[result['language']].capitalize()
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
