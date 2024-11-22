## Basic Concepts

- **Definition of Some Basic Concepts**
    - **Data** consists of information coming from observations, counts, measurements, or responses.
    - A **population** is the collection of all outcomes, responses, measurements, or counts that are of interest. Population may be finite or infinite.
    - A **sample** is a subset of a population.
    - A **parameter** is a numerical description of a population characteristics.
    - A **statistic** is a numerical description of a sample characteristic.

- **Branches of Statistics**
    - **Descriptive statistics** is the branch of statistics that involves the organization, summarization, and display of data.
    - **Inferential statistics** is the branch of statistics that involves using a sample to draw conclusions about a population.  
    - e.g. estimation and hypothesis testing.

- **Notation**  
  |                  |  Population  |   Sample   |
  |------------------|--------------|------------|
  |       Size       |      $N$     |     $n$    |
  |                  |   Parameter  |  Statistic |
  |       Mean       |     $\mu$    | ${\bar{x}}$|
  |     Variance     |   $\sigma^2$ |    $s^2$   |
  |Standard Deviation|    $\sigma$  |     $s$    |
  |    Proportion    |     $\pi$    | $\hat{\pi}$|
  |    Correlation   |    $\rho$    |     $r$    |
     

- **Types of Data (Econometrics)**
    - **Qualitative (categorical) data** consist of attributes, labels, or nonnumerical entries.  
    e.g. name of cities, gender etc.
    - **Quantitative data** consist of numerical measurements or counts.
    e.g. heights, weights, age.
        - **Discrete data** result when the number of possible values is either a finite number or a “countable” number.  
        e.g. the number of phone calls you received in any given day, age.
        - **Continuous data** result from infinitely many possible values that correspond to some continuous scale that covers a range of values without gaps, interruptions, or jumps.  
        e.g. height, weight, sales and market shares.

- **Levels of Measurement**
    - **Nominal**
        Categories only, data cannot be arranged in an ordering scheme.  
        e.g. Marital status: single, married etc.
        
    - **Ordinal**
        Categories are ordered, but differences cannot be determined or they are meaningless.  
        e.g. poor-average-good.
        
    - **Interval**        
        Differences between values are meaningful, but there is no natural starting point, ratios are meaningless.  
        e.g. we cannot say that the temperature 80℉ is twice as hot as 40℉.
        
    - **Ratio**
        Like interval level, but there is a natural zero starting point and rations are meaningful.  
        e.g. ₤20 is twice as much as ₤10.


## Descriptive Statistics

- **Central Tendency**
    - **Mean(Average)**
    : The sum of the data values divided by the number of observations.
        
        Sample mean: $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} {x_i}$ 
       
    - **Median**
    : The middle observation when the data set is sorted in ascending or descending order.  
    If the data set has an even number of observations, the median is the mean of the two middle observations.
    - **Mode**
    : The data value that occurs with the greatest frequency.  
    If no entry is repeated, the data set has no mode. If (more than) two values occur with the same greatest frequency, each value is a mode and the data set is called bimodal (multimodal).

- **Variation(Dispersion)**
    - **Range** = max. data value - min. data value
    - **Variance**
    : The variability or spread of the observations from the mean.
        
        Sample variance: $s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$
        
        Shortcut formula for sample variance: $s^2 = \frac{1}{n-1} \{\sum_{i=1}^{n} x_i^2 - n\bar{x}^2\}$
        
    - **Standard deviation($s$)**
    : The square root of the sample variance.

 - **Shapes of a Distribution**
   - **Skewness** is a measure of the asymmetry of the distribution  
     (Negatively skewed = Skewed to the left / Positively skewed = Skewed to the right)
     ![img](https://i0.wp.com/alevelmaths.co.uk/wp-content/uploads/2019/02/Skewness_1.png?w=761&ssl=1)
   - **Kurtosis** measures the degree or flatness of the distribution.
     ![img](https://www.scribbr.com/wp-content/uploads/2022/07/The-difference-between-skewness-and-kurtosis.webp)

- **Empirical Rule**   
  ![img](https://i0.wp.com/statisticsbyjim.com/wp-content/uploads/2021/08/empirical_rule_graph2.png?w=572&ssl=1)  
  For a normally distributed data,
  - 68% of the data falls within one standard deviation (1s);
  - 95% of the data falls within two standard deviations (2s);
  - 98% of the data falls within three standard deviations (3s) from the mean.
 
- **Measure of Position: z-score**
    - The z-score of an observation tells us the number of standard deviations that the observation is from the mean, that is, _how far the observation is from the mean in units of standard deviation_.
    - $z = \frac{x-\bar{x}}{s}$
    - z-score has _no unit_: we can compare values from different data sets or compare values within the same data set.
    - Mean of z-score = 0; Standard deviation = 1
    - s >0 , if z < 0, the corresponding x-value is below the mean and vice versa.

- **Percentiles & Quartiles**
    - $P_k$ (*k*th percentile) is the value of X such that *k*% or less of the observations are less than $P_k$ and (100-*k*)% or less of the observations are greater than $P_k$.
    - $Q_1$ = 25th percentile, referred to as _the first quartile_.
    - $Q_2$ = 50th percentile, _the median_, referred to as the second or middle quartile.
    - $Q_3$ = 75th percentile, referred to as _the third quartile_.
    - **Interquartile range(IQR)**
    : The difference between the first and third quartiles.
        
        $IQR = Q_3 - Q_1$
        
- **Five-number Summary & Boxplots**
    - The minimum entry
    - The first quartile Q1
    - The median (Q2)
    - The third quartile (Q3)
    - The maximum entry
      ![img](https://www.standarddeviationcalculator.io/storage/2023/Mar/lowerquartile_70.png)

- **Outliers & Extreme Values**
    - **Outliers**
    : Cases with values between 1.5 and 3 box lengths (the box length is IQR) from the upper or lower edge of the box.
    - **Extremes**
    : Cases with values more than 3 box lengths from the upper or lower edge of the box.



[Original author: Tahani Coolen-Maturi]
