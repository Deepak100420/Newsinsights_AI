import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.category_filter import output
from backend.functions import load_animation

import streamlit as st
from streamlit_lottie import st_lottie





st.set_page_config(
    page_title="NewsGlance AI",
    page_icon=":newspaper:",
    layout="wide",
    initial_sidebar_state="auto"
)




title = "📰 Newsglance AI"
st.markdown(f'<h1 style="text-align: center;font-family: Roboto">{title}</h1>', unsafe_allow_html=True)


st.write("---")



# List of categories
categories = [
    "Politics", "Sports", "Business", "Technology", "Entertainment", "Science",
    "Health", "Environment", "Education", "Crime", "World News", "Local News",
    "Weather", "Lifestyle", "Travel", "Finance", "Cultural Events",
    "Social Issues", "Disasters and Accidents", "Obituaries"
]

 # Default selection
countries = ["Select",
    "India", "United States", "United Kingdom", "Canada", "Australia", "Germany", 
    "France", "Japan", "South Korea", "China", "Brazil", "Russia", "Italy", "Spain", 
    "Mexico", "Indonesia", "Netherlands", "Saudi Arabia", "South Africa", "Argentina"
]

# "with" notation
with st.sidebar:
    st.title("🌐 Customize Your News")
    option = st.selectbox(
    "Select country for current news :world_map:",
    options=countries,
)



    add_radio = selected_category = st.pills("Select Area of Interest :fire:", categories, selection_mode="single")


    
    submit_container=st.container(border=False)
    with submit_container:
        aa=st.button("Submit", type="primary",icon=":material/upload:")
       # st.write("Click submit")


    

with st.sidebar:
    with st.container(border=True):
        
        chat=st.chat_input("Enter Your Query")



if chat:
    result = output(query=chat)

    # Loop through each item in the result
    for article in result:
        with st.container(border=True):
            # Display the headline
            st.subheader(f'_:blue[{article['title']}]_',  divider="gray",anchor=False)
            
            # Display the summary
            st.write(article['summary'])
            
            if 'link' in article and article['link']:
                st.write(f":link: [:red[Read the full article]]({article['link']})")




elif aa:

    if option == "Select":
        with submit_container:
            st.write("Please Select the country")

        with st.container():
            col5,col6=st.columns(spec=[2,1],border=False,vertical_alignment="top")
            
            with col5:

                
                st.subheader("🚀 _:blue[ **How It Works?**]_",anchor=False)

                

                st.markdown(
        """
    <style>
    .big-font {
        font-size: 18px;
        line-height: 1.8;
        
        text-align: center;
    }
    .progress-arrow {
        font-size: 24px;
        color: #007BFF; /* Blue color for arrows */
        font-weight: bold;
        display: inline-block;
        margin: 0 10px;
    }
    .or-section {
        font-size: 18px;
        
        text-align: center;
        margin: 10px 0;
    }
    .search-section {
        font-size: 18px;
        line-height: 1.8;
       
        text-align: center;
    }
    </style>
    
    <div class="container">
        <div class="big-font">
            <strong>👆🏻 Select Your Country</strong>
            <strong class="progress-arrow">➔</strong>
            <strong>💖 Pick Your Favorite Topics</strong>
            <strong class="progress-arrow">➔</strong>
            <strong>⚒️ AI Does the Work</strong>
        </div>
        <div class="or-section">
            <strong>OR</strong>
        </div>
        <div class="search-section">
            <strong>🔍 Simply Search for What You Need</strong>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )



            with col6:

                lottie=load_animation("assets/ai2.json")

                    

                st_lottie(
                        lottie,speed=2
                    )



    elif option != "Select":
        result = output(query=option + (add_radio if add_radio else ""))

        # Loop through each item in the result
        for article in result:
            with st.container(border=True):
                # Display the headline
                st.subheader(f'_:blue[{article['title']}]_',  divider="gray",anchor=False)
                
                # Display the summary
                st.write(article['summary'])
                
                if 'link' in article and article['link']:
                    st.write(f":link: [:red[Read the full article]]({article['link']})")



    
else:
    

    with st.container():
            col5,col6=st.columns(spec=[2,1],border=False,vertical_alignment="top")
            
            with col5:

                
                st.subheader("🚀 _:blue[ **How It Works?**]_",anchor=False)

                import streamlit as st

                st.markdown(
        """
    <style>
    .big-font {
        font-size: 18px;
        line-height: 1.8;
       
        text-align: center;
    }
    .progress-arrow {
        font-size: 24px;
        color: #007BFF; /* Blue color for arrows */
        font-weight: bold;
        display: inline-block;
        margin: 0 10px;
    }
    .or-section {
        font-size: 18px;
       
        text-align: center;
        margin: 10px 0;
    }
    .search-section {
        font-size: 18px;
        line-height: 1.8;
        
        text-align: center;
    }
    </style>
    
    <div class="container">
        <div class="big-font">
            <strong>👆🏻 Select Your Country</strong>
            <strong class="progress-arrow">➔</strong>
            <strong>💖 Pick Your Favorite Topics</strong>
            <strong class="progress-arrow">➔</strong>
            <strong>⚒️ AI Does the Work</strong>
        </div>
        <div class="or-section">
            <strong>OR</strong>
        </div>
        <div class="search-section">
            <strong>🔍 Simply Search for What You Need</strong>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )



            with col6:

                lottie=load_animation("assets/ai2.json")

                    

                st_lottie(
                        lottie,speed=2
                    )








    


