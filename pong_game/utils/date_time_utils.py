from datetime import datetime
import pytz
class DateTimeUtils():
    
    def __init__(self, tz: str = 'America/Denver'):
        local_tz = pytz.timezone(tz)
        self.dt_now = datetime.now(local_tz)
        self.local_datetime = local_tz.localize(datetime.now())
        
    def get_current_date(self, format: str = '%B %d, %Y'):
        """
        Gets the current date as a string.
        """
        return self.local_datetime.strftime(format)
    
    def get_current_time(self, format: str = '%H:%M:%S'):
        """
        Gets the current time as a string.
        """
        return self.local_datetime.strftime(format)
    
    
        
    
    