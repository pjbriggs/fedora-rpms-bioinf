%global ceas_name CEAS

# For EPEL 5 make a python26 package
# See http://mirror.choon.net/choonrpms.choon.net/sl/6/choonrpms/SPECS/Cython-0.14.1-3.el6.spec for hints
%if 0%{?el5}
%global __python %{_bindir}/python26
%global python_sitelib /usr/lib/python2.6/site-packages
%endif

%if 0%{?el5}
Name:		python26-CEAS
%else
Name:		CEAS
%endif
Version:	1.0.2
Release:	2%{?dist}
Summary:	CEAS: Cis-regulatory Element Annotation System

Group:		Applications/Engineering
License:	Artistic
URL:		http://liulab.dfci.harvard.edu/CEAS/index.html
Source0:	http://liulab.dfci.harvard.edu/CEAS/src/CEAS-Package-1.0.2.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?el5}
BuildRequires:	python26 python26-devel
%else
BuildRequires:	python python-devel
%endif
BuildArch:	noarch

%description
A tool designed to characterize genome-wide protein-DNA interaction patterns
from ChIP-chip and ChIP-Seq of both sharp and broad binding factors. As a
stand-alone extension of our web application CEAS (Cis-regulatory Element
Annotation System), it provides statistics on ChIP enrichment at important
genome features such as specific chromosome, promoters, gene bodies, or exons,
and infers genes most likely to be regulated by a binding factor. CEAS also
enables biologists to visualize the average ChIP enrichment signals over
specific genomic features, allowing continuous and broad ChIP enrichment to
be perceived which might be too subtle to detect from ChIP peaks alone.

%prep
%setup -q -n CEAS-Package-%{version}

%build

%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

# Do our own byte compilation for EL5
%if 0%{?el5}
%{__python}    -c 'import compileall; compileall.compile_dir("'"$RPM_BUILD_ROOT%{python_sitelib}"'", 10, "%{python_sitelib}", 1)' > /dev/null
%{__python} -O -c 'import compileall; compileall.compile_dir("'"$RPM_BUILD_ROOT%{python_sitelib}"'", 10, "%{python_sitelib}", 1)' > /dev/null
%endif

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc ChangeLog
%{python_sitelib}/%{ceas_name}*
#%{python_sitelib}/%{ceas_name}_Package-%{version}-py*.egg*
%{_bindir}/ceas
%{_bindir}/build_genomeBG
%{_bindir}/gca
%{_bindir}/sitepro


%changelog
* Fri Nov 18 2011 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.0.2-2
- updated to build 'python26-CEAS' package using python 2.6 on EL5 systems

* Fri Nov 11 2011 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.0.2-1
- initial version
