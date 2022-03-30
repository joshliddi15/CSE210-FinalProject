from shared_data import SharedData

class Game():
    
    def __init__(self):
        self._data = SharedData()
    
    def start(self):
        print(f"\nStarting {self._data.CAPTION} v{self._data.get_game_version()}...\n")
        print(f"Current date is: {self._data.date_utils.get_current_date()}.\n")
        print(f"Current local time is: {self._data.date_utils.get_current_time()}.\n")
        
        
