from color import Color, _print, _error, _info, _warning, _success
from _input import Input
from exercise_14 import Exercise14


def main():
    execute_question = Input()
    execute_question.get_input({
        execute_question.text_key: 'Escolha uma questão para executar[14|17|24]: ',
        execute_question.type_key: execute_question.INT,
        execute_question.acceptable_input_key: '14|17|24'
    })
    if execute_question._input == 14:
        _e = Exercise14()
        sentence = _e.start_quiz()
        _info('A vítima é :%s' % sentence.upper())


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        _info('Bye')
        exit(0)
