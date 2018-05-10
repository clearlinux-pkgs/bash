#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB5869F064EA74AB (chet@cwru.edu)
#
Name     : bash
Version  : 4.4.18
Release  : 45
URL      : http://mirrors.kernel.org/gnu/bash/bash-4.4.18.tar.gz
Source0  : http://mirrors.kernel.org/gnu/bash/bash-4.4.18.tar.gz
Source99 : http://mirrors.kernel.org/gnu/bash/bash-4.4.18.tar.gz.sig
Summary  : Bash headers for bash loadable builtins
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: bash-bin
Requires: bash-doc
Requires: bash-locales
BuildRequires : bison
BuildRequires : ncurses-dev
Patch1: nodlopen.patch
Patch2: stateless.patch
Patch3: 0001-Support-stateless-inputrc-configuration.patch
Patch4: cve-2017-5932.nopatch

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
%setup -q -n bash-4.4.18
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517364649
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
%configure --disable-static --enable-cond-command --enable-history --enable-job-control --enable-readline --enable-extended-glob --enable-progcomp --enable-arith-for-command --enable-directory-stack --with-bash-malloc=no
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check

%install
export SOURCE_DATE_EPOCH=1517364649
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

