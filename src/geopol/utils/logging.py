import logging

def setup_logging(level="INFO"):
    """
    Configure le logging pour l'application.

    Args:
        level (str): Niveau de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )