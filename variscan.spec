Name:		variscan
Version:	2.0.2
Release:	1%{?dist}
Summary:	Analysis of DNA sequence polymorphisms at the whole genome scale

Group:		Applications/Engineering
License:	GPLv2
URL:		http://www.ub.edu/softevol/variscan/
Source0:	http://www.ub.es/softevol/variscan/%{name}-%{version}.tar.gz

BuildRequires:	automake
##Requires:	

%description
variscan implements some of the basic algorithms of nucleotide
variability for intra- and/or interspecific polymorphism data. It
was designed to work together with the 'LastWave' package, but can
also be used as stand-alone software.


%prep
%setup -q


%build
# Variscan
sh autogen.sh
make

%install
rm -rf %{buildroot}

# Install variscan executable
mkdir -p %{buildroot}%{_bindir}
install -m 0755 src/variscan %{buildroot}%{_bindir}

# Install GUI
mkdir -p %{buildroot}/%{_datadir}/%{name}-%{version}/GUI
install -m 0644 GUI/VariScanGUI.jar %{buildroot}/%{_datadir}/%{name}-%{version}/GUI

# Scripts
mkdir -p %{buildroot}/%{_datadir}/%{name}-%{version}/scripts
install -m 0644 scripts/* %{buildroot}/%{_datadir}/%{name}-%{version}/scripts

# Install data/examples
mkdir -p %{buildroot}/%{_datadir}/%{name}-%{version}/data
install -m 0644 data/* %{buildroot}/%{_datadir}/%{name}-%{version}/data


%files
%doc README COPYING ChangeLog AUTHORS NEWS doc/VariScan_v2_Documentation.pdf
%{_bindir}/*
%{_datadir}/%{name}-%{version}/GUI/*
%{_datadir}/%{name}-%{version}/data/*
%{_datadir}/%{name}-%{version}/scripts/*


%changelog
* Fri Mar 30 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.0.2-1
- initial version

