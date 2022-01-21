class BaseAction:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(self, type(other))

    def __hash__(self):
        return self.name.__hash__()

class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')

    def __gt__(self, other):
        return isinstance(other, ScissorsAction)


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')

    def __gt__(self, other):
        return isinstance(other, RockAction)


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')

    def __gt__(self, other):
        return isinstance(other, PaperAction)
