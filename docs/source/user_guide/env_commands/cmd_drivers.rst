.. _cmd_drivers:

apio drivers
============

.. contents::

Usage
-----

.. code::

    apio drivers [OPTIONS]

Description
-----------

Enable/Disable the FTDI drivers.

* Linux: add a rules file. It may require a reboot.
* Mac OSX: configures FTDIUSBSerialDriver and AppleUSBFTDI keys.
* Windows: opens a web browser with a tutorial.

.. note::

  More information in :ref:`install_drivers`

Options
-------

.. program:: apio drivers

.. option::
    -e, --enable

Enable FPGA drivers

.. option::
    -d, --disable

Disable FPGA drivers

Examples
--------

1. Enable the FTDI drivers on Linux

.. code::

  $ apio drivers --enable
  Configure FTDI drivers for FPGA
  [sudo] password for user:
  FPGA drivers enabled

1. Disable the FTDI drivers on Linux

.. code::

  $ apio drivers --disable
  Revert FTDI drivers configuration
  [sudo] password for user:
  FPGA drivers disabled
