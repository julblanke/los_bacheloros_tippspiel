import streamlit as st
import pandas as pd
from pathlib import Path


def render_scoreboard() -> None:
    try:
        base_path = Path(__file__).resolve().parents[1]
        scores_path = base_path / "scores.csv"
        scores_df: pd.DataFrame = pd.read_csv(scores_path)

        scores_df = scores_df.sort_values("total_points", ascending=False).reset_index(drop=True)
        if not scores_df.empty:
            max_pts = scores_df.loc[0, "total_points"]
            for row in scores_df.itertuples():
                name: str = row.name
                pts: int = row.total_points
                rel: float = pts / max_pts if max_pts > 0 else 0.0
                cols = st.columns([1, 6, 1])
                cols[0].markdown(
                    f"<span class='name-label'>{name}</span>",
                    unsafe_allow_html=True
                )
                bar_html = (
                    "<div style='background:#eee;border-radius:0.25rem;'>"
                    f"<div style='width:{rel*100}%;background:#f06292;"
                    "height:1.5rem;border-radius:0.25rem;'></div></div>"
                )
                cols[1].markdown(bar_html, unsafe_allow_html=True)
                cols[2].markdown(
                    f"<span class='bar-label'>{pts}</span>",
                    unsafe_allow_html=True
                )

        st.download_button(
            label="Download scores.csv",
            data=scores_df.to_csv(index=False).encode("utf-8"),
            file_name="scores.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"Failed to load scores.csv: {e}")
