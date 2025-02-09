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

def save_image_and_info(uploaded_file, age, gender):
    upload_path = "uploaded_images"
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    
    file_path = os.path.join(upload_path, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    txt_file_path = os.path.join(upload_path, uploaded_file.name.split('.')[0] + "_info.txt")
    with open(txt_file_path, "w") as f:
        f.write(f"Age: {age}\nGender: {gender}")

    return file_path, txt_file_path

def main():
    st.title("DermaScan: Dermatological Condition Detection")
    
    st.write("Upload your image and let the AI analyze it to detect potential skin conditions!")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    st.subheader("Enter your Age:")
    age = st.number_input("Age", min_value=1, max_value=100, value=25, step=1)

    # Gender selection (Male/Female)
    st.subheader("Select your Gender:")
    gender = st.radio("Gender", options=["Male", "Female"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        saved_image_path, saved_txt_path = save_image_and_info(uploaded_file, age, gender)
        st.write(f"Image saved at: {saved_image_path}")
        st.write(f"Information saved at: {saved_txt_path}")
        
        prediction = predict_image(image)
        
        st.write(f"Prediction: {prediction}")
    
    
    
if __name__ == "__main__":
    main()


