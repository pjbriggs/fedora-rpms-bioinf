Name:		SOAPsnp
Version:	1.03
Release:	1%{?dist}
Summary:	Consensus sequence builder to calculate quality scores for SNP calling 

Group:		Applications/Engineering
License:	GPLv3
URL:		http://soap.genomics.org.cn/soapsnp.html
Source0:	http://soap.genomics.org.cn/down/SOAPsnp-v1.03.tar.gz

BuildRequires:	boost-devel zlib-devel
Requires:	zlib

%description
SOAPsnp is a member of the SOAP (Short Oligonucleotide Analysis Package).

The program is a resequencing utility that can assemble consensus
sequence for the genome of a newly sequenced individual based on the
alignment of the raw sequencing reads on the known reference. The SNPs
can then be identified on the consensus sequence through comparison with
the reference.

%prep
%setup -q -n %{name}Z


%build
make all


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 soapsnp %{buildroot}%{_bindir}


%files
%doc readme COPYING release
%{_bindir}/soapsnp


%changelog
* Thu Mar 29 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.03-1
- initial version

