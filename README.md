# Streamlit and MongoDB API for retrieving data from sample Airbnb using ID number 

This project is developed specially in Streamlit and MongoDB for [Streamlit Connections Hackathon.](https://discuss.streamlit.io/t/connections-hackathon/47574)

# Application
Based on ID number, you can extract the information of the listing including but not limited to these, like current listing_url, property_type, number of bedrooms and bathrooms, amenities provided and price .

**Sample Output:**\
{
  "_id": "10306879",\
  "listing_url": "https://www.airbnb.com/rooms/10306879"\
  "name": "Alugo Apart frente mar Barra Tijuca",\
  "property_type": "Apartment",\
  "bedrooms": 1,\
  "bathrooms": "Decimal128('1.0')",\
  "amenities": [
    "TV",
    "Wifi",
    "Air conditioning",
    "Pool",
    "Kitchen",
    "Free parking on premises",
    "Pets allowed",
    "Doorman",
    "Gym",
    "Elevator",
    "Hot tub",
    "Buzzer/wireless intercom",
    "Family/kid friendly",
    "Washer",
    "Dryer",
    "Hangers",
    "Iron",
    "Laptop friendly workspace"
  ],\
  "price": "Decimal128('933.00')"\
}

## Sample ID number to test

- 10306879 - Expected sample output (name : "Alugo Apart frente mar Barra Tijuca")
- 1047087 - Expected sample output (name : "The Garden Studio")
- 10612199 - Expected sample output (name : "Serene luxury in Harlem")
- 10092679 - Expected sample output (name : "Cozy house at Beyoğlu")
- 10006546 - Expected sample output (name : "Ribeira Charming Duplex")
