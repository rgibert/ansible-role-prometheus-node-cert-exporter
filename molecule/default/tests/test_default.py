import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_enabled(host):
    assert host.service('prometheus_node_cert_exporter').is_enabled


def test_service_running(host):
    assert host.service('prometheus_node_cert_exporter').is_running
