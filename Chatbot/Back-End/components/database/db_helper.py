import mysql.connector, csv

class DbHelper():
    """ This class defines a Database Helper that can:

    - create tables
    - drop tables 
    - insert records
    - delete records
    - update records
    - return tables as csv files
    """
    
    def create(table, cursor):
        """ Creates a Table in the Database
        
        Keyword Arguments:
        table       -- name of the table to be created in the database
        cursor      -- database cursor which manages the context of a fetch operation 

        Table has the form: name (col_name_1 TYPE, col_name_2 TYPE, ... col_name_n TYPE)
        """

        sql_statement = "CREATE TABLE " + table
        cursor.execute(sql_statement)

    def drop(table, cursor):
        """ Deletes a Table from the Database. 
        
        Keyword Arguments:
        table       -- name of the table to delete from the database 
        cursor      -- database cursor which manages the context of a fetch operation 

        Table has the form: name 
        DROP TABLE IF EXISTS table 
        """

        sql_statement = "DROP TABLE IF EXISTS " + table
        cursor.execute(sql_statement)

    def insert(table, record, cursor):
        """ Inserts a single record into the appropriate Table. 
        
        Keyword Arguments: 
        table  -- name of the table to insert the record into 
        record -- a tuple of data which will be inserted into the table 
        cursor -- database cursor which manages the context of a fetch operation

        Table has the form: name(col, col... col, col)
        INSERT INTO table (col_1, col_2, ... col_n) VALUES (%s_1, %s_2 ... %s_n) 
        """

        s = ""
        for i in range(0, len(record)):
            s += "%s" if i == len(record) - 1 else "%s, "

        sql_statement = "INSERT INTO " + table + " VALUES (" + s + ")"
        cursor.execute(sql_statement, record)
        print(cursor.rowcount, "Record Inserted")

    def insert_many(table, records, cursor):
        """ Inserts multiple records into the appropriate Table. 
        
        Keyword Arguments:
        table   -- name of the table to insert the record into
        records -- a list of tuples which will be inserted into the table 
        cursor  -- database cursor which manages the context of a fetch operation 

        Table has the form: name(col, col... col, col)
        INSERT INTO table (col_1, col_2, ... col_n) VALUES (%s_1, %s_2 ... %s_n) 
        """

        record = records[0]
        s = ""
        for i in range(0, len(record)):
            s += "%s" if i == len(record) - 1 else "%s, "

        sql_statement = "INSERT INTO " + table + " VALUES (" + s + ")"
        cursor.executemany(sql_statement, records)
        print(cursor.rowcount, "Record(s) Inserted")

    def delete(table, col, placeholder, cursor):
        """ Deletes a single record from the appropriate Table. 
        
        Keyword Arguments:
        table       -- name of the table to delete the record from 
        col         -- name of the column used to find row to delete
        placeholder -- represents the key that will be deleted  
        cursor      -- database cursor which manages the context of a fetch operation 

        Table has the form: name 
        Placeholder must be a tuple, list or dict
        DELETE FROM table WHERE col = placeholder 
        """

        sql_statement = "DELETE FROM " + table + " WHERE " + col + " = %s"
        cursor.execute(sql_statement, placeholder)
        print(cursor.rowcount, "Record(s) Deleted")
        
    def update(table, columns, values, condition, cursor):
        """ Updates a single record from the appropriate Table. 
        
        Keyword Arguments: 
        table     -- name of the table where the update will happen 
        columns   -- list of the column names that will be updated
        values    -- list of the new values to place inside columns 
        condition -- 
        cursor    -- database cursor which manages the context of a fetch operation 

        Table has the form: name
        Condition has the form: column_name = condition (ex/ gold = 3)
        UPDATE table SET col_1 = val_1, col_2 = val_2 ... col_n = val_n WHERE condition
        """
        
        s = ""
        i = 0
        for c in columns:
            s += c + " = " + str(values[i]) if c == columns[-1] else c + " = " + str(values[i]) + ", " 
            i += 1

        sql_statement = "UPDATE " + table + " SET " + s + " WHERE " + condition
        cursor.execute(sql_statement)
        print(cursor.rowcount, "Record(s) Updated")

    def to_csv(table, filename, cursor):
        """ Returns a Database Table as a csv file. 
        
        Keyword Arguments:
        table    -- name of the table to return 
        filename -- name of the .csv file to create 
        cursor   -- database cursor which manages the context of a fetch operation 

        Do not include '.csv' in your file name 
        """

        sql_statement = "SELECT * FROM " + table 

        cursor.execute(sql_statement)
        rows = cursor.fetchall()

        filename += ".csv"
    
        f = open(filename, "w", newline='', encoding='utf-8')
        writer = csv.writer(f)
        field_names = [i[0] for i in cursor.description]
        writer.writerow(field_names)
        writer.writerows(rows)
        f.close()