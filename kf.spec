Summary:	Simple Jabber client
Summary(pl):	Prosty klient Jabbera
Name:		kf
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.habazie.rams.pl/%{name}/files/%{name}-%{version}.tar.gz
# Source0-md5:	61091daffbd03ef4eb3155df3abed0ca
Source1:	%{name}.desktop
URL:		http://www.habazie.rams.pl/kf/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	gtkspell-devel >= 2.0.5
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	loudmouth-devel >= 0.16
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Komunikator Fisha is a simple Jabber client using GTK+2 Toolkit.

%description -l pl
Komunikator Fisha jest prostym klientem Jabbera u¿ywaj±cym biblioteki
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

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install data/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT/%{_bindir}/%{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}isha

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
