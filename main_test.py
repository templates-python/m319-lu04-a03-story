import pytest
from main import main

def test_main(monkeypatch, capsys):
    input_values = ['John', 'Engineer']
    input_generator = iter(input_values)
    prompts = []

    def mock_input(prompt):
        prompts.append(prompt)
        return next(input_generator)

    monkeypatch.setattr('builtins.input', mock_input)
    main()
    captured = capsys.readouterr()

    # Check the input prompts
    assert prompts == [
        'What is the main character called?\n',
        'What is their job?\n'
    ]

    # Check the printed output
    assert captured.out == (
        'I will tell you a story, but I need some information first.\n'
        'Here is the story:\n'
        'Once upon a time there was John, who was a Engineer.\n'
        'On the way to work, John reflected on life.\n'
        'Perhaps John will not be a Engineer forever.\n'
    )
