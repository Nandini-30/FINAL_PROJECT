from model import Store , StoreStatus
from app import db

class StoreDB:

    def findStore(self,quanorder):
        user = Store.query.filter_by(email=email).first()