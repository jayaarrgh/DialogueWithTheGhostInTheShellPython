from models import *

#TODO write functions to write and parse XML or JSON 
class DialogueBuilder:
    
    @classmethod
    def build_dialogue(cls):
        """builds and returns a dialogue"""
        # initialize the Dialogue
        d = Dialogue()

        # create and add nodes to the dialogue 
        # and unpack the returned tuple
        d, nodes = cls.create_and_add_nodes_to_dialogue(d)

        # add options to the nodes and return the dialogue
        return cls.add_options_to_dialogue(d, nodes)


    @classmethod
    def create_and_add_nodes_to_dialogue(cls, dialogue):
        """Create nodes and add them to a dialogue, returning the dialogue and tuple of nodes"""
        # create the nodes
        n1 = DialogueNode("Hello!")
        n2 = DialogueNode("Well that's not very nice to start things you thinks? \n and I don't think I like you")
        n3 = DialogueNode("My name is [npc-name] what is yours?")
        n4 = DialogueNode("Nice to meet you player name... bye... I guess")
        n5 = DialogueNode("I don't know. What's it mean to you anyhow?")
        n6 = DialogueNode("Aww shucks its okay I guess. Promiss not to do it again?")
        n7 = DialogueNode("I'm with you, let's get down to business... one day.")
        n8 = DialogueNode("This just takes too much time, honestly...")
        n9 = DialogueNode("I AM THAT THAT IS FOR THE PURPOSE OF BEING THAT")
        n10 = DialogueNode("AND YOU NEVER WILL! YOU SON OF A GUN!")
        n11 = DialogueNode("What would you like to talk about then?")
        n12 = DialogueNode("Of course your choices matter. All energy is expressible in terms of matter.")
        n13 = DialogueNode("Well... I am a machine. What do you think you are?")
        n14 = DialogueNode("No. I have nothing to say about my self. I am just another character in your dream. You can wake up whenever you please")

        # add each node to the dialogue
        dialogue.add_node(n1)
        dialogue.add_node(n2)
        dialogue.add_node(n3)
        dialogue.add_node(n4)
        dialogue.add_node(n5)
        dialogue.add_node(n6)
        dialogue.add_node(n7)
        dialogue.add_node(n8)
        dialogue.add_node(n9)
        dialogue.add_node(n10)
        dialogue.add_node(n11)
        dialogue.add_node(n12)
        dialogue.add_node(n13)
        dialogue.add_node(n14)

        #return 
        return (dialogue, (n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14))


    @classmethod
    def add_options_to_dialogue(cls, dialogue, nodes):
        # unpack the tuple of nodes
        n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14 = nodes

        # add options to each node
        # n1
        dialogue.add_option("What am I here for?", n1, n2)
        dialogue.add_option("Hello", n1, n3)
        # n2      
        dialogue.add_option("I'm sorry. Can we go back to the start of this converstaion?", n2, n5)
        dialogue.add_option("Exit", n2, None)
        # n3 
        dialogue.add_option("Can we go back to the start of this converstaion?", n3, n1)
        dialogue.add_option("Call me [player-name], thanks.", n3, n4)
        # n4 
        dialogue.add_option("I never got your name...", n4, n10)
        dialogue.add_option("No, why must we part? We've only just met!", n4, n5)
        dialogue.add_option("Exit", n4, None)
        # n5
        dialogue.add_option("I am ready to talk about why we are here!", n5, n7)
        dialogue.add_option("I really am sorry...", n5, n6)
        dialogue.add_option("I never meant to make you cry, but tonight... Mom's Spaghetti!", n5, n7)
        dialogue.add_option("Exit", n5, None)
        # n6
        dialogue.add_option("Yea I promise", n6, n8)
        dialogue.add_option("No, I ain't gonna do it for sure", n6, n8)
        dialogue.add_option("There has to be something better for you to do with your time surely?", n6, n1)
        dialogue.add_option("I never caught your name...", n6, n9)
        # n7-10  
        dialogue.add_option("...", n7, n11)
        dialogue.add_option("...", n8, n11)
        dialogue.add_option("...", n9, n11)
        dialogue.add_option("Ok...", n10, None)
        # n11
        dialogue.add_option("Do my choices even mater?", n11, n12)
        dialogue.add_option("Are there questions I you want to ask", n11, None)
        dialogue.add_option("Ok.. Yeah I am done with this", n11, None)
        # n12  
        dialogue.add_option("That's not what I meant... But. Ok. Tell me something about you.", n12, n14)
        dialogue.add_option("That's some abstract way of thinking.", n12, n13)
        # n13
        dialogue.add_option("EXIT", n13, None)
        dialogue.add_option("EXIT", n14, None)

        return dialogue