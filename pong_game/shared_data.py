from utils.fs_utils import FSUtils
from utils.audio_utils import AudioUtils
from utils.data_downloader import DataDownloader
from utils.input_handler import InputHandler

from art import tprint

import log21
from log21 import Levels

class LogUtils():
    
    def __init__(self, log_name: str, log_level: int):
        self.fs_utils = FSUtils()
        self._logger = log21.getLogger(log_name, log_level, True, True, True)
        self._log_file = f"{self.fs_utils.get_cwd()}{self.fs_utils.get_os_sep}logs{self.fs_utils.get_os_sep}"

class SharedData():
    
    def __init__(self) -> None:
        self.data_dlr = DataDownloader()
        self.snd_helper = AudioUtils()
        self.fs_utils = FSUtils()
        self.input_mgr = InputHandler()
        self.game_name = "To Be Determined"
        self.current_cwd = self.fs_utils.get_cwd()
        self.os_sep = self.fs_utils.get_os_sep()
    
    def get_game_version(self):
        self.game_version = self.data_dlr.get_version_from_url("https://treasurevalley.tech/game_ver.txt")
    
    def print_fancy(self, text: str, font: str = None):
        tprint(text, font)
        
        
        