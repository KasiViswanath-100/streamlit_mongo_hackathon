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
        "_id": 1,               # Exclude the MongoDB default "_id" field
        "name": 1,              # Include the "name" field
        "property_type": 1,     # Include the "property_type" field
        "price": 1,             # Include the "price" field
        "bedrooms": 1,          # Include the "bedrooms" field
        "bathrooms": 1,         # Include the "bathrooms" field
        "amenities": 1,         # Include the "amenities" field
    }
    # results = collection.find({"some_key": "some_value"})
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
    
