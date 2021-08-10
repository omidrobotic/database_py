#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h>
#include <string.h>

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif
class sqlInit{
public:
    sqlite3 *db;
    char *zErrMsg = 0;
    char *sql = 0;
    char *location=0;

};
sqlInit configDataBase;
sqlInit refreeDataBase;
sqlInit robotsDataBase;
const char* data = "Callback function called";
class setData {
public:
    std::string name;
    float value;
};
setData seter;
static int callback(void *data, int argc, char **argv, char **azColName){
    int i;
    //fprintf(stderr, "%s: ", (const char*)data);

    for(i = 0; i<argc; i++){
        //printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
    }
    seter.name=azColName[0];
    seter.value=atof(argv[0]);
    //printf("\n");
    return 0;
}
int dataBase(char *command,sqlInit *sqlData)
{

    /* Execute SQL statement */
    int rc = sqlite3_exec(sqlData->db, command, callback, (void*)data, &sqlData->zErrMsg);
    if( rc != SQLITE_OK ) {
        fprintf(stderr, "SQL error: %s\n", sqlData->zErrMsg);
        sqlite3_free(sqlData->zErrMsg);
        return false;
    } else {
        fprintf(stdout, "Operation done successfully\n");
        return true;
    }
    return false;
}
int removeDataInDataBase(int ID,char* table,sqlInit *sqlData)
{
    char *command;
    sprintf(command,"DELETE from %s where ID=%d;",table,ID);
    return dataBase(command,sqlData);

}
int insertDataInDataBase(char* table,int ID,char* name,float value,sqlInit *sqlData)
{
    char *command;
    sprintf(command,"INSERT INTO %s VALUES(%d, '%s', %f );",table,ID,name,value);
    return dataBase(command,sqlData);
}
int updateDataBase(char* table,char *name,float value,sqlInit *sqlData)
{
    char *command;
    sprintf(command,"UPDATE %s set EQUL = %f where NAME='%s'; ",table,value,name);
    return dataBase(command,sqlData);
}
int findDataBase(char *table,char *name,sqlInit *sqlData)
{
    char *command;
    sprintf(command,"SELECT EQUL FROM %s WHERE NAME='%s';",table,name);
    return dataBase(command,sqlData);
}
int openDataBase(sqlInit *sqlData)
{
    int rc;

    rc = sqlite3_open(sqlData->location, &sqlData->db);
    if( rc ) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(sqlData->db));
    } else {
        fprintf(stderr, "Opened database successfully\n");
    }
    /* Execute SQL statement */
    rc = sqlite3_exec(sqlData->db, sqlData->sql, callback, 0, &sqlData->zErrMsg);

    if( rc != SQLITE_OK ){
        fprintf(stderr, "SQL error: %s\n", sqlData->zErrMsg);
        sqlite3_free(sqlData->zErrMsg);
        return false;
    } else {
        fprintf(stdout, "Table created successfully\n");
        return true;
    }
    return false;
}
void closeDataBase(sqlInit *sqlData)
{
    sqlite3_close(sqlData->db);
}
void configConfigDatabase(sqlInit *sqlData)
{
    sqlData->sql=
            "CREATE TABLE omid("  \
      "ID INT PRIMARY KEY     NOT NULL," \
      "NAME           TEXT    NOT NULL," \
      "EQUL            REAL     NOT NULL);";
    sqlData->location="/home/mhz/database/config.db";
}
void configRobotsDatabase(sqlInit *sqlData)
{
    sqlData->sql=
            "CREATE TABLE omid("  \
      "ID INT PRIMARY KEY     NOT NULL," \
      "NAME           TEXT    NOT NULL," \
      "EQUL            REAL     NOT NULL);";
    sqlData->location="/home/mhz/database/robots.db";
}
void configRefreeDatabase(sqlInit *sqlData)
{
    sqlData->sql=
            "CREATE TABLE omid("  \
      "ID INT PRIMARY KEY     NOT NULL," \
      "NAME           TEXT    NOT NULL," \
      "EQUL            REAL     NOT NULL);";
    sqlData->location="/home/mhz/database/refree.db";
}


int main() {
    configConfigDatabase(&configDataBase);
    openDataBase(&configDataBase);

    /*
       sql = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) "  \
            "VALUES (1, 'Paul', 32, 'California', 20000.00 ); " \
            "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) "  \
            "VALUES (2, 'Allen', 25, 'Texas', 15000.00 ); "     \
            "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)" \
            "VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );" \
            "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)" \
            "VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );";

       *//* Execute SQL statement *//*
    rc = sqlite3_exec(db, sql, callback, 0, &zErrMsg);

    if( rc != SQLITE_OK ){
        fprintf(stderr, "SQL error: %s\n", zErrMsg);
        sqlite3_free(zErrMsg);
    } else {
        fprintf(stdout, "Records created successfully\n");
    }*/



std::  cout << "";

 //   removeDataInDataBase(3,"COMPANY");
    /* Create SQL statement */
    char *sql;
   sql = "SELECT * from omid";
    //std::  cout << "aaaaaaaaaa  "<<sqlSetData.zErrMsg;
    //insertDataInDataBase("omid",2,"ufo",2.5,&configDataBase);
    //updateDataBase("omid","omid",3,&configDataBase);
    while (1) {
        findDataBase("omid", "ufo", &configDataBase);
        if(seter.value==1)
        {
            break;
        }
    }
    updateDataBase("omid","omid",1,&configDataBase);
    /* Execute SQL statement */
    dataBase(sql,&configDataBase);
    closeDataBase(&configDataBase);

    return 0;
}


