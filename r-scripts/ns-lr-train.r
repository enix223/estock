setwd('D:/Source/python/estock')

source('./r-scripts/config.r')

csv.path <- get_config('EAST_CSV_PATH')
print(csv.path)
data <- read.csv(file=csv.path, header=F, sep=',', quote='', colClasses=c(rep('character', 43)), fileEncoding='utf-8')

