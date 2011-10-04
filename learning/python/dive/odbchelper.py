def buildConnectionString(params):
  """ Build a connection string from a dictionary of patrameters 
      Returs String."""
  return ";".join(["%s=%s" % (k,v) for k, v in params.items()])



if __name__ == "__main__":
  myParams = { "server" : "devsundar",
               "database" : "master",
               "uid" : "sa",
               "pwd" : "secret"
             }
  print buildConnectionString(myParams)

