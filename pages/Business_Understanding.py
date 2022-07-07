import streamlit as st

st.markdown("<h1 style='text-align: center'>Our Business Understanding Process</h1>", unsafe_allow_html=True)
st.markdown("""<p style='text-align: center'>While many teams hurry through this phase, establishing a strong business understanding
         is like building the foundation of a house – absolutely essential.</p>""", unsafe_allow_html=True)


with st.expander("Motivation"):
    st.write("""What was our motivation? We are excited about machine learning in relation to visual challenges,
    for example autonomous driving, which can provide more safety on the road. For this reason, we really wanted to create an application in the field
    of caption generation and specifically asked for another group.Through the project, we hoped to be able to practically apply our theoretical foundations
    and expand our knowledge in the field of image recognition and captioning.""")

with st.expander("Determining Business Objectives"):
    st.write("""We had many ideas at the beginning, which typically had to be modified during the course of the project due to factors such as time,
             feasibility and difficulty. The goal was, of course, to train a model that could generate captions as accurately as possible.
             Finding a pre-trained model as well as fine-tuning and transferring it into the Streamlit application also turned out to be
             more difficult than expected in some cases. Nevertheless, in the end we can now present a relatively good model with 
             some features to involve the user in the application.""")

with st.expander("Assess Situation"):
    st.write("""In advance, of course, we thought about what resources we would need and what problems we might encounter.
            For the research, Google Schoolar and Papers with code were of great importance, of course. Software-wise, we relied on
            Kaggle, TensorFlow, Pycharm, and Jupyter, among others. Concrete libraries that we used for the implementation were of course Streamlit and Torch.
            We identified the quality of the images and captions provided with the initial LAION dataset as a potential problem. """)

with st.expander("Determine Data Mining Goals"):
    st.write("""We have not set ourselves a specific technical target. First of all, it was important for us to build up an understanding
             and consequently to have a model that can roughly recognize the image content in a comprehensible way. Based on this, we definitely
             wanted to include the user as well as some features. """)

with st.expander("Product Projekt Plan"):
    st.write("""We designed our project plan to be relatively flexible. We had set ourselves certain deadlines early on, divided up tasks among ourselves accordingly,
             and consulted at least weekly to see how things were going with the current development. Roughly speaking, it was a matter of first doing research,
             preparing the data, training a model and finally evaluating it. Of course, there were always problems along the way, which we solved together. """)