%define ver 0.98
%define release %mkrel 4
%define oname pexpect
%define dname %{oname}-%{ver}

Name: python-%oname
Version: %{ver}
Release: %{release}
Source0: %{dname}.tar.bz2
Source1: %{oname}-doc.tar.bz2
Source2: %{oname}-examples.tar.bz2
Summary: An efficient, pure-python replacement for Expect
License: Python Software Foundation License
Group: Development/Python
Url: http://pexpect.sourceforge.net/
BuildRequires: python >= %{pyver}
BuildRequires: libpython-devel >= %{pyver}
BuildArch: noarch

%description
This is a pure-python replacement for Expect, a module that
allows easy control of other applications (including interactive
applications that would drive popen crazy). It's not 100%
compatible with the real thing, but its at least 90% compatible,
and much easier to use.

%prep
%setup -q -n %{dname}
%setup -q -T -D -a 1 -n %{dname}
%setup -q -T -D -a 2 -n %{dname}
rm -rf doc/CVS
rm -rf examples/CVS

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt PKG-INFO doc examples
%{python_sitelib}/%{oname}.py*
%{python_sitelib}/*.egg-info



