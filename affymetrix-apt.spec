Name:		affymetrix-apt
Version:	1.14.3
Release:	1%{?dist}
Summary:	Tools for analyzing and working with Affymetrix GeneChip arrays

Group:		Applications/Productivity
License:	GNU Lesser General Public License version 2.1
URL:		http://www.affymetrix.com/partners_programs/programs/developer/tools/powertools.affx
Source0:	http://www.affymetrix.com/estore/partners_programs/programs/developer/apt_download/apt_thank_you.affx?onloadforward=http://media.affymetrix.com//Download/updates/apt-1.14.3-src.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
	

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
%setup -q -n apt-1.14.3-src


%build
cd sdk
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
# Doesn't have a make install of its own so fudge it here
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp sdk/output/amd64-pc-linux/bin/apt-* $RPM_BUILD_ROOT/usr/bin
rm $RPM_BUILD_ROOT/usr/bin/apt-rt-*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*


%changelog
