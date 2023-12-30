from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def show_time():
    # You can change timezone by replacing 'UTC' with your desired timezone.
    timezone = pytz.timezone("UTC")
    current_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
    return f'Current Time: {current_time}'


@app.route('/<timezone>')
def show_time_by_region(timezone):
    # You can change timezone by replacing 'UTC' with your desired timezone.
    timezone = timezone.replace('-', '/')  # AsiaColombo
    timezone = pytz.timezone(timezone)
    current_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
    return f'Current Time: {current_time}'


if __name__ == '__main__':
    app.run(debug=True)
