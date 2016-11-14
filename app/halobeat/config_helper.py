from datetime import date
import os


class ConfigHelper(object):
    """Manage all configuration information for the application"""
    def __init__(self, halobeat_version=0):
        self.halo_key = os.getenv("HALO_API_KEY")
        self.halo_secret = os.getenv("HALO_API_SECRET_KEY")
        self.start_timestamp = ConfigHelper.get_timestamp()
        self.ua_string = "Halo-Filebeat/%s" % halobeat_version
        self.max_threads = 10
        self.halo_batch_size = 20

    @classmethod
    def get_timestamp(cls):
        env_time = os.getenv("HALO_EVENTS_START", "")
        if env_time == "":
            env_time = ConfigHelper.iso8601_today()
        return env_time

    @classmethod
    def iso8601_today(cls):
        today = date.today()
        retval = today.isoformat()
        return retval
