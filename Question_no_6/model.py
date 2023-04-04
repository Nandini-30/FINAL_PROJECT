from route import db

class StoreStatus:
    def __init__(self,status_code,message,storeobject):
        self.status_code=status_code
        self.message=message
        self.storeobject=storeobject


class Store(db.Model):
    __tablename__="MyStore" #table name
    quanorder=db.Columndb.Column(db.Integer(), unique=True, nullable=False, primary_key=True)
    nameacc=db.Column(db.String(), unique=True, nullable=False)
    quanremain=db.Column(db.Integer(), unique=True, nullable=False)
    vendorname=db.Column(db.String(), unique=True, nullable=False)
    pppi=db.Column(db.Integer(), unique=True, nullable=False)
    sppi=db.Column(db.Integer(), unique=True, nullable=False)
    datetimeadd=db.Column(db.Integer(), unique=True, nullable=False)
    datetimeupdated=db.Column(db.Integer(), unique=True, nullable=False)

def __init__(self,quanorder,nameacc,quanremain,vendornam,pppi,sppi,datetimeadd,datetimeupdated):
    self.quanorder 
    self.nameacc
    self.quanremain
    self.vendornam
    self.pppi
    self.sppi
    self.datetimeadd
    self.datetimeupdated

def __repr__(self):
    return f"{self.quanorder},{self.nameacc},{self.quanremain},{self.vendornam},{self.pppi},{self.sppi},{self.datetimeadd},{self.datetimeupdated}"
