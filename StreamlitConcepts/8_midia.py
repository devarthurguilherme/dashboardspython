import streamlit as st
# from PIL import image

st.header("Image")
img = 'StreamlitConcepts\meusArquivos\img2.jpg'
st.image(img, caption='Sunrise by the mountains')

st.header("Audio")
st.audio("StreamlitConcepts\meusArquivos\in-slow-motion-inspiring-ambient-lounge-219592.mp3",
         format="audio/mpeg", loop=True)

st.header("Video")
VIDEO_URL = 'StreamlitConcepts\meusArquivos\jideo1.mp4'
st.video(VIDEO_URL)
