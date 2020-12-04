class Format:
	tags = frozenset(("div", "h1", "p", "span"))

    def __init__(self):
        _html_string_start = []
        _html_string_end = []
    
    def div(self, *args):

        self._html_string_start.append("<div>")
        self._html_string_end.append("</div>")

        return 



format = Format()