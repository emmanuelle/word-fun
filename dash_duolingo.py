from dash import html, dcc, Input, Output, State, Dash, no_update, ctx
import dash_bootstrap_components as dbc
import base64
import random
import os
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets += [dbc.themes.BOOTSTRAP]

app = Dash(__name__,
        external_stylesheets=external_stylesheets)

# Encode the local sound file.
sound_filename = os.path.join('audio_files', 'farine.mp3')
encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())

question_mark_url = 'https://live.staticflickr.com/5217/5471047557_4dc13f5376_n.jpg'

cute_img_url = 'https://i.pinimg.com/736x/9e/0a/4a/9e0a4a2928afbd156281834fb2f18fbc.jpg'

word_list = pd.read_excel('words.ods')['mot']

word_number = len(word_list)

app.layout = html.Div(children=[
    html.H3(children="Apprends les mots en t'amusant!"),

    html.Div(id='output-image-container'),

    html.Audio(id='audio-player', src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode()),
                          controls=True,
                          autoPlay=True,
                          ),
    html.Br(),
    dcc.Store(id='my-store', data=word_list[0]),
    dcc.Store(id='score', data=0),
    dcc.Input(id='text-input', debounce=True, placeholder="Ecris ici"),
    html.Button('Mot suivant', id='next-button', n_clicks=0),
    html.H3(id="message", children="", style={'color': '#fc03fc'}),
    html.Img(id='img', src=question_mark_url, height=300)
    ])



@app.callback(
        [
    Output('message', 'children', allow_duplicate=True),
    Output('score', 'data'),
    Output('img', 'src', allow_duplicate=True)
    ],
    Input('text-input', 'value'),
    State('my-store', 'data'),
    State('score', 'data'),
    prevent_initial_call=True
        )
def update_input(val, word, score_value):
    if val == '':
        return no_update, no_update, no_update
    elif val == word:
        new_score = score_value + 1
        return f"bravo \N{winking face}! Ton nouveau score est {new_score} point", new_score, cute_img_url
    else:
        return 'essaye encore', no_update, no_update

@app.callback(
        [
    Output('message', 'children', allow_duplicate=True),
    Output('audio-player', 'src'),
    Output('my-store', 'data'),
    Output('text-input', 'value'),
    Output('img', 'src', allow_duplicate=True)
    ],
    Input('next-button', 'n_clicks'),
    prevent_initial_call=True
        )
def next_word(n_clicks):
    i = random.randint(0, word_number - 1)
    word = word_list[i]
    print(word)
    sound_filename = os.path.join('audio_files', word + '.mp3')
    encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())
    sound_str = 'data:audio/mpeg;base64,{}'.format(encoded_sound.decode())
    return '', sound_str, word, '', question_mark_url


if __name__ == '__main__':
    app.run_server(debug=True)
