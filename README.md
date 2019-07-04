mkinitcpio-ykfde
================

**Full disk encryption with Yubikey (Yubico key)**

This allows to automatically unlock a LUKS encrypted hard disk from `systemd`-
enabled initramfs.

This fork adds support for Opensuse (tested with Opensuse Leap 15.1).

Requirements, building, installing and usage
--------------------------------------------

Most of this is generic, but it still differs in detail for
distributions. Please look at what matches best for you.

* [dracut based initramfs (Opensuse, Fedora, ...)](README-dracut.md)
* [mkinitcpio based initramfs (Arch Linux, ...)](README-mkinitcpio.md)

Limitation / TODO
-----------------

Maximum of four encrypted devices supported for now.

### Upstream

URL:
[GitHub.com](https://github.com/eworm-de/mkinitcpio-ykfde#mkinitcpio-ykfde)

Mirror:
[eworm.de](https://git.eworm.de/cgit.cgi/mkinitcpio-ykfde/)
[GitLab.com](https://gitlab.com/eworm-de/mkinitcpio-ykfde#mkinitcpio-ykfde)
