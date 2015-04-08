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
