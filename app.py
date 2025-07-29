import streamlit as st
from fruit_manager import *

# st.set_page_config(layout="wide")

# -- Interface
st.title("🍇 Dashboard de la Plantation")

inventaire = ouvrir_inventaire()
prix = ouvrir_prix()
tresorerie = ouvrir_tresorerie()

st.header("💰 Trésorerie")
st.metric(label="Montant disponible", value=f"{tresorerie:.2f} $")

st.header("📦 Inventaire")
st.table(inventaire)

st.sidebar.subheader("🛒 Vendre des Fruits")

select_fruit = st.sidebar.selectbox("Choisir un fruit", inventaire)
qte_vente = st.sidebar.number_input("Quantité à vendre", value=5, min_value=0)

if st.sidebar.button("Vendre"):
    inventaire, tresorerie = vendre(
        inventaire, select_fruit, qte_vente, tresorerie, prix
    )
    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)
    st.rerun()
