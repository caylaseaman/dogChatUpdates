import pyodbc 
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=server_name;'
#                       'Database=database_name;'
#                       'Trusted_Connection=yes;')

server = 'tcp:server-dogchat3.database.windows.net'
database = 'dogchat'
username = 'dogchatadmin'
password = 'Test1234'

def get_posts():
  conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)


  cursor = conn.cursor()
  cursor.execute('SELECT Post.Handle, Post.Text, Dog.Name FROM Post INNER JOIN Dog ON Post.Handle = Dog.Handle')
  columns = [column[0] for column in cursor.description]
  results = []

  for row in cursor:
    d = dict(zip(columns,row))
    results.append(d)
    
    
  return results

def get_dogs():
  conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)


  cursor = conn.cursor()
  cursor.execute('SELECT * FROM Dog')
  columns = [column[0] for column in cursor.description]
  results = []

  for row in cursor:
    d = dict(zip(columns,row))
    results.append(d)
    print(d)
    
    
  return results
  
def get_dog_by_handle(handle):
  conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)


  cursor = conn.cursor()
  cursor.execute("SELECT * FROM Dog WHERE Handle = ?", handle)

  columns = [column[0] for column in cursor.description]
  results = []

  for row in cursor:
    d = dict(zip(columns,row))
    results.append(d)
    
  if len(results) > 0:
    return results[0]
  else:
    return None  
def get_posts_by_handle(handle):
  conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM Post WHERE Handle = ?", handle)
  columns = [column[0] for column in cursor.description]
  results = []

  for row in cursor:
    d = dict(zip(columns,row))
    results.append(d)
      
      
  return results
