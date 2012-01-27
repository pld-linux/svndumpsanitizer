Summary:	svndump sanitizer
Name:		svndumpsanitizer
Version:	0.8.3
Release:	1
License:	GPL v3+
Group:		Development/Version Control
Source0:	http://miria.linuxmaniac.net/svndumpsanitizer/%{name}-%{version}.tar.bz2
# Source0-md5:	d5b241f35049fb8a6362022131fca83a
URL:		http://miria.linuxmaniac.net/svndumpsanitizer/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
svndumpfilter that can handle paths outside included set.

%prep
%setup -q

%build
%{__cc} -o %{name} %{rpmcflags} %{rpmcppflags} %{rpmldflags} %{name}.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/svndumpsanitizer
