import streamlit as st

st.markdown("<h1 style='text-align: center'> Our Data Preparation Process</h1>", unsafe_allow_html=True)

with st.expander("Information in advance"):
    st.write("""At the beginning of the project, each of us had chosen a different approach or model, so we could later decide on the best one.
             Since the current module was already excellently pre-trained, the following process refers to a different model that was just less precise.
             The model can also be found in the Github repository.""")

with st.expander("Data Understanding"):
    st.write("""To train, validate and test the model, we were first provided with the LAION dataset, which is available to us as a CSV file. With 240 TB, 
             this is currently the largest freely accessible image-text dataset in the world. Due to the often inaccurate captions and vague image content,
             we searched for other, more suitable datasets to form the basis of our project. After research, we decided to use the Flickr dataset, which stores 
             Images and captions stored separately. The dataset contains high-quality images with varying content, but all can be meaningfully classified.""")

with st.expander("Data Selection"):
    st.write("""As explained in the previous step, we used the Fickr 8k dataset. This consists of 8,000 images, which is the total amount we used for training, 
             validation and testing.""")


with st.expander("Data Cleaning"):
    st.write("""Since the Flickr dataset is already designed for our use case, including the image caption, we had to do very little preparation of the data.
             For each image, there are 5 different exact captions that we loaded into the dictionary, using the image as the key and the caption as the value.
             In addition, the captions were written in lowercase letters. In the LAION dataset I had tried before, the situation was different. 
             There we cleaned up the captions for English, NSFW, a maximum length for the captions, and matching keywords.""")

with st.expander("Feature Engineering"):
    st.write("""For feature engineering, the Inception V3 transfer learning model was provided, which used the pre-trained weights from the image network dataset.""")


with st.expander("Data Splitting"):
    st.write("""Of the total 8,000 images, we used 5,000 (62.5%) for training, 2,000 (25%) for validation, and 1,000 (12.5%) for testing.
             This was due to the storage capacities in Streamlit and the training effort.""")
