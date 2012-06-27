Name:		augustus
Version:	2.5.5
Release:	1%{?dist}
Summary:	AUGUSTUS: gene prediction program for eukaryotes

Group:		Applications/Engineering
License:	Artistic License 2.0
URL:		http://augustus.gobics.de/
Source0:	http://augustus.gobics.de/binaries/%{name}.%{version}.tar.gz
Patch0:		%{name}-src-makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
AUGUSTUS is a gene prediction program for eukaryotes written by Mario Stanke
and Oliver Keller. It can be used as an ab initio program, which means it bases
its prediction purely on the sequence. AUGUSTUS may also incorporate hints on
the gene structure coming from extrinsic sources such as EST, MS/MS, protein
alignments and synthenic genomic alignments.


%package          config
Summary:          AUGUSTUS config and data files
Group:            Applications/Engineering
Requires:         %{name} = %{version}
BuildArch:	  noarch


%description config

Config and data files needed for AUGUSTUS gene prediction program.
Set the environment variable AUGUSTUS_CONFIG_PATH to
%{_datadir}/%{name}-%{version}/config before running AUGUSTUS.


%package          tutorial
Summary:          AUGUSTUS tutorial files
Group:            Applications/Engineering
Requires:         %{name} = %{version}
Requires:         %{name}-config = %{version}
BuildArch:	  noarch


%description tutorial

Tutorial for the AUGUSTUS gene prediction program.


%prep
%setup -q -n %{name}.%{version}
# Patch to remove -static flag from src/Makefile
%patch0 -p1

%build
cd src
make


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 bin/* %{buildroot}%{_bindir}

# Configuration files
mkdir -p %{buildroot}%{_datadir}/%{name}-%{version}
cp -a config %{buildroot}%{_datadir}/%{name}-%{version}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.TXT HISTORY.TXT retraining.html
%{_bindir}/*


%files config
%defattr(-,root,root,-)
%{_datadir}/%{name}-%{version}/config


%files tutorial
%defattr(-,root,root,-)
%doc docs/tutorial

%changelog
* Wed Jun 27 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.2.0-1
- initial version



