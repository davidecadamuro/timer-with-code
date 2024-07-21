import streamlit as st
import time

if 'key' not in st.session_state:
    st.write("initialising state")
    st.session_state.N = 5*60
st.write(st.session_state)
#N = 5*60

with st.container():
    st.title("💣💣💣 Es ist eine Bombe! 🧨🧨🧨")

    st.write(
        "Um den Countdown zu stoppen, geben Sie den Code ein."
    )
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        n1 = st.number_input("", value=None, min_value=0, max_value=9, step=1, placeholder="", key="n1")
    with col2:
        n2 = st.number_input("", value=None, min_value=0, max_value=9, step=1, placeholder="", key="n2")
    with col3:
        n3 = st.number_input("", value=None, min_value=0, max_value=9, step=1, placeholder="", key="n3")
    with col4:
        n4 = st.number_input("", value=None, min_value=0, max_value=9, step=1, placeholder="", key="n4")

    #6459
    if(n1 == 6 and n2 == 4 and n3 == 5 and n4 == 9):
        st.write(
            f"code is right {st.session_state.N}",

        )
    else:
        st.write(
            f"code is wrong {st.session_state.N}"
        )

    ph = st.empty()
    for secs in range(st.session_state.N, 0,-1):
        #N = secs
        st.session_state.N = secs
        mm, ss = secs//60, secs%60
        ph.metric("Countdown", f"{mm:02d}:{ss:02d}, {st.session_state.N}")
        time.sleep(1)

    