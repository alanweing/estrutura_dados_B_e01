from color import Color, _print
from _input import Input

class Exercise14:

    questions = None
    answers = None
    sentence = None

    def __init__(self):
        self.questions = [
            'Telefonou para a vítima?',
            'Esteve no local do crime?',
            'Mora perto da vítima?',
            'Devia para a vítima?',
            'Já trabalhou para a vítima?'
        ]
        self.answers = {}

    def add_question(self, question):
        if question not in self.questions:
            self.questions.extend(question)
        else:
            _print('Essa questão já está cadastrada! Deseja continuar? [s/n]', Color.YELLOW)

    def remove_question(self, question):
        try:
            self.questions.remove(question)
        except ValueError:
            _print('\n\t=>Essa questão não está cadastrada!\n', Color.RED, True)

    def add_answer(self, key, answer):
        # self.answers[key] = answer
        self.answers.update({key:answer})

    def start_quiz(self):
        c_input = Input()
        for question in self.questions:
            print('\n')
            c_input.get_input({
                c_input.type_key: c_input.STRING,
                c_input.text_key: '\t' + question + ' [sim/nao]: ',
                c_input.acceptable_input_key: 'sim|nao|s|n'
            })
            self.add_answer(question, c_input._input)
        return self.parse_quiz()

    def parse_quiz(self):
        score = 0
        for key in list(self.answers):
            if self.answers[key] == 'sim' or self.answers[key] == 's':
                score += 1
        if score == 2:
            self.sentence = 'Suspeita'
        elif 3 <= score <= 4:
            self.sentence = 'Cúmplice'
        elif score == 5:
            self.sentence = 'Assassino'
        else:
            self.sentence = 'Inocente'
        return self.sentence
