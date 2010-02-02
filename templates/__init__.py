from web.template import CompiledTemplate, ForLoop


def index():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__ (error_msg=None, url=None, short_url=None):
        yield '', join_('<h1>Enter the URL you want to shorten below</h1>\n')
        yield '', join_('<div id="url_input_div">\n')
        yield '', join_('    <form method="post" action="/" id="url_input_form">\n')
        yield '', join_('        <label for="url" id="in">URL:</label>\n')
        yield '', join_('        <input type="text" id="url" class="url_text" value="" name="url"></input>\n')
        yield '', join_('        <input type="submit" id="submit_button" value="Generate URL"></input>\n')
        yield '', join_('    </form>\n')
        yield '', join_('    \n')
        if url:
            yield '', join_('    ', '<div id="short_url_info">\n')
            yield '', join_('    ', '    <label for="out">Short URL:</label>\n')
            yield '', join_('    ', '    <input type="text" name="out" class="url_text" value="', escape_(short_url, True), '"></input>\n')
            yield '', join_('    ', '    <p>Original URL: ', escape_(url, True), '</p>\n')
            yield '', join_('    ', '</div>\n')
        if error_msg:
            yield '', join_('    ', '<div id="short_url_info">\n')
            yield '', join_('    ', '    <p class="error">', escape_(error_msg, True), '</p>\n')
            yield '', join_('    ', '</div>\n')
        yield '', join_('</div>\n')
    return __template__

index = CompiledTemplate(index(), 'templates/index.html')


def layout():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__ (content):
        yield '', join_('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\n')
        yield '', join_('"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n')
        yield '', join_('\n')
        yield '', join_('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n')
        yield '', join_('<head>\n')
        yield '', join_('    <title>Short URL App</title>\n')
        yield '', join_('    <meta name="description" content="A basic URL shortener application built using web.py and Google App Engine" />\n')
        yield '', join_('    <meta name="keywords" content="url shortener, web.py, app engine, python, url" />\n')
        yield '', join_('    <link rel="stylesheet" href="/static/print.css" content="text/css" media="print">\n')
        yield '', join_('    <link rel="stylesheet" href="/static/screen.css" content="text/css" media="screen">\n')
        yield '', join_('    <link rel="stylesheet" href="/static/style.css" content="text/css" media="screen"/>\n')
        yield '', join_('    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon"/>\n')
        yield '', join_('    \n')
        yield '', join_('    <script type="text/javascript" src="/static/yahoo-min.js"></script>\n')
        yield '', join_('    <script type="text/javascript" src="/static/dom-min.js"></script>\n')
        yield '', join_('    <script type="text/javascript" src="/static/event-min.js"></script>\n')
        yield '', join_('    <script type="text/javascript" src="/static/connection-min.js"></script>\n')
        yield '', join_('    <script type="text/javascript" src="/static/shortenurl.js"></script>\n')
        yield '', join_('</head>\n')
        yield '', join_('<body>\n')
        yield '', join_('    <div id="header">\n')
        yield '', join_('        <h1><a href="/">Short URL App</a></h1>\n')
        yield '', join_('    </div>\n')
        yield '', join_('    <div id="content">\n')
        yield '', join_('        <div class="container">\n')
        yield '', join_('            ', escape_(content, True), '\n')
        yield '', join_('            <div id="how" class="span-24">\n')
        yield '', join_('                <h2>How To Use</h2>\n')
        yield '', join_('                <p>Enter URL that you wish to shorten into the textbox and click the \n')
        yield '', join_('                    Generate URL button. The application will then generate a short URL \n')
        yield '', join_('                    for you to use in text messages, on Twitter, in instant messaging \n')
        yield '', join_('                    applications, or anywhere else you wish to have a short URL. When the\n')
        yield '', join_("                    user clicks the link, they'll be taken to the original web site.</p>\n")
        yield '', join_('            </div>\n')
        yield '', join_('            <div class="span-12">\n')
        yield '', join_('                <h2>About</h2>\n')
        yield '', join_('                <p>This is a simple URL shortener created by Nick Weinhold in order to \n')
        yield '', join_('                    gain more experience in developing user-friendly web applications.</p>\n')
        yield '', join_("                <p>Whilst the site does work, it should not be considered 'fully \n")
        yield '', join_("                    functional' and it is not intended to be a replacement for URL \n")
        yield '', join_('                    shortening services such as bit.ly or TinyURL.</p>\n')
        yield '', join_('            </div>\n')
        yield '', join_('            <div class="span-12 last">\n')
        yield '', join_('                <h2>Technologies Used</h2>\n')
        yield '', join_('                <p>This site was created using the Python web framework web.py and Google \n')
        yield '', join_('                    App Engine. The site uses a mixture of handwritten CSS and the \n')
        yield '', join_('                    Blueprint CSS framework for styling and layout. Javascript is a \n')
        yield '', join_('                    mixture of handwritten Javascript and the Yahoo YUI 2 framework.</p>\n')
        yield '', join_('            </div>\n')
        yield '', join_('        </div>\n')
        yield '', join_('    </div>\n')
        yield '', join_('    <div id="footer">\n')
        yield '', join_('        <p class="footer_text">Powered by web.py and Google App Engine</p>\n')
        yield '', join_('    </div>\n')
        yield '', join_('</body>\n')
        yield '', join_('</html>\n')
        yield '', join_('    \n')
    return __template__

layout = CompiledTemplate(layout(), 'templates/layout.html')


def notfound():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__ (url):
        yield '', join_('\n')
        yield '', join_('<h1>Link not found!</h1>\n')
        yield '', join_('<p class="error">The short URL ', escape_(url, True), ' was not found in our database.</p>\n')
    return __template__

notfound = CompiledTemplate(notfound(), 'templates/notfound.html')

