import streamlit as st
import time


@st.cache_resource
def create_list():
    l = [15*60]
    return l


st.markdown(
    """
    <style>
   div[data-testid="stStatusWidget"] div button {
        display: none;
        }
        </style>
""",
    unsafe_allow_html=True,
)


l = create_list()
N = l[0]

st.title("💣💣💣 Das ist eine Bombe! 🧨🧨🧨")

st.write(
    "Um den Countdown zu stoppen, geben Sie den Code ein."
)
with st.form("my_form"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        n1 = st.number_input("", value=None, min_value=0, max_value=9, step=1, placeholder="", key="n1")
    with col2:
        n2 = st.number_input("", value=None, min_value=0, max_value=9, step=1, placeholder="", key="n2")
    with col3:
        n3 = st.number_input("", value=None, min_value=0, max_value=9, step=1, placeholder="", key="n3")
    with col4:
        n4 = st.number_input("", value=None, min_value=0, max_value=9, step=1, placeholder="", key="n4")

    code = st.form_submit_button("Submit")
    # 6459

ph = st.empty()
for secs in range(N, -1, -1):
    if secs == 0:
        ph.header("💥💥💥💥BOOOOM!!!💥💥💥💥")
        break
    else:
        l[0] = secs
        mm, ss = secs//60, secs%60
        if n1 == 6 and n2 == 4 and n3 == 5 and n4 == 9:
            ph.metric("Countdown", f"{mm:02d}:{ss:02d} - {'Countdown gestoppt'}")
            break
        else:
            ph.metric("Countdown", f"{mm:02d}:{ss:02d}")        
            time.sleep(1)

    