import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import scipy.io
import os

st.set_page_config(
    page_title="Home"
)


CLASS_NAMES = {
    0: 'Chihuahua', 1: 'Japanese Spaniel', 2: 'Maltese Dog', 3: 'Pekinese', 4: 'Shih-Tzu',
    5: 'Blenheim Spaniel', 6: 'Papillon', 7: 'Toy Terrier', 8: 'Rhodesian Ridgeback', 9: 'Afghan Hound',
    10: 'Basset', 11: 'Beagle', 12: 'Bloodhound', 13: 'Bluetick', 14: 'Black-and-Tan Coonhound',
    15: 'Walker Hound', 16: 'English Foxhound', 17: 'Redbone', 18: 'Borzoi', 19: 'Irish Wolfhound',
    20: 'Italian Greyhound', 21: 'Whippet', 22: 'Ibizan Hound', 23: 'Norwegian Elkhound', 24: 'Otterhound',
    25: 'Saluki', 26: 'Scottish Deerhound', 27: 'Weimaraner', 28: 'Staffordshire Bullterrier', 29: 'American Staffordshire Terrier',
    30: 'Bedlington Terrier', 31: 'Border Terrier', 32: 'Kerry Blue Terrier', 33: 'Irish Terrier', 34: 'Norfolk Terrier',
    35: 'Norwich Terrier', 36: 'Yorkshire Terrier', 37: 'Wire-Haired Fox Terrier', 38: 'Lakeland Terrier', 39: 'Sealyham Terrier',
    40: 'Airedale', 41: 'Cairn', 42: 'Australian Terrier', 43: 'Dandie Dinmont', 44: 'Boston Bull',
    45: 'Miniature Schnauzer', 46: 'Giant Schnauzer', 47: 'Standard Schnauzer', 48: 'Scotch Terrier', 49: 'Tibetan Terrier',
    50: 'Silky Terrier', 51: 'Soft-Coated Wheaten Terrier', 52: 'West Highland White Terrier', 53: 'Lhasa', 54: 'Flat-Coated Retriever',
    55: 'Curly-Coated Retriever', 56: 'Golden Retriever', 57: 'Labrador Retriever', 58: 'Chesapeake Bay Retriever', 59: 'German Short-Haired Pointer',
    60: 'Vizsla', 61: 'English Setter', 62: 'Irish Setter', 63: 'Gordon Setter', 64: 'Brittany Spaniel',
    65: 'Clumber', 66: 'English Springer', 67: 'Welsh Springer Spaniel', 68: 'Cocker Spaniel', 69: 'Sussex Spaniel',
    70: 'Irish Water Spaniel', 71: 'Kuvasz', 72: 'Schipperke', 73: 'Groenendael', 74: 'Malinois',
    75: 'Briard', 76: 'Kelpie', 77: 'Komondor', 78: 'Old English Sheepdog', 79: 'Shetland Sheepdog',
    80: 'Collie', 81: 'Border Collie', 82: 'Bouvier Des Flandres', 83: 'Rottweiler', 84: 'German Shepherd',
    85: 'Doberman', 86: 'Miniature Pinscher', 87: 'Greater Swiss Mountain Dog', 88: 'Bernese Mountain Dog', 89: 'Appenzeller',
    90: 'EntleBucher', 91: 'Boxer', 92: 'Bull Mastiff', 93: 'Tibetan Mastiff', 94: 'French Bulldog',
    95: 'Great Dane', 96: 'Saint Bernard', 97: 'Eskimo Dog', 98: 'Malamute', 99: 'Siberian Husky',
    100: 'Affenpinscher', 101: 'Basenji', 102: 'Pug', 103: 'Leonberg', 104: 'Newfoundland',
    105: 'Great Pyrenees', 106: 'Samoyed', 107: 'Pomeranian', 108: 'Chow', 109: 'Keeshond',
    110: 'Brabancon Griffon', 111: 'Pembroke', 112: 'Cardigan', 113: 'Toy Poodle', 114: 'Miniature Poodle',
    115: 'Standard Poodle', 116: 'Mexican Hairless', 117: 'Dingo', 118: 'Dhole', 119: 'African Hunting Dog'
}

MODEL_PATH = "./model/model_adamw.keras"

try:
    model = load_model(MODEL_PATH)
    st.success("Model successfully loaded")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()


st.title("Dog Breed Classification")

uploaded_file = st.file_uploader("Upload an image of a dog", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array)
    predicted_index = np.argmax(predictions)
    confidence = predictions[0][predicted_index]

    if CLASS_NAMES:
        predicted_class = CLASS_NAMES[predicted_index]
        st.write(f"Prediction: **{predicted_class}**")
        st.write(f"Confidence: **{confidence:.2f}**")
    else:
        st.error("Class names not available. Unable to display prediction.")