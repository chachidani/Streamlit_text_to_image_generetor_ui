import streamlit as st
from PIL import Image
import io

# Set the page title and layout
st.set_page_config(page_title="ImagineArt - AI Art Generator", layout="centered")

# CSS to set the background image and title color
background_image_url = "https://images.pexels.com/photos/376533/pexels-photo-376533.jpeg?auto=compress&cs=tinysrgb&w=600"  # Replace with the URL or path to your background image

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-attachment: fixed;
        background-size: cover;
    }}
    .custom-title {{
        color: #FF6347; /* Tomato color */
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("ImagineArt")
st.sidebar.markdown("AI-powered art generation")

# Header
st.markdown('<h1 class="custom-title">Imagine Generator</h1>', unsafe_allow_html=True)
st.subheader("Turn your imagination into reality with AI-generated visuals!")

# Description
st.write("Enter text or upload an image to start.")

# Option to select between Text-to-Image and Image-to-Image
option = st.selectbox("Choose a generation type", ["Text to Image", "Image to Image"])

# For Text-to-Image Generation
if option == "Text to Image":
    text_input = st.text_input("Enter a description of your desired image:", placeholder="e.g., 'A futuristic cityscape at sunset'")
    if st.button("Generate from Text"):
        if text_input:
            # Replace with actual function to generate an image from text
            # generated_image = generate_image_from_text(text_input)
            st.image("path/to/generated/image.png", caption="Generated Image", use_column_width=True)
        else:
            st.warning("Please enter a description.")

# For Image-to-Image Generation
elif option == "Image to Image":
    uploaded_image = st.file_uploader("Upload an image to modify", type=["jpg", "jpeg", "png"])
    if st.button("Generate from Image") and uploaded_image is not None:
        image = Image.open(uploaded_image)
        # Replace with actual function to generate a new image from the input image
        # generated_image = generate_image_from_image(image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.image("path/to/generated/image.png", caption="Generated Image", use_column_width=True)
    elif uploaded_image is None:
        st.warning("Please upload an image.")

# Footer
st.markdown("---")
st.write("© 2024 ImagineArt - Powered by AI Art Generation")
