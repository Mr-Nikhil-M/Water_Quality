import streamlit as st
import pickle
from PIL import Image
import sklearn

def main():
    st.title("Water Quality Prediction")
    # image=Image.open("house.png")
    # st.image(image,width=800)
    aluminium=st.text_input("House age","type here")
    ammonia=st.text_input("House age","type here")
    arsenic=st.text_input("House age","type here")
    barium=st.text_input("House age","type here")
    cadmium=st.text_input("House age","type here")
    chloramine=st.text_input("House age","type here")
    chromium=st.text_input("House age","type here")
    copper=st.text_input("House age","type here")
    flouride=st.text_input("House age","type here")
    bacteria=st.text_input("House age","type here")
    viruses=st.text_input("House age","type here")
    lead=st.text_input("House age","type here")
    nitrates=st.text_input("House age","type here")
    nitrites=st.text_input("House age","type here")
    mercury=st.text_input("House age","type here")
    perchlorate=st.text_input("House age","type here")
    radium=st.text_input("House age","type here")
    selenium=st.text_input("House age","type here")
    silver=st.text_input("House age","type here")
    uranium=st.text_input("House age","type here")
    features=[aluminium,ammonia,arsenic,barium,cadmium,chloramine,chromium,copper,flouride,bacteria,viruses,lead,nitrates,nitrites,mercury,perchlorate,radium,selenium,silver,uranium]
    model=pickle.load(open('water.sav','rb'))
    scaler=pickle.load(open('scalerwater.sav','rb'))
    pred=st.button('PREDICT')
    if(pred):
        prediction=model.predict(scaler.transform([features]))
        st.write("Prediction=",prediction)
        print(prediction)
main()