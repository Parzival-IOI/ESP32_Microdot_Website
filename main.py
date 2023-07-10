from lib.microdot_asyncio import Microdot, Response, send_file, redirect
from lib.microdot_utemplate import render_template
from control import Led
from lib.microdot_session import get_session, update_session, delete_session, with_session, set_session_secret_key

pw = "Glory_to_Ainz"

class Value:
    def __init__(self, led):
        self.led = led
        self.text = ['Getting Started']
    def add_Text(self, text):
        self.text.append(text)

app = Microdot()
set_session_secret_key(pw)
Response.default_content_type = 'text/html'

# Our LED Module
led = Led(pinNum=2)

value = Value(led.get_value())

# startingm of web


@app.route('/')
@with_session
async def index(req, session):
    key = session.get('key')
    if key == pw:
        return redirect('/main')
    return render_template('index.html', value = value)
    

@app.post('/')
async def index(req):
    if (req.method == 'POST' and req.form.get('username')== "Parzival" and req.form.get('password')== pw):
        update_session(req, {'key': pw})
        return redirect('/main')
    return redirect('/')
        

@app.route('/main')
@with_session
async def index(req, session):
    key = session.get('key')
    if key != pw:
        return redirect('/')
    return render_template('main.html', value = value)
        
@app.route('/logout')
async def logout(req):
    delete_session(req)
    return redirect('/')

@app.route('/other')
@with_session
async def index(req, session):
    key = session.get('key')
    if key != pw:
        return redirect('/')
    return render_template('other.html', value = value)

@app.post('/other')
async def index(req):
    if req.method == 'POST':
        name = req.form.get('text-box')
        print(name)
        value.add_Text(name)
    return redirect('/other')

@app.route('/order/delete')
async def delete_order(req):
    value.text = ['Getting Started']
    print("Deleting Text")
    return redirect('/other')

@app.route('/main/toggle')
async def toggle_led(req):
    print("Receive Toggle Request!")
    led.toggle()
    return "OK"

@app.errorhandler(404)
async def not_found(req):
    return {'error': 'resource not found'}, 404

@app.errorhandler(ZeroDivisionError)
async def division_by_zero(req, exception):
    return {'error': 'division by zero'}, 500

@app.errorhandler(RuntimeError)
async def runtime_error(req, exception):
    return 'Runtime error'

@app.route('/static/<path:path>')
async def static(req, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path)


@app.route('/shutdown')
def shutdown(req):
    req.app.shutdown()
    return 'The server is shutting down...'

app.run(debug=True)