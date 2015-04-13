require('RMySQL')
require('RSQLite')

get_config <- function(key){
  driver <- dbDriver("SQLite")
  con    <- dbConnect(driver, dbname = 'estock.s3db')
  rs     <- dbSendQuery(con, paste("select key, value from config where key='", key, "'", sep=""))
  val    <- fetch(rs, n = 1)
  
  dbHasCompleted(rs)
  dbClearResult(rs)
  dbDisconnect(con)
  
  return(val$value)
}

getConnection <- function(){  
  con <- dbConnect(MySQL(), 
                   host     = get_config('DB_HOST'),
                   dbname   = get_config('DB_DATABASE'), 
                   username = get_config('DB_USER'), 
                   password = get_config('DB_PASSWORD'))
}

result.newstock.save <- function(df){
  con    <- getConnection()
  dbBegin(con) 
  dbSendQuery(con,'SET NAMES utf8')
  dbWriteTable(con, 'console_newstockrate', df, append=T, row.names=NA)  
  dbCommit(con)
  dbDisconnect(con)
}
