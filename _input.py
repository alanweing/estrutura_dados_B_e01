from color import _print, Color, _error, _warning, _info

class Input:

    type_key = 'type'
    text_key = 'text'
    acceptable_input_key = 'acceptable'
    stop_on_empty_key = 'stop'

    INT = 'int'
    FLOAT = 'float'
    STRING = 'string'

    _input = None
    _dict = None

    def get_input(self, _dict):
        self._dict = _dict
        if self.type_key in _dict and self.text_key in _dict and self.acceptable_input_key in _dict:
            _input = input(str(_dict[self.text_key]))
            self._input = self.cast_value(self, _input, _dict[self.type_key])
            if not self.validate_value(self._input, _dict[self.acceptable_input_key]):
                if _dict[self.acceptable_input_key] is None:
                    if self.stop_on_empty_key in list(_dict) and _dict[self.stop_on_empty_key] is True:
                        return False
                    _warning('Entre com um nome!')
                else:
                    _warning('Esse valor não é válido!')
                    _info('Entre com um valor dentre os listados: \n\t%s\n' % _dict[self.acceptable_input_key].split('|'))
                self.get_input(self._dict)
            return True
        else:
            _error('ERROR in Input._input! Missing arguments')
            return False

    @staticmethod
    def cast_value(self, value, _type):
        try:
            if _type == self.INT:
                value = int(value)
            elif _type == self.FLOAT:
                value = float(value)
            elif _type == self.STRING:
                value = str(value)
        except ValueError:
            _error('Entre com um valor válido! [%s]' % _type)
            self.get_input(self._dict)
        else:
            return value

    @staticmethod
    def validate_value(value, acceptable_values):
        if acceptable_values is None:
            if value == '':
                return False
            return True
        acceptable_values = acceptable_values.split('|')
        return True if str(value) in acceptable_values else False
