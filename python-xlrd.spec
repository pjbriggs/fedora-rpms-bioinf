%define modulename xlrd
%define version 0.7.1
%define unmangled_version 0.7.1
%define release 1

Summary: Library for developers to extract data from Microsoft Excel (tm) spreadsheet files
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
Url: http://www.lexicon.net/sjmachin/xlrd.htm

BuildRequires: python
BuildRequires: python-setuptools

%description
Extract data from new and old Excel spreadsheets on any platform. Pure Python (2.1 to 2.6). Strong support for Excel dates. Unicode-aware.

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
