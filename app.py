from flask import Flask
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

@app.route('/')
def hello_world():
    return html
