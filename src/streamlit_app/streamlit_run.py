import streamlit as st
from typing import List
from utils import (
    get_team_images, TEAM_IMAGES,
    IMG_LENA, IMG_CLARA, IMG_SEYMA, IMG_AYLIN, IMG_PAULINA, IMG_VIVIANE,
    IMG_ANN_KATHRIN, IMG_LEONIE, IMG_LOUISA, IMG_NADINE, IMG_ISABELLE, IMG_HANNAH, IMG_PLACEHOLDER
)
import pandas as pd
from pathlib import Path


IMAGE_NAME_MAP: dict[str, str] = {
    IMG_LENA: "Lena",
    IMG_CLARA: "Clara",
    IMG_SEYMA: "Seyma",
    IMG_AYLIN: "Aylin",
    IMG_PAULINA: "Paulina",
    IMG_VIVIANE: "Viviane",
    IMG_ANN_KATHRIN: "Ann-Kathrin",
    IMG_LEONIE: "Leonie",
    IMG_LOUISA: "Louisa",
    IMG_NADINE: "Nadine",
    IMG_ISABELLE: "Isabelle",
    IMG_HANNAH: "Hannah",
    IMG_PLACEHOLDER: "TBA",
}

class Gui:
    @staticmethod
    def run_streamlit():
        st.set_page_config(page_title="Der Bachelor", layout="wide")

        st.markdown(
            """<style>
            [data-testid="stAppViewContainer"] {
                background: linear-gradient(to right bottom, #ffffff, #ffcccc);
            }
            [data-baseweb="tab"] {
                background-color: #ffb3d9;
                color: #880e4f;
                padding: 0.5rem 1rem;
                border-radius: 0.5rem 0.5rem 0 0;
                font-weight: bold;
                margin-right: 0.25rem;
            }
            [data-baseweb="tab"][aria-selected="true"] {
                background-color: #880e4f;
                color: white;
            }
            .stButton>button {
                background-color: #f06292;
                color: white;
                border: none;
                border-radius: 0.5rem;
                padding: 0.5rem 1rem;
                margin: 0;
            }
            .stButton>button:hover {
                background-color: #ec407a;
            }
            </style>""",
            unsafe_allow_html=True,
        )

        tabs = st.tabs(["Scoreboard", "Timeline", "Extrapoints", "Teams"])

        with tabs[0]:
            st.header("Scoreboard")
            try:
                base_path = Path(__file__).resolve().parents[1]
                scores_df: pd.DataFrame = pd.read_csv(base_path / "scores.csv")
                scores_df = scores_df.sort_values("total_points", ascending=False).reset_index(drop=True)
                if not scores_df.empty:
                    max_pts = scores_df.loc[0, "total_points"]
                    st.subheader("Points Overview")
                    for row in scores_df.itertuples():
                        name = row.name
                        pts = row.total_points
                        rel = pts / max_pts if max_pts > 0 else 0
                        cols = st.columns([1, 6, 1])
                        cols[0].write(name)
                        bar_html = (
                            f"<div style='background:#eee;border-radius:0.25rem;'>"
                            f"<div style='width:{rel*100}%;background:#f06292;height:1.5rem;border-radius:0.25rem;'>"
                            f"</div></div>"
                        )
                        cols[1].markdown(bar_html, unsafe_allow_html=True)
                        cols[2].write(int(pts))
            except Exception as e:
                st.error(f"Failed to load scores.csv: {e}")

        with tabs[1]:
            st.header("Timeline")
            st.info("Timeline content will go here.")

        with tabs[2]:
            st.header("Extrapoints")
            st.info("Extrapoints content will go here.")

        with tabs[3]:
            st.header("Teams")
            persons: List[str] = list(TEAM_IMAGES.keys())
            default_idx = st.session_state.get("team_idx", 0)
            selected_person = st.selectbox(
                "Choose a player:", persons, index=default_idx, key="team_select"
            )
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


if __name__ == "__main__":
    Gui.run_streamlit()
