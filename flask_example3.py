from flask import Flask, jsonify
from user_sqlamerchy import get_user_details  # Corrected import statement

app = Flask(__name__)

@app.route('/api/user/<int:user_id>/details')
def user_details(user_id):
    user_details_list = get_user_details(user_id)
    # Assuming we only want the first item if there are multiple for some reason
    if user_details_list:
        # Extract the first user's details
        user_detail_tuple = user_details_list[0]
        # Convert the tuple to a dictionary
        user_detail_dict = {
            'user_id': user_detail_tuple[0],
            'name': user_detail_tuple[1],
            'email': user_detail_tuple[2],
            'age': user_detail_tuple[3],
            'description': user_detail_tuple[4]
        }
    else:
        user_detail_dict = {}
    return jsonify(user_detail_dict)

if __name__ == '__main__':
    app.run(debug=True)
