# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 17:23:38 2015

@author: dustin
"""

string = """WHEN error ilike '%not allowed in group by%' THEN 'not allowed in group by'
WHEN error ilike '%not allowed in where%' THEN 'not allowed in where'
WHEN error ilike '%must appear in the group by clause%' THEN 'must appear in group by'
WHEN error ilike '%isn_t in group by%' THEN 'must appear in group by'
WHEN error ilike '%aggregate%nested%' THEN 'aggregate functions may not be nested'
WHEN error ilike '%window function%' THEN 'error in window function'

WHEN error ilike '%order by%not in select list%' THEN 'order by refers to a column not in select statement'
WHEN error ilike '%group by%not in select list%' THEN 'group by refers to a column not in select statement'

WHEN error ilike '%not supported on redshift tables%' THEN 'not supported by redshift'
WHEN error ilike '%cross-database references are not implemented%' THEN 'cross-database references not implemented'

WHEN error ilike '%permission denied%' THEN 'permission denied'
WHEN error ilike '%command denied to user%for table%' THEN 'permission denied'
WHEN error ilike '%cannot execute%in a read-only%' THEN 'no database write permissions'

WHEN error ilike '%timeout%' THEN 'timeout'
WHEN error ilike '%timed out%' THEN 'timeout'
WHEN error ilike '%lost connection%' THEN 'timeout'
WHEN error ilike '%no serializer found%' THEN 'no serializer found'
WHEN error ilike '%connection refused%' THEN 'bad connection'
WHEN error ilike '%could not establish connection%' THEN 'bad connection'
WHEN error ilike '%connection%closed%' THEN 'connection closed'
WHEN error ilike '%cancelled on user_s request%' THEN 'query cancelled by user'

WHEN error ilike '%type%does not exist%' THEN 'LOOK INTO THESE'
WHEN error ilike '%exception parsing for named parameter replacement%' THEN 'exception parsing for named parameter replacement'"""

string = string.split('\n')

for i in string:
    parts = i.split("' THEN '")
    if parts !=[] and parts!=['']:
        #print parts
        print 'elif "'+parts[0][19:-1]+ '" in errString.lower():'
        print '    return "'+parts[1][:-1]+'"'