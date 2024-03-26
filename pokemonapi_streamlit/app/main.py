import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import requests
from api.data_manager import save_data_to_json, load_data_from_json

def fetch_pokemon_data(endpoint_url):
    response = requests.get(endpoint_url)
    data = response.json()
    return data

def display_pokemon_info(endpoints, search_term, limit):
    st.title("PokeAPI Data")
    st.markdown("---")

    if endpoints:
        for endpoint, url in endpoints.items():
            if search_term.lower() in endpoint.lower() or search_term == "":
                if st.checkbox(f"Show {endpoint}"):
                    items_response = fetch_pokemon_data(url)
                    items = items_response.get("results", [])[:limit]
                    if items:
                        st.write(f"### {endpoint}:")
                        st.write("#### Results:")
                        for item in items:
                            st.write(f"- {item['name']}")
                    else:
                        st.write("No items found.")
    else:
        st.error("Failed to fetch data from the PokeAPI. Please try again later.")



def main():
    st.markdown("# Welcome to the PokeAPI Explorer!")
    st.markdown("Use the options below to explore different endpoints of the PokeAPI.")

    endpoints_data = load_data_from_json()
    
    if endpoints_data is None:
        response = requests.get("https://pokeapi.co/api/v2/")
        endpoints_data = response.json()
        save_data_to_json(endpoints_data)

    endpoints = endpoints_data if isinstance(endpoints_data, dict) else {}

    if endpoints:
        search_term = st.text_input("Search for an endpoint:", "")
        limit = st.slider("Select the limit of items to display:", 1, 20, 20)  # Set the maximum limit back to 20
        display_pokemon_info(endpoints, search_term, limit)
    else:
        st.error("Failed to fetch endpoints from the PokeAPI. Please try again later.")

if __name__ == "__main__":
    main()
