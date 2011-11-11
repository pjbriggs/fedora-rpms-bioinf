Name:		CEAS
Version:	1.0.2
Release:	1%{?dist}
Summary:	CEAS: Cis-regulatory Element Annotation System

Group:		Applications/Engineering
License:	Artistic
URL:		http://liulab.dfci.harvard.edu/CEAS/index.html
Source0:	http://liulab.dfci.harvard.edu/CEAS/src/CEAS-Package-1.0.2.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	python-devel
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

%clean
rm -rf ${buildroot}


%files
%defattr(-,root,root,-)
%doc ChangeLog
%{python_sitelib}/%{name}*
%{python_sitelib}/%{name}_Package-%{version}-py*.egg*
%{_bindir}/ceas
%{_bindir}/build_genomeBG
%{_bindir}/gca
%{_bindir}/sitepro


%changelog
* Fri Nov 11 2011 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.0.2
- initial version
