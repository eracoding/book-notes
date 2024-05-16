# 1. Introduction to Professional Certificate

1. A Front-end developer is someone that works on all parts of a website or web app that users will interact with. This can be anything from the style colors, buttons, menus or
user interactions as they click swipe and interact with the site.
The skills of a front end developer can vary, but
they will always focus on three leading technologies.
Html CSS and javascript.

2. A back end developer works on the parts of a website or
web app that the end users don't see.
These activities occur behind the scenes, particularly on the web
server in the database or in constructing the architecture.
Back end developers are responsible for creating and
maintaining functionality when users request information or
when the website needs to communicate to another part of the web architecture.

# 2. How the web works

1. A web page is a document that displays images, texts, videos and other content in the web browser, a website is a collection of webpages that link together. 

2. Browser renders the web pages.

3. Web hosting is a service where you place your website and files on the hosting companies web server. You're essentially renting the space in return for stable and secure storage. 

4. Types of hosting: shared hosting, virtual private hosting, dedicated hosting, cloud hosting.

5. HTTP is a protocol used for transferring web resources such as HTML documents, images, styles, and other files. HTTP is a request response based protocol. An HTTP requests consists of a method (GET, POST, PUT, DELETE), path ('/' -endpoint), version and headers.

HTTP status codes contained within the header
indicate if the HTTP request successfully completed.
The code values are in the range of
100-599 and are grouped by purpose. 

There are five groups of status codes.
They are grouped by the first digit of the error number.
Informational is grouped 100-199.
Successful responses are grouped from 200-299.
Redirection message are 300-399.
Client error responses range from 400-499,
and server error responses are 500-599. 

1. Information responses are
provisional responses sent by the server.
These responses are interim before the actual response.
The most common information response is 100 continue,
which indicates that the web client should continue to
request or ignore the response
if the request is already finished. 

2. Successful responses indicate that
the request was successfully processed by the web server,
with the most common success response
being 200 OK.
You're receiving these responses every day when you
receive content successfully from a website. 

3. Redirection responses indicate to the web client
that the requested resource
has been moved to a different path.
The most common response codes used are
301 moved permanently and 302 found.
The difference between the redirection messages
301 and 302 is that
302 indicates a temporary
redirection.The resource has been temporarily moved.
When web browsers receive these responses,
they will automatically submit
the request for the resource at the new path. 

4. Client error responses indicate
that the requests contained
bad syntax or content
and cannot be processed by the web server.
The most common codes used are 400 is
used when the web browser or
client submitted bad data to the web server,
401 is used to indicate that the user
must log into an account
before the request can be processed,
403 is used to indicate the request was valid,
but that the web server is refusing to process it.
This is often used to indicate that a user does not have
sufficient permissions to execute
an action in a web application,
404 is used to indicate that
the request resource was not found on the web server. 

5. Server error responses indicate that a failure
occurred on the web server
while trying to process the request.
The most common code used is 500 internal server error,
which is a generic error status
indicating that the server failed to process the request. 


**HTTPS**

Have you ever bought something
online and needed to enter your credit card information?
You wouldn't want someone else to get
this information from the HTTP request.
This is where HTTPS is involved.
HTTPS is the secure version of HTTP.
It is used for secure communication between two computers
so that nobody else can see
the information being sent and received.
It does this by using something called encryption.

Like in HTTP, the requests and responses
still behave in the same way and have the same content.
The big difference is that before the content is sent,
it is turned into a secret code.
Only the other computer can turn
the secret code back into its original content.
If someone else was to look at the code,
it wouldn't be understandable.