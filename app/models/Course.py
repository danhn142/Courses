""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """
    def get_all_courses(self):
        course_list = self.db.query_db("SELECT * FROM courses")
        return course_list

    def add_course(self, course_details):
        sql = "INSERT into courses (course_name, course_description, created_at) VALUES (:course, :description, NOW())"
        data = {
            'course': course_details['course'], 'description': course_details['description']
        } 
        return self.db.query_db(sql, data)

    def destroy(self, course_id):
        query = "SELECT * FROM courses WHERE id = :course_id"
        data = {"course_id": course_id }
        return self.db.query_db(query, data)

    def destroyed(self, remove_id):
        query = "DELETE FROM courses WHERE id = :course_id"
        data = {"course_id": remove_id}
        return self.db.query_db(query, data)








