#!/bin/sh
hovercraft ceilometer.rst build

# scp -r build/* people.apache.org:public_html/presentations/new_in_24
scp -r build/* sycamore.rcbowen.com:/var/www/vhosts/www.rcbowen.com/speaks/slides/ceilometer

