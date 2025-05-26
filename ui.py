import streamlit as st

#page configuration
def setup_ui(reset_chat,remove_file,extract_text_from_file):
    # set page config
    st.set_page_config(
        page_title="Date AI Chatbot",
        page_icon=":robot:",
        layout="wide" 
    )
    
    #apply  custom css
    apply_custom_css()
    
    # sidebar elements
    with st.sidebar:
        st.title("Date AI Chatbot")
        st.markkdown("---")
        
        # language selection
        languages = {
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Russian": "ru",
            "Hindi": "hi" 
        }
        selected_language = st.selectbox("Select Language", list(languages.keys()),index=0)
        
        st.session_state.language = languages[selected_language]
        
        # file upload
        uploaded_file = st.file_uploader("Upload additional documents", 
                                         type=["pdf", "txt","md","html", "docx"],
                                         help="Upload files to enhance the AI's knowledge base.")
        
        if uploaded_file:
            file_text = extract_text_from_file(uploaded_file)
            if file_text:
                file_info = {
                    "name": uploaded_file.name,
                    "content": file_text
                }
                if file_info not in st.session_state.uploaded_files:
                    st.session_state.uploaded_files.append(file_info)
                    st.session_state.knowledge_updated = True
                    st.success(f"Added '{uploaded_file.name}' to knowledge base")
                    
                    
                # show uploaded files
                if st.session_state.uploaded_files:
                    st.markdown("### Uploaded Files")
                    for i,file_info in enumerate(st.session_state.uploaded_files):
                        st.markdown(f"**{i+1}. {file_info['name']}**")
                        remove_button_key = f"remove_file_{i}"
                        if st.button(f"Remove {file_info['name']}",
                        key=remove_button_key):
                            remove_file(i)
                            
                # reset chat button
                if st.button("Resett chat",key="reset_chat"):
                    reset_chat()

# avatar images
def get_avatar_html(avatar_type):
    if avatar_type == "user":
        avatar_url = "https://api.dicebear.com/7.x/personas/svg?seed=user"
    else:
        avatar_url = "https://api.dicebear.com/7.x/bottts/svg?seed=techease" 
                        