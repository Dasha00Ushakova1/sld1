import streamlit as st
from PIL import Image
image = Image.open('shoco.png')

st.title('Выбери вкусняшку:)')

am = st.radio(
    "Что ты хотел бы скушать",
    ('Сладкое',"Кислое","Острое"))
if am == "Сладкое":
    sweet = st.radio(
        "Что бы ты хотел скушать сладкое?",
        ("Шоколад", "Мороженное", "Леденец", "Печеньку", "Тортик"))
    if sweet == 'Шоколад':
        st.write("Скушай шоколадку")
        st.image(image, caption = '  Самая вкусная шоколадка')
elif am == 'Кислое':
    sour = st.radio(
        "Что бы ты хотел скушать кислое ?",
        ("Лимон", "Кислючку", "Мармеладки"))
else:
    st.write('Купите себе дошик')
