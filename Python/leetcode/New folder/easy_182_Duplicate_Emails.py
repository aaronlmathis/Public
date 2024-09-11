import pandas as pd
data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # Find duplicate emails and drop duplicates
    duplicate_emails = person[person.duplicated('email', keep=False)]['email'].drop_duplicates()

    # Convert to DataFrame for a clean output
    duplicate_emails_df = pd.DataFrame(duplicate_emails, columns=['Email'])

    return duplicate_emails_df

        



duplicate_emails(person)