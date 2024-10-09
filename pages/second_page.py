import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Исследование по чаевым')

# Функция для проверки соответсвия файла
def check_file_tips(file):
    try:
        df = pd.read_csv(file)
        expected_columns = ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size', 'time_order']
        # Проверям по колоннам
        if all(column in df.columns for column in expected_columns):
            return True, df
        else:
            return False, None
    except Exception as e:
        st.error(f"Ошибка при проверке файла: {e}")

uploaded_file = st.sidebar.file_uploader('Загрузите файл tips.csv, находящийся в папке Streamlit_training', type='csv')
# Если файл загружен
if uploaded_file is not None:
    is_valid, df = check_file_tips(uploaded_file)
    # Если функция вернула True
    if is_valid:
        st.success("Файл успешно загружен и прошел проверку!")
        st.subheader("Первые 5 строк таблицы tips")
        st.dataframe(df.head(5))

        # Далее я буду писать шаг и номер согласну файлу vis-04.ipynb и график по счету в streamlit
        # Я решил переназначать переменные <fig, ax, figure> для экономии памяти и упрощения кода
        
        # Шаг 4, график 1
        fig, ax = plt.subplots(figsize=(13,8))
        daily_tips = df.groupby('time_order')['tip'].sum().reset_index()
        plt.plot(daily_tips['time_order'], daily_tips['tip'], marker='o')
        ax.set_ylabel('Размер чаевых, $')
        ax.set_xlabel('Дата')
        ax.grid(axis='x')
        fig.autofmt_xdate()
        st.subheader("1. График показывающий динамику чаевых во времени")
        st.pyplot(fig)
        
        # Шаг 5, график 2
        fig, ax = plt.subplots()
        sns.histplot(df['total_bill'], kde=True)
        ax.set_ylabel('Количество чеков')
        ax.set_xlabel('Общая суммая в чеке, $')
        ax.grid()
        st.subheader("2. Динамика суммы чека")
        st.pyplot(fig)

        # Шаг 6, график 3
        fig, ax = plt.subplots()
        sns.scatterplot(x='total_bill', y='tip', data=df)
        ax.set_ylabel('Чаевые, $')
        ax.set_xlabel('Общая сумма в чеке, $')
        ax.grid()
        st.subheader("3. Связь между итогом чека и чаевыми")
        st.pyplot(fig)

        # Шаг 7, график 4
        fig, ax = plt.subplots()
        sns.scatterplot(x='total_bill', y='tip', size='size', data=df, ax=ax)
        ax.set_ylabel('Чаевые, $')
        ax.set_xlabel('Общая сумма в чеке, $')
        ax.grid()
        st.subheader("4. Связь между итогом чека и чаевыми c учетом размера")
        st.pyplot(fig)

        # Шаг 8, график 5
        fig, ax = plt.subplots()
        plt.bar(df['day'], df['total_bill'])
        ax.set_ylabel('Общая суммая в чеке, $')
        ax.set_xlabel('День недели')
        st.subheader("5. Связь между днем недели и размером счета")
        st.pyplot(fig)

        # Шаг 9, график 6
        fig, ax = plt.subplots()
        sns.scatterplot(x='tip', y='day', hue='sex', data=df)
        ax.set_ylabel('День недели')
        ax.set_xlabel('Чаевые, $')
        st.subheader("6. Связь между днем недели и чаевыми, с учетом полом заказчика")
        st.pyplot(fig)

        # Шаг 10.0, график 7
        fig, ax = plt.subplots()
        sns.boxplot(x='day', y='total_bill', hue='time', data=df)
        ax.set_ylabel('Сумма, $')
        ax.set_xlabel('День недели')
        st.subheader("7. Связь между суммой счетов и днем недели, с учетом времени приема пищи")
        st.pyplot(fig)

        # Шаг 10.1, график 8
        figure = sns.catplot(x='day', y='total_bill', hue='time', data=df, kind='strip')
        figure.set_axis_labels('Сумма, $', 'День недели')
        st.subheader("8. Связь между суммой счетов и днем недели, с учетом времени приема пищи")
        st.pyplot(figure)

        # Шаг 11, график 9
        figure = sns.displot(df, x='tip', col='time', height=6, aspect=0.7)
        figure.set_axis_labels('Чаевые, $', 'Сумма чека, $')
        st.subheader("9. Распределение чаевых и чеков на обед и ужин")
        st.pyplot(figure)

        # Шаг 12, график 10
        fig, (ax, ax1) = plt.subplots(1, 2, sharey=True)

        sns.scatterplot(x='total_bill', y='tip', hue='smoker', data=df[df['sex'] == 'Male'], ax=ax)
        ax.set_title('Мужчины')
        ax.set_xlabel('Размер счета, $')
        ax.set_ylabel('Размер чаевых, $')
        ax.legend(title='Курящий', loc='upper left')

        sns.scatterplot(x='total_bill', y='tip', hue='smoker', data=df[df['sex'] == 'Female'], ax=ax1)
        ax1.set_title('Женщины')
        ax1.set_xlabel('Размер счета, $')
        ax1.legend(title='Курящий', loc='upper left')
        st.subheader("10. Связь размера счета и чаевых, по курящим/некурящим")
        st.pyplot(fig)

        # Шаг 13, график 11
        numer_col = df.select_dtypes(include='number')
        corr_matrix = numer_col.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')
        st.subheader("11. Карта зависимостей численных переменных")
        st.pyplot(fig)

    else:
        st.error("Это неправильный файл. Пожайлуста, загрузите файл tips.csv с правильной структурой")
else:
    st.sidebar.info("Пожалуйста, загрузите файл tips.csv")