import ConfigParser

config = ConfigParser.ConfigParser()
config.read('/home/meenu/ws/hg/learn/python/readini/config.ini')

print "Section read from ini file:" + config.get('isection', 'testparam')




