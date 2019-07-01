# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:08:36 2018

@author: RO389222
"""

import pyodbc as db
import threading
from Queue import Queue

def PopQ(q):
  while not q.empty():
    row= q.get()
    print row
    con = db.connect(Trusted_Connection='yes', driver = '{SQL Server}',server = 'D-441006464\SQLEXPRESS' , database = 'PYSQLE')
    cur=con.cursor()
    cur.execute("insert into FailureAnalysis (BuildNumber,Variant,Regional,TestCaseId,FailureDesc,Module,ConfidentFactor,StakeHolder) values('%s','%s','%s','%s','%s','%s','%s','%s')"%(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]))
    cur.commit()
    q.task_done()
    
q = Queue(maxsize=0)
a=['BF 4.1','MY_20_RC3','China', 'tst_Applink_Android_API_1.0_RPC_TC_151', 'Test', 'Applink', 'Script Issue', u'Wipro']
b=['BF 4.1','MY_20_RC3','China', 'tst_Applink_Android_API_1.0_RPC_TC_171', 'Test', 'Applink', 'Script Issue', u'Wipro']
q.put(a)
q.put(b)
threadcount=2
for i in range(threadcount):
    worker=threading.Thread(target=PopQ(q))
    worker.setDaemon(True)
    worker.start()
q.join()

