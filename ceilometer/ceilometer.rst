:title: If it's not metered, it's not cloud
:data-transition-duration: 500
:css: css/hovercraft.css

If it's not metered, it's not cloud

----

If it's not metered, it's not cloud
===================================

Rich Bowen - rbowen@redhat.com

@rbowen

@rdocommunity

----

Ceilometer
==========

Measures the height of the clouds.

.. image:: images/ceilometer.jpg

----

Ceilometer
==========

* https://wiki.openstack.org/wiki/Ceilometer
* Metrics/Metering of your OpenStack cloud
* Because billing is important

----

History
=======

* Initial OpenStack mission didn't contain billing
* Everybody did their own thing
* Each component collected metrics (or not) as it liked
* Ceilometer was envisioned as a centralized metrics hub

----

Mission
=======

The project aims to become the infrastructure to collect measurements
within OpenStack so that no two agents would need to be written to
collect the same data. Its primary targets are monitoring and metering,
but the framework should be easily expandable to collect for other
needs. To that effect, Ceilometer should be able to share collected data
with a variety of consumers.

----

Definitions
===========

Metering:
    Measure and record what's happening

Monitoring:
    Notify ("alarm") when one of the meters reaches a threshold

----

API
===

* "... Ceilometer should be able to share collected data with a variety of consumers."
* This is done via the HTTP API
* http://docs.openstack.org/developer/ceilometer/webapi/v2.html

----

Installation
============

* Ceilometer is part of what gets installed by RDO
* Devstack also installs and enables ceilometer

----

RDO
===

* Easy deployment of OpenStack on Fedora/RHEL/CentOS
* http://openstack.redhat.com/Quickstart

    sudo yum install -y http://rdo.fedorapeople.org/rdo-release.rpm
    sudo yum install -y openstack-packstack
    packstack --allinone

----

Configuration
=============

* Speed up collecting - default is every ten minutes.
* In /etc/ceilometer/pipeline.yaml

    < interval: 600
    > interval: 60

----

Alarms
======

* Not what this presentation is about
* Notify when a given metric crosses a threshold
* We will come back to this at the end if there's time




