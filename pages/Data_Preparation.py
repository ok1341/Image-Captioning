import streamlit as st

st.markdown("<h1 style='text-align: center'> Our Data Preparation Process</h1>", unsafe_allow_html=True)

with st.expander("Data Understanding"):
    st.write("""To train, validate and test the model, we were first provided with the LAION dataset, which is available to us as a CSV file. With 240 TB, 
             this is currently the largest freely accessible image-text dataset in the world. Due to the often inaccurate captions and vague image content,
             we searched for other, more suitable datasets to form the basis of our project. After research, we decided on the Flickr dataset, which stores 
             images and captions separately. The dataset contains high-quality images with varying content, but all can be meaningfully classified.
             2-3 Beispiel Bilder zeigen aus flickr einfügen """)