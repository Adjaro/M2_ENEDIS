import streamlit as st

def show():

    # Titre de la page
    st.header("Prédiction")

    # Créer un formulaire
    with st.form(key='prediction_form'):
       
        surface = st.number_input("Surface (en m²)", min_value=0, step=1)
        commune = st.selectbox("Commune", ["Commune 1", "Commune 2", "Commune 3", "Commune 4"])
        current_year = 2024  
        years = list(range(1950, current_year + 1))[::-1] 
        year_of_construction = st.selectbox("Année de construction", years)

        # soumettre
        submit_button = st.form_submit_button("Soumettre")

        # Action à effectuer lors de la soumission
        if submit_button:
            # Logique de prédiction avec les valeurs récupérées
            st.success(f"Formulaire soumis avec succès ! Surface: {surface} m², Région: {commune}, Année de construction: {year_of_construction}")
