import streamlit as st
import sqlite3
import os

def init_db():
    if not os.path.exists('messaggi.db'):
        conn = sqlite3.connect('messaggi.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS messaggi (id INTEGER PRIMARY KEY, testo TEXT)')
        cursor.execute('DELETE FROM messaggi')
        cursor.executemany('INSERT INTO messaggi (id, testo) VALUES (?, ?)', [
            (1, 'Messaggio 1: Benvenuto nella app!'),
            (2, 'Messaggio 2: Questo è il secondo messaggio dal database.'),
            (3, 'Messaggio 3: Hai selezionato la terza opzione.')
        ])
        conn.commit()
        conn.close()

init_db()

def get_message(msg_id):
    conn = sqlite3.connect('messaggi.db')
    cursor = conn.cursor()
    cursor.execute('SELECT testo FROM messaggi WHERE id = ?', (msg_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "Messaggio non trovato"

st.title("My Simple Streamlit App as test")

option = st.selectbox(
    'Seleziona un opzione (1, 2 o 3):',
    (1, 2, 3)
)

st.write('Hai selezionato:', option)
st.info(get_message(option))

if st.button("Click Me!"):
    st.write("You clicked the button!")
