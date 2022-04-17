import streamlit as st
import pickle
import numpy as np
import pandas as pd
import time


model = pickle.load(open("RentPredictionProject\pune_rent.pkl", 'rb'))
data = pd.read_csv('RentPredictionProject\Cleaned_data.csv')


seller_list = sorted(data['seller_type'].unique())
localities = sorted(data['locality'].unique())
prop_list = sorted(data['property_type'].unique())
furnish_list = sorted(data['furnish_type'].unique())
layout_list = sorted(data['layout_type'].unique())
bed_list = sorted(data['bedroom'].unique())
bath_list = sorted(data['bathroom'].unique())


def predict_price(seller, bedroom, bhk, prop, locality, area, furnish, bathroom):
    # input = np.array([[seller, bedroom, bhk, prop, locality, area, furnish, bathroom]]).astype(np.float64)
    input = pd.DataFrame([[seller, bedroom, bhk, prop, locality, area, furnish, bathroom]],columns=['seller_type', 'bedroom', 'layout_type', 'property_type', 'locality', 'area', 'furnish_type', 'bathroom'])
    prediction = model.predict(input)
    return float(prediction)

def main():
    st.set_page_config('Pune Property Rent Prediction App')
    # st.title("Rent prediction in Pune")
    html_temp = """
    <div style="background-color:#2a9609 ;padding:10px">
    <h2 style="color:white;text-align:center;">🏠Pune Property Rent Prediction App💸</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.sidebar.markdown("<h2 style='text-align: center;'>About</h2> ", unsafe_allow_html=True)
    about_expander = st.sidebar.expander("About")
    with about_expander:
        st.write("This is a machine learning project made using pipeline and linear regression.\n I hope you like my work! 😸")
    git_expander = st.sidebar.expander("Github")
    with git_expander:
        st.write("Github Repo: [Github](https://github.com/Kai-Infernus/pune_house_rent_prediction)")
    ds_expander = st.sidebar.expander("Dataset")
    with ds_expander:
        st.write("Dataset: [Pune House Rent Prediction](https://www.kaggle.com/datasets/rahulmishra5/pune-house-rent-prediction)")

    seller_choice = st.selectbox(label='Select your Seller Type', options=seller_list)

    bedroom_choice = st.selectbox(label='Select number of Bedrooms', options=bed_list)

    layout_choice = st.selectbox(label='Select your Layout Type', options=layout_list)

    prop_choice = st.selectbox(label='Select your Property Type', options=prop_list)

    locality_choice = st.selectbox(label='Select your Locality', options=localities)

    area_choice = st.slider("Choose the Area", 100, 1800)

    furnish_choice = st.selectbox(label='Select your Furnish Type', options=furnish_list)

    bath_choice = st.selectbox(label='Select number of Bathrooms', options=bath_list)
    
    if st.button('Predict'):

        'Computing...'

        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'{i+1}%')
            bar.progress(i + 1)
            time.sleep(0.01)

        '...and we\'re done!'

        output = predict_price(seller_choice,bedroom_choice,layout_choice,prop_choice,locality_choice,area_choice,furnish_choice,bath_choice)
        st.success('₹ {} INR'.format(round(output)))
        # st.markdown("<h5 style='text-align: left;'> INR </h5>", unsafe_allow_html=True)

if __name__=='__main__':
    main()