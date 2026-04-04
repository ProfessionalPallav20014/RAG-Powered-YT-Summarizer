import streamlit as st
import os
from youtube_transcript_api import YouTubeTranscriptApi
import ollama
from langchain_text_splitters import RecursiveCharacterTextSplitter

def build_prompt(chunk):
    return f"""
You are an AI assistant that summarizes YouTube transcripts.

STRICT RULES:
- Do NOT show reasoning, thinking, or explanations.
- Do NOT include tags like <think> or internal thoughts.
- Output ONLY the final answer.
- Keep it concise and structured.

TASK:
Summarize the following transcript clearly.

TRANSCRIPT:
{chunk}

OUTPUT FORMAT:
- Key Points (bulleted)
- Short Summary (3-4 lines)
"""

## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        yta_class=YouTubeTranscriptApi()
        transcript_data=yta_class.fetch(video_id)
        text_list=[snippet.text for snippet in transcript_data]

        transcript = " ".join(text_list)
        return transcript

    except Exception as e:
        raise e

## chunking the data
def chunk_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_text(text)
    return chunks

## summarizing the chunk
def summarize_chunk(chunk):
    response = ollama.chat(
        model="deepseek-r1:8b",
        messages=[
            {"role": "user", "content": build_prompt(chunk)}
        ],
        options={
            "temperature": 0.3
        }
    )
    return response['message']['content']

## combining all summaries
def summarize_video(youtube_video_url):
    transcript = extract_transcript_details(youtube_video_url)
    chunks = chunk_text(transcript)

    summaries = []
    for chunk in chunks:
        summaries.append(summarize_chunk(chunk))

    final_prompt = f"""
    Combine the following summaries into one final clean summary.
    
    RULES:
    - No thinking or explanation
    - Only final structured output
    
    {chr(10).join(summaries)}
    """

    final_summary = ollama.chat(
        model="deepseek-r1:8b",
        messages=[{"role": "user", "content": final_prompt}],
        options={"temperature": 0.2}
    )

    return final_summary['message']['content']

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Get Detailed Notes"):
    summary=summarize_video(youtube_link)
    st.markdown("## Detailed Notes:")
    st.write(summary)