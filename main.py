from flask import Flask, request, make_response, render_template
app = Flask('app')

@app.route('/')
def hello_world():
  return make_response(render_template('index.html'))

@app.route('/ehc', methods=["GET"])
def welcome():
    ehc = 0
    print(request.host)
    if request.user_agent.string.lower() == 'ehc':
      print(request.host + "1")
      ehc = 1
    if ehc == 1 and request.referrer == 'http://' + request.host:
      ehc = 3
    if ehc == 3 and request.headers.get('DNT') == '1':
      ehc = 4
    if ehc == 4 and request.headers.get('Accept-Language') == 'ja':
      ehc = 5
    if ehc == 5 and request.headers.get('Date') == '2017':
      ehc = 6
    return make_response(render_template('ehc.html', flag=ehc))


app.run(host='0.0.0.0', port=8090)