import streamlit as st
import pandas as pd
from pathlib import Path


def render_scoreboard() -> None:
    base_path = Path(__file__).resolve().parents[1]
    scores_path = base_path / "scores.csv"
    try:
        scores_df: pd.DataFrame = pd.read_csv(scores_path)
        scores_df = scores_df.sort_values("total_points", ascending=False).reset_index(drop=True)

        st.markdown("""<style>
            .card {
                background: rgba(255,255,255,0.95);
                padding: 1rem;
                margin-bottom: 1rem;
                border-radius: 0.75rem;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                display: grid;
                grid-template-columns: 1fr 3fr auto;
                align-items: center;
                gap: 1rem;
            }
            .name-label {
                font-size: 1.4rem;
                font-weight: 700;
                color: #5b1220;
            }
            .bar-container {
                background: #eee;
                border-radius: 0.5rem;
                height: 1.5rem;
                overflow: hidden;
            }
            .bar-fill {
                background: #c2185b;
                height: 100%;
                border-radius: 0.5rem;
            }
            .right-number {
                font-size: 1.0rem;
                font-weight: 700;
                color: #000;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        if not scores_df.empty:
            max_pts = scores_df.loc[0, "total_points"]
            for row in scores_df.itertuples():
                name: str = row.name
                pts: int = row.total_points
                rel: float = pts / max_pts if max_pts > 0 else 0.0

                bar_html = (
                    f"<div class='bar-container'>"
                    f"<div class='bar-fill' style='width:{rel * 100}%;'></div>"
                    f"</div>"
                )

                card_html = (
                    "<div class='card'>"
                    f"<div class='name-label'>{name}</div>"
                    f"{bar_html}"
                    f"<div class='right-number'>{pts}</div>"
                    "</div>"
                )

                st.markdown(card_html, unsafe_allow_html=True)

        st.download_button(
            label="Download scores.csv",
            data=scores_df.to_csv(index=False).encode("utf-8"),
            file_name="scores.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"Failed to load scores.csv: {e}")
