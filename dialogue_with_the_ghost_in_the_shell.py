from utility.getch_utility import _Getch
from services.dialogue_builder import DialogueBuilder as DB
from view.display_controller import Messenger

#TODO: Add coloring to display_controller::Messenger
class App:
    # set up the key reader (could be in the view layer)
    getch = _Getch()

    @staticmethod
    def main():
        d = DB.build_dialogue()
        Messenger.inform_user_of_exit()
        App.run_dialogue(d)

    @staticmethod
    def run_dialogue(d):
        node_id = 0
        while(node_id != -1):
            node_id = App.run_node(d.nodes[node_id])
        import view.display_controller as dc
        Messenger.clear()  
    
    @staticmethod
    def run_node(n):
        Messenger.display_node(n)
        #read input
        return App.get_input_for_next_node(n)
    
    @staticmethod
    def get_input_for_next_node(n):
        key = App.getch()

        if ord(key) == 27:
            return App.validate_escape(n)

        return App.validate_next_node_input(key, n)
        
    @staticmethod
    def validate_next_node_input(key, n):
        next_node = -1
        try:
            next_node = n.options[int(key)-1].destination_node_id
        except ValueError:
            Messenger.format_exception()
            return App.run_node(n)
        except IndexError:
            Messenger.range_exception()
            return App.run_node(n)
        except:
            print("Unexpected Error")
            return App.run_node(n)
        return next_node
    
    @staticmethod
    def validate_escape(n):
        Messenger.escape_key_hit()
        key = App.getch()
        if ord(key) == 27:
            Messenger.player_wants_to_leave()
            return -1
        Messenger.player_wants_to_stay()
        return App.run_node(n)

if __name__ == '__main__':
    App.main()