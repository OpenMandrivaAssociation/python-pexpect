%define module  pexpect

Summary:       An efficient, pure Python replacement for Expect
Name: 	       python-%{module}
Version:       2.5.1
Release:       1
Source0:       http://pypi.python.org/packages/source/p/pexpect-u/pexpect-u-%{version}.tar.gz
Source100:     %name.rpmlintrc
License:       MIT
Group:         Development/Python
Url:           http://pexpect.sourceforge.net/
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

%package -n python3-pexpect
Summary:        Unicode-aware Pure Python Expect-like module for Python 3
Group:          Development/Python
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-distribute

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


