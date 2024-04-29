import streamlit as st
import pandas as pd
import datetime

# Función para mostrar el calendario semanal
def weekly_calendar():
    today = datetime.date.today()
    days_of_week = [(today + datetime.timedelta(days=i)).strftime('%A') for i in range(7)]

    # Crear un DataFrame para representar el calendario
    df = pd.DataFrame(index=range(8, 24), columns=days_of_week)

    return df

# Función principal de la aplicación
def main():
    st.title('Calendario Semanal')

    # Mostrar el calendario semanal
    st.dataframe(weekly_calendar())

if __name__ == '__main__':
    main()
