
class State():

    Number = 0

    def __init__(self):
        self.name = "State_"+str(State.Number)
        State.Number = State.Number + 1
