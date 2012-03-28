#%define debug_package %{nil}

Name:		gimmemotifs
Version:	0.65
Release:	1%{?dist}
Summary:	De novo motif prediction pipeline suited for ChIP-seq datasets

Group:		Applications/Engineering
License:	MIT
URL:		http://131.174.221.43/bioinfo/gimmemotifs/index.htm
Source0:	%{name}-%{version}.tar.gz
Patch0:		gimmemotifs-tools.patch

# Disable automatic dependency checking to avoid issues with missing
# /bin/perl and Alogorithm::Cluster
AutoReqProv:	no

%if 0%{?el6}
BuildRequires:	python, scipy >= 0.7.2, pp >= 1.6.0, python-matplotlib >= 0.98, gsl-devel >= 1.13, python-kid, weeder
Requires:	python, scipy >= 0.7.2, pp >= 1.6.0, python-matplotlib >= 0.98, python-kid, weeder
%else
BuildRequires:	python, scipy >= 0.7.2, python-pp >= 1.6.0, python-matplotlib >= 0.98, gsl-devel >= 1.13, python-kid, weeder
Requires:	python, scipy >= 0.7.2, python-pp >= 1.6.0, python-matplotlib >= 0.98, python-kid, weeder
%endif

%description

GimmeMotifs is a de novo motif prediction pipeline, especially suited for ChIP-seq
datasets. It incorporates several existing motif prediction algorithms in an ensemble
method to predict motifs and clusters these motifs using the WIC similarity scoring
metric.


%prep
%setup -q

# Patch to remove check on weeder FreqFiles
%patch0 -p1

%build
%{__python} setup.py build


%install
rm -rf %{buildroot}

%{__python} setup.py install --skip-build --root %{buildroot}

# Deal with the configuration file
sed -i 's/\/local\/bin/\/share\/gimmemotifs\/tools/g' %{buildroot}/usr/share/gimmemotifs/gimmemotifs.cfg
sed -i 's/\/share\/Weeder/\/bin/g' %{buildroot}/usr/share/gimmemotifs/gimmemotifs.cfg

# Documentation etc
# NB can't mix the %doc directive with manually populating the doc area
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 README %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 COPYING %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 ChangeLog %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 doc/%{name}_manual.pdf %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 doc/%{name}_manual.html %{buildroot}/%{_docdir}/%{name}-%{version}

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}/*
%{python_sitearch}/%{name}*
%{_bindir}/*
%{_datadir}/%{name}



%changelog
* Tue Mar 27 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 0.65-1
- initial version

