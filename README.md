# ansible-role-kali #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-kali/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-kali/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-kali.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-kali/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-kali.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-kali/context:python)

An Ansible role for installing the packages required in a CISA VM Kali
instance.

## Requirements ##

None.

## Role Variables ##

In addition to the variables defined in
[`defaults/main.yml`](defaults/main.yml) (for which the default values
should suffice) this role requires the following variables:

* `gitlab_token` - the Gitlab personal access token to use when
  accessing the `dns-profile-randomizer` private repository

## Dependencies ##

* [cisagov/ansible-role-pip](https://github.com/cisagov/ansible-role-pip)

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - kali
```

## Contributing ##

We welcome contributions!  Please see [here](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Kyle Evers - <kyle.evers@trio.dhs.gov>
