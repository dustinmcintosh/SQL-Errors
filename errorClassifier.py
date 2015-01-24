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
