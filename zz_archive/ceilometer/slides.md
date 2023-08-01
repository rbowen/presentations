# OpenStack metering and alarming with Ceilometer 

Rich Bowen, OpenStack Community Liaison

Red Hat

rbowen@redhat.com

---

## Whoami

* OpenStack community guy at Red Hat - http://openstack.redhat.com/
* Board member and EVP at the Apache Software Foundation - http://apache.org/
![rbowen](images/rbowen_linuxcon_japan_keynote_small.jpg)

---

## Ceilometer

Measures the height of clouds

![Ceilometer](images/ceilometer.jpg)

---

## Why?

![dollar](images/dollar.jpg)

* Billing
* Capacity planning
* Alarms

Note:

Elastic is great, but if you don't know how far it's being
stretched, you'll find out the hard way when it snaps.

Infinite resources is a nice illusion, but an illusion all the same.

Alarms trigger when a threshold is reached, and can take action
based on that event.

---

## Mission

* Prior to Ceilometer, every component did its own metrics reporting (Or not)
* Ceilometer is a centralized metrics hub that everything can sent metrics to
* Not everything takes full advantage of it yet

---

## Mission statement

<blockquote>
The Ceilometer project aims to deliver a unique point of contact for
billing systems to acquire all of the measurements they need to
establish customer billing, across all current OpenStack core components
with work underway to support future OpenStack components.
</blockquote>

---

## What does it do?

* Provide efficient collection of metering data, in terms of CPU and network costs.
* Allow deployers to integrate with the metering system directly or by replacing components.
* Data may be collected by monitoring notifications sent from existing services or by polling the infrastructure.
* Allow deployers to configure the type of data collected to meet their operating requirements.
* The data collected by the metering system is made visible to some users through a REST API.
* The metering messages are signed and non-repudiable.

---

## Definitions

Metering:
    Measure and record what's happening

Monitoring:
    Notify ("alarm") when one of the meters reaches a threshold

---

## Monitoring

* Ceilometer **meters** whether you ask it to or not
* You can query it (monitor) later when you realize you need it

---

## Architecture

![arch](images/arch.png)

---

## Collection methods

* Bus listener agent
* Push agent
* Polling agents

    <p>From most to least preferred</p>

Note:

Bus listener agent which takes events generated on the Oslo notification bus and transforms them into Ceilometer sample. Again this is the preferred method of data collection. If you are working on some OpenStack related project and are using the Oslo library, you are kindly invited to come and talk to one of the project members to learn how you could quickly add instrumentation for your project.

Push agents which is the only solution to fetch data within projects which do not expose the required data in a remotely usable way. This is not the preferred method as it makes deployment a bit more complex having to add a component to each of the nodes that need to be monitored. However, we do prefer this compared to a polling agent method as resilience (high availability) will not be a problem with this method.

Polling agents which is the least preferred method, that will poll some API or other tool to collect information at a regular interval. The main reason why we do not like this method is the inherent difficulty to make such a component be resilient.

---

## Installation

* Ceilometer is part of what gets installed by most OpenStack deployment tools
* Devstack also installs and enables ceilometer
* http://docs.openstack.org/developer/ceilometer/install/manual.html

Note:

Don't really have time to go through manual installation. It's on
the wiki.

---

## RDO

![RDO](images/RDO_icon.jpg)

* Easy deployment of OpenStack on Fedora/RHEL/CentOS
* http://openstack.redhat.com/Quickstart

        sudo yum install -y http://rdo.fedorapeople.org/rdo-release.rpm
        sudo yum install -y openstack-packstack
        packstack --allinone

Note:

This is not a product pitch. RDO is a community project
sponsored by Red Hat, but isn't a product.

---

## Configuration - collection speed

* For demo/testing purposes, speed up collecting - default is every ten minutes.
* If you're mailing interested in billing, every 10 or 30 minutes may be sufficient
* If you want to actively monitor other things, you might want it shorter.
* In /etc/ceilometer/pipeline.yaml

        < interval: 600
        > interval: 60

---

## Configuration

* Full configuration options at http://docs.openstack.org/developer/ceilometer/configuration.html

---

## Database

* http://docs.openstack.org/developer/ceilometer/install/dbreco.html

![db](images/ceilometer_database.png)

* MongoDB default, due to limitations of other databases, and because
  it's more widely tested

* The database schema is not guaranteed, so you should use the API to
  access data, whenever possible.

---

## Database

* If you prefer another database, such as MySQL or Pgsql ...
* Create the database
* Initialize it using `ceilometer-dbsync`
* Point `ceilometer.conf` at it:

        [database]
        connection = mysql://username:password@host/ceilometer?charset=utf8

---

## API

* "... Ceilometer should be able to share collected data with a variety of consumers."
* This is done via the HTTP API
* http://docs.openstack.org/developer/ceilometer/webapi/v2.html

---

## Auth

* Before you can do anything, you need an auth token

        curl -i 'http://192.168.0.177:5000/v2.0/tokens'
        -X POST -H "Content-Type: application/json"
        -H "Accept: application/json"
        -d '{"auth": {"tenantName": "admin", 
             "passwordCredentials": {"username":
             "admin", "password": "885d4b669cc04a1b"}}}'

* Returns a token that you can then use for other API calls
* This is standard across all OpenStack components
* Auth token expires (by default) after 24 hours

---

## API

* HTTP requests to port 8777
* Requires auth token you got from Keystone
* GET for read, POST for write

---

## Meters

        curl -H 'X-Auth-Token: <inserttokenhere>' \
          "http://localhost:8777/v2/meters"

* Returns a list of all of the meters that have ever been tracked on this install
* Note: Sample expiry is not enabled by default, so you keep everything forever

---

## Example result 

        [
          {
            "user_id": null,
            "name": "storage.objects",
            "resource_id": "2477d5ce0cfc4cc796635dacef13a7ec",
            "source": "openstack",
            "meter_id": "MjQ3N2Q1Y2UwY2ZjNGNjNzk2NjM1ZGFjZWYxM2E3ZWMrc3RvcmFnZS5vYmplY3Rz\n",
            "project_id": "2477d5ce0cfc4cc796635dacef13a7ec",
            "type": "gauge",
            "unit": "object"
          },
          {
            "user_id": null,
            "name": "storage.objects.size",
            "resource_id": "2477d5ce0cfc4cc796635dacef13a7ec",
            "source": "openstack",
            "meter_id": "MjQ3N2Q1Y2UwY2ZjNGNjNzk2NjM1ZGFjZWYxM2E3ZWMrc3RvcmFnZS5vYmplY3RzLnNpemU=\n",
            "project_id": "2477d5ce0cfc4cc796635dacef13a7ec",
            "type": "gauge",
            "unit": "B"
          },
          {
            "user_id": null,
            "name": "storage.objects.containers",
            "resource_id": "2477d5ce0cfc4cc796635dacef13a7ec",
            "source": "openstack",
            "meter_id": "MjQ3N2Q1Y2UwY2ZjNGNjNzk2NjM1ZGFjZWYxM2E3ZWMrc3RvcmFnZS5vYmplY3RzLmNvbnRhaW5l\ncnM=\n",
            "project_id": "2477d5ce0cfc4cc796635dacef13a7ec",
            "type": "gauge",
            "unit": "container"
          },

          ...

Note:

JSON, not nicely formatted like that.

---

## Or, from the cli, for human-readable

![meter](images/meter-list.png)

---

## Ceilometer CLI

      <subcommand>

        ... alarm stuff snipped until later ...

        meter-list          List the user's meters.
        resource-list       List the resources.
        resource-show       Show the resource.
        sample-create       Create a sample.
        sample-list         List the samples for this meters.
        statistics          List the statistics for this meter.
        help                Display help about this program or one of its
                                subcommands.

---

## CLI auth

* Uses command line switches to handle auth, 

      --os-username OS_USERNAME
                        Defaults to env[OS_USERNAME]
      --os-password OS_PASSWORD
                        Defaults to env[OS_PASSWORD]
      --os-tenant-id OS_TENANT_ID
                        Defaults to env[OS_TENANT_ID]
      --os-tenant-name OS_TENANT_NAME
                        Defaults to env[OS_TENANT_NAME]
      --os-auth-url OS_AUTH_URL
                        Defaults to env[OS_AUTH_URL]

---

## CLI auth

* ... or env vars.

        export OS_USERNAME=admin
        export OS_TENANT_NAME=admin
        export OS_PASSWORD=381fc546d189474a
        export OS_AUTH_URL=http://192.168.0.176:5000/v2.0/
        export PS1='[\u@\h \W(keystone_admin)]\$ '

    source ~/keystonerc_admin

---

## Meter by name

* Note that names aren't unique.
* The meter resourceID and projectID are a unique pair

---

## Meters ...

    +-------------+-------+-----------+--------------------------------------+--------------+----------------------------------+
    | Name        | Type  | Unit      | Resource ID                          | User ID      | Project ID                       |
    +-------------+-------+-----------+--------------------------------------+--------------+----------------------------------+
    | image       | gauge | image     | 1fa61a12-c989-4b23-bd5f-a158475daea6 | None         | 6fb06ac9d9b24ed6bf7705fa31b4c3a4 |
    | image       | gauge | image     | 8fb29395-c054-4d2d-9064-7a440b817d4d | None         | f484a01f83634a54ad06ac7b5b51a964 |
    | image       | gauge | image     | 9845726d-10fd-4b47-911e-38e167432406 | None         | 9c487ce650d4456687599cd7add7f6a9 |

---

## Type

Each meter has a type:

* `Cumulative`:
    Increasing over time (instance hours, cpu usage)
* `Gauge`:
    Discrete items (floating IPs, image uploads) 
    and fluctuating values (disk I/O)
* `Delta`:
    Changing over time (eg change in number of routers)

---

## Unit

* Gauge meters will typically be in something discreet - subnet, router, image, network
* Other meters will have a measured unit such as kb, ms, and so on

---

## Meters have samples
        
    # ceilometer sample-list -m cpu
    +--------------------------------------+------+------------+---------------+------+---------------------+
    | Resource ID                          | Name | Type       | Volume        | Unit | Timestamp           |
    +--------------------------------------+------+------------+---------------+------+---------------------+
    | a940742a-e5ea-4ca5-8b72-3d69a40bb90f | cpu  | cumulative | 71250000000.0 | ns   | 2014-01-22T16:00:05 |
    | a940742a-e5ea-4ca5-8b72-3d69a40bb90f | cpu  | cumulative | 65300000000.0 | ns   | 2014-01-22T15:59:05 |
    | a940742a-e5ea-4ca5-8b72-3d69a40bb90f | cpu  | cumulative | 59390000000.0 | ns   | 2014-01-22T15:58:05 |
    | a940742a-e5ea-4ca5-8b72-3d69a40bb90f | cpu  | cumulative | 52990000000.0 | ns   | 2014-01-22T15:57:06 |
    +--------------------------------------+------+------------+---------------+------+---------------------+

---

## Filtered by timestamp

     $ ceilometer sample-list --meter cpu -q \
    'resource_id=INSTANCE_ID_1;timestamp>2013-10-01T09:00:00;timestamp<=2013-10-01T09:30:00'
     +---------------+------+------------+---------------+------+---------------------+
     | Resource ID   | Name | Type       | Volume        | Unit | Timestamp           |
     +---------------+------+------------+---------------+------+---------------------+
     | INSTANCE_ID_1 | cpu  | cumulative | 1.7234e+11    | ns   | 2013-10-01T09:08:28 |
     | INSTANCE_ID_1 | cpu  | cumulative | 1.743e+11     | ns   | 2013-10-01T09:18:28 |
     | INSTANCE_ID_1 | cpu  | cumulative | 1.7626e+11    | ns   | 2013-10-01T09:28:28 |
     +---------------+------+------------+---------------+------+---------------------+

---

## Statistics

* Aggregate stats on any meter
* The statistics API lets you do all sorts of filtering

---

## All stats, for all time

    $ ceilometer statistics --meter cpu_util
     +--------+--------------+------------+-------+------+-----+-----+-----+----------+----------------+----
     | Period | Period Start | Period End | Count | Min  | Max | Sum | Avg | Duration | Duration Start | ...
     +--------+--------------+------------+-------+------+-----+-----+-----+----------+----------------+----
     | 0      | PERIOD_START | PERIOD_END | 2024  | 0.25 | 6.2 | 550 | 2.9 | 85196.0  | DURATION_START | ...
     +--------+--------------+------------+-------+------+-----+-----+-----+----------+----------------+----

---

## Filtered by time, every 60 seconds

     $ ceilometer --debug statistics -m cpu_util -q 'timestamp>START;timestamp<=END' --period 60
     +--------+--------------+------------+-------+-----+-----+-----+-----+----------+----------------+----
     | Period | Period Start | Period End | Count | Min | Max | Sum | Avg | Duration | Duration Start | ...
     +--------+--------------+------------+-------+-----+-----+-----+-----+----------+----------------+----
     | 60     | START        | START+60   | 2     | 1.5 | 2.5 | 4.0 | 2.0 | 0.0      | DURATION_START | ...
     | 60     | START+60     | START+120  | 2     | 2.5 | 3.5 | 6.0 | 3.0 | 0.0      | DURATION_START | ...
     | ...[snip]
     +--------+--------------+------------+-------+-----+-----+-----+-----+----------+----------------+----

---

## Across the entire period (eg, for billing)

    # ceilometer statistics -m cpu -q \
      "timestamp>2014-01-22T16:05:00;timestamp<2014-01-22T17:05:00"

Output is intended to be human-readable rather than machine readable, so the API may be better suited to automated reporting.

---

results:

    +--------+---------------------+---------------------+-------+----------------+----------------+--------------+----------------+----------+
    | Period | Period Start        | Period End          | Count | Min            | Max            | Sum          | Avg            | Duration |
    +--------+---------------------+---------------------+-------+----------------+----------------+--------------+----------------+----------+
    | 0      | 2014-01-22T17:04:05 | 2014-01-22T17:04:05 | 60    | 101730000000.0 | 467430000000.0 | 1.700835e+13 | 283472500000.0 | 3540.0   |
    +--------+---------------------+---------------------+-------+----------------+----------------+--------------+----------------+----------+

---

## From the API:

CPU utilization on a particular resource in June.

    GET /v2/meters/cpu_util/statistics
    q: [{"field": "timestamp",
        "op": "ge",
        "value": "2013-06-01T00:00:00"},
        {"field": "timestamp",
        "op": "lt",
        "value": "2013-07-01T00:00:00"},
        {"field": "resource_id",
        "op": "eq",
     "value": "64da755c-9120-4236-bee1-54acafe24980"}]

---

## Syntax

If you're not familiar with the syntax:

            GET /v2/meters/cpu_util/statistics
            q: [{"field": "timestamp",
               "op": "ge",
               "value": "2013-06-01T00:00:00"},
               {"field": "timestamp",
               "op": "lt",
               "value": "2013-07-01T00:00:00"},
               {"field": "resource_id",
               "op": "eq",
               "value": "64da755c-9120-4236-bee1-54acafe24980"}]
            period: 600

* 'q' vars passed as, eg, 'q.op' and 'q.value' in the query string
* 'period' is passed as 'period' in the qs.

---

So, a URL might look like:

            http://192.168.0.177:8777/v2/meters/memory/statistics
                ?q.field=resource_id&q.op=eq&q.value=
                36907e0e-0beb-46d8-854f-eb91c886a6dc
                &q.field=timestamp&q.op=ge
                &q.value=2011-06-01T00:00:00
                &q.field=timestamp&q.op=lt
                &q.value=2014-07-01T00:00:00
                &period=600

* This is the Python WSME (Web Services Made Easy) format, not unique to Ceilometer

---

## Stats output

Output will vary depending on what you're querying:

            'duration_start' => '2013-11-19T20:43:50.013000',
            'duration_end' => '2013-11-25T17:10:40.135000'
            'duration' => '505610.122',
            'period_start' => '2013-11-19T20:43:50.013000',
            'period_end' => '2013-11-19T20:43:50.013000',
            'period' => 0,
            'groupby' => undef,
            'unit' => 'MB',
            'count' => 8,
            'sum' => '4096',
            'avg' => '512',
            'min' => '512',
            'max' => '512',

---

## Billing

* Ceilometer can give you stats grouped by project
* ... or by resource
* so that you can bill a particular customer by utilization

---

## Alarms

![alarm](images/alarm.jpg)

* Notify when a given metric crosses a threshold
* Another relevant presentation at http://tm3.org/alarming
* Can send alarm to log, or can POST to a HTTP URL for actions

Note:

Capacity planning vs point in time monitoring

You'll need to think ahead about what you want to be notified about,
of course, since you only get notified about things that you set
alarms for. ie, you don't know you need it
until you need it that first time.

---

## Alarms

* Set alarms with the `ceilometer alarm-threshold-create` command

---

* For example:

       ceilometer alarm-threshold-create \
        --name high_cpu_alarm \
        --description 'instance running hot'  \
        --meter-name cpu_util  --threshold 75.00 \
        --comparison-operator gt  --statistic avg \
        --period 60 --evaluation-periods 1 \
        --alarm-action 'log://' \
        --query resource_id=$INSTANCE_ID

---

## Trigger

        --meter-name cpu_util  --threshold 75.00 \
        --comparison-operator gt  --statistic avg \
        --period 60 --evaluation-periods 1 \

* This is when you want to be notified
* operators are the usual (gt, lt, eq, and so on)
* --statistic is count, avg, max, min, or sum

---

Then ...

    [root@localhost ~(keystone_admin)]# ceilometer alarm-list
    +--------------------------------------+----------------+-------------------+---------+------------+-------------------------------+
    | Alarm ID                             | Name           | State             | Enabled | Continuous | Alarm condition               |
    +--------------------------------------+----------------+-------------------+---------+------------+-------------------------------+
    | bea23f44-16e0-4faf-9d85-e04d8c3bc13d | high_cpu_alarm | insufficient data | True    | False      | cpu_util > 5.0 during 1 x 60s |
    +--------------------------------------+----------------+-------------------+---------+------------+-------------------------------+

---

## Then

    # tail /var/log/ceilometer/alarm-notifier.log

    ... time passes ...

    2014-01-22 13:29:15.989 16226 INFO 
    ceilometer.alarm.notifier.log
    [req-ecbc19b0-d9bb-4f6e-9a2a-5e3a519f112c None None] 
    Notifying alarm bea23f44-16e0-4faf-9d85-e04d8c3bc13d
    from insufficient data to alarm with action 
    SplitResult(scheme=u'log', netloc=u'', path=u'', 
    query='', fragment='') because Transition to alarm
    due to 1 samples outside threshold, most recent: 10.2

---

## Actions

* Can be either `log://` to write to a log file
* Or point to an http action, which is given a JSON representation of
  the alert event.

    --alarm-action 'http://localhost/alarm.php'

---

## POST body

    body: {"current": "alarm", 
        "alarm_id": "91d7dae0-6d20-4c84-b9f7-a46bc71942bc", 
        "reason": "Transition to alarm due to 1 samples outside threshold, most recent: 1.0",
        "reason_data": 
            {"count": 1, 
            "most_recent": 1.0, 
            "type": "threshold", 
            "disposition": "outside"}, 
        "previous": "insufficient data"}

---

## Heat

* For example, an alarm might be sent to Heat, the orchestration engine
* Heat can create a new instance when load reaches a certain maximum ...
* and reap instances when it dips below a minimum

---

## Other alarming stuff

    ceilometer --help

      <subcommand>
        alarm-combination-create
                            Create a new alarm based on state of other alarms.
        alarm-combination-update
                            Update an existing alarm based on state of other
                            alarms.
        alarm-create        Create a new alarm (Deprecated).
        alarm-delete        Delete an alarm.
        alarm-history       Display the change history of an alarm.
        alarm-list          List the user's alarms.
        alarm-show          Show an alarm.
        alarm-state-get     Get the state of an alarm.
        alarm-state-set     Set the state of an alarm.
        alarm-threshold-create
                            Create a new alarm based on computed statistics.
        alarm-threshold-update
                            Update an existing alarm based on computed statistics.
        alarm-update        Update an existing alarm.

---

## In Juno

* Ceilometer summit at the OpenStack Summit in Atlanta
* Lots of new stuff on the list for Juno

---

## Raising the bar

* The bar is now higher for projects to graduate from Incubation
* All existing projects also need to meet that bar

---

## Mission

* New mission statement will reflect broader new mission in metering and measurement
* Debate of metering vs monitoring is ongoing

---

## SQL Alchemy driver support

* MongoDB has been focus of development
* Performance issues around SQL Alchemy have prevented it being part of
  the test suite
* Much improvement in the last few weeks to resolve this problem, and
  make SQL Alchemy a first class storage engine

---

## Documentation improvements

* Currently very developer-centric
* User/Admin documentation being added
* Starting from howtos posted on the RDO site

---

## Upgrade testing

* Better participation in upgrade testing
* Javeline/Grenade testing harness to verify upgrade
* Verify time ranges that span an upgrade

---

## Metadata

* Improve the way that metadata snapshotting is done
* Better performance by doing a time series and only capturing the
  deltas

---

## Project governance

* Moving to a more collaborative model rather than top-down decisions
* Tighter rules around major changes and new features - prevent
  last-minute scrambles and extension requests

---

## SNMP

* Adding support for SNMP monitoring, to expand range of things that can
  be monitored and responded to

---

## Other

* Complex queries for statistics
* Per-tenant reporting
* Efficiency improvements for common "sliding window" types of queries

Note:

* Advancing overlapping time window, like "last 7 days" where most of
  the data is the same as the last time we did this query

---

## More Info

* \#openstack-ceilometer (freenode)
* \#heat (freenode)
* openstack-dev@lists.openstack.org
* https://wiki.openstack.org/wiki/Ceilometer/Alerting

---

<p>Thank you</p>

- http://openstack.redhat.com/
- Twitter - @RDOCommunity
- rbowen@redhat.com

