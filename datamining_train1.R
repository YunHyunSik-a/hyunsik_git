crime <- read.csv("crime.csv")
View(crime)

model1 <- lm(tc2009 ~ low, data=crime)

summary(model1)

predict(model1)

resid(model1)

plot(model1)

wages <- read.csv("wages.csv")
View(wages)

hmod <-lm(earn ~ height,data=wages)
summary(hmod)

model4 <- lm(earn ~ height + sex + race + ed + age,data = wages)
summary(model4)

model5 <- lm(earn ~ height + sex +height:sex,data = wages)
coef(model5)