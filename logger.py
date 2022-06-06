from loguru import logger
import json

# For later sprints, a sink could/should be this https://docs.python.org/3/glossary.html#term-file-object

def __serialize(record):
    print(record)
    subset = {"level": record["level"].name.lower(), "ts": int(record["time"].timestamp()), "msg": record["message"], **record["extra"]}
    return json.dumps(subset)

def __sink(message):
    print(__serialize(message.record))

def init_logger():
    logger.remove(0)
    logger.add(__sink)
