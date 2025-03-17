import streamlit as st
import joblib #buat import pickle

def main():
  st.title('Dermatology Machine Learning')  
  st.info('This app using machine learning')

  #input data by user
  erythema = st.slider('Erythema', min_value=0, max_value=3, value=2) #erythema tulisan buat judul dari slider value itu settingan default pas launch, min nilai slider terkiri, max slider terkanan
if __name__ == "__main__":
  main()
