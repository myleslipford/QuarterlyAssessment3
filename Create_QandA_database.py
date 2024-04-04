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
    'Business Database mgmt Science': [
     ('1. What does the acronym SQL stand for?',
      'A) Structured Query Language',
      'B) Sequential Query Language',
      'C) Simplified Query Language', 
      'D) Systematic Query Language', 
      'A) Structured Query Language'),

    ('2. Which of the following is not a SQL data type?',
    'A) INTEGER',
    'B) FLOAT',
    'C) CHARACTER', 
    'D) BOOLEAN', 
    'C) CHARACTER'),

    ('3. In SQL, which command is used to retrieve data from a database?',
    'A) GET',
    'B) FETCH',
    'C) SELECT', 
    'D) QUERY', 
    'C) SELECT'),

    ('4. What is the primary key in a database table?',
    "A) A key that uniquely identifies each record in the table",
    "B) A key used to establish a relationship between two tables",
    "C) A key that is automatically generated by the database system", 
    "D) A key used for sorting records in the table", 
    "A) A key that uniquely identifies each record in the table"),

    ("5. Which SQL command is used to add data to a database table?",
    "A) ADD",
    "B) INSERT",
    "C) UPDATE",
    "D) MODIFY",
    "B) INSERT"
    ),

    ('6. In SQL, what is the purpose of the WHERE clause?',
   "A) To specify the columns to be retrieved from the table",
   "B) To specify the order in which the results should be displayed",
   "C) To filter rows based on a specified condition",
    "D) To join multiple tables together", 
    "C) To filter rows based on a specified condition"),

    ('7. Which SQL command is used to delete data from a database table?',
    "A) REMOVE",
    "B) DELETE",
    "C) DROP",
    "D) ERASE",
    'B) DELETE'),

    ('8. What is a primary advantage of using a relational database management system (RDBMS)?',
    "A) Reduced redundancy and improved data integrity",
    "B) Increased security and data encryption",
    "C) Faster data access and retrieval",
    "D) Greater scalability and flexibility",
    "A) Reduced redundancy and improved data integrity"),

    ('9. In SQL, what is the purpose of the ORDER BY clause?',
    "A) To filter rows based on a specified condition",
    "B) To group rows that have the same value in a specified column",
    "C) To specify the columns to be retrieved from the table",
    "D) To sort the results of a query in ascending or descending order",
    'D) To sort the results of a query in ascending or descending order'),

    ("10. Which SQL command is used to update data in a database table?",
    "A) MODIFY",
    "B) CHANGE",
    "C) UPDATE",
    "D) ALTER",
    "C) UPDATE")
    ],

    'General Biology II': [
    ('1. What is the primary function of DNA?',
      'A) Energy storage',
      'B) Structural support',
      'C) Genetic information storage', 
      'D) Enzyme production', 
      'C) Genetic information storage'),

    ('2. Which organelle is responsible for protein synthesis?',
    'A) Golgi apparatus',
    'B) Endoplasmic reticulum',
    'C) Ribosome', 
    'D) Nucleus', 
    'C) Ribosome'),

    ('3. What is the powerhouse of the cell?',
    'A) Mitochondrion',
    'B) Nucleus',
    'C) Chloroplast', 
    'D) Endoplasmic reticulum', 
    'A) Mitochondrion'),

    ('4. What is the function of chlorophyll in plant cells?',
    "A) Photosynthesis",
    "B) Cell division",
    "C) Protein synthesis", 
    "D) Energy storage", 
    "A) Photosynthesis"),

    ("5. Which of the following is not a characteristic of prokaryotic cells?",
    "A) Presence of a nucleus",
    "B) Lack of membrane-bound organelles",
    "C) Smaller size compared to eukaryotic cells",
    "D) Presence of ribosomes",
    "A) Presence of a nucleus"
    ),

    ('6. Which cellular structure is responsible for cell movement?',
    "A) Flagellum",
    "B) Cilium",
    "C) Microvilli",
    "D) Nucleolus", 
    "A) Flagellum"),

    ('7. What is the process by which cells replicate their DNA?',
    "A) Translation",
    "B) Transcription",
    "C) Reproduction",
    "D) DNA replication",
    'D) DNA replication'),

    ('8. Which molecule serves as the primary energy source for cellular activities?',
    "A) Glucose",
    "B) ATP",
    "C) DNA",
    "D) RNA", 
    "B) ATP"),

    ('9. What is the function of the cell membrane?',
    "A) Regulation of cell processes",
    "B) Storage of genetic information",
    "C) Synthesis of proteins",
    "D) Control of cellular respiration",
    'A) Regulation of cell processes'),

    ("10. Which organelle is responsible for detoxification in liver cells?",
    "A) Nucleus",
    "B) Golgi apparatus",
    "C) Smooth endoplasmic reticulum",
    "D) Lysosome",
    "C) Smooth endoplasmic reticulum")
    ],

    'Mgmt organization Behavior': [
        ('1. What is the primary focus of organizational behavior?',
      'A) Studying individual behavior in organizations',
      'B) Analyzing financial performance',
      'C) Developing marketing strategies', 
      'D) Implementing technological innovations', 
      'A) Studying individual behavior in organizations'),

    ('2. What is the Hawthorne effect?',
    'A) The tendency for individuals to perform better when they are aware of being observed',
    'B) The impact of economic conditions on organizational behavior',
    'C) The influence of social norms on decision-making processes', 
    'D) The relationship between job satisfaction and productivity', 
    'A) The tendency for individuals to perform better when they are aware of being observed'),

    ('3. Which theory of motivation emphasizes the role of intrinsic factors?',
    'A) Expectancy theory',
    'B) Two-factor theory',
    'C) Equity theory', 
    'D) Self-determination theory', 
    'D) Self-determination theory'),

    ('4. What is the primary goal of organizational development (OD)?',
    "A) Improving organizational effectiveness and employee well-being",
    "B) Maximizing short-term profits",
    "C) Minimizing employee turnover", 
    "D) Reducing production costs", 
    "A) Improving organizational effectiveness and employee well-being"),

    ("5. Which leadership style involves high concern for both people and production?",
    "A) Autocratic",
    "B) Laissez-faire",
    "C) Transactional",
    "D) Transformational",
    "D) Transformational"
    ),

    ('6. What is the process of evaluating and rewarding employee performance?',
   "A) Performance appraisal",
   "B) Job analysis",
   "C) Recruitment",
    "D) Training", 
    "A) Performance appraisal"),

    ('7. Which conflict resolution strategy involves finding a solution that satisfies both parties?',
    "A) Avoidance",
    "B) Accommodation",
    "C) Collaboration",
    "D) Competition",
    'C) Collaboration'),

    ('8. What is the purpose of job enrichment?',
    "A) Increasing job specialization",
    "B) Reducing job complexity",
    "C) Adding variety and challenge to a job",
    "D) Decreasing employee autonomy", 
    "C) Adding variety and challenge to a job"),

    ('9. What is the primary focus of organizational culture?',
    "A) Employee job satisfaction",
    "B) Workplace diversity",
    "C) Shared values and beliefs",
    "D) Technological innovation",
    'C) Shared values and beliefs'),

    ("10. Which type of organizational structure emphasizes flexibility and decentralized decision-making?",
    "A) Functional",
    "B) Divisional",
    "C) Matrix",
    "D) Organic",
    "D) Organic")
    ],

    'Business Applications': [
    ('1. What is the primary purpose of a balance sheet?',
      'A) To show a company\'s revenues and expenses over a period of time',
      'B) To provide information about a company\'s cash flows',
      'C) To report a company\'s financial position at a specific point in time', 
      'D) To outline a company\'s business strategy', 
      'C) To report a company\'s financial position at a specific point in time'),

    ('2. What is the function of a profit and loss statement (P&L)?',
    'A) To show a company\'s revenues and expenses over a period of time',
    'B) To provide information about a company\'s cash flows',
    'C) To report a company\'s financial position at a specific point in time', 
    'D) To outline a company\'s business strategy', 
    'A) To show a company\'s revenues and expenses over a period of time'),

    ('3. Which financial metric indicates a company\'s ability to pay off short-term liabilities with its current assets?',
    'A) Debt-to-equity ratio',
    'B) Return on investment (ROI)',
    'C) Current ratio', 
    'D) Earnings per share (EPS)', 
    'C) Current ratio'),

    ('4. What is the purpose of financial forecasting?',
    "A) To predict a company's future stock price",
    "B) To estimate future cash flows and financial performance",
    "C) To calculate the company's net income for the current year", 
    "D) To evaluate the company's return on investment (ROI)", 
    "B) To estimate future cash flows and financial performance"),

    ("5. Which financial statement shows a company's revenues, expenses, and net income over a period of time?",
    "A) Balance sheet",
    "B) Income statement",
    "C) Statement of cash flows",
    "D) Statement of retained earnings",
    "B) Income statement"
    ),

    ('6. What is the purpose of a cash flow statement?',
   "A) To report a company's financial position at a specific point in time",
   "B) To show a company's revenues and expenses over a period of time",
   "C) To provide information about a company's cash flows",
    "D) To outline a company's business strategy", 
    "C) To provide information about a company's cash flows"),

    ('7. Which financial ratio measures a company\'s efficiency in using its assets to generate revenue?',
    "A) Return on equity (ROE)",
    "B) Gross profit margin",
    "C) Asset turnover ratio",
    "D) Price-to-earnings (P/E) ratio",
    'C) Asset turnover ratio'),

    ('8. What is the purpose of financial statement analysis?',
    "A) To evaluate a company's stock price",
    "B) To assess a company's financial health and performance",
    "C) To determine a company's market share",
    "D) To calculate a company's earnings per share (EPS)", 
    "B) To assess a company's financial health and performance"),

    ('9. Which financial metric measures a company\'s profitability relative to its shareholders\' equity?',
    "A) Return on equity (ROE)",
    "B) Gross profit margin",
    "C) Debt-to-equity ratio",
    "D) Asset turnover ratio",
    'A) Return on equity (ROE)'),

    ("10. What is the primary goal of financial management in a business?",
    "A) To maximize shareholder wealth",
    "B) To minimize employee turnover",
    "C) To increase market share",
    "D) To reduce operating expenses",
    "A) To maximize shareholder wealth"
    )
    ],
}

for category, questions in sample_questions.items():
    cursor.executemany(f'''
        INSERT INTO {category.replace(" ", "_")} (question, option1, option2, option3, option4, answer)
        VALUES (?, ?, ?, ?, ?, ?);
    ''', questions)

# Commit changes and close the connection
conn.commit()
conn.close()
