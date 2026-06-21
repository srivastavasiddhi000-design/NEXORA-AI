import speech_recognition as sr
import tempfile
import os

from pydub import AudioSegment
from streamlit_mic_recorder import mic_recorder

AudioSegment.converter = r"C:\ffmpeg\ffmpeg-8.1.1-essentials_build\bin\ffmpeg.exe"
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\ffmpeg-8.1.1-essentials_build\bin"

import streamlit as st
from pypdf import PdfReader

from langchain_core.messages import HumanMessage, AIMessage
from main import ask_ai


st.set_page_config(
    page_title="NEXORA AI",
    page_icon="🤖",
    layout="wide"
)


st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Poppins:wght@300;400;600;700&display=swap');


*{
font-family:'Poppins',sans-serif;
}


.stApp{

background:
linear-gradient(
rgba(0,5,20,.55),
rgba(0,8,30,.75)
),
url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUQ5MFL2uwBPrbUx6JPMW8-AEPOzMM5DYgEe8hcYuJww&s=10");

background-size:cover;
background-position:center;
background-attachment:fixed;
}


#MainMenu, footer, header{
visibility:hidden;
}



.logo{

text-align:center;
font-family:'Orbitron';
font-size:72px;
font-weight:900;
letter-spacing:15px;
color:white;

text-shadow:
0 0 15px #00ffff,
0 0 40px #008cff,
0 0 90px #004cff;

}


.brain{
text-align:center;
margin-top:-20px;
}


.brain img{

width:95px;

filter:
drop-shadow(0 0 20px #00eaff)
drop-shadow(0 0 50px #0066ff);

animation:pulse 2s infinite;

}


@keyframes pulse{

0%{
transform:scale(1);
}

50%{
transform:scale(1.08);
}

100%{
transform:scale(1);
}

}



.glass{


background:
rgba(5,20,45,.55);

border:
1px solid rgba(0,220,255,.65);

border-radius:28px;

backdrop-filter:blur(30px);

box-shadow:

0 0 30px rgba(0,200,255,.35),
inset 0 0 25px rgba(255,255,255,.05);

padding:30px;

}



.card-title{

font-size:25px;
font-weight:700;
color:white;

}



.status{

color:#00ffae;
font-weight:700;

}



section[data-testid="stSidebar"]{

background:
rgba(0,10,30,.65)!important;

backdrop-filter:blur(30px);

border-right:
1px solid #00eaff;

}



[data-testid="stChatMessage"]{

background:
rgba(0,20,60,.55);

border:
1px solid rgba(0,220,255,.35);

border-radius:25px;

backdrop-filter:blur(20px);

}



[data-testid="stChatMessage"] *{

color:white!important;

}



div[data-testid="stChatInput"]{

background:
rgba(0,180,255,.18)!important;

border:
2px solid #00eaff!important;

border-radius:50px!important;

box-shadow:
0 0 35px #009dff;

}



div[data-testid="stChatInput"] textarea{

color:white!important;
font-size:17px!important;

}



.stButton button{

background:
linear-gradient(
135deg,
#00eaff,
#0066ff
);

border:none;

border-radius:30px;

color:white;

box-shadow:
0 0 25px #009cff;

}



[data-testid="stFileUploader"]{

background:
rgba(0,150,255,.15);

border-radius:25px;

border:1px solid #00eaff;

}


::-webkit-scrollbar{
width:5px;
}


::-webkit-scrollbar-thumb{

background:#00eaff;
border-radius:20px;

}

</style>
""", unsafe_allow_html=True)



st.markdown("""
<div class="brain">

<img src="https://static.vecteezy.com/system/resources/previews/053/964/142/non_2x/a-digital-representation-of-a-brain-connected-by-glowing-lines-and-nodes-symbolizing-neural-networks-and-cognitive-processes-png.png">

</div>


<div class="logo">
NEXORA
</div>


<h3 style="text-align:center;color:white;">
MULTI AI AGENT SYSTEM
</h3>


<p style="text-align:center;color:#00eaff;">
Think - Search - Analyze - Plan
</p>

""", unsafe_allow_html=True)



a,b,c = st.columns(3)

with a:

    st.markdown("""
    <div class="glass">

    <div class="card-title">
    🔍 Research Agent
    </div>

    <br>

    Web intelligence,
    analysis & deep search.

    <br><br>

    <span class="status">
    🟢 ONLINE
    </span>

    </div>
    """,unsafe_allow_html=True)



with b:

    st.markdown("""
    <div class="glass">

    <div class="card-title">
    📚 Knowledge Agent
    </div>

    <br>

    PDF understanding,
    summarization & insights.

    <br><br>

    <span class="status">
    🟢 ONLINE
    </span>

    </div>
    """,unsafe_allow_html=True)



with c:

    st.markdown("""
    <div class="glass">

    <div class="card-title">
    🚀 Planner Agent
    </div>

    <br>

    Task planning
    & execution.

    <br><br>

    <span class="status">
    🟢 ONLINE
    </span>

    </div>
    """,unsafe_allow_html=True)



# SESSION

if "messages" not in st.session_state:
    st.session_state.messages=[]


if "pdf" not in st.session_state:
    st.session_state.pdf=""



# SIDEBAR

with st.sidebar:

    st.markdown(
    """
    # ⚡ NEXORA AI

    ## 🤖 AGENTS

    🔍 Research Agent  
    🟢 Online

    📑 Summary Agent  
    🟢 Online

    🚀 Planner Agent  
    🟢 Online


    ## 📚 KNOWLEDGE BASE

    """
    )


    if st.button("💬 Chat"):

        st.rerun()


    if st.button("➕ New Chat"):

        st.session_state.messages=[]
        st.rerun()


    file = st.file_uploader(
        "Upload PDF",
        type="pdf"
    )


    if file:

        reader = PdfReader(file)

        text=""

        for page in reader.pages:

            text += page.extract_text() or ""


        st.session_state.pdf=text

        st.success("PDF Loaded ✅")





# CHAT HISTORY


for msg in st.session_state.messages:

    if isinstance(msg,HumanMessage):

        with st.chat_message("user"):
            st.write(msg.content)

    else:

        with st.chat_message("assistant"):
            st.write(msg.content)





# VOICE INPUT


voice = mic_recorder(

    start_prompt="🎤",
    stop_prompt="⏹",
    key="mic"

)



if voice:


    audio_bytes = voice["bytes"]


    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".webm"
    ) as f:

        f.write(audio_bytes)

        input_file=f.name



    output_file=input_file.replace(
        ".webm",
        ".wav"
    )


    sound = AudioSegment.from_file(
        input_file,
        format="webm"
    )


    sound.export(
        output_file,
        format="wav"
    )


    recognizer = sr.Recognizer()


    with sr.AudioFile(output_file) as source:

        audio = recognizer.record(source)



    try:


        text = recognizer.recognize_google(audio)


        answer = ask_ai(
            text,
            st.session_state.pdf
        )


        st.session_state.messages.append(
            HumanMessage(content=text)
        )


        st.session_state.messages.append(
            AIMessage(content=answer)
        )


        st.rerun()



    except:


        st.error(
            "Voice not detected 😭"
        )





# CHAT INPUT


prompt = st.chat_input(
    "Ask NEXORA anything..."
)



if prompt:


    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )


    with st.chat_message("user"):

        st.write(prompt)

      

    answer = ask_ai(
        prompt,
        st.session_state.pdf
    )



    st.session_state.messages.append(
        AIMessage(content=answer)
    )


    with st.chat_message("assistant"):

        st.write(answer)