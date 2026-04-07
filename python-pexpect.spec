%define module pexpect

Name:		python-pexpect
Summary:	An efficient, pure Python replacement for Expect
Version:	4.9.0
Release:	1
License:	ISC
Group:		Development/Python
URL:		https://github.com/pexpect/pexpect
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(ptyprocess)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%rename python3-pexpect

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

%prep -a
# Fix wrong-script-interpreter
find examples -type f -name "*.py" -exec sed -i "s|#!%{_bindir}/env python||" {} \;
find examples -type f -name "*.cgi" -exec sed -i "s|##!%{_bindir}/env python|##!%{__python3}|" {} \;
# Mark example *.py as non-executable
find examples -type f -name "*.py" -exec chmod 644 {} \;
# Remove shebang
sed -i '1 {/^#!/d}' pexpect/FSM.py

%files
%doc README.rst doc examples
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
