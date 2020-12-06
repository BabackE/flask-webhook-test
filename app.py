from flask import Flask, request
app = Flask(__name__)

html = '''
<HTML>
    <HEAD>
        <TITLE>webhook test on render</TITLE>
        <meta name="google-site-verification" content="3uZFaYKHtnZTBmjyloWwVVkE9kFyGvhRv6ZWM-XGNPA" />
    </HEAD>
    <BODY>
        Hello, webhook!
    </BODY>
</HTML>
'''

@app.route('/', methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return html

    if request.meth == 'POST':
        print (request.get_json())
        return html
