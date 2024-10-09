import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

st.title("Данные о котировках компаний")

# Подсмотрел эту идею(таблица СИП500 с селектбоксом) у Владислава, решил релизовать вместо со своей(ручной ввод тикера)
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
table = pd.read_html(url)
ticker = table[0]
ticker_list = table[0]['Symbol'].tolist()
st.subheader("Основная информация об компаниях в составе S&P500")
st.dataframe(ticker)
tiker_button = st.selectbox("Выбирите тикер из списка команий S&P500", options= ticker_list) 


manual_ticker = st.text_input("Либо введите название компании, например AAPL(Apple)")
years = st.slider("Выбирите количество лет", min_value=1, max_value=20)

# Приоритет ручному вводу
if manual_ticker:
    selected_tiker = manual_ticker
else:
    # По стандарту будет селектбокс, чтоб вывод данных был всегда
    selected_tiker = tiker_button

# Проверка на наличие выброного тикера
if selected_tiker: 

    # Расчет даты для получения истории
    start_date = datetime.today() - timedelta(days=years * 365)

    # Загрузка данных для тикера
    ticker_data = yf.Ticker(selected_tiker)
    stock_data = ticker_data.history(start=start_date, end=datetime.today())

    # Проверка данных по тикеру(для случаев когда ручной ввод был ошибочным)
    if not stock_data.empty:
        
        # Отображение данных по тикеру
        st.subheader(f"Котировки {selected_tiker} за последнии {years} лет")
        st.line_chart(stock_data['Close'])
        st.subheader("Историческая справка")
        st.dataframe(stock_data)

    else:
        st.warning(f"Нет данных для {selected_tiker}, или такой тикер компании не существует")
