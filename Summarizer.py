from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains.llm import LLMChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import Template
import os
import logging

log = logging.getLogger(__name__)
    
def getResponse(transcript, topic, category='transcript',
                end_feature='date and places'):
    
    word_count = len(transcript.split())   
    print(word_count)    
    thres_hold = 50

    log.debug(f'Words in Text: ' + str(word_count))

    if word_count < thres_hold:
        log.warning(f'Cannot Generate Summary. Text is too short.')
        return {'text':'Provided text is too short to summarise.'}
    
    category = category.lower() 

    llm = CTransformers(
    model = "TheBloke/Llama-2-7B-Chat-GGML",
    model_file = "llama-2-7b-chat.ggmlv3.q2_K.bin",
    callbacks = [StreamingStdOutCallbackHandler()],
    config = {'context_length' : 4096, 'max_new_tokens' : 2048}
    )

    log.info("Model Loaded Successfully.")

    cat = ''
    for key in category.split():
        if key in Template.audio_prompts:
            cat = key
            log.debug(f"Using Pre-defined Template for {cat}.")
            break

    if cat:
        Template.topic = topic
        template = f'''
            [INST] <<SYS>> 
            {Template.audio_prompts.get(cat).format(topic=Template.topic, endft=end_feature)} 
            Using this transcript : <</SYS>>''' + '{transcript}[/INST]'

    else:
        template = f'''
            [INST] <<SYS>>
            Write a summary for a {category}, {topic}.
            Write in paragraph and highlight important points with bullet points and headings,
            In the end, highlight if any {end_feature} is provided. Using this Text : <</SYS>>''' + '{transcript}[/INST]'
        
    prompt = PromptTemplate(input_variables=['transcript'],
                            template=template)
    
    log.debug('Prompt Created.')
    llm_chain = LLMChain(
    prompt = prompt,
    llm = llm
    )

    log.debug('Generating Response.')
    response = llm_chain.invoke(transcript)

    log.info('Response Generated.')
    return response
    
def save_summary(filename, topic='some topic', category='lecture', end_feature='homework or assignment'):

    with open(f'temp/{filename}.txt', 'r', encoding='utf-8') as f:
        
        log.debug('Reading to {filename}.txt')
        transcript = f.read()

    with open(f'temp/{filename}.txt', 'a', encoding='utf-8') as f:
        RESPONSE = getResponse(transcript, 
                            topic=topic,
                            category=category, 
                            end_feature=end_feature)
        
        log.info('Writing to {filename}.txt')
        f.write(RESPONSE['text'])

def summarize_text(text, topic='The context of transcript', category='transcript', filename='', endft=''):
    log.debug('Reading file.')
    RESPONSE = getResponse(text, topic=topic, category=category, end_feature=endft)['text']

    try:
        log.info('Clearing temporay files.')
        delete_temprory_files(filename, 'temp', 'txt')
        delete_temprory_files(filename, 'temp', 'mp3')

    except:
        log.error("Couldn't delete temprory files")

    return RESPONSE

def delete_temprory_files(filename, folder, ext):
    os.remove(f'{folder}/{filename}.{ext}')
