Name:           mkinitcpio-ykfde
Version:        0.7.7
Release:        lp151.1
Summary:        Full disk encryption with Yubikey
Group:          Productivity/Networking/Security
License:        GPLv3+
URL:            https://github.com/mrsmith1337/mkinitcpio-ykfde
Source0:        %{name}-%{version}.zip
Distribution:   openSUSE Leap 15.1

%description
Full disk encryption with Yubikey (Yubico key)
This allows to automatically unlock a LUKS encrypted hard disk from systemd-enabled initramfs.

%prep
%setup

%build
make MD=markdown_py

%install
make DESTDIR=%{buildroot} install-dracut

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
   /etc/ykfde.conf
   /etc/ykfde.d/.gitignore
   /usr/bin/ykfde
   /usr/bin/ykfde-cpio
   /usr/lib/dracut/modules.d/90ykfde/20-ykfde.rules
   /usr/lib/dracut/modules.d/90ykfde/module-setup.sh
   /usr/lib/dracut/modules.d/90ykfde/parse-mod.sh
   /usr/lib/dracut/modules.d/90ykfde/ykfde.sh
   /usr/lib/systemd/system/ykfde-2f.service
   /usr/lib/systemd/system/ykfde-worker.service
   /usr/lib/systemd/system/ykfde.service
   /usr/lib/ykfde/worker
   /usr/share/doc/ykfde/README-dracut.html
   /usr/share/doc/ykfde/README-dracut.md
   /usr/share/doc/ykfde/README-mkinitcpio.html
   /usr/share/doc/ykfde/README-mkinitcpio.md
   /usr/share/doc/ykfde/README.html
   /usr/share/doc/ykfde/README.md

%changelog

