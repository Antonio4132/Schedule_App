import streamlit as st
import pandas as pd

def create_calendar():
    # Crear un DataFrame para representar el calendario
    today = pd.Timestamp.today()
    days_of_week = [(today + pd.Timedelta(days=i)).strftime('%A') for i in range(7)]
    hours = [f'{hour}:00' for hour in range(8, 24)]
    df = pd.DataFrame(index=hours, columns=days_of_week)
    
    return df

def main():
    st.title('Calendario Semanal')

    # Crear el calendario inicial
    calendar = create_calendar()

    # Mostrar el calendario en una tabla
    edited_calendar = st.table(calendar)

    # Permitir la edición del calendario
    for day in calendar.columns:
        for hour in calendar.index:
            key = f"{day}-{hour}"
            calendar.loc[hour, day] = st.checkbox(label="", key=key)

    # Actualizar la tabla con los cambios realizados
    edited_calendar.table(calendar)

if __name__ == "__main__":
    main()
