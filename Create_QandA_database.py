import sqlite3

# Connect to the SQLite database (or create it if not exists)
conn = sqlite3.connect('QuestionsDatabase.db')
cursor = conn.cursor()

# Create tables for different categories
categories = [
    'Business Statistics',
    'Business Database mgmt Science',
    'General Biology II',
    'Mgmt organization Behavior',
    'Business Applications'
]

for category in categories:
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {category.replace(" ", "_")} (
            id INTEGER PRIMARY KEY,
            question TEXT,
            option1 TEXT, 
            option2 TEXT, 
            option3 TEXT, 
            option4 TEXT,
            answer TEXT
        )
    ''')

sample_questions = {
    'Business Statistics': [
        ('1. What statistical measure represents the average of a set of values and is commonly used in business to assess central tendency?',
          'A) Mean',
          'B) Median',
          'C) Mode', 
          'D) Range', 
          'A) Mean'),

        ('2. What is the purpose of descriptive statistics in business?',
        'A) To make predictions about future events',
        'B) To summarize and describe data',
        'C) To test hypotheses about population parameters', 
        'D) To determine cause-and-effect relationships', 
        'B) To summarize and describe data'),

        ('3. Which statistical test is appropriate for comparing the means of two independent groups?',
        'A) Chi-square test',
        'B) Paired t-test,',
        'C) Independent t-test', 
        'D) ANOVA', 
        'C) Independent t-test'),

        ('4. In a normal distribution, what percentage of data falls within one standard deviation from the mean?',
        "A) 34.13%",
        "B) 68.26%",
        "C) 95.44%", 
        "D) 99.73%", 
        "B) 68.26%"),

        ("5. What does the correlation coefficient measure?",
        "A) Strength and direction of the relationship between two variables",
        "B) Difference between the largest and smallest values in a dataset",
        "C) Frequency of occurrences of different values in a dataset",
        "D) Likelihood of an event occurring in a given time frame",
        "A) Strength and direction of the relationship between two variables"
        ),

        ('6. What statistical measure represents the average of a set of values and is commonly used in business to assess central tendency?',
       "A) To determine if there is a significant difference between two groups",
       "B) To predict the value of one variable based on the value of another variable",
       "C) To compare means across multiple groups",
        "D) To test for relationships between categorical variables", 
        "B) To predict the value of one variable based on the value of another variable"),

        ('7. What is the purpose of descriptive statistics in business?',
        "A) The probability of making a Type I error",
        "B) The probability of making a Type II error",
        "C) The probability of obtaining the observed result if the null hypothesis is true",
        "D) The probability of obtaining the observed result if the alternative hypothesis is true",
        'C) The probability of obtaining the observed result if the null hypothesis is true'),

        ('8. Which statistical test is appropriate for comparing the means of two independent groups?',
        "A) Range",
        "B) Variance",
        "C) Standard deviation",
        "D) Interquartile range", 
        "B) Variance"),

        ('9. Which type of sampling method involves dividing the population into subgroups and then randomly selecting individuals from each subgroup?',
        "A) Simple random sampling",
        "B) Stratified sampling",
        "C) Cluster sampling",
        "D) Convenience sampling",
        'B) Stratified sampling'),

        ("10.In a frequency distribution, what does the width of a class interval represent?",
        "A) The number of data points within the interval",
        "B) The range of values within the interval",
        "C) The probability of a data point falling within the interval",
        "D) The proportion of the total dataset within the interval",
        "B) The range of values within the interval")
    ],
}