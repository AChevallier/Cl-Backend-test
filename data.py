Scenario1 = {
    'name': 'scenario 1',
    'steps': [{
        'id': 1,
        'name': 'greetings',
        'actions': [{
            'type': 'text',
            'answer_text': 'Hi, how are you ?'
        }],
        'connections': [{
            'condition': 'fine',
            'next_step': 2
        }, {
            'condition': 'sad',
            'next_step': 3
        }, ]
    }, {
        'id': 2,
        'name': 'everything OK',
        'actions': [{
            'type': 'text',
            'answer_text': 'Cool'
        }],
    }, {
        'id': 3,
        'name': 'questionning',
        'actions': [{
            'type': 'text',
            'answer_text': 'Why ?'
        }],
        'connections': [{
            'condition': ['bad', 'day'],
            'next_step': 4
        }, ]
    }, {
        'id': 4,
        'name': 'giving happiness',
        'actions': [{
            'type': 'image',
            'answer_text': None,
            'url_data': 'https://i.imgur.com/4QvA1xc.gif'
        }]
    }, ]
}
