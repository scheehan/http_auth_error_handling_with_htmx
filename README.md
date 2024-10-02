![image](images/1.png)

# HTTP Authentication login failure Return Code handling usecases - Proficient Error Handling with hx-target-error and hx-responseError

When comes to User experience while tries to perform login process, which provides individual identity and credential to gain access and authorisation via HTTP authentication framework. it's often poses challenge to provide helpful information to user hinting what had happened upon a login failure.

I wanted to add a form and then either show an error message if the form failed to submit, or play the "close modal" animation if the form created a new record successfully.

This round of article meant to demontrate 2 approaches to proficiently handle HTTP [client error responses][5] code, whenever submitted credential via form submission doesn't matched with users database.

## htmx 

Htmx gives us access to AJAX directly in HTML by using attributes and provides an extensive events system that can be used to modify and enhance behavior. As per article title, we'll focus on below [htmx extension][2] and [events][3] attributes.

- hx-target-error
> This extension allows you to specify different target elements to be swapped when different HTTP response codes are received.
- hx-responseError
> This event is triggered when an HTTP error response occurs

## HTTP return Code: 

HTTP [client error responses][5] code, specifically 401 Unauthorized inform client must authenticate itself to get the requested response. Generally it may return in many forms as below whenever there is any HTTP authentication failure.

### 401 Error variations:
- HTTP Error 401 Unauthorized
- 401 Unauthorized Error
- Error 401 Unauthorized
- Access Denied
- 401 Authorization Required

Geenrally whenever there is any HTTP authentication failure 

This article will focus on HTTP return code 400. However, it can be 400 or 500 HTTP return code. 

401 Unauthorized
Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.


success velidation return with submitted usernameError 401 vs Error 403
When accessing or visiting a website, the WWW-authenticate header reviews the authentication method applied for granting you access to a web page. If it detects any missing valid authentication credentials, the error 401 error code will automatically display, indicating an unauthorized or expired session from your end.

On the other hand, error 403, or mostly known as the “403 Forbidden” error code, is a response status code indicating a denied access from the server despite acknowledging a requested resource access from you. This type of error is somewhat the same as 401 error. However, any re-authentication credentials your provided won’t change the web page access due to the website owner’s restrictions.

401 Error Code is an HTTP status code that refers to a client-side error caused by unauthorized access when visiting a password-protected website. This error can occur with any browser when a visitor fails to provide valid authentication credentials (e.g., incorrect URLs, outdated browser cache or cookies, plugin misconfiguration, etc.).

As a result, a variation of 401 error messages may appear on the screen depending on the browser the visitor is using.

## How It Works:

This article were focusing with below 2 solutions. htmx provides 2 htmx attributes capable to listens on error events, then perform certain action.


### solution 1:

response-targets extension

This extension allows you to specify different target elements to be swapped when different HTTP response codes are received.

It uses attribute names in a form of hx-target-[CODE] where [CODE] is a numeric HTTP response code with the optional wildcard character at its end. You can also use hx-target-error, which handles both 4xx and 5xx response codes.

Install htmc extension 

```html
<script src="https://unpkg.com/htmx-ext-response-targets@2.0.0/response-targets.js"></script>
```


```python
  <div hx-ext="response-targets">

        <form hx-post="/login" hx-target-401="#responsediv" hx-target="div#responsediv">
            Username: <input name="Username"><br>
            Password: <input name="password" type=password><br>
            <button type="submit">Log In</button>
          </form>

    <div id="responsediv">
    </div>

  </div>
```

### solution 2:



"htmx:responseError"
This event is triggered when an HTTP error response occurs

handling error with prompt

success velidation return with submitted username


hx-post  
hx-on  

event htmx:responseError

```python
    <div>
        <form hx-post="/login" hx-on:htmx:response-error="alert('Incorrect Username or Password Credential')" hx-target="#success-div">
            Username: <input name="Username"><br>
            Password: <input name="password" type=password><br>
            <button type="submit">Log In</button>
          </form>
    </div>
```

```html
<body hx-on::responseError="event.detail.xhr.status === 404 ?event.detail.shouldSwap = true : undefined"> 
```

## Final thoughts:

there is many other method to handle HTTP error
i find with htmx more easy and 




## Install

```
clone

```



[1]: https://htmx.org/attributes/hx-ext/
[2]: https://extensions.htmx.org/
[3]: https://htmx.org/events/#htmx:responseError
[4]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication
[5]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses
[6]: https://serjhenrique.com/create-dependent-dropdown-with-django-and-htmx/


---

The error handling was pretty straightforward, I just used the sendError and responseError events. It's the success handling portion that's giving me a hard time.

At the moment, returning Failure from an AuthenticationHandler results in a 401 Challenge response

HTTP provides a general framework for access control and
   authentication, via an extensible set of challenge-response
   authentication schemes, which can be used by a server to challenge a
   client request and by a client to provide authentication information.