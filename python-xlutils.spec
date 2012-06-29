%define modulename xlutils
%define version 1.5.2
%define unmangled_version 1.5.2
%define unmangled_version 1.5.2
%define release 1

Summary: Utilities for working with Excel files that require both xlrd and xlwt
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
Url: http://www.simplistix.co.uk/software/python/xlutils

BuildRequires: python
BuildRequires: python-setuptools
Requires: python-xlwt >= 0.7.0
Requires: python-xlrd >= 0.6.1
Requires: python-errorhandler

%description
-------
xlutils
-------

This package provides a collection of utilities for working with Excel
files. Since these utilities may require either or both of the xlrd
and xlwt packages, they are collected together here, separate from either
package.

Currently available are:

**xlutils.copy**
  Tools for copying xlrd.Book objects to xlwt.Workbook objects.

**xlutils.display**
  Utility functions for displaying information about xlrd-related
  objects in a user-friendly and safe fashion.

**xlutils.filter**
  A mini framework for splitting and filtering Excel files into new
  Excel files.  

**xlutils.margins**
  Tools for finding how much of an Excel file contains useful data.

**xlutils.save**
  Tools for serializing xlrd.Book objects back to Excel files.

**xlutils.styles**
  Tools for working with formatting information expressed in styles.

Installation
------------

The easyiest way to install `xlutils` is::

  easy_install xlutils

Or, if you're using zc.buildout, just specify 'xlutils' as 
a required egg.

However, you can also install in the usual python fashion of unpacking
the source distribution and running::

  python setup.py install

If you do not install using easy_install or zc.buildout, you will 
also need to make sure the following python packages are available 
on your PYTHONPATH:

- **xlrd**
   
  You'll need version 0.6.1a1 or later. Latest versions can be found
  here:

  http://pypi.python.org/pypi/xlrd
    
- **xlwt**

  You'll need version 0.7.0 or later. Latest versions can be found
  here:

  http://pypi.python.org/pypi/xlwt

- **errorhandler**

  This can be found here:

  http://pypi.python.org/pypi/errorhandler

If you're installing with either easy_install or buildout, these
dependencies will automatically be installed for you.


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
