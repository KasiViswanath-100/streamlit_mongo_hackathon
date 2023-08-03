from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
import streamlit as st
from pymongo import MongoClient

class MongoDBConnection(ExperimentalBaseConnection[MongoClient]):
    def _connect(self, **kwargs) -> MongoClient:
        db = kwargs.pop("database", None) or self._secrets.get("database")
        coll = kwargs.pop("collection", None) or self._secrets.get("collection")
        parameters = {**self._secrets.get("kwargs", {}), **kwargs}
        client = MongoClient(self._secrets.get("url"), **parameters)
        
        return client[db][coll]
        
MongoDBConnection("mongo_db")
