from .dialogue_option import DialogueOption

class Dialogue:
    """The Dialogue class
    
    Attributes: 
        nodes - a list of DialogueNode"""

    def __init__(self):
        self._nodes = []

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, input_nodes):
        self._nodes = input_nodes

    def add_node(self, node):
        if type(node) == None: return
        
        self._nodes.append(node)
        node._node_id = self._nodes.index(node)

    def add_option(self, text, node, dest):
        if dest not in self._nodes and dest is not None:
            self.add_node(dest)

        if node not in self._nodes:
            self.add_node(node)

        if dest is None:
            dialogue_option = DialogueOption(text, -1)
        else:
            dialogue_option = DialogueOption(text, dest.node_id)

        node.options.append(dialogue_option)

