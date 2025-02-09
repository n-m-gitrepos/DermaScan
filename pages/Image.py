import streamlit as st
from PIL import Image
import numpy as np
import os

# Load your pre-trained deep learning model
# model = tf.keras.models.load_model("your_model_path")

def predict_image(image):
    # Preprocess the image before passing it into the model
    img = image.resize((224, 224))  # Resize to your model's expected input size
    img = np.array(img) / 255.0  # Normalize if necessary
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    
    # Use the model to predict
    # prediction = model.predict(img)
    
    # For demonstration purposes, let's assume the model predicts a "skin condition"
    prediction = "Possible dermatological condition: Acne"  # This should be your model's output
    
    return prediction

def save_image(uploaded_file):
    upload_path = "uploaded_images"
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    
    file_path = os.path.join(upload_path, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def main():
    st.title("DermaScan: Dermatological Condition Detection")
    
    st.write("Upload your image and let the AI analyze it to detect potential skin conditions!")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        saved_image_path = save_image(uploaded_file)
        st.write(f"Image saved at: {saved_image_path}")
        
        prediction = predict_image(image)
        
        st.write(f"Prediction: {prediction}")
    
if __name__ == "__main__":
    main()


