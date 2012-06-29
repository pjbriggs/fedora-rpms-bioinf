%define modulename errorhandler
%define version 1.1.1
%define unmangled_version 1.1.1
%define unmangled_version 1.1.1
%define release 1

Summary: A logging framework handler that tracks when messages above a certain level have been logged.
Name: python-%{modulename}
Version: %{version}
Release: %{release}
Source0: %{modulename}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Chris Withers <chris@simplistix.co.uk>
Url: http://www.simplistix.co.uk/software/python/errorhandler

BuildRequires: python
BuildRequires: python-setuptools

%description
============
ErrorHandler
============

This is a handler for the python standard logging framework that can
be used to tell whether messages have been logged at or above a
certain level.

This can be useful when wanting to ensure that no errors have been
logged before committing data back to a database.

As an example, first, you set up the error handler:

>>> from errorhandler import ErrorHandler
>>> e = ErrorHandler()

Then you can log and check the handler at any point to see if it has
been triggered:

>>> e.fired
False
>>> from logging import getLogger
>>> logger = getLogger()
>>> logger.error('an error')
>>> e.fired
True

You can use the `fired` attribute to only perform actions when no
errors have been logged:

>>> if e.fired:
...   print "Not updating files as errors have occurred"
Not updating files as errors have occurred


%prep
%setup -n %{modulename}-%{unmangled_version} -n %{modulename}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog

* Fri Jun 29 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.1.1-1
- initial version modified from output of bdist_rpm --no-spec
