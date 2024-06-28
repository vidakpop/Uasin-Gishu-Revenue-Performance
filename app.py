import pandas as pd
import altair as alt
import streamlit as st
df=pd.read_csv('revenue_3(1).csv')
st.header('WEEK1 AND WEEK2 REPORT')
st.sidebar.subheader('TEAMS REVENUE PERFORMANCE')
st.dataframe(df)
st.write('The above dataset is a summary of total revenue collected by teams in the first two weeks of Revenue Enhancement Exercise.')
scatter=alt.Chart(df).mark_circle().encode(
    x='TEAMS',
    y='TOTAL',
    color='TEAMS',
    tooltip=['27/05/2024','28/05/2024','29/05/2024','30/05/2024','31/05/2024','03/06/2024','04/06/2024','05/06/2024','06/06/2024','07/06/2024']
).properties(
title=('REVENUE SCATTER PLOT'),
width=600,
height=400

).interactive()
st.altair_chart(scatter)
########################################################
bargraph=alt.Chart(df).mark_bar().encode(
    y='TEAMS',
    x='TOTAL',
    color='TEAMS',
    tooltip=['27/05/2024','28/05/2024','29/05/2024','30/05/2024','31/05/2024','03/06/2024','04/06/2024','05/06/2024','06/06/2024','07/06/2024']
).properties(
title=('REVENUE BARGRAPH PLOT'),
width=600,
height=400

).interactive()
st.altair_chart(bargraph)
bargraph=alt.Chart(df).mark_bar().encode(
    x='TEAMS',
    y='TOTAL',
    color='TEAMS',
    tooltip=['27/05/2024','28/05/2024','29/05/2024','30/05/2024','31/05/2024','03/06/2024','04/06/2024','05/06/2024','06/06/2024','07/06/2024']
).properties(
title=('REVENUE BARGRAPH PLOT'),
width=600,
height=400

).interactive()
#######################################
st.altair_chart(bargraph)
st.write('Above graphs show the comparison of teams performance in revenue collection.')
