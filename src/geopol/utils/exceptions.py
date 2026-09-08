class GeopolError(Exception):
    """Base class for exceptions in this module."""
    pass

class FetchError(GeopolError):
    """Exception raised for errors in the fetching process."""
    pass

class ParseError(GeopolError):
    """Exception raised for errors in the parsing process."""
    pass