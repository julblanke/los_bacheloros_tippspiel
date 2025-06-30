import streamlit as st
import pandas as pd
from pathlib import Path


def render_timeline() -> None:
    st.header("History")
    base_path = Path(__file__).resolve().parents[1]
    timeline_file = base_path / "timeline.csv"
    if not timeline_file.exists():
        st.info("No events logged yet.")
        return
    try:
        tl_df: pd.DataFrame = pd.read_csv(timeline_file)

        for row in tl_df.sort_values("timestamp", ascending=False).itertuples():
            st.markdown(
                f"**{row.timestamp}**: {row.event} (+{row.points}) "
                f"for **{row.candidate}**, awarded to: {row.impacted}"
            )
        st.download_button(
            label="Download timeline.csv",
            data=tl_df.to_csv(index=False).encode("utf-8"),
            file_name="timeline.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"Failed to load timeline: {e}")
