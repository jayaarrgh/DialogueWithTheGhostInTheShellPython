class DialogueOption:
    def __init__(self, text, dest=-1):
        self._text = text
        self._destination_node_id = dest
    
    @property
    def text(self):
        return self._text

    @text.setter
    def destination_node_id(self, text):
        self._text = text

    @property
    def destination_node_id(self):
        return self._destination_node_id

    @destination_node_id.setter
    def destination_node_id(self, value):
        self._destination_node_id = value
