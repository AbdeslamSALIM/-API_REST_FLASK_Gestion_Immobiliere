import secrets as sc

mySQLConnection = f"mysql://{sc.DBUSER}:{sc.DBPASS}@{sc.DBHOST}/{sc.DBNAME}"
