from color import Color, _print, _error, _info, _warning, _success
from _input import Input
from exercise_14 import Exercise14
from exercise_17 import Exercise17
from exercise_24 import Exercise24


def main():
    execute_question = Input()
    execute_question.get_input({
        Input.text_key : 'Escolha uma questão para executar[14|17|24]: ',
        Input.type_key : Input.INT,
        Input.acceptable_input_key : '14|17|24'
    })
    if execute_question._input == 14:
        _e = Exercise14()
        sentence = _e.start_quiz()
        _info('Sentença: %s' % sentence.upper())
    elif execute_question._input == 17:
        _e = Exercise17()
        _e.start_quiz()
        _e.print_athletes_performance()
    elif execute_question._input == 24:
        _e = Exercise24(100)
        _e.play()
        _e.show_statistics()
        _e.reset()
    del(_e)



if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\n\n')
        _info('Bye!')
        exit(0)
