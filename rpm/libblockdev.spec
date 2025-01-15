Name:        libblockdev
Version:     3.2.1
Release:     1
Summary:     A library for low-level manipulation with block devices
License:     LGPLv2+
URL:         https://github.com/storaged-project/libblockdev
Source0:     %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(libkmod)
BuildRequires: pkgconfig(libkeyutils)
BuildRequires: gettext-devel
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libfdisk-devel
BuildRequires: e2fsprogs-devel
Patch0001: 0001-Require-linux-kernel-4.10-for-LO_FLAG_DIRECT_IO.patch

%description
The libblockdev is a C library with GObject introspection support that can be
used for doing low-level operations with block devices like setting up LVM,
BTRFS, LUKS or MD RAID. The library uses plugins (LVM, BTRFS,...) and serves as
a thin wrapper around its plugins' functionality. All the plugins, however, can
be used as standalone libraries. One of the core principles of libblockdev is
that it is stateless from the storage configuration's perspective (e.g. it has
no information about VGs when creating an LV).

%package devel
Summary:     Development files for libblockdev
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel

%description devel
This package contains header files and pkg-config files needed for development
with the libblockdev library.

%package utils
Summary:     A library with utility functions for the libblockdev library
Requires: %{name} = %{version}-%{release}

%description utils
The libblockdev-utils is a library providing utility functions used by the
libblockdev library and its plugins.

%package utils-devel
Summary:     Development files for libblockdev-utils
Requires: %{name}-utils = %{version}-%{release}
Requires: glib2-devel

%description utils-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-utils library.

%package crypto
BuildRequires: pkgconfig(libcryptsetup) >= 1.4.0
BuildRequires: pkgconfig(nss)
Summary:     The crypto plugin for the libblockdev library

%description crypto
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to encrypted devices (LUKS).

%package crypto-devel
Summary:     Development files for the libblockdev-crypto plugin/library
Requires: %{name}-crypto = %{version}-%{release}
Requires: glib2-devel

%description crypto-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-crypto plugin/library.

%package fs
BuildRequires: libblkid-devel
BuildRequires: libmount-devel
Summary:     The FS plugin for the libblockdev library
Requires: %{name}-utils >= 0.11

%description fs
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to operations with file systems.

%package fs-devel
Summary:     Development files for the libblockdev-fs plugin/library
Requires: %{name}-fs = %{version}-%{release}
Requires: %{name}-utils-devel
Requires: glib2-devel

%description fs-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-fs plugin/library.

%package loop
Summary:     The loop plugin for the libblockdev library
Requires: %{name}-utils >= 0.11

%description loop
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to loop devices.

%package loop-devel
Summary:     Development files for the libblockdev-loop plugin/library
Requires: %{name}-loop = %{version}-%{release}
Requires: %{name}-utils-devel
Requires: glib2-devel

%description loop-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-loop plugin/library.

%package part
Summary:     The partitioning plugin for the libblockdev library
Requires: %{name}-utils >= 0.11
Requires: util-linux

%description part
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to partitioning.

%package part-devel
Summary:     Development files for the libblockdev-part plugin/library
Requires: %{name}-part = %{version}-%{release}
Requires: %{name}-utils-devel
Requires: glib2-devel

%description part-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-part plugin/library.

%package swap
Summary:     The swap plugin for the libblockdev library
Requires: %{name}-utils >= 0.11
Requires: util-linux

%description swap
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to swap devices.

%package swap-devel
Summary:     Development files for the libblockdev-swap plugin/library
Requires: %{name}-swap = %{version}-%{release}
Requires: %{name}-utils-devel
Requires: glib2-devel

%description swap-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-swap plugin/library.

%package plugins-all
Summary:     Meta-package that pulls all the libblockdev plugins as dependencies
Requires: %{name} = %{version}-%{release}

Requires: %{name}-crypto = %{version}-%{release}
Requires: %{name}-fs = %{version}-%{release}
Requires: %{name}-loop = %{version}-%{release}
Requires: %{name}-swap = %{version}-%{release}
Requires: %{name}-part = %{version}-%{release}

%description plugins-all
A meta-package that pulls all the libblockdev plugins as dependencies.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}


%build
%autogen

# Not disabled: crypto, loop, swap, fs, disable-introspection
%configure \
    --without-btrfs \
    --without-lvm \
    --without-lvm_dbus \
    --without-kbd \
    --without-mpath \
    --without-dm \
    --without-mdraid \
    --without-vdo \
    --without-nvdimm \
    --without-escrow \
    --without-tools \
    --without-smart \
    --without-smartmontools \
    --without-nvme \
    --with-python2=no \
    --with-python3=no \
    --with-gtk-doc=no \
    --enable-tests=no
%make_build

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post utils -p /sbin/ldconfig
%postun utils -p /sbin/ldconfig

%post crypto -p /sbin/ldconfig
%postun crypto -p /sbin/ldconfig

%post fs -p /sbin/ldconfig
%postun fs -p /sbin/ldconfig

%post loop -p /sbin/ldconfig
%postun loop -p /sbin/ldconfig

%post part -p /sbin/ldconfig
%postun part -p /sbin/ldconfig

%post swap -p /sbin/ldconfig
%postun swap -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/libblockdev.so.*
%{_libdir}/girepository*/BlockDev*.typelib
%dir %{_sysconfdir}/libblockdev
%dir %{_sysconfdir}/libblockdev/3/conf.d
%config %{_sysconfdir}/libblockdev/3/conf.d/00-default.cfg

%files devel
%{_libdir}/libblockdev.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/blockdev.h
%{_includedir}/blockdev/plugins.h
%{_libdir}/pkgconfig/blockdev.pc
%{_datadir}/gir*/BlockDev*.gir

%files utils
%{_libdir}/libbd_utils.so.*

%files utils-devel
%{_libdir}/libbd_utils.so
%{_libdir}/pkgconfig/blockdev-utils.pc
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/utils.h
%{_includedir}/blockdev/sizes.h
%{_includedir}/blockdev/exec.h
%{_includedir}/blockdev/extra_arg.h
%{_includedir}/blockdev/dev_utils.h
%{_includedir}/blockdev/module.h
%{_includedir}/blockdev/dbus.h
%{_includedir}/blockdev/logging.h

%files crypto
%{_libdir}/libbd_crypto.so.*

%files crypto-devel
%{_libdir}/libbd_crypto.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/crypto.h

%files fs
%{_libdir}/libbd_fs.so.*

%files fs-devel
%{_libdir}/libbd_fs.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/fs.h
%{_includedir}/blockdev/fs/*.h

%files loop
%{_libdir}/libbd_loop.so.*

%files loop-devel
%{_libdir}/libbd_loop.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/loop.h

%files part
%{_libdir}/libbd_part.so.*

%files part-devel
%{_libdir}/libbd_part.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/part.h

%files swap
%{_libdir}/libbd_swap.so.*

%files swap-devel
%{_libdir}/libbd_swap.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/swap.h

%files plugins-all
