Ansible-kpi
=========

Use this role to install and configure KPI.

Role Dependencies
------------

- onaio.collectd
- onaio.monit
- onaio.postgresql
- ANXS.python
- onaio.nvm
- onaio.django
- Stouts.backup

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

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

License
-------

Apache 2

Author Information
------------------

[Ona Engineering](https://ona.io)
