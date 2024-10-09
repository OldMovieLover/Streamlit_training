import streamlit as st


st.title("Мой Streamlit")
message = f"Для тренировки я реализовал две страницы:\n\n`first page` - это реализация приложения для работы с котировками компаний\n\n`second page` - это реализация приложения для отоброжения моего исследования по чаевым (датасет *tips.csv*)"
st.markdown(message)

image_url = 'https://248006.selcdn.ru/main/upload/setka_images/13564202042021_db52642fc67f6c7c46657360f234a883af322464.png'
st.image(image_url, use_column_width=True)
