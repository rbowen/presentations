# Configurable Configuration in Apache httpd 2.4

Rich Bowen - rbowen@apache.org

ApacheCon NA 2014

SLIDES ARE AT: http://boxofclue.com/presentations/

---

## Subtitle: Lots of great reasons not to use mod_rewrite any more!

![book](images/book.jpg)

---

![agenda](images/agenda.jpg)
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

<small>*Photo Credit: [shoehorn99](http://www.flickr.com/photos/27664925@N00/2458505877/) on Twitter.*</small>

---

Frequently asked question

> Can I use some kind of variable or conditionals in my configuration file?

---

![pony](images/pony.jpg)

---

Apache 2.4

![pony](images/mypony.jpg)

---

Actually, you have a wide selection of ponies

![ponies](images/ponies.jpg)

---

![pony](images/pony1.jpg)

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

        # httpd -DDev
        <IfDefine Dev>
            Include conf/dev.conf
        </IfDefine Dev>

        # httpd -DStage
        <IfDefine Stage>
            Include conf/stage.conf
        </IfDefine Stage>

        # httpd -DProduction
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

![pony](images/pony1.jpg)

`<If>` ... `<ElseIf>` ... `<Else>`

---

`<If>`

- Evaluate arbitrary expression
- Apply contained configuration
- The rest of these are request-time configuration settings
- Can be slower than static config
- Better alternative to mod_rewrite in most cases

---

So ... what does an expression look like?

---

# Expression parser

- New in 2.4
- Arbitrary expression evaluation
- Can be used in many different configuration directives

---

## Examples: Comparison

        %{HTTP_HOST} == 'example.com'

        %{QUERY_STRING} =~ /forcetext/

        %{TIME_HOUR} -gt 9 && %{TIME_HOUR} -lt 17

---

## Comparisons

- Can be string (==, !=, <, <=, >, >=)
- Or numerical (eq, ne, lt, le, gt, ge)
- Or regex (=~, !~)

---

## Special comparisons

<table border="2">

<tr><th>Comparison operator:</th>
</th></th>
</tr>

<tr>

<td>-ipmatch</td>
<td>IP address matches address/netmask</td>
</tr>

<tr><td>-strmatch</td>
<td>left string matches pattern given by right string (containing wildcards `*`, `?`, `[]`)</td></tr>

<tr><td>-strcmatch</td>
<td>same as -strmatch, but case insensitive</td></tr>

<tr><td>-fnmatch</td>
<td>same as -strmatch, but slashes are not matched by wildcards</td></tr>
</table>

---

## Example: in list

        Require expr %{TIME_WDAY} in {0,2,4}

---

## Unary operators

<table class="bordered"><tr class="header"><th>Name</th><th>Description</th></tr>
<tr><td><code>-d</code></td>
<td>The argument is treated as a filename.  True if the file exists and is a directory</td></tr>
<tr class="odd"><td><code>-e</code></td>
<td>The argument is treated as a filename.  True if the file (or dir or special) exists</td></tr>
<tr><td><code>-f</code></td>
<td>The argument is treated as a filename.  True if the file exists and is regular file</td></tr>
<tr class="odd"><td><code>-s</code></td>
<td>The argument is treated as a filename.  True if the file exists and is not empty</td></tr>
</table>

---

## Unary operators

<table class="bordered"><tr class="header"><th>Name</th><th>Description</th></tr>
<tr><td><code>-L</code></td>
<td>The argument is treated as a filename.  True if the file exists and is symlink</td></tr>
<tr class="odd"><td><code>-h</code></td>
<td>Alias for -L</td></tr>
<tr><td><code>-F</code></td>
<td>True if string is a valid file, accessible via all the server's
currently-configured access controls for that path. This uses an
internal subrequest to do the check, so use it with care - it can
impact your server's performance!</td><td /></tr>
<tr class="odd"><td><code>-U</code></td>
<td>True if string is a valid URL, accessible via all the server's
currently-configured access controls for that path. This uses an
internal subrequest to do the check, so use it with care - it can
impact your server's performance!</td><td /></tr>
</table>

---

## Unary operators

<table class="bordered"><tr class="header"><th>Name</th><th>Description</th></tr>
<tr><td><code>-A</code></td>
<td>Alias for <code>-U</code></td><td /></tr>
<tr class="odd"><td><code>-n</code></td>
<td>True if string is not empty</td><td /></tr>
<tr><td><code>-z</code></td>
<td>True if string is empty</td><td /></tr>
<tr class="odd"><td><code>-T</code></td>
<td>False if string is empty, "<code>0</code>", "<code>off</code>",
"<code>false</code>", or "<code>no</code>" (case insensitive).
True otherwise.</td><td /></tr>
<tr><td><code>-R</code></td>
<td>Same as "<code>%{REMOTE_ADDR} -ipmatch ...</code>", but more
efficient
</td><td /></tr>
</table>

---

# Back to `<If>`

`<If>` allows you to do conditional request-time evaluation in your
configuration, making impossible things possible, and hard things easy.

---

![www](images/www.svg)

        <If "req('Host') = 'example.com' ">
            Redirect Permanent / http://www.example.com/
        </If>

---

![dino](images/dino2.gif)

        RewriteEngine On
        RewriteCond %{HTTP_REFERER} !www.example.com [NC]
        # Bah. Had to hard code the server name!
        RewriteRule \.(gif|jpg|png)$ http://other.example.com/images/diaf.jpg   [R]

---

![diaf](images/diaf.jpg)

        <If "%{HTTP_REFERER} != %{SERVER_NAME}">
            RedirectMatch \.(gif|jpg|png)$ /images/diaf.jpg
        </If>

---

![dino](images/dino3.gif)

        RewriteEngine on
        RewriteCond   %{TIME_HOUR}%{TIME_MIN} >0700
        RewriteCond   %{TIME_HOUR}%{TIME_MIN} <1900
        RewriteRule   ^/foo\.html$             /foo.day.html [PT]
        RewriteRule   ^/foo\.html$             /foo.night.html [PT]

---

![daynight](images/daynight.jpg)

        <If "%{TIME_HOUR} -gt 9 && %{TIME_HOUR} -lt 17">
            Redirect /hours.html /open.html
        </If>
        <Else>
            Redirect /hours.html /closed.html
        </Else>

More lines, but clearer to read.

---

# `<If>`

- Evaluated at request time, so there might be a performance penalty.
- Probably on par with mod_rewrite
- Consider maintainability as well as performance

note:: Most websites are *not* CPU-bound. Be careful what you optimize

---

## Optimize

- If you're calling a handler (php, mod_lua, whatever), you might want to do logic there
- Put more likely options earlier (if, elseif, else)

---

# Where else?

- expressions in auth
- expressions in mod_include
- expressions in mod_rewrite

---

![pony](images/pony7.jpg)
Authorization with expressions

---

# Authorization

- Can now authorize based on arbitrary expressions
- Remember: authorization != authentication

---

## Example

        Require expr %{TIME_HOUR} -gt 9 && %{TIME_HOUR} -lt 17

        Require expr %{HTTP_USER_AGENT} != 'BadBot'

        Require expr %{HTTPS} == 'on'
        # Which is the same as ...
        Require ssl

---

### Caveat

        Require expr %{TIME_HOUR} -gt 9 && %{TIME_HOUR} -lt 17

not

        Require expr "%{TIME_HOUR} -gt 9 && %{TIME_HOUR} -lt 17"

---

![pony](images/pony6.jpg)

mod_include

---

## mod_include

Can use expr format in `#if` elements in SSI (Server-Side Include) doucuments

---

## Example

        <!--#if expr='-R "10.0.0.0/8"' -->
            from local net
        <!--#else -->
            from somewhere else
        <!--#endif -->

-R is the same as `"%{REMOTE_ADDR} -ipmatch ..."`

---

If you're not familiar with mod_include ...

- Directives go into the HTML
- Are parsed on the server side at request time

    Options +Includes
    AddOutputFilter INCLUDES .shtml

http://httpd.apache.org/docs/mod/mod_include.html

---

![pony](images/pony5.jpg)

mod_rewrite

note:: Was going to use a picture of a dead horse, but ...

---

## expr in mod_rewrite

expr can be used in `RewriteCond`

        RewriteCond expr "! %{HTTP_REFERER} -strmatch '*://%{HTTP_HOST}/*'"
        RewriteRule ^/images - [F]

Simplifies comparisions that were previously very difficult

---

![pony](images/pony4.jpg)

mod_macro

---

# mod_macro

- In 2.2 and earlier, a third-party module available from https://people.apache.org/~fabien/mod_macro/#download
- Download and enable using

        apxs -cia mod_macro.c

---

## mod_macro

- In 2.4.6, became part of the HTTP Server distribution

        LoadModule macro_module modules/mod_macro.so

---

## mod_macro

![grinder](images/meatgrinder.jpg)

- As the name implies ... define macros in your configuration file
- Invoke those macros, with arguments, at server startup
- Results of macro are then evaluated as part of the configuration

---

## Example

        <Macro VHost $name $domain>
        <VirtualHost *:80>
            ServerName $domain
            ServerAlias www.$domain

            DocumentRoot /var/www/vhosts/$name
            ErrorLog /var/log/httpd/$name.error_log
            CustomLog /var/log/httpd/$name.access_log combined
        </VirtualHost>
        </Macro>

---

## Invoke with ...

        Use VHost example example.com
        Use VHost myhost hostname.org
        Use VHost apache apache.org
        Use VHost pony  pony.com

---

## Clean up with

        UndefMacro VHost

In case there's a name conflict elsewhere. (Macro names are global)

---

## Example

        <Macro DirGroup $dir $group>
          <Directory $dir>
            Require group $group
          </Directory>
        </Macro>

        Use DirGroup /www/apache/private private
        Use DirGroup /www/apache/server  admin

        UndefMacro DirGroup

---

## Example

        # Macro definition for a generic virtual host
        <Macro BeginVHost $fqdn>
            <VirtualHost *:80>
                ServerName $fqdn
                DocumentRoot /var/www/$fqdn

                ErrorLog /var/log/apache2/$fqdn/error_log
                CustomLog /var/log/apache2/$fqdn/access_log common
                php_admin_value error_log "/var/log/apache2/$fqdn/php_error_log"
        </Macro>
        <Macro EndVHost>
            </VirtualHost>
        </Macro>

        # virtual hosts defined with:
        Use BeginVHost www.example.org
            # Define specific virtual host configuration here.
            # Example:
            # Use ZendFramework
        Use EndVHost

<small>*Stolen from http://patrickallaert.blogspot.com/2007/12/templatize-your-apache-configuration.html*</small>

---

![pony](images/pony3.jpg)

mod_vhost_alias

---

## mod_vhost_alias

Yes, there's mod_vhost_alias, but it's very limiting

        UseCanonicalName    Off
        VirtualDocumentRoot /usr/local/apache/vhosts/%3+/%2.1/%2.2/%2.3/%2

`www.apache.org` becomes `/usr/local/apache/vhosts/org/a/p/a/apache`

---

## mod_proxy_express

Simplifies setting up large numbers of proxypass conditions

---

![dino](images/dino4.gif)

        <VirtualHost *:80>
           ServerName foo.example.com

           ProxyPass / back.end.server:8090
           ProxyPassReverse / back.end.server:8090
        </VirtualHost>

---

But if you have hundreds of those ...

## Make a ProxyExpress map file with the entries:

        ##
        ##express-map.txt:
        ##

        www1.example.com http://192.168.211.2:8080
        www2.example.com http://192.168.211.12:8088
        www3.example.com http://192.168.212.10

---

## Create DBM file

        httxt2dbm -i express-map.txt -o emap

---

## Configuration

        ProxyExpressEnable on
        ProxyExpressDBMFile /path/to/emap

---

![pony](images/pony8.jpg)
## What else?

- Many client-side options via varios Javascript frameworks
- Various third-party modules at modules.apache.org
- Things like `mod_sed` and `mod_proxy_html` that do request-time rewriting

---

# Questions?

- \#httpd on Freenode
- @apache_httpd on Twitter
- @rbowen on Twitter
- users@httpd.apache.org

---

## Finis

rbowen@apache.org

@rbowen

Slides at http://boxofclue.com/presentations and at https://github.com/rbowen/presentations/

