import os
from datetime import datetime, timedelta

def make_commit(days: int, start_date: str):
    """
    Makes commits for 'days' number of days starting from 'start_date'.

    :param days: Number of commits (days) to create
    :param start_date: Starting date in 'YYYY-MM-DD' format
    """
    date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    
    for i in range(days):
        commit_date = date_obj + timedelta(days=i)
        date_str = commit_date.strftime("%Y-%m-%d 12:00:00")  # commit at noon

        # Append to file
        with open('data.txt', 'a') as file:
            file.write(f'{date_str}\n')

        # Stage the file
        os.system('git add data.txt')

        # Commit with the specified date
        os.system(f'git commit --date="{date_str}" -m "Commit for {date_str}"')

    # Push all commits at the end
    os.system('git push')

# Usage: 365 commits starting from August 25, 2025
make_commit(365, "2025-08-25")
