%define modulename xlwt
%define version 0.7.2
%define unmangled_version 0.7.2
%define release 1

Summary: Library to create spreadsheet files compatible with MS Excel 97/2000/XP/2003 XLS files, on any platform, with Python 2.3 to 2.6
Name: python-%{modulename}
Version: %{version}
Release: %{release}
Source0: %{modulename}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: John Machin <sjmachin@lexicon.net>
Url: https://secure.simplistix.co.uk/svn/xlwt/trunk

BuildRequires: python
BuildRequires: python-setuptools

%description
xlwt is a library for generating spreadsheet files that are compatible
with Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement is
Python 2.3 to 2.6. xlwt is a fork of pyExcelerator.


%prep
%setup -n %{modulename}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog

* Fri Jun 29 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.1.1-1
- initial version modified from output of bdist_rpm --no-spec
