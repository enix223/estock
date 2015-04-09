library('RSQLite')

get_config <- function(key){
  driver <- dbDriver("SQLite")
  con    <- dbConnect(driver, dbname = 'settings.s3db')
  rs     <- dbSendQuery(con, paste("select key, value from config where key='", key, "'", sep=""))
  val    <- fetch(rs, n = 1)
  
  dbHasCompleted(rs)
  dbClearResult(rs)
  dbDisconnect(con)
  
  return(val$value)
}

result.newstock.save <- function(df){
  driver <- dbDriver("SQLite")
  con    <- dbConnect(driver, dbname = 'estock.s3db')
  dbBegin(con) 
  dbGetPreparedQuery(con, "insert into new_stock_odd_success_rate(
                     'plate'     , 
                     'stock_code', 
                     'apply_code', 
                     'stock_name', 
                     'price'     , 
                     'apply_date', 
                     'odd_success_rate') 
                     values(?,?,?,?,?,?,?)", df)
  dbCommit(con)
}