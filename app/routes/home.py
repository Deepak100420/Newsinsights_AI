import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from streamlit_lottie import st_lottie
from backend.functions import load_animation

# Set up page configuration
st.set_page_config(page_title="Newsglance AI", page_icon="📰", layout="wide")

# CSS for custom styles




# Centered title and subtitle using HTML with Streamlit
st.markdown("<h1 style='text-align: center; font-family: Roboto   '>📰 Newsglance AI</h1>", unsafe_allow_html=True)

st.write("----")
#st.markdown("<h1 style='text-align: center; color: black;'>Real-Time News Insights</h1>", unsafe_allow_html=True)


col1,col2= st.columns(spec=[2,1])

with col1:
    st.markdown("""
    <style>
    .big-fontt {
        font-size: 20px;
    }
    </style>
    
    <div class="big-fontt">
    Welcome to <strong>Newsglance AI</strong>, the ultimate platform for staying up-to-date with the latest news from around the world. 
    Our innovative tool combines cutting-edge <strong>large language models (LLMs)</strong> with real-time news aggregation to deliver 
    the information you need in a concise, personalized, and user-friendly format. 
    
                
    Whether you're a news enthusiast, a professional, or someone who simply wants to stay informed, Newsglance AI 
    ensures you never miss out on the latest updates. Explore news filtered by <strong>country</strong> and **category**—from politics 
    and sports to entertainment and technology. Our platform leverages **Google News** as a reliable source and summarizes 
    articles into easy-to-read, bite-sized insights using state-of-the-art AI technology.

   
    Let Newsglance AI redefine the way you consume news—one click, one insight, one story at a time.
    
    </div>
""", unsafe_allow_html=True)
    
with col2:
    lottie=load_animation("assets/ai.json")

        

    st_lottie(
            lottie,speed=2
        )
     






st.write("------")





#st.markdown("<h1 style='text-align: center; font-family: Roboto   '>:blue[Newsglance AI]</h1>", unsafe_allow_html=True)

with st.container():
    

    col3,col4=st.columns(spec=[1.5,1],vertical_alignment="center",gap="small",border=False)

    with col3:
        st.subheader("🌟 _:blue[Why Choose Newsglance AI?]_",anchor=False)
        
        st.markdown("""
            <style>
            .big-font {
                font-size: 20px;
            }
            </style>
            
            <div class="big-font">
            
           **🌍Country-Wise News**  
            Get instant updates from the country of your choice.
            
            **🔍 Personalized Insights**  
            Browse topics like politics, sports, entertainment, technology, health, and business.
            
            **🤖 AI-Generated Summaries**  
            Save time with summaries that deliver key takeaways from lengthy articles.
            
            **📈 Real-Time Updates**    
            Stay ahead with automatic refreshes that bring you the latest stories as they happen.
                    
            **🔗 Reliable Sources**    
            Aggregated content from trusted platforms like Google News.
            
            </div>
        """, unsafe_allow_html=True)
    with col4:
        
            

        lottie=load_animation("assets\Animation2.json")

        

        st_lottie(
            lottie,speed=2
        )



st.write("---")




