:title: Demystifying mod_rewrite
:data-transition-duration: 500
:css: css/hovercraft.css

Demystifying mod_rewrite

----

Demystifying mod_rewrite
========================

Less magic, more science

Rich Bowen - rbowen@apache.org

@rbowen

http://rcbowen.com/

SLIDES ARE AT: http://tm3.org/rewrite_ac2014

----

.. image:: images/voodoo.jpg


Despite the tons of examples and docs, mod_rewrite is voodoo. Damned
cool voodoo, but still voodoo.

-- Brian Moore

----

.. image:: images/wizard.gif

And numerous websites offer mod_rewrite advice that is much more akin to
magic than science.

----

.. image:: images/algebra.gif

I'd like to show you that mod_rewrite is a clear, concise,
algebraic notation, not a magical incantation.

----

Regular Expressions
===================

.. image:: images/mre.jpg

* Atomic description of text patterns
* Start with a small vocabulary and work up
* Essential building block of mod_rewrite syntax
* PCRE

.. note:: Mastering Regular Expressions, Jeffrey Friedl

----

.
===


* Wildcard character
* Matches one "atom"
* In mod_rewrite syntax, it matches a 'character'
* Use \. if you want to match a literal "."

----

Tangent
=======

* 'Character' vs 'Byte'

.. image:: images/chinese.jpg
   :height: 507px
   :width: 600px

----

.. image:: images/axb.png

----

+/\*/?
======

* Repetition characters
* Turns an atom into a molecule


----

\+ - One or more
================

.. image:: images/a+.png

----

\* - Zero or more
=================

* a* matches zero or more 'a' characters
* a
* aaaaa
* Also matches "Fish", which contains zero 'a' characters

----

\?
=====

* Makes a match optional
* That is, matches zero or one

----

.. image:: images/colour.png

----

^ and $
=======

* Anchors
* Starts with
* Ends with

----

.. image:: images/anchora.png

----

.. image:: images/anchora2.png

----

^$ and ^
=========

* ^$ is a special case - matches empty string
* starts with ends with (nothing between)
* ^ (all by itself) matches every string (including empty string)

----

( )
====

* Turns several atoms into a molecule (grouping)
* Can apply repetition characters to this molecule
* (ab)+ matches "abababab"

----

( )
=====

* Also "captures"
* The matched set of parentheses becomes $1
* The next one $2, and so on
* Examples in just a moment

----

[ ]
=====

* Character class
* Match one of these things

----

.. image:: images/coat.png

----

Not
===

* Any regex can be negated in a RewriteRule or RewriteCond by putting a ! in front of it
* A character class is negated with a ^

::

    [^abc]

Matches anything EXCEPT a, b, c

----

RewriteRule

----

Syntax

----

Flags

----

Examples


----

Expressions

----

RewriteCond

----

RewriteMap

----

Avoiding

----

Finis

Email: rbowen@apache.org

Twitter: @rbowen

Slides: http://tm3.org/rewrite_ac2014


