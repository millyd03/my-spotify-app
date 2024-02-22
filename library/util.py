import secrets  # Use secrets module for improved security


def get_all_results(api_call, next_page_key="next"):
    """
    Retrieves all results from a paginated API call and returns them as a list.

    Args:
        api_call (callable): The API call function that takes arguments
            and returns a dictionary with results and a next page key.
        next_page_key (str, optional): The key in the response dictionary
            that indicates the next page URL. Defaults to "next".

    Returns:
        list: A list containing all retrieved results.
    """

    all_results = []
    page = 1
    while True:
        response = api_call(page=page)  # Assuming your API call accepts page argument

        if not response:  # Handle empty response
            break

        all_results.extend(response["results"])

        next_page_url = response.get(next_page_key, None)
        if not next_page_url:
            break

        page += 1

    return all_results


def get_random_int(min_value, max_value):
    """Generates a random integer within the specified range (inclusive) using a cryptographically secure random number generator.

    Args:
        min_value (int): The minimum value (inclusive) of the range.
        max_value (int): The maximum value (inclusive) of the range.

    Returns:
        int: A random integer between min_value and max_value, inclusive.

    Raises:
        ValueError: If min_value is greater than max_value.
    """

    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value.")

    rand_int = secrets.randbelow(max_value - min_value + 1)  # Adjust for inclusive range
    return rand_int + min_value  # Shift to desired minimum
