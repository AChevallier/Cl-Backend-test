Scenario1 = {
    'name': 'scenario 1',
    'steps': [{
        'id': 1,
        'name': 'greetings',
        'actions': [{
            'type': 'text',
            'data': 'Hi, how are you ?'
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
            'data': 'Cool'
        }],
    }, {
        'id': 3,
        'name': 'questionning',
        'actions': [{
            'type': 'text',
            'data': 'Why ?'
        }],
        'connections': [{
            'condition': ['bad', 'day'],
            'next_step': 4
        }, ]
    }, {
        'id': 4,
        'name': 'giving happiness',
        'actions': [
            {
                'type': 'text',
                'data': 'Look at that'
            }, {
                'type': 'image',
                'data': 'https://i.imgur.com/4QvA1xc.gif'
            }]
    }, ]
}

Scenario2 = {
    'name': 'scenario 1',
    'steps': [{
        'id': 1,
        'name': 'greetings',
        'actions': [{
            'type': 'text',
            'data': 'Hi, what\'s up?'
        }],
        'connections': [{
            'condition': 'nothing',
            'next_step': 2
        }, {
            'condition': 'beautiful',
            'next_step': 3
        },
            {
            'condition': 'bad',
            'next_step': 5
        }, ]
    }, {
        'id': 2,
        'name': 'nothing OK',
        'actions': [{
            'type': 'text',
            'data': 'Perfect !'
        }],
    }, {
        'id': 3,
        'name': 'weather good',
        'actions': [{
            'type': 'text',
            'data': 'It is true beautiful weather,isn\'t it ?'
        }],
        'connections': [{
            'condition': 'yes',
            'next_step': 4
        }, {
            'condition': 'no',
            'next_step': 6
        }]
    }, {
        'id': 4,
        'name': 'giving happiness',
        'actions': [
            {
                'type': 'text',
                'data': 'You reply what i said, lol'
            }]
    },
        {
        'id': 5,
        'name': 'bad weather',
        'actions': [
            {
                'type': 'text',
                'data': 'rainy day'
            }]
    },
        {
        'id': 6,
        'name': 'lol check outside',
        'actions': [
            {
                'type': 'text',
                'data': 'Check outside, dude'
            }]
    }, ]
}
