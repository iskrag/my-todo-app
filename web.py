import streamlit as sl
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = sl.session_state['new_todo'] + '\n'
    if todo_local not in todos:
        todos.append(todo_local)
        functions.write_todos(todos)


sl.session_state['new_todo'] = ''

sl.title('My Todo App')
sl.subheader('This is my todo app.')
sl.write('This app is to increase your productivity.')

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=f'checkbox_{index}')
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del sl.session_state[f'checkbox_{index}']
        sl.rerun()


sl.text_input(label='', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')

# sl.session_state
