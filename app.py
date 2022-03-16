from requests import request
from urllib import request
import streamlit as st
import numpy as np
import pandas as pd
import datetime


'''
# TaxiFareModel front
'''

st.markdown('''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

''')



'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


date = st.date_input(
    "Fecha de Viaje",
    datetime.date(2022, 3, 15))

time = st.time_input('Hora del embarque: ', date.time(17,45))

pickup_longitude = st.number_input('Ingrese latidud inicial')
pickup_latitude = st.number_input('Ingrese longitud final')
dropoff_longitude = st.number_input('Ingrese latidud inicial')
dropoff_latitude = st.number_input('Ingrese longitud final')
passenger_count = st.number_input('Ingrese numero de personas')

# 2. Let's build a dictionary containing the parameters for our API...
fare = request.get(url).json()

params = {"pickup_datetime" : date_time,
    "pickup_longitude": float(pickup_longitude),
    "pickup_latitude": float(pickup_latitude),
    "dropoff_longitude": float(dropoff_longitude),
    "dropoff_latitude": float(dropoff_latitude),
    "passenger_count": int(passenger_count)}


# url = 'https://taxifare.lewagon.ai/predict'
r = request.get(url,params = params)


st.write(fare['fare'])

'''


2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
