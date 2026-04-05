import streamlit as st
from dotenv import load_dotenv

load_dotenv() ##load all the environment variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv(dotenv_path="Env.env")

# create a .env file and store your api into it
# or you can simply use this
# genai.configure(api_key="enteryourapikey")
genai.configure(api_key=os.getenv("MY_GEMINI_KEY"))

prompt="""
    You are a precise video assistant. Use the provided transcript to fulfill the user's request.
    
    TRANSCRIPT:
    {transcript_text}
    
    RULES:
    1. If the user asks to "summarize", provide a concise summary of the key points.
    2. If the user asks a specific question, answer it directly using ONLY the transcript and your UNDERSTANDING based on the video.
    3. Do NOT use any introductory fillers like "Sure," "Based on the video," or "Here is your answer."
    4. If the answer is not related to the transcript or video, state: "The video does not mention this." and if it's related then answer the question with the best possible conclusions or answer based on the understanding of the video and try not to go off topic.
    5. You can also introduce some possible theories related to the video if you don't find any useful answer from the video which is necessary to answer the question.
    """

## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        yta_class=YouTubeTranscriptApi()
        # transcript_list=yta_class.list(video_id)
        transcript_data=yta_class.fetch(video_id, languages=['en','hi'])

        # Needs improvement, coming soon!
        # try:
        #     transcript_data=yta_class.fetch(video_id)
        # except:
        #     transcript_list=yta_class.list(video_id)
        #     required_transcript=transcript_list.find_transcript(['hi'])
        #     transcript_data=required_transcript.translate('en')

        text_list=[snippet.text for snippet in transcript_data]

        transcript = " ".join(text_list)
        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini 2.5 Flash
def generate_gemini_content(transcript_text,prompt,user_query):

    model=genai.GenerativeModel("gemini-2.5-flash")
    response=model.generate_content(f"{prompt+transcript_text}\n\nUSER REQUEST: {user_query}")
    # response=model.generate_content(prompt+transcript_text)
    return response.text

st.title("YouTube Video Assistant")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    # print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

    user_query=st.text_input("Enter your query:")
    if st.button("Get Answer"):
        if not user_query:
            st.error("Please enter the required query!")
        else:
            with st.spinner("Processing video..."):
                transcript_text=extract_transcript_details(youtube_link)
                if transcript_text:
                    response=generate_gemini_content(transcript_text,prompt,user_query)
                    st.markdown("## Response:")
                    st.write(response)