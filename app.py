import streamlit as st
import pandas as pd 

df = pd.read_csv('Dataset/epl-2022.csv')
df.index += 1

Home_Team = df['Home Team'].unique().tolist()
Home_Team.sort()
Away_Team = df['Away Team'].unique().tolist()
Away_Team.sort()

st.markdown("<h1 style='text-align: center; color: white; font-size: 33px;'> EPL 2022-2023 Scores of Matches App </h1 >", unsafe_allow_html=True)

option_1 = st.selectbox('Select your home team', Home_Team)
st.write('selected:', option_1)

option_2 = st.selectbox('Select away team', Away_Team)
st.write('selected:', option_2)

if st.button('Send'):
    if option_1 == option_2:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 25px;'>You chose the same team</h1>",
                    unsafe_allow_html=True)
    else:
        df_match = df[(df['Home Team'] == option_1) & (df['Away Team'] == option_2)]
        if not df_match.empty:
            score = df_match.iloc[0]['Result'] 
            home_team = df_match.iloc[0]['Home Team']
            home_away = df_match.iloc[0]['Away Team']
            st.markdown("<h1 style='text-align: center; color: white; font-size: 25px;'>{}</h1>".format(home_team + " " + score + " " + home_away),
                    unsafe_allow_html=True)
        else: 
            st.markdown("<h1 style='text-align: center; color: white; font-size: 25px;'>Match not found</h1>", unsafe_allow_html=True)
    if st.button('Reset'):
        st.write(' ')
