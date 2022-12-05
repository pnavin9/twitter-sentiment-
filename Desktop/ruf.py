import streamlit as st
def main():

    # Giving a title
    st.title("Tweet sentiment prediction web app")

    # getting the input data from the user

    string = st.text_input('Tweet')

    # code for making prediction

    prediction = ''

    # creating a button for prediction

    if st.button('Twitter Test Result'):
        prediction = 1

    st.success(prediction)

if __name__ == '__main__':
    main()
