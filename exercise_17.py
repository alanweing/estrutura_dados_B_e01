from _input import Input
import color


class Exercise17:

    athletes = None
    number_of_jumps = None

    def __init__(self):
        self.athletes = {}
        self.number_of_jumps = 5

    def start_quiz(self):
        color._info('Entre com as informações do atleta:')
        c_input = Input()
        while c_input.get_input({Input.acceptable_input_key : None, Input.text_key : 'Nome: ', Input.type_key : Input.STRING, Input.stop_on_empty_key : True}):
            self.add_athlete(c_input._input)
            athlete_name = c_input._input
            for i in range(0, self.number_of_jumps):
                c_input.get_input({
                    Input.acceptable_input_key : None,
                    Input.text_key : 'Salto %s: ' % str(i+1),
                    Input.type_key : Input.FLOAT
                })
                self.add_jump_to_athlete(athlete_name, {i: c_input._input})

    def add_athlete(self, name):
        self.athletes.update({name: None})

    def add_jump_to_athlete(self, name, jump):
        try:
            self.athletes[name].update(jump)
        except AttributeError:
            self.athletes[name] = jump

    def print_athletes_performance(self):
        color._info('Resumo dos saltos dos atletas:')
        for athlete in self.athletes:
            average = 0
            color._print('\t=>Atleta: %s\n' % athlete, color.Color.RED, True, True)
            for jump in self.athletes[athlete]:
                color._print('==>Salto %s: %s m' % (str(jump+1), self.athletes[athlete][jump]), color.Color.GREEN)
                average += self.athletes[athlete][jump]
            color._print('\nA média dos saltos é de: %s m' % (str(average/self.number_of_jumps)), color.Color.DARKCYAN, True, True)
            print('\n')
