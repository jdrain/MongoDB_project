__author__ = 'jason'

"""
The template for all collection objects

"""

from mongoengine import *
import datetime

class Groups(DynamicDocument):

    name = StringField(max_length=200, required=True)
    institution = StringField(max_length=250, required=True)

class Scientists(DynamicDocument):

    name = StringField(max_length=150, required=True)
    email = StringField(max_length=150)
    phone = StringField(max_length=50)
    group = ReferenceField(Groups)

class Processes(DynamicDocument):

    name = StringField(max_length=10**3, required=True)
    amount = DecimalField(max_length=10)
    composition = StringField(max_length=10**3)
    CAS_number = StringField(required=True)

class Support(DynamicDocument):

    name = StringField(max_length=100, required=True)
    details = StringField(max_length=10**3)

class Hazards(DynamicDocument):

    ignitable = IntField(required=True)
    corrosive = IntField(required=True)
    reactive = IntField(required=True)
    poisonous = IntField(required=True)

class Characterization(DynamicDocument):

    name = StringField(max_length=100, required=True)
    details = StringField(max_length=10**3)

class SyntheticProducts(DynamicDocument):

    composition = DecimalField(required=True)
    date = DateTimeField(default=datetime.datetime.now)
    notebook_reference = StringField(max_length=10**4)

class Samples(DynamicDocument):

    concentration = DecimalField(required=True)
    comments = StringField(max_length=10**4)
    scientist = ReferenceField(Scientists)
    product = ReferenceField(SyntheticProducts)
    process = ReferenceField(Processes)
    support = ReferenceField(Support)
    hazards = ReferenceField(Hazards)
    characterization = ReferenceField(Characterization)

class Shipments(DynamicDocument):

    date = DateTimeField(required=True)
    recipient = StringField(max_length=100, required=True)
    scientist = ReferenceField(Scientists)
    address = StringField(max_length=10**3, required=True)

class Vials(DynamicDocument):

    amount = DecimalField(required=True)
    concentration = DecimalField(required=True)
    quantity = DecimalField(required=True)
    shipment = ReferenceField(Shipments)
    sample = ReferenceField(Samples)

class ExperimentType(DynamicDocument):

    type = StringField(max_length=100, required=True)

class PlannedExperiments(DynamicDocument):

    type = ReferenceField(ExperimentType)
    priority = IntField()
    planned_date = DateTimeField()
    scientist = ReferenceField(Scientists)

class RanExperiments(DynamicDocument):

    plan = ReferenceField(PlannedExperiments)
    scientist = ReferenceField(Scientists)
    images = StringField(max_length=10**4)

class DataProcessing(DynamicDocument):

    experiment = ReferenceField(RanExperiments)
    software_version = StringField(max_length=10**3)
    kwargs = StringField(max_length=10**4)
    procedure = StringField(max_length=10**5)
    processed_data = StringField(10**3)

class Simulations(DynamicDocument):

    starting_atoms = StringField(max_length=10**4)
    finished_atoms = StringField(max_length=10**4)
    calculator = StringField(max_length=10**3)
    data = ReferenceField(DataProcessing)