from dash import html, dcc, Input, Output, State, Dash, no_update
import base64
import random
app = Dash(__name__)

# Encode the local sound file.
sound_filename = 'guitare.mp3'  # replace with your own .mp3 file
encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())

word_list = ["guitare",
        "dessus",
        "bientôt",
        "poule",
        "manger",
        "petit",
        "rapide"
        ]

word_number = len(word_list)

app.layout = html.Div(children=[
    html.H1(children="Apprends les mots en t'amusant!"),

    html.Div(id='output-image-container'),

    html.Button(id="button1", children="Click me for changing sound"),
    html.Audio(id='audio-player', src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode()),
                          controls=True,
                          autoPlay=False,
                          ),
    html.Div(id="message", children=[]),
    dcc.Store(id='my-store', data=word_list[0]),
    dcc.Input(id='text-input', debounce=True),
    ])



@app.callback(
        [
    Output('message', 'children'),
    Output('audio-player', 'src'),
    Output('my-store', 'data')
    ],
    Input('text-input', 'value'),
    State('my-store', 'data')
        )
def update_input(val, word):
    print(val, word)
    if val == word:
        i = random.randint(0, word_number - 1)
        word = word_list[i]
        print(word)
        sound_filename = word + '.mp3'
        encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())
        sound_str = 'data:audio/mpeg;base64,{}'.format(encoded_sound.decode())
        return 'bravo', sound_str, word
    else:
        return 'essaye encore', no_update, no_update


if __name__ == '__main__':
    app.run_server(debug=True)
