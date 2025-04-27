import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

# === Dane przykładowe ===
questions = [
    {
        "question": "Firma ma nadwyżkę budżetową. Co powinna zrobić?",
        "options": [
            "Zainwestować w marketing",
            "Zwiększyć zatrudnienie",
            "Oszczędzać na koncie firmowym"
        ],
        "charts": [
            px.sunburst(
                names=["Marketing", "Social Media", "TV", "Internet"],
                parents=["", "Marketing", "Marketing", "Marketing"],
                values=[100, 30, 40, 30],
                title="Dystrybucja budżetu marketingowego"
            ),
            go.Figure(go.Indicator(
                mode="number+delta",
                value=120,
                delta={"reference": 100},
                title={"text": "Wzrost efektywności zespołu"}
            )),
            go.Figure(go.Scatterpolar(
                r=[80, 85, 83],
                theta=["Miesiąc 1", "Miesiąc 2", "Miesiąc 3"],
                fill='toself'
            )).update_layout(title="Stabilny wzrost oszczędności")
        ]
    },
    {
        "question": "Czy warto zainwestować w nową technologię (koszt: 50 000 zł)?",
        "options": [
            "Tak, przyniesie długoterminowe zyski",
            "Nie, to zbyt ryzykowne",
            "Może za rok, po analizie"
        ],
        "charts": [
            px.funnel(x=["Inwestycja", "Zysk po 2 latach", "Zysk po 3 latach"], y=[50000, 80000, 120000], title="Zwrot z inwestycji w technologię"),
            px.treemap(
                names=["Ryzyko", "Technologia", "Niezgodność", "Nieprzewidywalność"],
                parents=["", "Ryzyko", "Ryzyko", "Ryzyko"],
                values=[100, 40, 30, 30],
                title="Elementy ryzyka technologicznego"
            ),
            go.Figure(go.Indicator(
                mode="gauge+number",
                value=65,
                title={'text': "Oczekiwany zysk za rok"},
                gauge={'axis': {'range': [None, 100]}}
            ))
        ]
    },
    {
        "question": "Jak firma powinna zareagować na spadek popytu?",
        "options": [
            "Obniżyć ceny produktów",
            "Zwiększyć budżet marketingowy",
            "Zredukować koszty operacyjne"
        ],
        "charts": [
            px.area(x=["Tydzień 1", "Tydzień 2"], y=[70, 90], title="Efekt obniżki cen na sprzedaż"),
            px.scatter_3d(
                x=[1, 2, 3], y=[10000, 15000, 19000], z=[5, 10, 15],
                title="Skuteczność marketingu w czasie",
                labels={"x": "Tydzień", "y": "Przychód", "z": "Nowi klienci"}
            ),
            px.sunburst(
                names=["Koszty", "Logistyka", "Administracja", "Technologie"],
                parents=["", "Koszty", "Koszty", "Koszty"],
                values=[100, 30, 30, 40],
                title="Obszary redukcji kosztów"
            )
        ]
    },
    {
        "question": "Jak najlepiej zainwestować zysk firmy?",
        "options": [
            "W szkolenia pracowników",
            "W nowy sprzęt IT",
            "W kampanię reklamową"
        ],
        "charts": [
            px.bar_polar(r=[70, 85], theta=["Przed", "Po"], title="Wzrost kompetencji po szkoleniu"),
            px.scatter(x=["Stary", "Nowy"], y=[50, 100], size=[20, 40], title="Efektywność sprzętu IT"),
            px.treemap(
                names=["Klienci", "Nowi", "Stali"],
                parents=["", "Klienci", "Klienci"],
                values=[100, 60, 40],
                title="Struktura klientów po kampanii reklamowej"
            )
        ]
    }
]

st.set_page_config(page_title="Quiz ekonomiczny z wizualizacjami", layout="wide")
st.title("💼 Interaktywny Quiz Ekonomiczny z Wizualizacjami")

score = 0

for i, q in enumerate(questions):
    st.header(f"Pytanie {i+1}: {q['question']}")
    selected = st.radio("Wybierz odpowiedź:", q['options'], index=None, key=f"question_{i}")

    if selected:
        chart_index = q['options'].index(selected)
        st.plotly_chart(q['charts'][chart_index], use_container_width=True)

        if i == 0 and selected == "Zainwestować w marketing":
            score += 1
        elif i == 1 and selected == "Tak, przyniesie długoterminowe zyski":
            score += 1
        elif i == 2 and selected == "Zwiększyć budżet marketingowy":
            score += 1
        elif i == 3 and selected == "W szkolenia pracowników":
            score += 1
    else:
        st.warning("👉 Wybierz odpowiedź, aby zobaczyć wykres")

st.markdown("---")
st.subheader(f"✅ Twój wynik: {score}/{len(questions)}")
if score == len(questions):
    st.success("🎉 Świetnie! Twoje decyzje pokazują, że masz zmysł do biznesu!")
elif score >= len(questions) // 2:
    st.info("👍 Nieźle! Masz dobre wyczucie ekonomiczne.")
else:
    st.error("📘 Przemyśl jeszcze raz swoje decyzje. Każda decyzja w biznesie ma konsekwencje!")
