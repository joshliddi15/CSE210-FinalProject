from playsound import playsound

class AudioUtils():
    
    def __init__(self) -> None:
        pass
            
    def play_sound(self, path: str):
        playsound(sound=path)