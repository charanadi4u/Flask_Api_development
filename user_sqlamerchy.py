from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select, and_

# Assuming you have SQLAlchemy installed and your database connection set up
engine = create_engine('sqlite:///yourdatabase.db')  # Update with your actual database URL
# metadata = MetaData(bind=engine)
# Create a MetaData instance
metadata = MetaData()
metadata.bind = engine  # Bind the engine to the metadata

# Assuming 'users' and 'profiles' tables are defined in your database
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('email', String))

profiles = Table('profiles', metadata,
                 Column('user_id', None, ForeignKey('users.id')),
                 Column('age', Integer),
                 Column('bio', String))

metadata.create_all(engine)

# # Insert some example data
# with engine.connect() as conn:
#     conn.execute(users.insert(), [
#         {'name': 'John Doe', 'email': 'johndoe@example.com'},
#         {'name': 'Jane Doe', 'email': 'janedoe@example.com'}
#     ])
#     conn.execute(profiles.insert(), [
#         {'user_id': 1, 'age': 30, 'bio': 'A mysterious person'},
#         {'user_id': 2, 'age': 25, 'bio': 'An adventurous person'}
#     ])
#     conn.commit()

def get_user_details(user_id):
    query_config = {
        "table": users,
        "columns": [users.c.id, users.c.name, users.c.email, profiles.c.age, profiles.c.bio],
        "filters": users.c.id == user_id,
        "join": profiles,  # Simplified for clarity
        "on": users.c.id == profiles.c.user_id
    }
    
    # The key change: Unpack the columns list using * in the select() call
    query = select(*query_config['columns']).select_from(
        query_config['table'].join(query_config['join'], query_config['on'])
    ).where(query_config['filters'])
    
    with engine.connect() as connection:
        result = connection.execute(query)
        user_details = result.fetchall()  # Fetching all results
        return user_details

# Example usage
# user_id = 1  # Example user ID
# user_details = get_user_details(user_id)
# print(user_details)
    
try:
    user_id = 1
    user_details = get_user_details(user_id)
    print(user_details)
except Exception as e:
    print(f"An error occurred: {e}")

