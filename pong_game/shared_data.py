from utils.date_time_utils import DateTimeUtils
from utils.fs_utils import FSUtils
from utils.audio_utils import AudioUtils
from utils.data_downloader import DataDownloader

from art import tprint
from art.art import DEFAULT_FONT

import log21
from log21 import Levels

class LogUtils():
    
    def __init__(self, log_name: str, log_level: int):
        self.fs_utils = FSUtils()
        self._logger = log21.getLogger(log_name, log_level, True, True, True)
        self._log_file = f"{self.fs_utils.get_cwd()}{self.fs_utils.get_os_sep}logs{self.fs_utils.get_os_sep}"

class SharedData():
    
    def __init__(self):
        self.data_dlr = DataDownloader()
        self.date_utils = DateTimeUtils()
        self.snd_helper = AudioUtils()
        self.fs_utils = FSUtils()
        self.CAPTION = "Pong"
        self.MAX_X = 1080
        self.MAX_Y = 720
        self.FRAME_RATE = 60
        self.CELL_SIZE = 15
        self.FONT_SIZE = 15
        self.current_cwd = self.fs_utils.get_cwd()
        self.os_sep = self.fs_utils.get_os_sep()
    
    def get_game_version(self):
        return self.data_dlr.get_version_from_url("https://treasurevalley.tech/game_ver.txt")
    
    def print_fancy(self, text: str, font: str = DEFAULT_FONT):
        tprint(text, font)
        
        
        