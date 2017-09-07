import os

confdir = os.getenv("my_config")
conffile = 'env_check.conf'
conffilename = os.path.join(confdir,conffile)
print conffilename
print confdir