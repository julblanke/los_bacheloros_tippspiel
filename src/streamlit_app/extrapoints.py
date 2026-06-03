import streamlit as st
import pandas as pd
from pathlib import Path
from typing import Any, Dict, List
from utils import TEAM_IMAGES, IMAGE_NAME_MAP


EXTRA_EVENTS: List[Dict[str, Any]] = [
    {"event": "Allererste Rose bei jeder Nacht der Rosen", "points": 1},
    {"event": "Letzte Rose bei jeder Nacht der Rosen", "points": 1},
    {"event": "Rose vor der Nacht der Rosen", "points": 2},
    {"event": "Ablehnung der Rose", "points": 3},
    {"event": "Erstes Übernachtungsdate (Fantasy Suite)", "points": 3},
    {"event": "Kuss", "points": 1},
    {"event": "Intim", "points": 3},
    {"event": "Händchenhalten in der Öffentlichkeit", "points": 2},
    {"event": "Frauenkuss", "points": 2},
    {"event": "Nacktbaden im Pool", "points": 2},
    {"event": "Rumgeheule", "points": 1},
    {"event": "Beef", "points": 2},
    {"event": "Wurf von Gegenständen bei einem Beef", "points": 3},
    {"event": "Verletzung (mimimi)", "points": 1},
    {"event": "Kandidatin, die den Bachelor wechselt", "points": 3},
    {"event": "Liebeserklärung bzw. Ich bin verliebt", "points": 3},
    {"event": "Frau tanzt aktiv für den Bachelor", "points": 2},
    {"event": "Runde weiter", "points": 1},
    {"event": "Meltdown - verlässt wütend das Gespräch", "points": 2},
    {"event": "Fake Detektor - behauptet jemand sei Fake", "points": 1},
    {"event": "Unterbricht ein Date oder Gespräch", "points": 1},
    {"event": "Windows Update - sieht so aus als würde das Gehirn gerade neu starten", "points": 1},
    {"event": "Bundestrainer - gibt ungefragt Ratschläge", "points": 1},
    {"event": "Golden Retriever - freut sich über alles", "points": 1},
    {"event": "Ninja - belauscht ein Gespräch", "points": 1},
    {"event": "Bachelor heult rum", "points": 2},
    {"event": "Zieht sein Hemd aus", "points": 1},
    {"event": "Horny Bachelor - schaut offensichtlich auf Ausschnitt oder Arsch", "points": 1},
    {"event": "Bachelor vergisst, dass Kameras noch laufen", "points": 1},
    {"event": "Bachelor's Flirtversuch, aber in cringe", "points": 1},
    {"event": "Kuss vom Bachelor wird abgelehnt", "points": 3},
]


def render_extrapoints() -> None:
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
