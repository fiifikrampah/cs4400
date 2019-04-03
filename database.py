# This file interacts with the main database

from datetime import datetime
import pymysql
import traceback


# Establish a secure connection to the database (which will be hosted on some gatech server?)

#Global variables for use [local to this file. Do not get imported in the other python files:
_connected = False
_database = None
_cursor = None  

def set_connection(): 
	global _connected
	global _database
	global _cursor 

	if not _connected:
		try:
			print("********************************************")
            print("*          Preparing for connection          *")

            _database = pymysql.connect(host="",
                                        user="",
                                        passwd="",
                                        db="")

            print("*    Connection is secure and ready to go     *")
            _cursor = _database.cursor()
            _connected = True
            if _connected:
                print("*            Connection Setup Successfully!            *")
            else:
                print("*            Connection Setup Failed!              *")
            print("********************************************\n")

        except Exception as e:
            _connected = False
            traceback.print_exc()

def close_connection():
    global _connected

    if _connected:
        _database.close()
        _connected = False
    print("********************************************\n" +
          "*            Connection Closed            *\n" +
          "********************************************\n")