import streamlit as st
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary
import random
import string
import requests
from streamlit_image_comparator import st_image_comparator

# Cloudinary Configuration
cloudinary.config(
    cloud_name=st.secrets['cloud_name'],
    api_key=st.secrets['api_key'],
    api_secret=st.secrets['api_secret'],
    secure=True
)

# Page Configuration
st.set_page_config(layout="wide", page_title="Pixify 🎨")

# Custom CSS for Buttons and Font
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #6C63FF;
        color: white;
        border-radius: 12px;
        font-family: 'Poppins', sans-serif;
        font-size: 16px;
    }
    .stMarkdown h1, h3 {
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize Session State
if "first_time" not in st.session_state:
    st.session_state.first_time = False

if not st.session_state.first_time:
    st.balloons()
    st.session_state.first_time = True

# Application Name and Tagline
st.markdown("<h1 style='text-align: center;'>Pixify 🎨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Transform Your Images Like a Pro!</h3>", unsafe_allow_html=True)

# Image Input Section
st.markdown("### Choose Your Input Method:")
input_method = st.radio("Select an option:", ['Upload an Image 📤', 'Take a Picture 📸'])

# Handle File Upload or Camera Input
my_upload = None
if input_method == 'Upload an Image 📤':
    my_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
elif input_method == 'Take a Picture 📸':
    my_upload = st.camera_input("Take a picture")

if my_upload is not None:
    # Tabs for Operations
    tabs = st.tabs(["Resize 🖼️", "Effects 🎨", "Layers ✍️"])

    # Resize Tab
    with tabs[0]:
        st.markdown("### Resize Your Image")
        operation = st.selectbox("Select a Resize Operation:", ['Scale', 'Limit Fit', 'Fill', 'Fit', 'Crop'])
        if operation:
            col1, col2 = st.columns(2)
            with col1:
                width = st.number_input("Width (px):", min_value=1, max_value=2000, value=500)
            with col2:
                height = st.number_input("Height (px):", min_value=1, max_value=2000, value=500)

            # Generate Random ID
            r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            image = upload(my_upload, public_id=f"pixify_{r}", width=width, height=height, crop=operation.lower())

            # Display Output Image
            st_image_comparator("Original Image", my_upload, image['url'])
            st.download_button(label="Download Resized Image", data=requests.get(image['url']).content, file_name="resized_image.jpg", mime="image/jpg")

    # Effects Tab
    with tabs[1]:
        st.markdown("### Apply Effects")
        effect = st.selectbox("Select an Effect:", ['Blur Faces', 'Grayscale'])
        if effect:
            # Generate Random ID
            r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            if effect == 'Blur Faces':
                image = upload(my_upload, public_id=f"pixify_{r}", effect="blur_faces:2000")
            elif effect == 'Grayscale':
                image = upload(my_upload, public_id=f"pixify_{r}", effect="grayscale")

            # Display Output Image
            st_image_comparator("Original Image", my_upload, image['url'])
            st.download_button(label="Download Effected Image", data=requests.get(image['url']).content, file_name="effect_image.jpg", mime="image/jpg")

    # Layers Tab
    with tabs[2]:
        st.markdown("### Add Text Layers")
        text = st.text_input("Enter Text:", "Pixify")
        font_size = st.slider("Font Size:", min_value=10, max_value=100, value=20)
        font_color = st.color_picker("Pick a Font Color:", "#FF0000")

        # Generate Random ID
        r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        image = upload(
            my_upload,
            public_id=f"pixify_{r}",
            overlay={"text": text, "font_size": font_size, "color": font_color},
            gravity="center"
        )

        # Display Output Image
        st_image_comparator("Original Image", my_upload, image['url'])
        st.download_button(label="Download Image with Text", data=requests.get(image['url']).content, file_name="text_layer_image.jpg", mime="image/jpg")

# Footer
st.markdown(
    """
    <footer style="text-align: center; font-family: 'Poppins', sans-serif; color: #999;">
    Made with ❤️ by Pixify Team | <a href="https://github.com/your_repo" target="_blank">GitHub</a>
    </footer>
    """,
    unsafe_allow_html=True,
)
