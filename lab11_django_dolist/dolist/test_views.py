from django.test import TestCase
from django.urls import reserve
from . models import Todolist
from . forms import TodoListForm
from . views import addTodoItem, completedTodo

class TodoViewsTestCase(TestCase):
    def setup(self):
        # create inital data for testing
        self.task1 = Todolist.objects.create(text="Task 1", completed = False)
        self.task2 = Todolist.objects.create(text="Task 2", completed = False)
        self.task3 = Todolist.objects.create(text="Task 3", completed = True)
        
    # test the index view renders the correct context and template
    def test_index_view(self):
       response = self.client.get(reverse('index')) 
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'index.html')

       #check if all tasks are included in the context
       self.assertQuerySetEqual(
           response.context['todo_tasks'],
           Todolist.objects.order_by('id'),
           transform=lambda x:x,


       )
       self.assertIsInstance(response.context['form'], TodoListForm)
