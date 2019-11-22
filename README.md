# Single Binary Service

![Ansible Role](https://img.shields.io/ansible/role/44838?style=flat-square)
![Molecule Test Status](https://img.shields.io/travis/rgibert/ansible-role-prometheus-node-cert-exporter?label=molecule&style=flat-square)
![Ansible Quality Score](https://img.shields.io/ansible/quality/44838?style=flat-square)
![Ansible Role](https://img.shields.io/ansible/role/d/44838?label=downloads&style=flat-square)

## Description

Ansible role to install a Prometheus certificate file exporter

## Requirements

- RHEL-based or Debian-based OS

## Role Variables

| Variable | Description |
|----------|-------------|
| prometheus_node_cert_exporter_base_url | Base URL for download package |
| prometheus_node_cert_exporter_dl_url | Download URL |
| prometheus_node_cert_exporter_group | Primary group for the exporter user | 
| prometheus_node_cert_exporter_user | User to run the exporter as |
| prometheus_node_cert_exporter_version | Version of the exporter to run |
| prometheus_node_cert_exporter_paths | List of paths to watch |

## Dependencies

- rgibert.user_setup:1.2.0
- rgibert.single_binary_service:1.2.1

## Example Playbook

```yaml
- hosts:
    - servers
  roles:
    - role: rgibert.prometheus_node_cert_exporter
```

## License

GPLv3

## Author Information

Richard Gibert  
[richard@gibert.ca](mailto:richard@gibert.ca)  
[https://richard.gibert.ca/](https://richard.gibert.ca/)
