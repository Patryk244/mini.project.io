from dashboard import dashboard
from fetch_api import fetch_api
from count_from_or_for_api import count_from_or_for_api


class main:
    url: str = "https://jsonplaceholder.typicode.com"
    x = count_from_or_for_api(fetch_api(url))
    average_post: float = x.average_amount("/users", "/posts")
    average_comments: float = x.average_amount("/posts", "/comments")
    percent_for_executed_tasks:float = x.percent_of_executed_task_by_user("/todos")
    all_todos = x.count_element_from_api("/todos")
    (dashboard(average_comments, average_post, percent_for_executed_tasks, all_todos)
     .show_info_on_the_screen(x.count_element_from_api("/posts"), x.count_element_from_api("/comments")))

if __name__ == "__main__":
    main()