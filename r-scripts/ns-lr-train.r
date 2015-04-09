require(sqldf)

# Init env
setwd('D:/Source/python/estock')

# Load source script
source('./r-scripts/config.r')

# -----------------------------------------------------

# -----------------------------------------------------

# read the data from csv
csv.path <- get_config('EAST_CSV_PATH')
colClasses <- c(rep('character',6), rep('numeric', 5), rep('character', 3), rep('numeric', 5), rep('character', 1), rep('numeric', 6), rep('character', 2), rep('numeric', 10), rep('character', 1), rep('numeric', 3), rep('character', 1))
data <- read.csv(file=csv.path, header=F, sep=',', quote='', colClasses=colClasses, fileEncoding='utf-8')

data.hist <- sqldf("select * from data t where t.V16 is not null")
data.test <- sqldf("select * from data t where t.V16 is null")

# Build train set, and test set
train.index <- sample(nrow(data.hist), size=nrow(data.hist)*0.8)
train.set   <- data.hist[train.index, ]
test.set    <- data.hist[-train.index, ]

# Purge the obsoleted objects
remove(data, colClasses, csv.path, train.index)

# Use linear regression to train
train.set$V71 <- scale(train.set$V7)
train.set$V81 <- scale(train.set$V8)
myfit <- lm(V16 ~ V81 + V11 - 1, train.set)

# Test the modle
#test.set$V81 <- scale(test.set$V8)
#test.fit <- fitted(myfit, test.set$V8)

# Predict the hit value
data.test$V11     <- data.test$V35
data.test$V81     <- scale(data.test$V8)
data.test$predict <- predict(myfit, newdata=data.test)

#print(data.test[order(data.test$V20, -data.test$predict), c('V20', 'V5', 'V4', 'V11', 'V12', 'predict')])

# Save the result to db
result <- data.test[order(data.test$V20, -data.test$predict), c('V20', 'V5', 'V6', 'V4', 'V11', 'V12', 'predict')]
print(result)
result.newstock.save(result)




