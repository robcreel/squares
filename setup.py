class Setup(object):

    def __init__(self, cli):
        self.cli = cli

    def get_dimensions(self):
        self.cli.clear_screen()
        self.cli.display("===========")
        self.cli.display("= SQUARES =")
        self.cli.display("===========")
        self.cli.display("How many rows?")
        rows = int(self.cli.get_input())
        self.cli.display("How many columns?")
        cols = int(self.cli.get_input())
        return {"rows":rows, "cols":cols}
