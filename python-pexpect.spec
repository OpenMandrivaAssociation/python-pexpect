%define module  pexpect
%define name    python-%{module}
%define version 2.4
%define release %mkrel 5

Summary:       An efficient, pure Python replacement for Expect
Name: 	       %{name}
Version:       %{version}
Release:       %{release}
Source0:       %{module}-%{version}.tar.gz
License:       MIT
Group:         Development/Python
Url:           http://pexpect.sourceforge.net/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:     noarch
BuildRequires: python
BuildRequires: python-devel

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

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= \
%__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc README LICENSE doc/ examples/


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4-4mdv2011.0
+ Revision: 668021
- mass rebuild

* Thu Nov 04 2010 Paulo Andrade <pcpa@mandriva.com.br> 2.4-3mdv2011.0
+ Revision: 593484
+ rebuild (emptylog)

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4-2mdv2010.1
+ Revision: 523853
- rebuilt for 2010.1

* Sun Mar 29 2009 Lev Givon <lev@mandriva.org> 2.4-1mdv2010.0
+ Revision: 362207
- Update to 2.4.

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 2.3-6mdv2009.1
+ Revision: 323925
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.3-5mdv2009.0
+ Revision: 269037
- rebuild early 2009.0 package (before pixel changes)

* Wed May 14 2008 Lev Givon <lev@mandriva.org> 2.3-4mdv2009.0
+ Revision: 206873
- Update to 2.3.

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.98-4mdv2008.1
+ Revision: 136454
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.98-4mdv2007.0
+ Revision: 90623
- Rebuild against new python
- import python-pexpect-0.98-3mdk

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.98-3mdk
- Rebuild for new python

