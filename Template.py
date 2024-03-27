audio_prompts = {
    "lecture": '''Write a summary for a lecture on {topic}. 
    Write in paragraph and highlight important points with bullet points and headings, 
    in the end, highlight if any homework or assignment is provided. 
    Mention {endft} are used in a different paragraph.''',
    
    "call": '''Provide a summary of the call. Find the relationship between the caller and the callee.
    Highlight important points, key arguments, and any relevant background information. 
    In the end, Include key discussion points, decisions made, action items, and any follow-up required.
    Mention {endft} are used in a different paragraph.''',
    
    "recording": '''Provide a summary of the recorded audio. 
    Highlight important points, key arguments, and any relevant background information. 
    In the end, Include key discussion points, decisions made, action items, and any follow-up required.
    Mention {endft} are used in a different paragraph.''',
    
    "note": """Condense the information conveyed in the voice notes into a brief summary. 
    Capture the main ideas and messages conveyed, ensuring clarity and coherence.
    Mention {endft} are used in a different paragraph.""",
    
    "youtube": '''Summarize the content of the YouTube video on {topic}. 
    Begin with the channel name (if applicable) and Highlight main ideas, 
    key arguments, and any relevant statistics or examples mentioned.
    Mention {endft} are used in a different paragraph.''',
    
    "announcements": '''Write a summary of the announcements made on {topic}. 
    Highlight important dates, events, deadlines, and any actions required by the audience.''',
    
    "news": '''Write a summary of the news report in context of {topic}. 
    Include major headlines, key events, and any relevant background information or context provided.
    Mention {endft} are used in a different paragraph.''',
    
    "interview": '''Provide a summary of the interview for {topic}. 
    Highlight key questions asked, responses given, and any significant insights or conclusions drawn.
    In the end, finish this with your thoughts on the interview as if you were recruiter, 
    and include any recommendations or advice for the candidate for next interview.''',

    "group Discussion": '''Summarize the group discussion on {topic}. 
    Highlight key points, arguments presented by different participants, and any consensus reached.
    Include a brief overview of the topics discussed and the overall tone of the conversation.''',
    
    "webinar": '''Provide a summary of the {topic} webinar. 
    Highlight the main themes, key takeaways, and insights shared by the presenter(s) or speaker(s).
    Include any audience interaction or Q&A sessions if applicable.''',

    "workshop": '''Provide a summary of the {topic} Workshop. 
    Highlight the main themes, key takeaways, and insights shared by the presenter(s) or speaker(s).
    Include any audience interaction or Q&A sessions if applicable.''',
    
    "customer": '''Summarize the customer service interaction about {topic}.
    Include details of the customer's inquiry or issue, 
    the agent's response, and any resolutions or follow-up actions discussed. 
    Highlight key points of contention or areas requiring further clarification.''',
    
    "service": '''Summarize the service interaction about {topic}.
    Include details of the inquiry or issue, 
    the agent's response, and any resolutions or follow-up actions discussed. 
    Highlight key points of contention or areas requiring further clarification.''',
    
    "podcast": '''Write a summary for the {topic} podcast episode. 
    Highlight the main topics discussed, key insights shared by the host(s) or guest(s), 
    and any memorable quotes or anecdotes. Include a brief overview of the episode's structure and format.
    Mention examples, names or characters that have been mentioned in the episode.''',
    
    "legal": '''Provide a summary of the legal transcription related to {topic}. 
    Highlight key arguments, rulings, and legal precedents discussed during the proceedings. 
    Include relevant case details, witness testimonies, and court decisions.''',
    
    "therapy": '''Summarize the therapy session on {topic}. 
    Highlight key topics addressed, therapeutic interventions used, 
    and any breakthrough moments or emotional revelations. 
    Include a brief overview of the client's background and therapy goals.''',
    
    "confession": '''Write a summary of the confessional statements made by the accused in relation to {topic}.
    Highlight admissions of guilt, remorse, or mitigating circumstances presented by the accused.
    Include any relevant details regarding the alleged offense and the legal context surrounding the confession.''',

    "cv" : '''Provide a summary of the CV for {topic}. Highlight the candidate's education, 
    work experience, skills, and accomplishments. 
    Include key details such as job titles, companies worked for, and academic achievements.''',
    
    "resume": '''Summarize the resume for {topic}. Highlight the candidate's professional summary,
    work history, skills section, and relevant certifications. 
    Include any notable achievements or awards mentioned in the resume.''',
    
    "article": """Summarize the article, highlighting the main points on {topic}, arguments, and conclusions. 
    Provide a succinct overview that captures the essence of the content.""",

    "biodata": '''Write a summary for the biodata for {topic}. 
    Highlight key personal details, family background, educational qualifications, and career aspirations.
    Include any hobbies, interests, or extracurricular activities mentioned in the biodata.''',

    "email": '''Imagine you're dictating an email to your personal assistant on {topic}. 
    Below is the content of the email, you need to provide a concise summary of the main points. 
    End with a clear call to action or next steps.
    Highlight key points, any relevant background information.''',

    "meeting": """Provide a summary of the meeting discussions on {topic}, 
    focusing on decisions made, action items assigned, and any important topics covered.
     Keep the summary concise and informative.""",

    "story": """Create a summary of the below story, capturing the main plot points,
    characters, and themes. Craft a concise overview that gives a sense of the narrative arc and key events.""",

    "code": "Summarize the code snippet provided, highlighting the key functionalities and any potential optimizations. Describe applications.",

    "program": "Generate a concise summary of the program's functionality, including its main features and intended usage.",

    "presentation": "Provide a brief overview of the presentation, highlighting the main points covered and any key insights presented."
}

topic = 'some topic'