import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)-4.4s] [%(name)s:%(lineno)d]  %(message)s",
    handlers=[logging.StreamHandler()])
