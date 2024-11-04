from database.DAO import DAO


aereoporti =DAO.getRotte()
for a in aereoporti:
    print(a)