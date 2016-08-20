from random import randint
import color


class Exercise24:

    moves = []
    number_of_moves = None
    _min = 1
    _max = 6

    def __init__(self, n_moves):
        self.number_of_moves = n_moves

    def play(self):
        for i in range(0, self.number_of_moves):
            self.moves.append(randint(self._min, self._max))

    def show_statistics(self):
        for i in range(self._min, self._max + 1):
            color._info('O lado %d foi sorteado %d vezes' % (i, self.moves.count(i)))

    def reset(self):
        self.moves[:] = []
