import streamlit as st

def show_menu():
    # CSS pour uniformiser la largeur des boutons et aligner le texte à gauche
    st.markdown("""
        <style>
        .stButton > button {
            width: 100%;        /* Largeur de 100% pour uniformiser */
            text-align: left;   /* Alignement du texte à gauche */
            display: flex;      /* Utiliser Flexbox */
            align-items: center; /* Centrer le contenu verticalement */
            justify-content: flex-start; /* Aligner le texte à gauche */
            padding-left: 10px; /* Décalage du texte à gauche */
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Titre de la sidebar
    st.sidebar.markdown("<h1 style='text-align: center; color: black;'>GreenTech</h1>", unsafe_allow_html=True)
    
    # Boutons de navigation dans le menu latéral
    if st.sidebar.button("🏠 Accueil"):
        st.session_state.page = 'Accueil'
    if st.sidebar.button("🗺️ Cartographie"):
        st.session_state.page = 'Cartographie'
    if st.sidebar.button("📊 Prédiction prix de vente"):
        st.session_state.page = 'Prédiction'
    if st.sidebar.button("📈 Évolution"):
        st.session_state.page = 'Évolution'
    
    # Pied de page
    st.sidebar.markdown("GreenTech Solutions © 2024")

