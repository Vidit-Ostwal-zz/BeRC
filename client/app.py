import  streamlit as st
from helper import get_matches,UI


# Layout
st.set_page_config(page_title="BeRC")
st.markdown(
    body=UI.css,
    unsafe_allow_html=True,
)
st.write(
    "<style>div.row-widget.stRadio > div{flex-direction:row; margin-left:auto; margin-right: auto; align: center}</style>",
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.markdown(UI.about_block, unsafe_allow_html=True)


st.title("Beat Recommender")

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    # to read files as bytes:
        bytes_data = uploaded_file.getvalue()
        
        matches = get_matches(bytes_data)
        
        if not matches:
            st.write("No matches found :(")
        
        for match in matches:
            st.audio(f"../{match['uri']}")