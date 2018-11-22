from models import *

#TODO write two functions to write and parse XML or JSON 
class DialogueBuilder:
    
    @staticmethod
    def build_dialogue():
        d = Dialogue()
        
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

        d.add_node(n1)
        d.add_node(n2)
        d.add_node(n3)
        d.add_node(n4)
        d.add_node(n5)
        d.add_node(n6)
        d.add_node(n7)
        d.add_node(n8)
        d.add_node(n9)
        d.add_node(n10)
        d.add_node(n11)
        d.add_node(n12)
        d.add_node(n13)
        d.add_node(n14)

        #node1
        d.add_option("What am I here for?", n1, n2)
        d.add_option("Hello", n1, n3)
        #node2      
        d.add_option("I'm sorry. Can we go back to the start of this converstaion?", n2, n5)
        d.add_option("Exit", n2, None)
        #node3 
        d.add_option("Can we go back to the start of this converstaion?", n3, n1)
        d.add_option("Call me [player-name], thanks.", n3, n4)
        #node4 
        d.add_option("I never got your name...", n4, n10)
        d.add_option("No, why must we part? We've only just met!", n4, n5)
        d.add_option("Exit", n4, None)
        #n5
        d.add_option("I am ready to talk about why we are here!", n5, n7)
        d.add_option("I really am sorry...", n5, n6)
        d.add_option("I never meant to make you cry, but tonight... Mom's Spaghetti!", n5, n7)
        d.add_option("Exit", n5, None)
        #n6
        d.add_option("Yea I promise", n6, n8)
        d.add_option("No, I ain't gonna do it for sure", n6, n8)
        d.add_option("There has to be something better for you to do with your time surely?", n6, n1)
        d.add_option("I never caught your name...", n6, n9)
        #n7-10  
        d.add_option("...", n7, n11)
        d.add_option("...", n8, n11)
        d.add_option("...", n9, n11)
        d.add_option("Ok...", n10, None)
        #n11
        d.add_option("Do my choices even mater?", n11, n12)
        d.add_option("Are there questions I you want to ask", n11, None)
        d.add_option("Ok.. Yeah I am done with this", n11, None)
        #n12  
        d.add_option("That's not what I meant... But. Ok. Tell me something about you.", n12, n14)
        d.add_option("That's some abstract way of thinking.", n12, n13)
        #n13
        d.add_option("EXIT", n13, None)
        d.add_option("EXIT", n14, None)

        return d
