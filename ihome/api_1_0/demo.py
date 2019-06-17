from . import api

@api.route("/index")
def Index():
    return 'Index'