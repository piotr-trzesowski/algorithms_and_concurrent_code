import concurrent.futures
import time


# Sample function to execute a query

def run_query(test_case, query):
    # Simulate a time-consuming query
    time.sleep(1)  # Simulates the query execution time
    result = f"Result for {test_case}: {query}"
    return result


# Function to run queries concurrently
def run_queries_concurrently(queries):
    results = {}

    # Use ThreadPoolExecutor to run queries concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Create a dictionary to map future objects to test cases
        future_to_query = {executor.submit(run_query, test_case, query): test_case for test_case, query in queries.items()}

        # Process the results as they complete
        for future in concurrent.futures.as_completed(future_to_query):
            test_case = future_to_query[future]
            try:
                result = future.result()
                results[test_case] = result
            except Exception as exc:
                results[test_case] = f"Exception: {exc}"

    return results

# Example input: dictionary of test cases and their corresponding queries
queries = {
    "test_case1": "SELECT * FROM users WHERE id=1",
    "test_case2": "SELECT * FROM orders WHERE id=2",
    "test_case3": "SELECT * FROM products WHERE id=3",
}

# Run queries concurrently
concurrent_results = run_queries_concurrently(queries)

# Print results
for test_case, result in concurrent_results.items():
    print(f"{test_case}: {result}")
