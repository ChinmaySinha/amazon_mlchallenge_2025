import pandas as pd

try:
    # Load your submission file and the sample submission file
    user_submission = pd.read_csv('test_out.csv')
    sample_submission = pd.read_csv('sample_test_out.csv')

    # --- Analysis ---

    # 1. Inspect column names and data types
    print("--- Your Submission File Info ---")
    user_submission.info()
    print("\n--- Sample Submission File Info ---")
    sample_submission.info()

    # 2. Check the number of rows
    print(f"\nNumber of rows in your submission: {len(user_submission)}")
    print(f"Number of rows in sample submission: {len(sample_submission)}")
    if len(user_submission) != len(sample_submission):
        print(">>> CRITICAL: Row count does not match!")


    # 3. Compare 'sample_id' columns
    user_ids = set(user_submission['sample_id'])
    sample_ids = set(sample_submission['sample_id'])

    if user_ids == sample_ids:
        print("\nThe 'sample_id' columns contain the same set of IDs.")
    else:
        print("\n>>> CRITICAL: The 'sample_id' columns do NOT contain the same set of IDs.")
        # Find the differences
        if len(user_ids - sample_ids) > 0:
            print(f"IDs in your submission but not in sample: {user_ids - sample_ids}")
        if len(sample_ids - user_ids) > 0:
            print(f"IDs in sample but not in your submission: {sample_ids - user_ids}")

    # 4. Check if 'sample_id's are in the same order
    if user_submission['sample_id'].equals(sample_submission['sample_id']):
        print("The 'sample_id' columns are in the same order.")
    else:
        print(">>> WARNING: The 'sample_id' columns are NOT in the same order.")

    # 5. Check for missing values
    print("\nMissing values in your submission:")
    print(user_submission.isnull().sum())
    print("\nMissing values in sample submission:")
    print(sample_submission.isnull().sum())


except FileNotFoundError as e:
    print(f"Error: {e}. Make sure the CSV files are in the same directory as the script.")


