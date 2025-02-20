import flask
from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import joblib

app = Flask(__name__)
app.secret_key = 'secret_key'  # Set a secret key for flash messages
loaded_mdl = joblib.load("model/trained-model.joblib")
mapping_data = pd.read_csv('labelled_features.csv')


def get_ordered_players(players_remaining):
    ordered = []
    hits = mapping_data[mapping_data['player'].isin(players_remaining)]

    if hits.empty:
        flash("Sorry! This player data does not exist in our system at the moment.")
        return ordered

    hits = hits.sort_values(by=['is_best_batsman', 'batting_average', 'strike_rate'],
                            ascending=[False, False, False])
    for index, player in enumerate(hits['player']):
        ordered.append((player, index + 1))

    return ordered

@app.route('/', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        team1 = request.form['team1']
        team2 = request.form['team2']
        balls_remaining = int(request.form['balls_remaining'])
        runs_required = int(request.form['runs_required'])
        players_remaining = request.form['players_remaining'].splitlines()

        results = get_ordered_players(players_remaining)
        flash(f"Now showing the results of {team1} vs {team2}. Who will be better suited for the batting order in order to chase runs successfully?")
        return render_template('results.html', results=results)

    return render_template('input_form.html')


@app.route('/results', methods=['POST'])
def get_prediction():
    team1 = request.form['team1']
    team2 = request.form['team2']
    balls_remaining = int(request.form['balls_remaining'])
    runs_required = int(request.form['runs_required'])
    players_remaining = request.form['players_remaining'].splitlines()

    results = get_ordered_players(players_remaining)
    return render_template('results.html', results=results)


@app.route('/get-prediction', methods=['POST'])
def get_results():
    team1 = request.form['team1']
    team2 = request.form['team2']
    balls_remaining = int(request.form['balls_remaining'])
    runs_required = int(request.form['runs_required'])
    players_remaining = request.form['players_remaining'].splitlines()

    results = get_ordered_players(players_remaining)
    return dict(get_results)


@app.route('/health')
def startup():
    return 'API is Live & ready to make predictions!'


if __name__ == '__main__':

    app.run(port=5001)