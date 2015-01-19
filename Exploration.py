# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib

font = {'family' : 'normal',
        'size'   : 24}

matplotlib.rc('font', **font)

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 8)

%matplotlib inline

data = pd.read_csv('error_message_data_v2.csv')

# <codecell>

data

# <codecell>

data.shape

# <codecell>

#user id has made how many queries
print data['executed_by_id'].value_counts()
#number of users that have made this number of queries
print data['executed_by_id'].value_counts().value_counts()
#print max(data['executed_by_id'].value_counts().value_counts())

# <codecell>

#user id has made how many queries
print data['executed_by_id'].value_counts()[:10]
print float(sum(data['executed_by_id'].value_counts()[:10]))/sum(data['executed_by_id'].value_counts())

# <codecell>

# A few users have made the plurality of errors (e.g., user 3992 above has made almost 6% of errors)
float(30948)/data.shape[0]

# <codecell>

fig = plt.figure(figsize = (8, 5))
ax = fig.add_subplot(1, 1, 1)

ax.plot(range(1,len(np.divide(data['executed_by_id'].value_counts().values.astype(float), 
          np.sum(data['executed_by_id'].value_counts().values)))+1), 
            np.divide(data['executed_by_id'].value_counts().values.astype(float), 
          np.sum(data['executed_by_id'].value_counts().values)), 'or')
ax.set_xscale('log')
plt.xlabel('user')
plt.ylabel('Frac. of queries by user')
plt.xlim([.5, 200])
plt.ylim([0, .1])

# <codecell>

fig = plt.figure(figsize = (8, 5))
ax = fig.add_subplot(1,1,1)

ax.plot(data['executed_by_id'].value_counts().value_counts().index, 
            np.divide(data['executed_by_id'].value_counts().value_counts().values.astype(float), 
          np.sum(data['executed_by_id'].value_counts().value_counts().values)), 'bo')
ax.set_xscale('log')
plt.xlabel('Num. queries from a user before quit')
plt.ylabel('Frac of user-base')
plt.xlim([.5, 200])
plt.ylim([0, .4])

# <codecell>

data.shape

# <codecell>

data.columns

# <codecell>

#how many of which type of errors (other than NaN)
data['error_message'].value_counts()/data.shape[0]

# <codecell>

#df = random subset of 1000 of the errors
#import random
#rows = random.sample(data.index, 1000)
#df = data.ix[rows]
#df

# <codecell>

#here I put the times into python's datetime

import datetime as dt

def get_time(Modedt):
    try:
        year = Modedt[:4]
        month = Modedt[5:7]
        day  = Modedt[8:10]
        hour  = Modedt[11:13]
        minute  = Modedt[14:16]
        sec  = Modedt[17:19]
        micsec  = Modedt[20:23]
        return dt.datetime(int(year), int(month), int(day), int(hour), int(minute), int(sec), int(micsec)*1000)
    except TypeError:
        #print Modedt
        return float('nan')
    
print get_time(df['created_at'].iloc[0])

#sometimes Completed_at = nan 
data['createdT'] = data['created_at'].apply(get_time)
data['completedT'] = data['completed_at'].apply(get_time)
data['deltaTime'] = (data['completedT']-data['createdT'])

# <codecell>

#df['deltaTime'] = df['deltaTime'].apply(dt.timedelta.total_seconds)

# <codecell>

#time from query run to query returned ~2s
np.median(data['deltaTime'])

# <codecell>

#Identify nature of the errors

import math
def identErr(errString):
    if type(errString) is str:
        if "syntax" in errString.lower():
            return "Syntax"
        else:
            return "String Other"
    elif type(errString) is float:
        if math.isnan(errString):
            return None
        else:
            return "Float Other"
        

# <codecell>

#Identify nature of the errors


import math
def identErr2(errString):
    if type(errString) is str:
        if False:
            pass
        #column issues
        elif "unknown column" in errString.lower():
            return "unknown column"
        elif "column" in errString.lower() and "does not exist" in errString.lower():
            return "unknown column"
        elif "invalidcolumnreference" in errString.lower():
            return "unknown column"
        elif "invalid column name" in errString.lower():
            return "unknown column"
        elif "no column name was specified" in errString.lower():
            return "unknown column"
        elif "invalid object" in errString.lower():
            return "unknown column"
        elif "no column name was specified" in errString.lower():
            return "unknown column"
        
        #table or schema issues
        elif "table" in errString.lower() and "does not exist" in errString.lower():
            return "unknown table or schema"
        elif "relation" in errString.lower() and "does not exist" in errString.lower():
            return "unknown table or schema"
        elif "schema" in errString.lower() and "does not exist" in errString.lower():
            return "unknown table or schema"
        elif "couldn't find a data source with name" in errString.lower() or "unknown table" in errString.lower() or "no tables used" in errString.lower():
            return "unknown table or schema"
        elif "table" in errString.lower() and "doesn't exist" in errString.lower():
            return "unknown table or schema"
        elif "Couldn't find a data source with name" in errString.lower():
            return "unknown table or schema"
        elif "missing from-clause entry for table" in errString.lower() or "every derived table must have its own alias" in errString.lower():
            return "unkown table alias"
        elif "subquery" in errString.lower() and "must have an alias" in errString.lower():
            return "subquery missing alias"
        elif "reference" in errString.lower() and "from-clause" in errString.lower():
            return "invalid reference to from-clause entry"
        elif "table" in errString.lower() and "specified more than once" in errString.lower():
            return "table name specified more than once"
        
        elif "transition state" in errString.lower():
            return "transition state error"
        
        elif "no tables specified" in errString.lower():
            return "no table specified"
        
        
        
        
        #Internal Errors
        elif "broken pipe" in errString.lower():
            return "Internal Error"
        elif "execution expired" in errString.lower():
            return "Internal Error"
        elif "out of memory" in errString.lower():
            return "Internal Error"
        elif "cache lookup failed" in errString.lower():
            return "Internal Error"
        elif "can't connect to mysql server" in errString.lower():
            return "Internal Error"
        elif "no connection to the server" in errString.lower():
            return "Internal Error"
        elif "no space left on device" in errString.lower():
            return "Internal Error"
        elif "no pg_hba.conf entry" in errString.lower():
            return "Internal Error"
        elif "password authentication failed" in errString.lower():
            return "Internal Error"
        elif "java heap space" in errString.lower():
            return "Internal Error"
        elif "pg::internalerror" in errString.lower():
            return "Internal Error"
        elif "timer already cancelled" in errString.lower():
            return "Internal Error"
        elif "we encountered an internal error" in errString.lower():
            return "Internal Error"
        elif "An I/O error occured while sending" in errString:
            return "Internal Error"
        elif "connection attempt failed" in errString.lower():
            return "Internal Error"
        elif 'communications link failure' in errString.lower():
            return 'communications link failure'
        
        #no results to display
        elif "no results were returned by the query" in errString.lower():
            return "No results"
        elif "null" in errString.lower():
            return "No results"
        
        elif "unknown error" in errString.lower():
            return "unknown error occurred"
        
        #function does not exist
        elif "function" in errString.lower() and "does not exist" in errString.lower():
            return "function or method does not exist"
        elif "undefined" in errString.lower() and "function" in errString.lower():
            return "function or method does not exist"
        elif "undefined" in errString.lower() and "method" in errString.lower():
            return "function or method does not exist"
        
        elif "operator" in errString.lower() and "does not exist" in errString.lower():
            return "operator does not exist"
        
        elif "is ambiguous" in errString.lower():
            return "column name is ambiguous"
        
        elif "operator" in errString.lower() and "is not unique" in errString.lower():
            return "operator is not unique"
        
        elif "type" in errString.lower() and "does not exist" in errString.lower():
            return "type does not exist"
        
        #Syntax errors
        elif "syntax error at or near" in errString.lower() or "error in your sql syntax" in errString.lower() or "incorrect syntax near" in errString.lower():
            if "select" in errString.lower():
                return 'SELECT syntax'
            elif "from" in errString.lower():
                return 'FROM syntax'
            elif "where" in errString.lower():
                return 'WHERE syntax'
            elif "group" in errString.lower():
                return 'GROUP syntax'
            elif "having" in errString.lower():
                return 'HAVING syntax'
            elif "order" in errString.lower():
                return 'ORDER syntax'        
            elif 'limit' in errString.lower():
                return 'LIMIT syntax'
            else:
                return "misc syntax error"
        elif "syntax error at end of input" in errString.lower():
            return "syntax error at end of input"
        
        #data of invalid type
        elif "invalid input syntax for" in errString.lower():
            return "data of invalid type"
        elif "argument of" in errString.lower() and "must be type" in errString.lower():
            return "data of invalid type"
        elif "argument of" in errString.lower() and "must be type" in errString.lower():
            return "data of invalid type"
        elif "argument of" in errString.lower() and "must be type" in errString.lower():
            return "data of invalid type"
        elif "argument of" in errString.lower() and "must be type" in errString.lower():
            return "data of invalid type"
        elif "argument of" in errString.lower() and "must be type" in errString.lower():
            return "data of invalid type"
        elif "argument of" in errString.lower() and "must be type" in errString.lower():
            return "data of invalid type"
        elif "cannot cast type" in errString.lower():
            return "data of invalid type"
        elif "date/time" in errString.lower() and "out of range" in errString.lower():
            return "date/time out of range"
        elif "no named parameter matches" in errString.lower() and "and no positional param" in errString.lower():
            return "no named parameter matches"
        
        #divide by zero
        elif "divi" in errString.lower() and "by zero" in errString.lower():
            return "cannot divide by zero"
        
        #Java error?
        elif "java.lang.NullPointerException" in errString:
            return "java.lang.NullPointerException"
        
        #?
        elif "cannot insert multiple commands into a prepared statement" in errString.lower():
            return "cannot insert multiple commands into a prepared statement"
        
        elif "unterminated quot" in errString.lower():
            return "unterminated quotation"
        
        elif "not allowed in group by" in errString.lower():
            return "not allowed in group by"
        elif "not allowed in where" in errString.lower():
            return "not allowed in where"
        elif "must appear in the group by clause" in errString.lower():
            return "must appear in group by"
        elif "isn_t in group by" in errString.lower():
            return "must appear in group by"
        elif "aggregate" in errString.lower() and "nested" in errString.lower():
            return "aggregate functions may not be nested"
        elif "window function" in errString.lower():
            return "error in window function"
        elif "order by" in errString.lower() and "not in select list" in errString.lower():
            return "order by refers to a column not in select statement"
        elif "group by" and "not in select list" in errString.lower():
            return "group by refers to a column not in select statement"
        elif "not supported on redshift tables" in errString.lower():
            return "not supported by redshift"
        elif "cross-database references are not implemented" in errString.lower():
            return "cross-database references not implemented"
        
        elif "permission denied" in errString.lower() or "permission was denied" in errString.lower():
            return "permission denied"
        elif "command denied to user" in errString.lower() and "for table" in errString.lower():
            return "permission denied"
        elif "cannot execute" in errString.lower() and "in a read-only" in errString.lower():
            return "permission denied"
        elif "read-only transaction" in errString.lower():
            return "permission denied"
        elif "PROTECTED" == errString:
            return "permission denied"
        
        elif "subquery has too many columns" in errString.lower():
            return "subquery has too many columns"
        
        elif "each UNION query must have the same number of columns" in errString:
            return "each UNION query must have the same number of columns"
    
        #time out
        elif "timeout" in errString.lower():
            return "timeout"
        elif "timed out" in errString.lower():
            return "timeout"
        elif "lost connection" in errString.lower():
            return "timeout"
        
        #execution canceled
        elif "canceling statement due to user request" in errString.lower():
            return "execution canceled/interupted"
        elif "cancelled on user's request" in errString.lower():
            return "execution canceled/interupted"
        elif "query execution was interrupted" in errString.lower():
            return "execution canceled/interupted"
        elif "cancelled due to client request" in errString.lower():
            return "execution canceled/interupted"
        
        elif 'no serializer found' in errString.lower():
            return 'no serializer found'
        elif 'connection refused' in errString.lower():
            return 'bad connection'
        elif 'could not establish connection' in errString.lower():
            return 'bad connection'
        elif 'connection' in errString.lower() and "closed" in errString.lower() :
            return 'connection closed'
        elif 'cancelled on user_s request' in errString.lower():
            return 'query cancelled by user'
        elif 'exception parsing for named parameter replacement' in errString.lower():
            return 'exception parsing for named parameter replacement'
        
        elif "AnalysisException" in errString:
            return "Misc Analysis Exception"
        
        elif "non-integer constant in" in errString.lower():
            return "non-integer constant in order or group by"
        
        elif "for SELECT DISTINCT, ORDER BY expressions must appear in select list" in errString:
            return "SELECT DISTINCT, ORDER BY expressions must appear in select list"
        
 #       elif 'select' in errString.lower():
 #           return 'SELECT'
 #       elif 'from' in errString.lower():
 #           return 'FROM'
 #       elif 'where' in errString.lower():
 #           return 'WHERE'
 #       elif 'group' in errString.lower():
 #           return 'GROUP'
 #       elif 'having' in errString.lower():
 #           return 'HAVING'
 #       elif 'order' in errString.lower():
 #           return 'ORDER'        
 #       elif 'limit' in errString.lower():
 #           return 'LIMIT'

        else:
            return "rare errors"
        

    elif type(errString) is float:
        if math.isnan(errString):
            return "no error"
        else:
            return "Float Other"
        
print identErr2("asdfzklnjdknfsyntaxasdf x")
print identErr2(float('nan'))

# <codecell>

#barplot of errors in full data set
data['Error Class'] = data['error_message'].dropna().apply(identErr2)
fig = plt.figure(figsize = (8, 5))

font = {'family' : 'normal',
        'size'   : 18}
matplotlib.rc('font', **font)

data['Error Class'].value_counts().plot(kind='bar', figsize=(20, 8),)

# <codecell>


ErrLeft = data.dropna()[data['Error Class'] == 'misc syntax error']
print ErrLeft.shape

# <codecell>

#generate list of errors
errlist = ErrLeft['error_message'].tolist()
#alphabetically sort them below
#sorted(errlist, key=str.lower)

# <codecell>

#print a single error and its raw source for examination
index = 16
print ErrLeft['error_message'].iloc[index]
print " "
print ErrLeft['raw_source'].iloc[index]

# <codecell>

def isNovice(SQLcommand):
    if type(SQLcommand) is str and "tutorial" in SQLcommand:
        return True
    else: 
        return False

#applied to each query as all users can be novices atsome point (e.g., interact with tutorials)
data['isNovice'] = data['raw_source'].apply(isNovice)

expertUsers = data['executed_by_id'].value_counts()[data['executed_by_id'].value_counts()>2000].index.tolist()

def isExpert(user):
    if user in expertUsers:
        return True
    else:
        return False


data['isExpert'] = data['executed_by_id'].apply(isExpert)
expertData = data[data['isExpert']==True]
noviceData = data[data['isNovice']==True]
expertData['Error Class'] = expertData['error_message'].dropna().apply(identErr2)
noviceData['Error Class'] = noviceData['error_message'].dropna().apply(identErr2)

# <codecell>

data.dropna()['isNovice'].value_counts().plot(kind='bar')

# <codecell>

fig = plt.figure(figsize = (8, 5))
font = {'family' : 'normal',
        'size'   : 18}

matplotlib.rc('font', **font)
expertData['Error Class'].value_counts().plot(kind='bar', figsize=(20, 8),)

# <codecell>

fig = plt.figure(figsize = (8, 5))
font = {'family' : 'normal',
        'size'   : 18}

matplotlib.rc('font', **font)
noviceData['Error Class'].dropna().value_counts().plot(kind='bar', figsize=(20, 8),)

# <codecell>

#Fraction of queries that are errors

print float(sum(expertData['Error Class'].value_counts()))/len(expertData)
print float(sum(noviceData['Error Class'].value_counts()))/len(noviceData)
print float(sum(expertData['Error Class'].value_counts())-expertData['Error Class'].value_counts()[0])/len(expertData)

# <codecell>

float(sum(expertData['Error Class'].value_counts())-expertData['Error Class'].value_counts()[0])/len(expertData)

# <codecell>

expertUsers

# <codecell>

timeOutData = data[data['Error Class']=='timeout']

# <codecell>

def getYearMonth(timestamp):
    return dt.date(timestamp.year, timestamp.month, 1)

timeOutData['YearMonth'] = timeOutData['createdT'].apply(getYearMonth)


timeOutData['YearMonth'].value_counts().plot(kind="bar")


# <codecell>

data['YearMonth'] = data['createdT'].apply(getYearMonth)

data['YearMonth'].value_counts().plot(kind="bar")

# <codecell>


