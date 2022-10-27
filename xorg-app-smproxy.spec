Summary:	smproxy application - Session Manager proxy
Summary(pl.UTF-8):	Aplikacja smproxy - proxy zarządcy sesji (SM)
Name:		xorg-app-smproxy
Version:	1.0.7
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/smproxy-%{version}.tar.xz
# Source0-md5:	9f7a4305f0e79d5a46c3c7d02df9437d
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
smproxy allows X applications that do not support X11R6 session
management to participate in an X11R6 session.

%description -l pl.UTF-8
smproxy pozwala uczestniczyć w sesji X11R6 aplikacjom X nie
obsługującym zarządzania sesjami X11R6.

%prep
%setup -q -n smproxy-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/smproxy
%{_mandir}/man1/smproxy.1*
