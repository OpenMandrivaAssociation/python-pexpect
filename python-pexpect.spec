%define module  pexpect

Summary:	An efficient, pure Python replacement for Expect
Name:		python-%{module}
Version:	2.5.1
Release:	2
License:	MIT
Group:		Development/Python
Url:		http://pexpect.sourceforge.net/
Source0:	http://pypi.python.org/packages/source/p/pexpect-u/pexpect-u-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
BuildArch:	noarch
BuildRequires:	pkgconfig(python)

%description
Pexpect is a pure Python module for spawning child applications,
controlling them, and responding to expected patterns in their
output. Pexpect works like Don Libes' Expect. Pexpect allows your
script to spawn a child application and control it as if a human were
typing commands.

Pexpect can be used for automating interactive applications such as
ssh, ftp, passwd, telnet, etc. It can be used to a automate setup
scripts for duplicating software package installations on different
servers. It can be used for automated software testing. Pexpect is in
the spirit of Don Libes' Expect, but Pexpect is pure Python. Unlike
other Expect-like modules for Python, Pexpect does not require TCL or
Expect, nor does it require C extensions to be compiled. It should work
on any platform that supports the standard Python pty module. The
Pexpect interface was designed to be easy to use.

%package -n python3-pexpect
Summary:	Unicode-aware Pure Python Expect-like module for Python 3
Group:		Development/Python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-distribute

%description -n python3-pexpect
Pexpect is a pure Python module for spawning child applications,
controlling them, and responding to expected patterns in their
output. Pexpect works like Don Libes' Expect. Pexpect allows your
script to spawn a child application and control it as if a human were
typing commands.

Pexpect can be used for automating interactive applications such as
ssh, ftp, passwd, telnet, etc. It can be used to a automate setup
scripts for duplicating software package installations on different
servers. It can be used for automated software testing. Pexpect is in
the spirit of Don Libes' Expect, but Pexpect is pure Python. Unlike
other Expect-like modules for Python, Pexpect does not require TCL or
Expect, nor does it require C extensions to be compiled. It should work
on any platform that supports the standard Python pty module. The
Pexpect interface was designed to be easy to use.

%prep
%setup -q -c
mv pexpect-u-%{version} python2
cp -r python2 python3
find python3 -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
pushd python2
%__python setup.py build
popd

pushd python3
python3 setup.py build
popd

%install
pushd python2
PYTHONDONTWRITEBYTECODE=  %__python setup.py install --skip-build --root=%{buildroot} --install-lib %{python_sitelib}
popd

pushd python3
PYTHONDONTWRITEBYTECODE=  python3 setup.py install --skip-build --root=%{buildroot} --install-lib %{python3_sitelib}
popd

%files
%doc python2/README python2/doc python2/examples python2/LICENSE
%{py_puresitedir}/*

%files -n python3-pexpect
%doc python3/README python3/doc python3/examples python3/LICENSE
%{py3_puresitedir}/*

