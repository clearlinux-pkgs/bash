#
# NOT autospec due to weird patch formats
#
Name     : bash
Version  : 4.4
Release  : 41
URL      : http://mirrors.kernel.org/gnu/bash/bash-4.4.tar.gz
Source0  : http://mirrors.kernel.org/gnu/bash/bash-4.4.tar.gz
Summary  : Bash headers for bash loadable builtins
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0 GPL-3.0+
Requires: bash-bin
Requires: bash-doc
Requires: bash-locales
BuildRequires : bison
BuildRequires : ncurses-dev
Patch1: nodlopen.patch
Patch2: stateless.patch
Patch3: 0001-Support-stateless-inputrc-configuration.patch
Patch4: tinfow.patch
Patch1001: bash44-001
Patch1002: bash44-002
Patch1003: bash44-003
Patch1004: bash44-004
Patch1005: bash44-005
Patch1006: bash44-006
Patch1007: bash44-007
Patch1008: bash44-008
Patch1009: bash44-009
Patch1010: bash44-010
Patch1011: bash44-011
Patch1012: bash44-012
Patch2001: cve-2017-5932.nopatch
 
%description
Introduction
============
This is GNU Bash, version 4.4.  Bash is the GNU Project's Bourne
Again SHell, a complete implementation of the POSIX shell spec,
but also with interactive command line editing, job control on
architectures that support it, csh-like features such as history
substitution and brace expansion, and a slew of other features.
For more information on the features of Bash that are new to this
type of shell, see the file `doc/bashref.texi'.  There is also a
large Unix-style man page.  The man page is the definitive description
of the shell's features.

%package bin
Summary: bin components for the bash package.
Group: Binaries

%description bin
bin components for the bash package.


%package doc
Summary: doc components for the bash package.
Group: Documentation

%description doc
doc components for the bash package.


%package extras
Summary: extras components for the bash package.
Group: Default

%description extras
extras components for the bash package.


%package locales
Summary: locales components for the bash package.
Group: Default

%description locales
locales components for the bash package.


%prep
%setup -q -n bash-4.4
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch1001 -p0
%patch1002 -p0
%patch1003 -p0
%patch1004 -p0
%patch1005 -p0
%patch1006 -p0
%patch1007 -p0
%patch1008 -p0
%patch1009 -p0
%patch1010 -p0
%patch1011 -p0
%patch1012 -p0

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
%configure --disable-static --enable-cond-command --enable-history --enable-job-control --enable-readline --enable-extended-glob --enable-progcomp --enable-arith-for-command --enable-directory-stack --with-bash-malloc=no
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make check

%install
rm -rf %{buildroot}
%make_install
%find_lang bash
## make_install_append content
ln -s bash %{buildroot}/usr/bin/sh
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/bashbug
/usr/bin/bash
/usr/bin/sh

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/bash/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files extras
%defattr(-,root,root,-)
/usr/bin/bashbug

%files locales -f bash.lang 
%defattr(-,root,root,-)

