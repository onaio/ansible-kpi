Ansible-kpi
=========

[![Build Status](https://travis-ci.org/onaio/ansible-kpi.svg?branch=master)](https://travis-ci.org/onaio/ansible-kpi)

Use this role to install and configure KPI.

Role Dependencies
------------

- onaio.collectd
- onaio.monit
- ANXS.python
- onaio.nvm
- onaio.django

Role Variables
--------------

You can see all variables by looking at the `defaults/main.yml` file.

You can look at `tests/test.yml` for examples of how to use these variables.

Testing
-------

You can test the role locally using Molecule by following these steps:

```sh
pip install molecule docker-py
molecule test
```


License
-------

Apache 2

Author Information
------------------

[Ona Engineering](https://ona.io)
