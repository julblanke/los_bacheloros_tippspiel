import streamlit as st
import pandas as pd
from pathlib import Path


def render_scoreboard() -> None:
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
