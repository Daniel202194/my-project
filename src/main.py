from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify

class MyFlaskApp(Flask):
    def run(self, host=None, port=None, debug=None, **options):
        super(MyFlaskApp, self).run(host=host, port=port, debug=debug, **options)


application = MyFlaskApp(__name__)
application.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@application.route("/")
def show_hello():
    return 'hello world'
if __name__ == '__main__':
    # run the Flask RESTful API, make the server publicly available (host='0.0.0.0') on port 8080
    application.run(host='0.0.0.0', port=8080, debug=False)
    #run_with_ngrok(app)
    #app.run()
