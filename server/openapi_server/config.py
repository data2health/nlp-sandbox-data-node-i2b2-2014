import os
# from abc import abstractmethod

defaultValues = {
    "SERVER_PROTOCOL": "http://",
    "SERVER_DOMAIN": "localhost",
    "SERVER_PORT": "8080",
    "DB_PROTOCOL": "mongodb://",
    "DB_DOMAIN": "localhost",
    "DB_PORT": "27017",
    "DB_DATABASE": "nlpsandbox",
    "DB_USERNAME": "nlpmongo",
    "DB_PASSWORD": "nlpmongo"
}


class AbstractConfig(object):
    """
    Parent Class containing get_property to return the ENV variable of default
    value if not found.
    """
    def __init__(self):
        self._defaultValues = defaultValues

    def get_property(self, property_name):
        if os.getenv(property_name) is not None:
            return os.getenv(property_name)
        # we don't want KeyError?
        if property_name not in self._defaultValues.keys():
            return None  # No default value found
        # return default value
        return self._defaultValues[property_name]


class Config(AbstractConfig):
    """
    THis Class is ued to provide hard coded values to the application, first
    using environment variables and if not found,  defaulting to those values
    provided in the defaultValues dictionary above.
    """

    @property
    def server_protocol(self):
        return self.get_property('SERVER_PROTOCOL')

    @property
    def server_domain(self):
        return self.get_property('SERVER_DOMAIN')

    @property
    def server_port(self):
        return self.get_property('SERVER_PORT')

    @property
    def server_url(self):
        return "%s%s:%s" % (
            self.server_protocol, self.server_domain, self.server_port)

    @property
    def server_api_url(self):
        return "%s%s" % (self.server_url(), "/api/v1")

    @property
    def db_protocol(self):
        return self.get_property('DB_PROTOCOL')

    @property
    def db_domain(self):
        return self.get_property('DB_DOMAIN')

    @property
    def db_port(self):
        return self.get_property('DB_PORT')

    @property
    def db_database(self):
        return self.get_property('DB_DATABASE')

    @property
    def db_username(self):
        return self.get_property('DB_USERNAME')

    @property
    def db_password(self):
        return self.get_property('DB_PASSWORD')

    @property
    def db_host(self):
        return "%s%s:%s" % (
            self.db_protocol, self.db_domain, self.db_port)