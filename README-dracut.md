Full disk encryption with Yubikey (Yubico key) for dracut (for Opensuse 15.1)
=============================================================================

This enables you to automatically unlock a LUKS encrypted filesystem from
a `systemd`-enabled initramfs.

Requirements
------------

To compile and use Yubikey full disk encryption you need:

* libyubikey-devel
* libykpers-devel
* libiniparser-devel
* libarchive-devel
* libcryptsetup-devel
* python2-Markdown
* systemd-devel
* keyutils-devel

Additionally you will need to have `make` and `pkg-config` installed to
successfully compile, and `rpmbuild` to create rpm.

Build and install
-----------------

Building and installing is very easy. Just run:

> make

Distributions like Opensuse do have different names for `markdown` executable.
For Opensuse you have to run:

> make MD=markdown_py

Build command is followed by:

> make install-dracut

This will place the files in their desired places in the filesystem.
Keep in mind that you need `root` privileges for installation, so switch
user or prepend the last command with `sudo`.

Build RPM package (preferred)
-----------------------------

> mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

> wget https://github.com/mrsmith1337/mkinitcpio-ykfde/archive/master.zip -O ~/rpmbuild/SOURCES/mkinitcpio-ykfde-master.zip

> wget https://github.com/mrsmith1337/mkinitcpio-ykfde/raw/master/mkinitcpio-ykfde.spec -O ~/rpmbuild/SPECS/mkinitcpio-ykfde.spec

> rpmbuild -bb ~/rpmbuild/SPECS/mkinitcpio-ykfde.spec

Then install the rpm package from ~/rpmbuild/RPMS/.

Usage
-----

### config files `/etc/crypttab` and `/etc/ykfde.conf`

Make sure systemd knows about your encrypted device by
adding a line to `/etc/crypttab`. It should read like:

> `mapping-name` `UUID=<uuid>`

Usually there is already an entry for your device.

Update `/etc/ykfde.conf` with correct settings. Add the value of
`mapping-name` from above to `device name` in the `general` section. Then
add a new section with your key's decimal serial number containing the key
slot setting. The minimal file should look like this:

    [general]
    device name 1 = cryptroot

    [1234567]
    luks slot = 1

You can add up to four (4) device names if you have several crypted devices:

    ...
    device name 2 = crypthome
    device name 3 = cryptswap
    ...

*Be warned*: Do not remove or overwrite your interactive (regular) key!
Keep that for backup and rescue - LUKS encrypted volumes have a total
of 8 slots (from 0 to 7).

### Key setup

`ykfde` will read its information from these files and understands some
additional options. Run `ykfde --help` for details. Then prepare
the key. Plug it in and make sure it is configured for `HMAC-SHA1`. This can
be done with `ykman` from terminal (package `yubikey-manager`; To use
slot 2 for challenge-response try `ykman otp chalresp -g 2`).
After that, run:

> ykfde

This will store a challenge in `/etc/ykfde.d/` and add a new slot to
your LUKS device based on the `/etc/ykfde.conf` configuration. When
`ykfde` asks for a passphrase it requires a valid passphrase from a
previously available slot.

Alternatively, adding a key with second factor (`foo` in this example)
is as easy:

> ykfde --new-2nd-factor foo

To update the challenge run:

> ykfde --2nd-factor foo

And changing second factor (from `foo` to `bar` in this example) is
straight forward:

> ykfde --2nd-factor foo --new-2nd-factor bar

The current and new second factor can be read from terminal, increasing
security by not displaying on display and not writing to shell history.
Use switches `--ask-2nd-factor` and `--ask-new-2nd-factor` for that.

Make sure to enable second factor in `/etc/ykfde.conf`.

### cpio archive with challenges (for now, not supported, i.e. not needed on Opensuse)

Every time you update a challenge and/or a second factor run:

> ykfde-cpio

This will write a cpio archive to `/boot/ykfde-challenges.img` containing
your current challenges. Enable systemd service `ykfde` to do this
automatically on every boot:

> systemctl enable ykfde.service

### `dracut`

Build the initramfs:

> dracut -f

This should be done after all key setups/changes.

### Boot loader (for now, not supported, i.e. not needed on Opensuse)

Make sure to load the cpio archive `/boot/ykfde-challenges.img`
as an additional initramfs.

With `grub` you need to list `ykfde-challenges.img` in configuration
variable `GRUB_EARLY_INITRD_LINUX_CUSTOM` in `/etc/default/grub`:

> GRUB_EARLY_INITRD_LINUX_CUSTOM="ykfde-challenges.img"

Then update your `grub` configuration by running:

> grub-mkconfig -o /boot/grub/grub.cfg

Reboot and have fun!
