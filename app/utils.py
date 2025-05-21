import pandas as pd
import os
import streamlit as st # For caching


def get_data_path(filename):
    """Tries to find the data file in common relative locations."""
    path_option1 = os.path.join('../data', filename) # If running from app/
    path_option2 = os.path.join('data', filename)    # If running from project root
    
    if os.path.exists(path_option1):
        return path_option1
    elif os.path.exists(path_option2):
        return path_option2
    else:
        return None # Or raise an error

@st.cache_data(ttl=3600)
def load_cleaned_data(country_name_full):
    """
    Loads a single cleaned dataset from Google Drive for a given country.
    """
    file_map = {
        'Benin (Malanville)': 'https://drive.google.com/uc?export=download&id=15b9GK44EsXAWef7gR8SYIsYC36jt-snV',
        'Sierra Leone (Bumbuna)': 'https://drive.google.com/uc?export=download&id=1cYIm1K2liDkdrHOmeILJqmduokdxt6Rk',
        'Togo (Dapaong QC)': 'https://drive.google.com/uc?export=download&id=1IkeFZIOkiUw3HLIQpzUgyXFtVyLfTZBD'
    }

    file_url = file_map.get(country_name_full)
    if not file_url:
        st.error(f"No file mapping found for country: {country_name_full}")
        return pd.DataFrame()

    try:
        df = pd.read_csv(file_url)
        if 'Timestamp' in df.columns:
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df['Country'] = country_name_full
        return df
    except Exception as e:
        st.error(f"Error loading data for {country_name_full} from Google Drive: {e}")
        return pd.DataFrame()


@st.cache_data(ttl=3600)
def load_all_cleaned_data(countries_to_load):
    """Loads and concatenates cleaned data for selected countries."""
    all_dfs = []
    for country_name in countries_to_load:
        df = load_cleaned_data(country_name)
        if not df.empty:
            all_dfs.append(df)
    
    if not all_dfs:
        return pd.DataFrame() # Return empty DataFrame if no data loaded
    
    combined_df = pd.concat(all_dfs, ignore_index=True)
    return combined_df