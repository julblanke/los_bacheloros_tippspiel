import streamlit as st
import pandas as pd
from pathlib import Path
from typing import Any, Dict, List
from utils import TEAM_IMAGES, IMAGE_NAME_MAP


EXTRA_EVENTS: List[Dict[str, Any]] = [
    {"event": "Allererste Rose", "points": 2},
    {"event": "Erste letzte Rose bei der Nacht der Rosen", "points": 2},
    {"event": "Rose vor der Nacht der Rosen", "points": 1},
    {"event": "Erste Ablehnung der Rose", "points": 3},
    {"event": "Erstes Geschenk", "points": 1},
    {"event": "Erstes Einzeldate", "points": 1},
    {"event": "Erstes Übernachtungsdate (Fantasy Suite)", "points": 3},
    {"event": "Erstes 2-on-1-Date", "points": 2},
    {"event": "Erstes Mal in einem Fluggerät", "points": 2},
    {"event": "Erste Fitness-Übung-Peinlichkeit", "points": 1},
    {"event": "Erstes Outfit-Wechsel-Desaster", "points": 1},
    {"event": "Kuss", "points": 1},
    {"event": "Intim", "points": 3},
    {"event": "Händchenhalten in der Öffentlichkeit", "points": 1},
    {"event": "Frauenkuss", "points": 2},
    {"event": "Nacktbaden im Pool", "points": 2},
    {"event": "Erste Frau im Pool", "points": 1},
    {"event": "Erstes Mal Rumgeheule", "points": 2},
    {"event": "Rumgeheule", "points": 1},
    {"event": "Beef", "points": 2},
    {"event": "Wurf von Gegenständen bei einem Beef", "points": 2},
    {"event": "Kandidatin stolpert in High-Heels", "points": 1},
    {"event": "Schnarch-Königin", "points": 1},
    {"event": "Verletzung (mimimi)", "points": 1},
    {"event": "Erstes Mal Angst überwunden", "points": 2},
    {"event": "Erstes Mal Heimweh", "points": 1},
    {"event": "Kandidatin, die den Bachelor wechselt", "points": 3},
    {"event": "Liebeserklärung bzw. Ich bin verliebt", "points": 3},
    {"event": "Hin- und Hergerissen zwischen den zwei Bachelors", "points": 2},
    {"event": "Spitzname für den Bachelor (erstmals)", "points": 1},
    {"event": "Erstes Verwenden von Connection", "points": 1},
    {"event": "Erste Nennung eines früheren Bachelor/Bachelorette", "points": 1},
    {"event": "Erstes Verwenden von classy", "points": 1},
    {"event": "Gespräch über sexuelle Aktionen", "points": 2},
    {"event": "Live-Musizieren während der Folge", "points": 2},
    {"event": "Frau tanzt aktiv für den Bachelor", "points": 2},
    {"event": "Erstes Duckface", "points": 1},
    {"event": "Runde weiter", "points": 1}
]


def render_extrapoints() -> None:
    st.header("Extrapoints")
    base_path = Path(__file__).resolve().parents[1]
    scores_file = base_path / "scores.csv"
    timeline_file = base_path / "timeline.csv"

    if "scores_df" not in st.session_state:
        if scores_file.exists():
            st.session_state.scores_df = pd.read_csv(scores_file)
        else:
            st.session_state.scores_df = pd.DataFrame(
                [(p, 0) for p in TEAM_IMAGES.keys()],
                columns=["name", "total_points"],
            )
    scores_df: pd.DataFrame = st.session_state.scores_df

    half = (len(EXTRA_EVENTS) + 1) // 2
    cols1, cols2 = st.columns(2)
    for i, ev in enumerate(EXTRA_EVENTS):
        container = cols1 if i < half else cols2
        rcols = container.columns([1, 1, 6])
        rcols[0].markdown(
            f"<div class='bar-label'>{ev['points']}</div>",
            unsafe_allow_html=True
        )
        if rcols[1].button("Add", key=f"add_ev_{i}"):
            st.session_state["selected_event"] = i
        rcols[2].write(ev["event"])

    if "selected_event" in st.session_state:
        ev = EXTRA_EVENTS[st.session_state["selected_event"]]
        candidate = st.selectbox(
            "Select contestant to award points:",
            list(IMAGE_NAME_MAP.values()),
            key="cand_select",
        )
        if st.button("Confirm", key="confirm_ev"):
            url = next(k for k, v in IMAGE_NAME_MAP.items() if v == candidate)
            impacted = [p for p, imgs in TEAM_IMAGES.items() if url in imgs]
            for p in impacted:
                scores_df.loc[scores_df.name == p, "total_points"] += ev["points"]
            scores_df.to_csv(scores_file, index=False)
            from datetime import datetime
            entry = {
                "timestamp": datetime.now().isoformat(sep=' ', timespec='seconds'),
                "event": ev["event"],
                "candidate": candidate,
                "points": ev["points"],
                "impacted": ", ".join(impacted),
            }
            if not timeline_file.exists():
                pd.DataFrame([entry]).to_csv(timeline_file, index=False)
            else:
                pd.DataFrame([entry]).to_csv(timeline_file, mode='a', header=False, index=False)
            st.success(
                f"Added {ev['points']} points to teams with {candidate}: {', '.join(impacted)}"
            )
            del st.session_state["selected_event"]
