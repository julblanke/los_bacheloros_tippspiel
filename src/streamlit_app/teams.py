import streamlit as st
from typing import List
from utils import get_team_images, TEAM_IMAGES, IMAGE_NAME_MAP


def render_teams() -> None:
    st.header("Teams")
    persons: List[str] = list(TEAM_IMAGES.keys())
    default_idx = st.session_state.get("team_idx", 0)
    selected_person = st.selectbox("Choose a player:", persons, index=default_idx, key="team_select")
    st.session_state["team_idx"] = persons.index(selected_person)

    st.subheader(f"{selected_person}'s Team")
    images = get_team_images(selected_person)
    for row in range(2):
        cols_img = st.columns(3)
        for col_idx in range(3):
            img_idx = row * 3 + col_idx
            url = images[img_idx]
            name = IMAGE_NAME_MAP.get(url, "")
            cols_img[col_idx].markdown(
                f"<p style='text-align:center; margin-bottom:0.25rem; font-weight:bold'>{name}</p>",
                unsafe_allow_html=True,
            )
            cols_img[col_idx].image(url, use_container_width=True)
