import Template
import os
import logging
from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate


groq_api_key=os.getenv('GROQ_API_KEY')

llm = ChatGroq(groq_api_key=groq_api_key, model='llama3-8b-8192')

log = logging.getLogger(__name__)
log.info("Model Loaded Successfully.")

    
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
        template=f''' [INST] <<SYS>>  Write in paragraph on {topic} and highlight important points with bullet points and headings,
            In the end, highlight if any {end_feature} is provided for a {category}. Using this Text : <</SYS>>''' + '{transcript}[/INST]'
        
    prompt = ChatPromptTemplate.from_template(template)
    log.debug('Prompt Created.')

    llm_chain = prompt | llm

    log.debug('Generating Response.')
    response = llm_chain.invoke({"transcript":transcript})

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
        f.write(RESPONSE.content)

def summarize_text(text, topic='The context of transcript', category='transcript', filename='', endft=''):
    log.debug('Reading file.')
    RESPONSE = getResponse(text, topic=topic, category=category, end_feature=endft).content

    try:
        log.info('Clearing temporay files.')
        delete_temprory_files(filename, 'temp', 'txt')
        delete_temprory_files(filename, 'temp', 'mp3')

    except:
        log.error("Couldn't delete temprory files")

    return RESPONSE

def delete_temprory_files(filename, folder, ext):
    file_ = os.path.join(folder, filename) + ext
    os.remove(file_)



query = '''
A stack is an Abstract Data Type (ADT), commonly used in most
 programming languages. It isnamedstackas itbehaves likeareal-world
 stack,forexample–adeckofcardsorapileofplates,etc.
 • ADT-TheDataTypeisbasicallyatypeofdatathatcanbeusedindifferent
 computerprogram. Itsignifiesthetypelikeinteger,floatetc,thespacelike
 integerwilltake4-bytes,characterwilltake1-byteofspaceetc.
 ADT Stack and its operations:
 Image source : Google
• Theabstractdatatypeisspecialkindofdatatype,whosebehavior isdefined
 byasetofvaluesandsetofoperations.Thekeyword“Abstract”isusedaswe
 canusethesedatatypes,wecanperformdifferentoperations.Buthowthose
 operationsareworkingthatistotallyhiddenfromtheuser.TheADTismadeof
 withprimitivedatatypes,butoperationlogicsarehidden.
 ADT Stack and its operations:
• A real-world stack allows operations at one end only. For example, we can 
place or remove a card or plate from the top of the stack only. Likewise, Stack 
ADT allows all data operations at one end only. At any given time, we can only 
access the top element of a stack.
 • This feature makes it LIFO data structure. LIFO stands for Last-in-first-out. 
Here, the element which is placed (inserted or added) last, is accessed first. In 
stack terminology, insertion operation
'''
print(summarize_text(query))