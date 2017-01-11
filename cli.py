import os

class CLI(object):

    def get_input(self):
        return raw_input()

    def display(self, output):
        print(output)

    def clear_screen(self):
        os.system('clear')

    def display_legend(self):
        self.display("===========")
        self.display("= SQUARES =")
        self.display("===========")
        self.display("Legend: i = up, j = left, k = down, l = right")
        self.display("        s = shuffle, e = exit")
