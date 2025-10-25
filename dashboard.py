import streamlit as st
import pandas as pd
import plotly.express as px

class dashboard:
    def __init__(self, average_comments: float, average_post: float, percent: float, all_todos: int):
        self.average_comments = average_comments
        self.average_post = average_post
        self.percent = percent
        self.all_todos = all_todos
    def show_info_on_the_screen(self, number_one: int, number_two: int) -> None:
        st.write(self.average_comments)
        st.write(self.average_post)
        self.___draw_chart_for_executed_tasks()
        self.___draw_chart_for_difference_between_posts_and_comments(number_one, number_two)

    def ___draw_chart_for_executed_tasks(self) -> None:
        st.title("Percent of executed tasks: ")
        dane = {'status': ['Executed', 'Not executed'],
                'number of tasks:': [self.all_todos-self.percent, self.percent],}
        df = pd.DataFrame(dane)
        fig = px.pie(df, values='number of tasks:', names='status', title='Percentage of tasks completed vs. not completed')
        fig.update_traces(textinfo='percent+label', marker=dict(colors=['green', 'red']))
        st.plotly_chart(fig, use_container_width=True)

    def ___draw_chart_for_difference_between_posts_and_comments(self, number_one: int, number_two: int) -> None:
        st.title("Difference between posts and comments:")

        dane = {'number of: ': ['Posts', 'Comments'],
                'number of elements: ': [number_one, number_two]}

        df = pd.DataFrame(dane)
        fig = px.bar(
            df,
            x='number of: ',
            y='number of elements: ',
            color='number of: ',
            color_discrete_map={'Posts': 'green', 'Comments': 'red'},
            title='Difference between posts and comments',
        )

        fig.update_traces(textposition='outside')
        fig.update_layout(
            yaxis_title='Number of elements',
            xaxis_title='Type',
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)