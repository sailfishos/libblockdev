Name:        libblockdev
Version:     2.26
Release:     1
Summary:     A library for low-level manipulation with block devices
License:     LGPLv2+
URL:         https://github.com/storaged-project/libblockdev
Source0:     %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(libkmod)
BuildRequires: gettext-devel
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libfdisk-devel
# i=1; for j in 00*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
Patch0001: 0001-utils-Allow-passing-NULL-for-error.patch
Patch0002: 0002-Implement-create_table-and-delete_part-using-libfdis.patch
Patch0003: 0003-Rewrite-bd_part_get_disk_spec-and-bd_part_set_disk_f.patch
Patch0004: 0004-Rewrite-bd_part_set_part_name-using-libfdisk.patch
Patch0005: 0005-Use-libfdisk-to-set-GPT-flags-instead-of-sgdisk.patch
Patch0006: 0006-Use-libfdisk-to-get-GPT-partition-flags-and-GUID.patch
Patch0007: 0007-Use-libfdisk-to-set-partition-type-id-instead-of-sfd.patch
Patch0008: 0008-Add-a-static-function-to-get-partition-number-from-n.patch
Patch0009: 0009-Use-libfdisk-to-get-partition-ID-instead-of-sfdisk.patch
Patch0010: 0010-Implement-bd_part_get_type_str-without-libparted.patch
Patch0011: 0011-Use-libfdisk-to-set-parted-flags-in-bd_part_set_flag.patch
Patch0012: 0012-Use-libfdisk-to-set-parted-flags-in-bd_part_set_flag.patch
Patch0013: 0013-Use-libfdisk-to-get-partition-spec.patch
Patch0014: 0014-Do-not-overwrite-errors-from-get_part_num.patch
Patch0015: 0015-Use-libfdisk-to-get-disk-partitions-and-free-regions.patch
Patch0016: 0016-Use-libfdisk-to-get-partition-by-its-position.patch
Patch0017: 0017-Do-not-remove-all-flags-in-bd_part_set_part_flags-on.patch
Patch0018: 0018-Manually-add-metadata-partitions-to-the-list-of-part.patch
Patch0019: 0019-Redirect-libfdisk-log-messages-to-our-log.patch
Patch0020: 0020-Use-libfdisk-to-create-new-partitions.patch
Patch0021: 0021-Call-fdisk_reread_changes-after-adding-removing-part.patch
Patch0022: 0022-Use-libfdisk-for-partition-resizing.patch
Patch0023: 0023-Remove-remaining-parted-functions-from-the-part-plug.patch
Patch0024: 0024-part-Take-exclusive-lock-instead-of-shared-before-wr.patch
Patch0025: 0025-Re-read-entire-partition-table-after-adding-extended.patch
Patch0026: 0026-part-Fix-few-typos-in-comments-and-docstrings.patch
Patch0027: 0027-part-Remove-libparted-information-from-the-plugin-do.patch
Patch0028: 0028-part-Fix-return-value-of-get_max_part_size-for-ungro.patch
Patch0029: 0029-part-When-resizing-allow-growing-up-to-4-MiB-above-m.patch
Patch0030: 0030-part-Fix-elements-leak-in-bd_part_get_part_by_pos.patch
Patch0031: 0031-Add-separate-tool-for-VFAT-filesystem-resize-and-use.patch


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
%dir %{_sysconfdir}/libblockdev/conf.d
%config %{_sysconfdir}/libblockdev/conf.d/00-default.cfg

%files devel
%doc features.rst specs.rst
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
%{_includedir}/blockdev/fs/ext.h
%{_includedir}/blockdev/fs/generic.h
%{_includedir}/blockdev/fs/mount.h
%{_includedir}/blockdev/fs/ntfs.h
%{_includedir}/blockdev/fs/vfat.h
%{_includedir}/blockdev/fs/xfs.h


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
