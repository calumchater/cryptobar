class Item:
    
    # Class to help access the various properties of our google search results

    def __init__(self, data: dict):
        self.data: dict = data

    @property
    def kind(self) -> str:
        return self.data["kind"]

    @property
    def title(self) -> str:
        "This is the title of the item."
        return self.data["title"]

    @property
    def url(self) -> str:
        "This is the url of the item."
        return self.data["link"]

    @property
    def display_url(self) -> str:
        "This is the display url of the item."
        return self.data["displayLink"]

    @property
    def html_title(self) -> str:
        "This is the html title of the item."
        return self.data["htmlTitle"]
