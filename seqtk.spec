Name:		seqtk
Version:	20121121
Release:	1%{?dist}
Summary:	Fast and lightweight tool for processing sequences the FASTA or FASTQ format

Group:		Applications/Productivity
License:	Open source
URL:		https://github.com/lh3/seqtk
Source0:	https://github.com/lh3/seqtk/archive/seqtk-master.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
	
BuildRequires:	gcc glibc-devel

%description
Seqtk is a fast and lightweight tool for processing sequences in the FASTA or FASTQ
format. It seamlessly parses both FASTA and FASTQ files which can also be optionally
compressed by gzip.

This package provides 'seqtk-new' as a more up-to-date version of 'seqtk' provided
by the samtools package.


%prep
%setup -q -n seqtk-master


%build
make


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
# Install as "seqtk-new"
install -m 0755 %{_builddir}/seqtk-master/seqtk %{buildroot}%{_bindir}/seqtk-new


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/seqtk-new


%changelog
* Wed Nov 21 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 20121121-1
- initial version

