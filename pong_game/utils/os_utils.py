from platform import system, version, release

class OSUtils():
    
    def __init__(self):
        print(f"You are running {system} {release} v{version}...")
    
    def get_current_os(self):
        return system
    
    def get_current_os_version(self):
        return version
    
    def get_current_os_release(self):
        return release