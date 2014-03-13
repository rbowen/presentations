# Configurable Configuration in Apache httpd 2.4

ApacheCon NA 2014

SLIDES ARE AT: http://boxofclue.com/presentations/

---

Agenda:

- The ancient past
- Config variables
- `<If>` syntax
- Expression parser
- mod_macro

---

In the distant past ...

![dino](images/dino.jpg)
Repeated config blocks, Maybe use `Include` to avoid repetition, Third party modules

*Photo Credit: [shoehorn99](http://www.flickr.com/photos/27664925@N00/2458505877/) on Twitter.*

---

Frequently asked question

> Can I use some kind of variable or conditionals in my configuration file?

---

![pony](images/pony.jpg)

---

Apache 2.4

![pony](images/mypony.jpg)

---

Config variables

---

## IfDefine

Even in ancient times ...

Start httpd with:

        httpd -DSSL

Then ...

        <IfDefine SSL>
            Listen 443
        </IfDefine>

---

One config to run them all

        <IfDefine Dev>
            Include conf/dev.conf
        </IfDefine Dev>

        <IfDefine Stage>
            Include conf/stage.conf
        </IfDefine Stage>

        <IfDefine Production>
            Include conf/production.conf
        </IfDefine>

---

## Define

Used with just one argument, sets a variable to true

        # Toggle on/off in one place
        Define SSL

        <IfDefine SSL>
            Listen 443
        </IfDefine>

---

## Define

New in 2.4

        Define docroot /var/www/
        DocumentRoot ${docroot}

        <Directory ${docroot}>
            Require all granted
        </Directory>

---

## UnDefine

![switch](images/switch.jpg)

Switch off variable

        UnDefine SSL

---

Request-time configuration settings

* There is request-time processing, so it can be slower than static config
* Better alternative to mod_rewrite in most cases
* YMMV

---

## `<If>`

![if](images/if.jpg)

---

`<If>`

- Evaluate arbitrary expression
- Apply contained configuration

---

So ... what does an expression look like?

---

# Expression parser

- New in 2.4
- Arbitrary expression evaluation
- Can be used in many different configuration directives

---

# Expressions

        %{HTTP_HOST} == 'example.com'

        %{QUERY_STRING} =~ /forcetext/

        %{TIME_HOUR} -gt 9 && %{TIME_HOUR} -lt 17

---

# Expressions

        Require expr %{TIME_WDAY} in {0,2,4}

---

- expressions in auth
- expressions in mod_include
- expressions in mod_rewrite

---

# mod_macro

---

## Finis

