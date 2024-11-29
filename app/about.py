import streamlit as st

def show_about():
    st.sidebar.title("About")

    st.sidebar.header("Welcome to Tris - A Tic Tac Toe Multiplayer game")
    st.sidebar.markdown("""
    This interactive multiplayer game was created as a demonstration of real-time 
    interaction capabilities using Python and Streamlit. <br>Also it was fun to build a 
    simple game in this way.
    """, unsafe_allow_html=True)

    st.sidebar.header("About the Developer")
    st.sidebar.write("""
    I'm Fabio Grasso, a passionate software engineer that loves creating Streamlit UI 
    for data applications.
    """)

    st.sidebar.header("Contact & Connect")
    st.sidebar.write("""
    I'd like to hear your thoughts about this project, you can reach me through:
    """)
    
    st.sidebar.link_button("🌐 Website", "https://fabiogra.com", use_container_width=True)
    st.sidebar.link_button("💼 LinkedIn", "https://linkedin.com/in/fabio-grasso", use_container_width=True)
    st.sidebar.link_button("🐱 GitHub", "https://github.com/fabiogra", use_container_width=True)

    st.sidebar.header("Contributing")
    st.sidebar.write("""
    This project is open source! If you'd like to contribute or check out the code, 
    visit the repository:
    """)
    st.sidebar.link_button("GitHub Repository", "https://github.com/fabiogra/tris", use_container_width=True)
