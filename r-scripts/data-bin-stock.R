require('quantmod')
require('sqldf')
require('TTR')

setwd('.')

estock.getCodes <- function(){
  codes <- read.csv('codes.txt', sep=",", header=F, quote="")
  colnames(codes) <- c('scode', 'name', 'fcode')
  return(codes)
}

estock.getHist <- function(code){  
  f <- NULL
  tryCatch({
      f <- file(paste('data/full/', code, '.day', sep=""), 'rb')
    }, error = function(e){return}
  )
  
  if(is.null(f)){
    return(NULL)
  }
  
  m <- NULL
  rec <- readBin(f, what=integer(), size=4, n=8)
  while(length(rec) == 8){
    m <- rbind(m, rec[1:7], deparse.level=0)
    rec <- readBin(f, what=integer(), size=4, n=8)
  }
  
  m <- data.frame(m)
  colnames(m) <- c('date', 'open', 'high', 'low', 'close', 'deal', 'amount')
  
  m$date <- as.Date(as.character(m$date), format="%Y%m%d")
  m[,2:5] <- m[,2:5] / 100
  
  close(f)
  
  return(m)
}

estock.getSteady <- function(MA=60, period=30){
  codes <- estock.getCodes()
  result = NULL
  fa <- function(x){
    code <- estock.getHist(x[3])
    code.ma <- tail(SMA(code$close, MA), period)
    code.ma.sd <- sd(code.ma)
    result <- rbind(result, c(code, code.ma.sd))
  }
  result <- apply(codes, 1, fa)
  return(result)
}