# _*_ coding:utf-8 _*_
import falcon
from wsgiref import simple_server
from views import ScreamerResource, JsonOnlyMiddleware, CommentsResource, LikesResource
from models import Base, engine

# Init DB
Base.metadata.create_all(engine)

# Callable WSGI app
app = falcon.API(middleware=[JsonOnlyMiddleware()])

# Resources for API
screamer_resource = ScreamerResource()
comments_resource = CommentsResource()
likes_resource = LikesResource()

# Routing
app.add_route('/check', screamer_resource)
app.add_route('/comments/{webm_id}', comments_resource)
app.add_route('/likes/{webm_id}', likes_resource)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever() #--- Starting wsgi app on Windows
