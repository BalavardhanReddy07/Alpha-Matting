import streamlit as st
from rembg import remove
from PIL import Image 

def main():
    st.title("Alpha Matting")
    uploaded_file = st.file_uploader(label="Upload an image",type=['png','jpg','jpeg'],accept_multiple_files=False)
    if st.button("Generate"):
        img = Image.open(uploaded_file)
        output = remove(img)
        st.toast("Completed",icon='🫡')
        col1,col2 = st.columns(2,gap='small')
        with col1:
            st.write("# Original Image")
            st.image(img)
        with col2:
            st.write("# Result Image")
            st.image(output)
    


if __name__ == "__main__":
    main()