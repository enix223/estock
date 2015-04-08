library(quantmod)
library(RMySQL)
library(TTR)

connect <- function(){
  con = dbConnect(RMySQL::MySQL(), dbname='estock', host='192.168.1.11', username='estock', password='12qwaszx');
  return(con);
}

query_all <- function(sql){
  con = connect();
  rs <- dbSendQuery(con, sql);
  result <- dbFetch(rs, n=-1);
  dbHasCompleted(rs);
  dbClearResult(rs);
  dbDisconnect(con);
  return(result);
}

get_latest_ma <- function(stock){
  # Get the data for a stock
  rs <- query_all(paste("SELECT * FROM estock_hist_sh WHERE code='", stock, "' order by date desc limit 120", sep="");
  
  # calc moving avg
  rs.sma5  <- SMA(rev(rs[,'close']), n=5)[61:120]
  rs.sma10 <- SMA(rev(rs[,'close']))[61:120]
  rs.sma20 <- SMA(rev(rs[,'close']), n=20)[61:120]
  rs.sma60 <- SMA(rev(rs[,'close']), n=60)[61:120]
  
  # order the data by date asc
  rs.origin <- rs[1:60,]
  rs.origin <- rs.origin[with(rs.origin, order(date)),]
  
  # Add MA 5/10/20/60 to data.frame
  rs.origin$ma5 = rs.sma5
  rs.origin$ma10 = rs.sma10
  rs.origin$ma20 = rs.sma20
  rs.origin$ma60 = rs.sma60

  #up <- rs.origin[rs.origin$ma5 > rs.origin$ma10 & rs.origin$ma10 > rs.origin$ma20 & rs.origin$ma20 > rs.origin$ma60,]
  return(rs)
}

check_qualified <- function(stock){
  rs = get_latest_ma(stock)  
  
}

process_main <- function(){
  stock_list = query_all('select code from estock_stock_tbl')
  
}





