Name:		matrix2png
Version:	1.2.2
Release:	1%{?dist}
Summary:	matrix2png: visualizations of microarray and other data

Group:		Applications/Productivity
License:	Apache
URL:		http://www.chibi.ubc.ca/matrix2png/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
	
BuildRequires:	gd-devel
Requires:	gd


%description
Matrix2png is a simple but powerful program for making visualizations of microarray
data and many other data types. It generates PNG formatted images from text files of
data. It is fast, easy to use, and reasonably flexible. It can be used to generate
publication-quality images, or to act as a image generator for web applications.


%prep
%setup -q


%build
./configure --prefix=%{_prefix}
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS README NEWS COPYING ChangeLog
%{_bindir}/%{name}


%changelog
* Thu Jun 21 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.2.2-1
- initial version


