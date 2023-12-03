
import streamlit as st

def calculate_tire_diameter(width, aspect_ratio, rim_diameter):
    sidewall_height = width * (aspect_ratio / 100.0)
    total_diameter = sidewall_height * 2 + rim_diameter * 25.4
    return total_diameter

st.title('タイヤサイズ計算アプリ')

with st.form("my_form"):
    st.write("タイヤサイズを入力してください")
    width = st.number_input('タイヤ幅（mm）', value=205, format='%d')
    aspect_ratio = st.number_input('側面比（%）', value=70, format='%d')
    rim_diameter = st.number_input('リム経（インチ）', value=15, format='%d')
    submitted = st.form_submit_button("計算")
    if submitted:
        diameter = calculate_tire_diameter(width, aspect_ratio, rim_diameter)
        st.write(f"タイヤの外径は: {diameter:.2f} mmです。")

    st.form_submit_button("クリア", on_click=lambda: st.experimental_rerun())
# フッターの追加footer = """
    <style>
    .footer {
        position: fixed;
        right: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        text-align: center;
        font-size: smaller;
        border-top: 1px solid #ddd;
        padding: 5px;
    }
    </style>
    <div class='footer'>
        Copyright (c) 2023 Kenji Tanaka<br>
        Released under the MIT license<br>
        <a href="https://opensource.org/licenses/mit-license.php" target="_blank">https://opensource.org/licenses/mit-license.php</a>
    </div>
    """
st.markdown(footer, unsafe_allow_html=True)
