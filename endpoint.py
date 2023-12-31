from flask import *
import datetime

app = Flask(__name__)

@app.route('/api', methods =['GET'])
def get_info():
    slack_name = request.args.get('Boniface')
    track = request.args.get('backend')
    current_day = datetime.datetime.now().strftime('%A')
    current_utc = datetime.datetime.utcnow().isoformat()+'Z'
    github_file_url = 'https://github.com/Benyedder98/hng/blob/main/endpoint.py'
    github_repo_url = 'https://github.com/Benyedder98/hng'

    data_set = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time':current_utc,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }
    return jsonify(data_set)
if __name__ == '__main__':
    app.run(debug=True)