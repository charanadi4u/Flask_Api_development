from flask import Flask,jsonify,session

app = Flask(__name__)

features = {'new_search_algorithm' : {'enabled': True, 'version' : 'v2'},
            'beta_features' : {'enabled' : True, 'version' : 'v3'}}

@app.route('/api/search')
def search():
    if features['new_search_algorithm']['enabled']:
        pass
    else:
        pass
    return jsonify(resutlts=[])

if __name__ == '__main__':
    app.run(debug=True)