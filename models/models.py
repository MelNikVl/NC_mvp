from datetime import datetime

from sqlalchemy import Integer, Column, Boolean, ForeignKey, ARRAY, DateTime, String


class Users(Base):
    tablename = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True)
    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    permission = Column(Integer)
    role = Column(Integer)
    phone = Column(Integer)
    bookmarks = Column(ARRAY(String))
    date_of_registrations = Column(DateTime)


class Ads_for_sale(Base):
    tablename = 'Ads_for_sale'

    id = Column(Integer, primary_key=True, index=True)
    x_coordinates = Column(Integer)
    y_coordinates = Column(Integer)
    title = Column(String)
    description = Column(String)
    price = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))
    object_type = Column(Integer)
    rooms_count = Column(Integer)
    number_of_toilets = Column(Integer)
    total_netto_area = Column(Integer)
    total_brutto_area = Column(Integer)
    kitchen_area = Column(Integer)
    address = Column(String)
    loggia = Column(Boolean)
    floor = Column(Integer)
    furnishing = Column(Boolean)
    year_of_construction = Column(Integer)
    elevator = Column(Boolean)
    closed_area = Column(Boolean)
    date_of_publication = Column(DateTime)
    uniq_number = Column(String)
    who_is_selling = Column(Integer)
    secondary_or_new_building = Column(Boolean)
    delivery_time = Column(DateTime)
    tapu_availability = Column(Boolean)


class Ads_for_rent(Base):
    tablename = 'Ads_for_sale'

    id = Column(Integer, primary_key=True, index=True)
    x_coordinates = Column(Integer)
    y_coordinates = Column(Integer)
    title = Column(String)
    description = Column(String)
    price = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))
    object_type = Column(Integer)
    rooms_count = Column(Integer)
    number_of_toilets = Column(Integer)
    total_netto_area = Column(Integer)
    total_brutto_area = Column(Integer)
    kitchen_area = Column(Integer)
    address = Column(String)
    loggia = Column(Boolean)
    floor = Column(Integer)
    furnishing = Column(Boolean)
    year_of_construction = Column(Integer)
    elevator = Column(Boolean)
    closed_area = Column(Boolean)
    date_of_publication = Column(DateTime)
    uniq_number = Column(String)
    who_is_selling = Column(Integer)
    tapu_availability = Column(Boolean)
    how_long = Column(Integer)
    residence_permit = Column(Boolean)


class Logs(Base):
    tablename = "logs"

    id: int = Column(Integer, primary_key=True, index=True)
    kind_table: str = Column(String)
    user_id: int = Column(Integer)
    passive_id: int = Column(Integer)
    modified_cols: str = Column(String)
    values_of_change: str = Column(String)
    date_time: str = Column(String)