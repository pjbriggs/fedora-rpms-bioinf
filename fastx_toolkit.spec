Name:		fastx_toolkit
Version:	0.0.13.2
Release:	1%{?dist}
Summary:	FASTX-Toolkit: tools for short-read FASTA/FASTQ preprocessing

Group:		Applications/Productivity
License:	GNU Affero GPLv3
URL:		http://hannonlab.cshl.edu/fastx_toolkit/index.html
Source0:	http://hannonlab.cshl.edu/fastx_toolkit/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
	
BuildRequires:	libgtextutils
Requires:	libgtextutils

%description
The FASTX-Toolkit is a collection of command line tools for Short-Reads
FASTA/FASTQ files preprocessing.

Next-Generation sequencing machines usually produce FASTA or FASTQ files,
containing multiple short-reads sequences (possibly with quality information).
The main processing of such FASTA/FASTQ files is mapping (aka aligning) the
sequences to reference genomes or other databases using specialized programs.

However, it is sometimes more productive to preprocess the FASTA/FASTQ files
before mapping the sequences to the genome - manipulating the sequences to
produce better mapping results.

The FASTX-Toolkit tools perform some of these preprocessing tasks. 

%prep
%setup -q


%build
./configure --prefix=%{_prefix} GTEXTUTILS_CFLAGS="-I%{_includedir}/gtextutils" GTEXTUTILS_LIBS=-lgtextutils
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
# Remove unwanted m4 files
rm -rf %{buildroot}%{_datadir}
# Disable RPATH check for standard paths otherwise
# rpmbuild stops with an error
export QA_RPATHS=0x0001

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS README NEWS COPYING THANKS ChangeLog
%{_bindir}/*


%changelog
* Wed Jun 20 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 0.0.13.2-1
- initial version

