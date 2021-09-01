#https://pymotw.com/3/logging/
#https://www.youtube.com/watch?v=-ARI4Cz-awo
#https://youtu.be/g8nQ90Hk328 ---- better of the two videos

"""
LOG LEVELS

Level 	   Value
------     ------
CRITICAL 	50
WARNING 	30
INFO 	    20
DEBUG       10
UNSET 	    0
"""

"""
import logging

# create and configure logger
# set logging format (or--what the output will look like). 
#these format codes come from the python logging website - https://docs.python.org/3/library/logging.html
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "logging_file.txt",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    #filemode is write vs. append
                    filemode = "w")
# basicConfig sets default log level to WARNING = 30
logger = logging.getLogger()

# test the logger
logger.info("SECOND msg")

# print(logger.level)

"""

####-------------

import logging 
import datetime

today = datetime.datetime.today()

LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"

logging.basicConfig(filename = "new_logger.txt",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = "w")
                    

logger = logging.getLogger()

logger.info(" -- HERE IS AN INFO MESSAGE - {}".format(today.strftime("%A")))
logger.debug(" -- HERE IS A DEBUG MESSAGE - {}".format(datetime.datetime.today()))




