class Mononomial:

    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power

    def derivate(self):
        if self.power != 0:
            derivative = Mononomial(self.coeff * self.power, self.power - 1)
        else:
            derivative = Mononomial(0, 0)
        return derivative

    def __str__(self):
        if self.coeff == 0:
            return self.__parse_zero_coeff()
        elif self.coeff == 1:
            return self.__parse_one_coeff()
        else:
            return self.__parse_regular_coeff()

    def __lt__(self, other):
        return self.power < other.power

    def __eq__(self, other):
        return self.power == other.power

    def __gt__(self, other):
        return self.power > other.power

    def __add__(self, other):
        if self.power != other.power:
            raise ValueError("Powers dont match")
        return Mononomial(self.coeff + other.coeff, self.power)

    def __parse_zero_coeff(self):
        if self.power != 0:
                return ''
        if self.power == 0:
            return '0'

    def __parse_one_coeff(self):
        if self.power == 0:
                return '1'
        elif self.power == 1:
            return 'x'
        else:
            return 'x^{0}'.format(self.power)

    def __parse_regular_coeff(self):
        if self.power == 0:
                return str(self.coeff)
        elif self.power == 1:
            return '{0}x'.format(self.coeff)
        else:
            return '{0}*x^{1}'.format(self.coeff, self.power)

class Polynomial:

    def __init__(self, mononoms):
        self.mononoms = mononoms
        self.__sort_input()
        self.__simplify_mononoms()
        
    def __sort_input(self):
        self.mononoms.sort()
        self.mononoms = self.mononoms[::-1]

    def __simplify_mononoms(self):
        new_mon_list = list()
        for ix in range(len(self.mononoms) - 1):
            if self.mononoms[ix] == self.mononoms[ix + 1]:
                self.mononoms[ix + 1] = self.mononoms[ix] + self.mononoms[ix + 1]
            else:
                new_mon_list.append(self.mononoms[ix])
        new_mon_list.append(self.mononoms[len(self.mononoms) - 1])
        self.mononoms = new_mon_list

    def derivate(self):
        derivative = Polynomial([p.derivate() for p in self.mononoms])
        return derivative

    def __str__(self):
        result = " + ".join([str(m) for m in self.mononoms])
        if result != '':
            return result
        else:
            return '0'

class Parser:

    def __init__(self, input):
        self.mononom_strings = input.split('+')
        self.mononoms = []
        self.__add_mononoms()

    def __split_by_arguments(self, m_str):
        if 'x' in m_str:
            coeff, power = self.__parse_coeff_and_pow(m_str)
        else:
            coeff = int(m_str.strip())
            power = 0
        return [coeff, power]

    def __parse_coeff_and_pow(sefl, m_str):
        args = [arg.strip() for arg in m_str.split('x')]
        if args[1]:
            power = int((args[1].split('^'))[1])
        else:
            power = 1
        if args[0]:
            coeff = int((args[0].split('*'))[0])
        else:
            coeff = 1
        return [coeff, power]

    def __add_mononoms(self):
        for m in self.mononom_strings:
            args = self.__split_by_arguments(m)
            self.mononoms.append(Mononomial(args[0], args[1]))


def main():
    polynom_parser = Parser('x^3+x')
    polynom = Polynomial(polynom_parser.mononoms)
    print(polynom)
    print(polynom.derivate())

if __name__ == "__main__":
    main()
