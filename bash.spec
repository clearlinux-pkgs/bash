#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB5869F064EA74AB (chet@cwru.edu)
#
Name     : bash
Version  : 5.1
Release  : 57
URL      : https://mirrors.kernel.org/gnu/bash/bash-5.1.tar.gz
Source0  : https://mirrors.kernel.org/gnu/bash/bash-5.1.tar.gz
Source1  : https://mirrors.kernel.org/gnu/bash/bash-5.1.tar.gz.sig
Summary  : The GNU Bourne Again shell
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: bash-bin = %{version}-%{release}
Requires: bash-info = %{version}-%{release}
Requires: bash-license = %{version}-%{release}
Requires: bash-locales = %{version}-%{release}
Requires: bash-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : ncurses-dev
Patch1: bash51-001.patch
Patch2: bash51-002.patch
Patch3: bash51-003.patch
Patch4: bash51-004.patch
Patch5: bash51-005.patch
Patch6: bash51-006.patch
Patch7: bash51-007.patch
Patch8: bash51-008.patch
Patch9: bash51-009.patch
Patch10: bash51-010.patch
Patch11: bash51-011.patch
Patch12: bash51-012.patch
Patch13: nodlopen.patch
Patch14: stateless.patch
Patch15: 0001-Support-stateless-inputrc-configuration.patch
Patch16: 0002-Add-a-few-missing-prerequisites-to-fix-parallel-buil.patch

%description
This is an sh-compatible shell that incorporates useful features from the Korn
shell (ksh) and the C shell (csh). It is intended to conform to the IEEE POSIX
P1003.2/ISO 9945.2 Shell and Tools standard. It offers functional improvements
over sh for both programming and interactive use. In addition, most sh scripts
can be run by Bash without modification.

%package bin
Summary: bin components for the bash package.
Group: Binaries
Requires: bash-license = %{version}-%{release}

%description bin
bin components for the bash package.


%package doc
Summary: doc components for the bash package.
Group: Documentation
Requires: bash-man = %{version}-%{release}
Requires: bash-info = %{version}-%{release}

%description doc
doc components for the bash package.


%package extras
Summary: extras components for the bash package.
Group: Default

%description extras
extras components for the bash package.


%package info
Summary: info components for the bash package.
Group: Default

%description info
info components for the bash package.


%package license
Summary: license components for the bash package.
Group: Default

%description license
license components for the bash package.


%package locales
Summary: locales components for the bash package.
Group: Default

%description locales
locales components for the bash package.


%package man
Summary: man components for the bash package.
Group: Default

%description man
man components for the bash package.


%prep
%setup -q -n bash-5.1
cd %{_builddir}/bash-5.1
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p0
%patch12 -p0
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639684519
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static --enable-cond-command \
--enable-history \
--enable-job-control \
--enable-readline \
--enable-extended-glob \
--enable-progcomp \
--enable-arith-for-command \
--enable-directory-stack \
--with-bash-malloc=no
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check

%install
export SOURCE_DATE_EPOCH=1639684519
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bash
cp %{_builddir}/bash-5.1/COPYING %{buildroot}/usr/share/package-licenses/bash/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/bash-5.1/lib/readline/COPYING %{buildroot}/usr/share/package-licenses/bash/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/bash-5.1/tests/COPYRIGHT %{buildroot}/usr/share/package-licenses/bash/771f6b3c33dd1c00e5d2f319cb801d0611ddd699
%make_install
%find_lang bash
## install_append content
ln -s bash %{buildroot}/usr/bin/sh
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bash
/usr/bin/sh

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/bash/*

%files extras
%defattr(-,root,root,-)
/usr/bin/bashbug

%files info
%defattr(0644,root,root,0755)
/usr/share/info/bash.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bash/771f6b3c33dd1c00e5d2f319cb801d0611ddd699
/usr/share/package-licenses/bash/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bash.1
/usr/share/man/man1/bashbug.1

%files locales -f bash.lang
%defattr(-,root,root,-)

