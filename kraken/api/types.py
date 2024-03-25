class Order:
    
    # Class to help access the various properties of the order request results

    def __init__(self, data: dict):
        self.data: dict = data

    @property
    def kind(self) -> str:
        return self.data["kind"]


class Price:
    
    # Class to help access the various properties of the price request results

    def __init__(self, data: dict):
        self.data: dict = data

    @property
    def ask(self) -> str:
        return self.data["a"][0]
