import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_kpi_service(host):
    kpi = host.service("kpi")
    assert kpi.is_running
    assert kpi.is_enabled
