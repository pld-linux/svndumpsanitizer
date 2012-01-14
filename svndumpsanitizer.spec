Summary:	svndump sanitizer
Name:		svndumpsanitizer
Version:	0.8.2
Release:	1
License:	GPL v3+
Group:		Development/Version Control
Source0:	http://miria.linuxmaniac.net/svndumpsanitizer/%{name}-%{version}.tar.bz2
# Source0-md5:	d1076e79645e1f8e63d4ffded8e2b96b
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
