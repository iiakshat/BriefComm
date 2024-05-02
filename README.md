# BriefComm

Keep the comm. brief.

## Approach

The approach for the BriefComm project involves a multi-step process to efficiently summarize audio content. Initially, raw text, audio, or video files are accepted as input. These files are then processed using an OpenAI's model called [Whisper](https://github.com/openai/whisper) for transcription, converting the audio content into text. The transcribed text is then processed further, potentially being translated into different languages using translation services. Next, the processed text is fed into an AI model by META called [Llama2](https://llama.meta.com/llama2/), which is fine-tuned for summarization tasks. Llama2 generates concise and coherent summaries of the input text. Finally, the summarized output is displayed on a webpage, allowing users to easily access and utilize the key insights and information extracted from the original audio content. This approach streamlines the process of summarizing audio content, enabling users to efficiently extract valuable insights for various applications and use cases.

## How to use BriefComm?

Visit [Hugging Face Space]() or Run locally using:
```
git clone https://github.com/iiakshat/BriefComm.git
```
and then, running:
```
pip install -r requirements.txt
```

- Once you run the above commands, you should see this interface:
![1](https://github.com/iiakshat/BriefComm/assets/92530735/cb3e1bdb-6a62-4a5e-9ee0-6accd8e3959c)

- Click on $submit$ after giving input,
![2](https://github.com/iiakshat/BriefComm/assets/92530735/7f31e776-e1ff-4732-a94d-9ba5c6f3a3dc)

- $(Optional)$ Enter additional details, choose output language and enter email (email doesn't work),
![5](https://github.com/iiakshat/BriefComm/assets/92530735/48136bee-98bd-4deb-a4be-5c8d18dc1573)

- Hit $Submit$ and you should see the output as:
  ![7](https://github.com/iiakshat/BriefComm/assets/92530735/69d7e153-da76-4760-9a82-7bd87a3fe834)
  
