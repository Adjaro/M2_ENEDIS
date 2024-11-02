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
        /* Agrandir le titre */
        .sidebar-title {
            font-size: 24px !important; /* Ajustez la taille selon vos besoins */
            text-align: center; 
            color: black; 
            margin: 20px 0; /* Espacement autour du titre */
        }
        /* Style pour le pied de page */
        .footer {
            position: relative; /* Changez en relative pour éviter de le coller en bas */
            margin-top: auto; /* Pour le pousser vers le bas si nécessaire */
            padding: 20px 0; /* Ajustez l'espacement autour du texte */
            text-align: center; /* Centrer le texte */
            color: black; /* Couleur du texte */
            font-size: 14px; /* Taille du texte */
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Titre de la sidebar
    st.sidebar.markdown("<h1 class='sidebar-title'>GreenTech Solutions</h1>", unsafe_allow_html=True)
    
    # Boutons de navigation dans le menu latéral
    if st.sidebar.button("🏠 Accueil"):
        st.session_state.page = 'Accueil'
    if st.sidebar.button("🗺️ Cartographie"):
        st.session_state.page = 'Cartographie'
    if st.sidebar.button("📊 Prédiction"):
        st.session_state.page = 'Prédiction'
    if st.sidebar.button("📈 Évolution"):
        st.session_state.page = 'Évolution'
    
    # Pied de page, placé avec du CSS
    st.sidebar.markdown("<div class='footer'>Awa Edina Nancy © 2024</div>", unsafe_allow_html=True)

