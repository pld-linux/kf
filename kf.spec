#
# Conditional build:
%bcond_with	gtkspell	# enable gtkspell support
#
Summary:	Simple Jabber client
Summary(pl):	Prosty klient Jabbera
Name:		kf
Version:	0.5.4
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://files.jabberstudio.org/kf/%{name}-%{version}.tar.gz
# Source0-md5:	c11dbc1c5873b405f5df65e72f8fc879
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-muc_join_enhance.patch
URL:		http://kf.jabberstudio.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
%{?with_gtkspell:BuildRequires:	gtkspell-devel >= 2.0.5}
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	loudmouth-devel >= 0.16
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kf Jabber Client is a simple Jabber IM client using GTK+2 Toolkit.

%description -l pl
Kf Jabber Client jest prostym klientem Jabbera używającym biblioteki
GTK+2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export LDFLAGS="$LDFLAGS -export-dynamic -g"
glib-gettextize --copy --force
%{__libtoolize}
intltoolize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_gtkspell:--enable-gtkspell}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

install kf.desktop $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install data/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}
mv $RPM_BUILD_ROOT/%{_bindir}/%{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}isha

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/*.h

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
