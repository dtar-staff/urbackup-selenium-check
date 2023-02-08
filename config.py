DOMAIN = "http(s)://your-server-domain-or.ip" # Where is the web UI of UrBackup located
PASSWORD="Y0uR_5up3r%53Cur3+p455w0rDD" # UrBackup authentication password
LOGIN_URL=DOMAIN + "/"			# I think URLs aren't required since UrBackup web UI is a javascript SPA, but who knows, what could change
MAIN_PAGE_URL = DOMAIN + "/"
FNAME = 'UrBackup - Keeps your data safe.csv' # Change it if doesn't work, for example, developers can change export file name
PATH = '/home/youruser/Downloads' # Default Downloads folder for your webdriver
