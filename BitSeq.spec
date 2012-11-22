Name:		BitSeq
Version:	0.4.3
Release:	1%{?dist}
Summary:	BitSeq: Bayesian Inference of Transcripts from Sequencing Data

Group:		Applications/Productivity
License:	Artistic Licence 2.0/Boost_1_0/MIT
URL:		http://code.google.com/p/bitseq/
Source0:	http://bitseq.googlecode.com/files/BitSeq-0.4.3.tar.gz
Patch0:		BitSeq-Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
	
BuildRequires:	gcc gcc-c++ glibc-devel zlib-devel
Requires:	glibc zlib


%description
BitSeq (Bayesian Inference of Transcripts from Sequencing Data) is an application
for inferring expression levels of individual transcripts from sequencing (RNA-Seq)
data and estimating differential expression (DE) between conditions. An advantage
of this approach is the ability to account for both technical uncertainty and
intrinsic biological variance in order to avoid false DE calls. The technical
contribution to the uncertainty comes both from finite read-depth and the possibly
ambiguous mapping of reads to multiple transcripts.


%prep
%setup -q
%patch0 -p1

%build
make


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
# Executables
install -m 0755 %{_builddir}/%{name}-%{version}/extractSamples %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/getGeneExpression %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/getWithinGeneExpression %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/estimateExpression %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/transposeLargeFile %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/estimateDE %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/getVariance %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/estimateHyperPar %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/getPPLR %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/convertSamples %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/parseAlignment %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/getFoldChange %{buildroot}%{_bindir}
# Python scripts
install -m 0755 %{_builddir}/%{name}-%{version}/parseAlignment.py %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/getCounts.py %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/extractTranscriptInfo.py %{buildroot}%{_bindir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/*


%changelog
* Thu Nov 22 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 0.4.3-1
- initial version

