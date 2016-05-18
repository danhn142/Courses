"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *


class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Course')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        courses = self.models['Course'].get_all_courses()
        return self.load_view('index.html', courses = courses)

    def add(self):
        if len(request.form['n_ame']) < 1:
            flash("Course and description cannot be empty")
            return redirect ('/')
        elif len(request.form['desc']) < 1:
            flash("Course and description cannot be empty")
            return redirect ('/')
        else:
            flash("Course has been added")

        course_details = {
            'course': request.form['n_ame'],
            'description': request.form['desc']

        }

        self.models['Course'].add_course(course_details)
        return redirect ('/')

    def remove(self, id):
        destroy = self.models['Course'].destroy(id)
        return self.load_view('delete.html', destroy = destroy[0])
    
    def removed(self, id):
        if request.form['No'] == "Cancel":
            return redirect ('/')
        
        self.models['Course'].destroyed(id)
        return redirect ('/')


        






