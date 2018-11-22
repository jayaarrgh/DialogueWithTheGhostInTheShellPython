class DialogueNode:
    """The Dialogue Node class represents a list of response option and their destination nodes
    
    Attributes:
        text -- the dialogue node text to display
        options -- list of dialogue options to display
        node_id -- the exit node is -1"""
        
    def __init__(self, text):
        self._text = text
        self._options = []
        self._node_id = -1

    @property
    def node_id(self):
        return self._node_id
    
    @node_id.setter
    def node_id(self, value):
        self._node_id = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, values):
        self._options = values
        