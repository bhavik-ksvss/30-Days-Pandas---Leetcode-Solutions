#Q5. Invalid Tweets

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df=tweets
    df['Length'] = df['content'].apply(len)

    res_df=df[df['Length']>15]

    result=res_df[['tweet_id']]

    return result
    ### (or)

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where the length of 'content' is strictly greater than 15
    invalid_tweets_df = tweets[tweets['content'].str.len() > 15]
    
    # Select only the 'tweet_id' column from the invalid tweets DataFrame
    result_df = invalid_tweets_df[['tweet_id']]
    
    return result_df

#Q6. Calculate Special Bonus

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Create a new column 'bonus' with default value 0
    employees['bonus'] = 0
    
    # Calculate bonus based on the conditions
    employees.loc[(employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']
    
    # Select only the required columns and sort the result table by employee_id in ascending order
    result_df = employees[['employee_id', 'bonus']].sort_values(by='employee_id', ascending=True)
    
    return result_df

#Q7.Fix Names in a Table
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
	# Using lambda function to modify name column
    def fix_name(name):
        return name.capitalize()
    users['name'] = users['name'].str.lower().apply(fix_name)
    
	# Sorting database on user_id column
    res = users.sort_values(by='user_id')
    
	# Return final result
    return res

#Q8. Find Users With Valid E-Mails
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    def is_valid_email(email):
        try:

            prefix, domain = email.split('@')
            if domain == 'leetcode.com' and prefix[0].isalpha() and all(c.isalnum() or c in ['_', '.', '-'] for c in prefix):
                return True
        except ValueError:  # Handle cases where email format is  incorrect
            pass    
        return False

# Filter users with valid emails
    valid_users = users[users['mail'].apply(is_valid_email)]

    return valid_users


#Q9. Patients With a Condition
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    filtered_rows = []
    for index, row in patients.iterrows():
        conditions = row['conditions'].split(' ')
        if any(condition.startswith('DIAB1') for condition in conditions):
            filtered_rows.append(row)
    filtered_df = pd.DataFrame(filtered_rows, columns=patients.columns)
    return filtered_df