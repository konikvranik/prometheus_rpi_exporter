#!/usr/bin/env python

from distutils.core import setup

setup(name='Prometheus RPi exporter',
      version='1.0',
      description='Prometheus exporter for RPi runtime statistics such as CPU temperature.',
      author='Petr Vraník',
      author_email='petr@vranik.name',
      url='https://github.com/konikvranik/prometheus_rpi_exporter',
      scripts=['prometheus-rpi-exporter.py'],
      data_files=[('/etc/systemd/system', ['rpi_exporter.service'])]
     )
