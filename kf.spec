# TODO:
# - .desktop
#
Summary:	Simple Jabber client
Summary(pl):	Prosty klient Jabbera
Name:		kf
Version:	0.1.6
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.habazie.rams.pl/kf/files/%{name}-%{version}.tar.gz
# Source0-md5:	0eb97a162b226ae58255898571e1df51
URL:		http://www.habazie.rams.pl/kf/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	gtkspell-devel >= 2.0.5
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	loudmouth-devel >= 0.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Komunikator Fisha is a simple Jabber client using GTK+2 Toolkit.

%description -l pl
Komunikator Fisha jest prostym klientem Jabbera używającym biblioteki
GTK+2.

%prep
%setup -q

%build
glib-gettextize --copy --force
%{__libtoolize}
intltoolize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/kf
