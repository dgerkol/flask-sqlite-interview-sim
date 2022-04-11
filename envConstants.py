#Directory and default DB file name
DB_FILE = 'db_files/init_db'
#Directory of all components logs
LOGS_DIR = 'site logs'
#Logs of site.py and flask app run
SITE_LOG = f'{LOGS_DIR}/flask_app.log'
#Rest server logs - for all http requests received, and operation status responded
REST_LOG = f'{LOGS_DIR}/rest_server.log'
#All logs of db queries requested by rest server to be performed by DBclient and thier result
DB_QUERY_LOG = f'{LOGS_DIR}/db_query.log'
#All logs of DBclient working directly with DB file - handle DB errors and return conn & cursor
DB_CLIENT_LOG = f'{LOGS_DIR}/db_client.log'