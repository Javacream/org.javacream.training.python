import logging
file = logging.FileHandler('./scratch.log')
console = logging.StreamHandler()#Standard: Streaming auf die Konsole
file.setLevel(logging.DEBUG)
console.setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG, handlers=[file, console])

logging.debug("a simple debug message")
logging.warning("a simple warning message")