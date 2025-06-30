import streamlit as st
from streamlit_app.styles import main_style
from streamlit_app.scoreboard import render_scoreboard
from streamlit_app.timeline import render_timeline
from streamlit_app.extrapoints import render_extrapoints
from streamlit_app.teams import render_teams


def run_streamlit() -> None:
    st.set_page_config(page_title="Der Bachelor", layout="wide")
    st.markdown(main_style, unsafe_allow_html=True)
    st.markdown('<div class="banner"></div>', unsafe_allow_html=True)
    tabs = st.tabs(["Scoreboard", "History", "Extrapoints", "Teams"])

    with tabs[0]:
        render_scoreboard()
    with tabs[1]:
        render_timeline()
    with tabs[2]:
        render_extrapoints()
    with tabs[3]:
        render_teams()


if __name__ == "__main__":
    run_streamlit()
