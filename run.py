from market import app

if __name__ == "__main__":
    # so no more 
    '''
    # for hot reload run
    $ export FLASK_APP=<filename.py>
    $ export FLASK_DEBUG=1
    '''
    app.run(debug = True)