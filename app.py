import streamlit as st
from pymongo import MongoClient
import toml
from streamlit.connections import ExperimentalBaseConnection
from connection import MongoDBConnection
import streamlit as st

@st.cache_data(ttl=None, max_entries=15, show_spinner=True)
def query(id_number):
    
    conn = st.experimental_connection("mongo_db", type=MongoDBConnection)
    mongo_conn = MongoDBConnection("mongo_db")
    collection = mongo_conn._connect(database="sample_airbnb", collection="listingsAndReviews")
    query = {"_id": id_number}
    
    projection = {
        "_id": 1,               
        "name": 1,              
        "property_type": 1,    
        "price": 1, 
        "listing_url":1,
        "bedrooms": 1,          
        "bathrooms": 1,         
        "amenities": 1,         
    }
    
    data = list(collection.find(query, projection))
    return data

def main():
    st.title("Streamlit MongoDB API Example")
    id_number = st.text_input("Enter the ID number:")

    if id_number:
        # Query specific details based on the ID number
        data = query(id_number)

        # Display the data on the Streamlit app
        if data:
            st.write("Data fetched from MongoDB:")
            for item in data:
                st.write(item)
        else:
            st.write("No data found in MongoDB for the specified ID.")

if __name__ == "__main__":
    main()
    
