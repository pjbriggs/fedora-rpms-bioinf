Name:		HTSeq
Version:	0.5.3p3
Release:	1%{?dist}
Summary:	Framework to process and analyze data from HTS assays

Group:		Applications/Engineering
License:	GPLv3
URL:		http://www-huber.embl.de/users/anders/HTSeq/doc/index.html
Source0:	http://pypi.python.org/packages/source/H/HTSeq/HTSeq-0.5.3p3.tar.gz

BuildRequires:	python-devel numpy python-sphinx
Requires:	python numpy python-matplotlib

%description

HTSeq is a Python package that provides infrastructure to process data
from high-throughput sequencing assays. While the main purpose of
HTSeq is to allow you to write your own analysis scripts, customized
to your needs, there are also a couple of stand-alone scripts for
common tasks that can be used without any Python knowledge.

%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Documentation
# NB can't mix the %doc directive with manually populating the doc area
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}/_images
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}/_static
install -m 0644 README %{buildroot}/%{_docdir}/%{name}-%{version}
# Build and install HTML docs (needs sphinx)
cd doc
make html
install -m 0644 _build/html/*.html %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 _build/html/_images/* %{buildroot}/%{_docdir}/%{name}-%{version}/_images
install -m 0644 _build/html/_static/* %{buildroot}/%{_docdir}/%{name}-%{version}/_static

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}/*
%{python_sitearch}/%{name}*
%{_bindir}/htseq-count
%{_bindir}/htseq-qa

%changelog
* Fri Feb  3 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 0.5.3p3-1
- initial version

