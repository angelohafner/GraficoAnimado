import streamlit as st
import pandas as pd
import plotly.express as px

df= px.data.gapminder()
year_options = df['year'].unique().tolist()
ano = st.selectbox('Qual ano você gostaria de ver?', year_options, 0)
# df = df[df['year']==year]

fig = px.scatter(df, x='gdpPercap', y='lifeExp',
                    size='pop', color='continent', hover_name='continent',
                    log_x=False, size_max=55, range_x=[0,50e3], range_y=[40,80],
                    animation_frame='year', animation_group='country'                    
                )

fig.update_layout(width=800)
st.write(fig)


# covid = pd.read_csv('https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')
covid = pd.read_csv('daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')
covid.columns = ['Country','Code','Date','Confirmed','Days since confirmed']
covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d')
st.write(covid)

country_options = covid['Country'].unique().tolist()
date_options = covid['Date'].unique().tolist()
Pais = st.multiselect('Qual país você gostaria de ver?', country_options)
Data = st.selectbox('Qual data você gostaria de ver?', date_options, 100)

covid = covid[covid['Country'].isin(Pais)]
covid = covid[covid['Date']==Data]

fig2 = px.bar(covid, x='Country', y='Confirmed', color='Country')
fig2.update_layout(width=800)
st.write(fig2)
