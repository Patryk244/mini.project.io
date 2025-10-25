from fetch_api import fetch_api

class count_from_or_for_api:
    def __init__(self, fetch_api: fetch_api):
        self.fetch_api = fetch_api

    def count_element_from_api(self, endpoint: str) -> int:
        element = self.fetch_api.get_desired_data(endpoint)
        try :
            number_of_element= len(element)
            return number_of_element
        except :
            return 0

    def is_not_equals_zero(self, element: int) -> bool:
        if element == 0:
            return False
        else:
           return True

    def average_amount(self, first_url: str, second_url: str) -> str:
        first_element = self.count_element_from_api(first_url)
        seconde_element = self.count_element_from_api(second_url)

        if self.is_not_equals_zero(first_element) and self.is_not_equals_zero(seconde_element):
            count_average: float = seconde_element / first_element
            return (f'Found {first_element} number of elements from {first_url} and found {seconde_element} number of '
                    f'elements from {second_url} so received {count_average} average number.')
        else:
            return "Incorrect api or element not found!"

    def percent_of_executed_task_by_user(self, first_url: str) -> float:
        init_executed_element: int = 0
        completed = self.fetch_api.get_desired_data(first_url)
        for element in completed:
            if element["completed"]:
                init_executed_element += 1
        return init_executed_element