import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "About Me", "Family & Relationships", 
                                       "Hobbies & Interests", 
                                      "Summary", "Contact"])

# Home Page
image = Image.open("images/pfp.jpg")
image = image.resize((500, 500))  # Adjust the size as needed

# Display the resized image

if page == "Home":
    st.title("Welcome 🤩")
    st.write("""
    Hello! I'm Joshua E. Briones, my friends call me "Josh", and this is my personal autobiography website. 
    I've created this space to share my journey, experiences, and thoughts with you. 
    Explore my life story, achievements, hobbies, and more through the sections provided.
    """)
    st.image(image, use_column_width=False)
    # st.image("images/pfp.jpg", use_column_width=True)
    st.write("Feel free to navigate through the menu to learn more about me! 🤗")

# About Me
elif page == "About Me":
    st.title("About Me")
    
    st.header("Early Life")
    st.write("""
    I was born in Greenhills, San Fernando, Cebu, far from the bustling city life, where I spent most of my childhood exploring nature and developing a deep appreciation for the outdoors. Growing up, I was always curious about how things worked and would often take things apart to understand their inner mechanisms. Whether it was a toy, a gadget, or even a simple household item, I was fascinated by the idea of how pieces came together to form a functioning whole. This innate curiosity laid the foundation for my passion for learning and discovery, guiding me through my educational journey and into the career path I would eventually pursue.

Despite the rural setting, my childhood was rich with experiences that shaped my character and values. The close-knit community and strong family bonds taught me the importance of relationships, responsibility, and perseverance. Ever since, I have always seek new knowledge and  strive for excellence.

As I grew older, my interests expanded beyond the confines of my small town. I developed a keen interest in technology and science, inspired by the endless possibilities they offered to solve real-world problems. This passion eventually led me to pursue formal education in these fields which I am currently taking (BSIT), marking the beginning of an exciting journey that would take me far from my humble beginnings.
    """)
    st.image("images/oldpic.jpg", caption="A snapshot from my early years", use_column_width=True)
    
    st.divider()
    st.header("Education")
    st.write("""
    My educational journey from gradeschool to high school was spent in Greenhills, San Fernando. I pretty much grew up in this place. I graduated from Greenhills Elementary School in 2014 and Greenhills National High School in 2018. I then transferred to CIT - U for senior highschool and after graduating I then pursued my college degree in Bachelor of Science in Information Technology in the same school. I am currently in my 4th year of college.
    """)
    st.map(pd.DataFrame({
        'lat': [10.2944808],
        'lon': [123.8785591]
    }), zoom=10)
    
   

# Family & Relationships
elif page == "Family & Relationships":
    st.title("Family & Relationships")
    st.write("""
    I come from a supportive family who have always been there for me. My parents, siblings, and relatives have had a strong influence on my life. I’m also grateful for the loving support of my friends and girlfriend.
    """)
    st.image("images/family.jpg", caption="My Family", use_column_width=True)
    
    st.subheader("Family Tree")
    family_data = {'Name': ['Nestor Briones', 'Edna Briones', 'Jhanin Briones', 'Jhoana Mae Briones', "Jelena Briones", 'Joshua Briones'], 
                   'Relation': ['Father', 'Mother', 'Eldest sibling', 'Second eldest', 'Third eldest', 'Me']}
    st.table(pd.DataFrame(family_data))



# Hobbies & Interests
elif page == "Hobbies & Interests":
    st.title("Hobbies & Interests")
    st.write("""
    In my free time, I enjoy a variety of activities that keep me engaged and happy. 
    Some of my favorite hobbies include:
    """)
    
    st.subheader("Playing Video Games 🎮")
    st.write("Gaming has been a passion of mine since childhood. I enjoy exploring virtual worlds and competing with friends. Games I've played are Dota 2, Crossfire, Genshin Impact, Minecraft, Call of Duty, COC, PUBG, and Mobile Legends.")
    st.image("images/dota2.jpg", caption="One of my favorite games", use_column_width=True)
    st.divider()

    st.subheader("Listening to Music 🎵")
    st.write("I enjoy listening to a wide range of genres, from pop and rock to classical and jazz.")
    st.image("images/band.jpg", caption="One of my favorite bands", use_column_width=True)
    st.divider()
    st.subheader("Traveling 🏖")
    st.write("Exploring new places and cultures is something I cherish.")
    st.map(pd.DataFrame({
        'lat': [9.2958145, 16.3992703, 15.0249205, 9.5201513, 14.5965778, 9.9043921],
        'lon': [123.2408675, 120.5475427, 120.3278504,123.3299344,120.9383599,125.8945466]
    }), zoom=5)
    st.divider()

    st.subheader("Watching Movies & TV Shows 🎬")
    st.write("I enjoy watching movies and TV shows in my free time. Some of my favorite genres are comedy,action, sci-fi, and fantasy.")
    image2 = Image.open("images/himym.jpg")
    image2 = image2.resize((450, 450)) 
    st.image(image2, caption="My all time favorite series", use_column_width=True)
    st.divider()

    st.subheader("Coding 💻")
    st.write("I love building things with code, whether it's a small script or a full-fledged application.")
    st.code("""
    def hello_world():
        print("Hello, World!")
        
    hello_world()
    """)


# Summary
elif page == "Summary":
    st.title("Summary")
    
    # Brief Introduction
    st.write("""
    Hi! I'm Joshua Briones, born on January 9, 2003. I'm 21 years old and currently pursuing a degree in Information Technology. 
    Despite being a shy person, I can be quite talkative and goofy around people I'm comfortable with. I have a deep passion for music, 
    particularly playing the guitar, and I also enjoy drawing in my free time. This summary section offers a glimpse into who I am and what I enjoy doing.
    """)
    
    # Hobbies Pie Chart
    st.subheader("My Hobbies")
    hobby_data = {
        "Playing Guitar": 15,
        "Drawing": 5,
        "Gaming": 40,
        "Listening to Music": 30,
        "Traveling": 10
    }
    hobbies = pd.DataFrame.from_dict(hobby_data, orient='index', columns=['Percentage'])
    st.write(hobbies)

    st.write("Here's a breakdown of how I typically spend my leisure time:")
    fig, ax = plt.subplots()
    ax.pie(hobby_data.values(), labels=hobby_data.keys(), autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#ffb3e6'])
    ax.axis('equal')
    st.pyplot(fig)

    # Education Timeline
    st.subheader("Education & Career Journey")
    st.write("""
    - **2009-2014**: Attended Greenhills Elementary School, San Fernando, Cebu.
    - **2014-2018**: Graduated from Greenhills National High School.
    - **2018-2020**: Senior High School at CIT-U, majoring in IT.
    - **2020-Present**: Pursuing a Bachelor of Science in Information Technology at CIT-U.
    """)
    
    # Personality Traits Radar Chart
    st.subheader("Personality Traits")
    st.write("Here's a visual representation of some of my key personality traits:")

    traits = {
        "Shyness": 8,
        "Talkativeness": 6,
        "Goofiness": 7,
        "Creativity": 9,
        "Curiosity": 8
    }
    
    trait_names = list(traits.keys())
    trait_values = list(traits.values())
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(trait_names, trait_values, color='blue', alpha=0.25)
    ax.plot(trait_names, trait_values, color='blue', linewidth=2)
    ax.set_ylim(0, 10)
    st.pyplot(fig)
    
    st.write("These charts offer a quick look into my hobbies and personality traits.")


# Contact
elif page == "Contact":
    st.title("Contact")
    st.write("Feel free to reach out to me via the following platforms:")
    
    st.write("Email: joshuabriones@gmail.com")
    st.write("LinkedIn: [joshua-briones2003](https://www.linkedin.com/in/joshua-briones2003/)")
    st.write("GitHub: [joshriones](https://github.com/yourprofile)")
    
    st.subheader("Send me a message")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Thank you for your message! I'll get back to you soon.")
