# mian file

#imports
from fileinput import filename
import logging as lg
import datetime




def initiate_logging():
    lg.basicConfig(filename="logs/daily_logs.log",level=lg.DEBUG,format ='%(asctime)s %(levelname)s %(message)s')
    now= datetime.datetime.now()
    lg.info("Application Started at %s ",now.strftime("%Y -%m -%d %H:%M:%S"))

#initialze logging
initiate_logging()
import frame