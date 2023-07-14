## PERT Beta Distribution

The three-point estimate is a simple approach to time analysis. According to the PMI methodology, it is used in the process “Estimate Activity Duration”. The method use next three different estimates:

- Optimistic estimate (OE). Minimum possible execution time.
- Pessimistic estimate (PE). Maximum possible execution time.
- Most likely estimate (MLE). Expert assessment or same case experience.

Usually, the values determined after discuss with person, who responsible for the final task.

In PERT beta distribution we mean that the MLE is more likely than other estimate. However, the longer the of the tasks, the greater the error of expert assessment.

#So, the time needed for the one task calculate next way:

T = (OE + 4*MLE + PE) / 6

In this formula used coefficient "4" before MLE. That is why the final result will be clouse to MLE, but shifted to the PE side. The shift depends on the amount of time per task. The more time needs, the shift bigger.


#So, what we need to do if we have't expert assessment or same case experience?

In this situation we use the next formula:

T = (3*OP + 2*PE) / 5

#Of course, every task has an time deviation. We can calculate this next way:

Tdeviation = (OE - PE) / 6. Its a deviation for one single iteration.

#So, if the project is a set of tasks. How to calculate project duration?

With next formula:

Pr = summ(T) + 2*sqrt(summ(Tdeviation)^2)

This formula means that the duration of the project will not exceed the calculated time with a probability of 95%
