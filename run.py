# from app import app

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask
from livereload import Server
from app import app

app.debug = True  # Enable Flask's debug mode for template auto-reloading

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('app/templates/*.*')  # Watch all template files
    server.watch('app/static/*.*')     # Watch all static files
    server.serve(port=5500, host='localhost', liveport=35729, debug=True)