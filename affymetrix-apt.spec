Name:		affymetrix-apt
Version:	1.14.3.1
Release:	1%{?dist}
Summary:	Tools for analyzing and working with Affymetrix GeneChip arrays

Group:		Applications/Productivity
License:	LGPLv2
URL:		http://www.affymetrix.com/partners_programs/programs/developer/tools/powertools.affx
Source0:	http://www.affymetrix.com/estore/partners_programs/programs/developer/apt_download/apt_thank_you.affx?onloadforward=http://media.affymetrix.com//Download/updates/apt-%{version}-src.zip
Patch0:		affymetrix-apt-configure-gcc.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
	
BuildRequires:	cppunit-devel

%description
Affymetrix Power Tools (APT) are a set of cross-platform command line programs
that implement algorithms for analyzing and working with Affymetrix GeneChip
arrays. APT is an open-source project licensed under the GNU General Public
License (GPL). (Developers who need a non-GPL license may purchase a commercial
license from Affymetrix.) APT programs are intended for "power users" who
prefer programs that can be utilized in scripting environments and are
sophisticated enough to handle the complexity of extra features and
functionality. The vision is that APT provides a platform for developing and
deploying new algorithms without waiting for the GUI implementations.

%prep
%setup -q -n apt-%{version}-src
# Patch sdk/configure to deal with gcc 4.6.x
%patch0 -p1

%build
cd sdk
./configure
make

%install
rm -rf %{buildroot}
# Doesn't have a make install of its own so fudge it here
mkdir -p %{buildroot}%{_bindir}
cp sdk/output/amd64-pc-linux/bin/apt-* %{buildroot}%{_bindir}
rm %{buildroot}%{_bindir}/apt-rt-*


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/*


%changelog
* Thu Jan 26 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.14.3.1-1
- updated to 1.14.3.1
- add patch for compiling with gcc 4.6.x

* Fri Oct 21 2011 Adam Huffman <adam.huffman@manchester.ac.uk> - 1.14.3-2
- use macros for %%buildroot and %%_bindir
- add BR for cppunit-devel
- fix license

* Fri Oct 14 2011 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.14.3-1
- initial version
