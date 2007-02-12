%bcond_with	debug	# enable debugging

Summary:	ksvn - SVN client for KDE
Summary(de.UTF-8):   ksvn - ein SVN Klient für KDE
Summary(pl.UTF-8):   ksvn - Klient SVN dla KDE
Name:		ksvn
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	dc005d97ba8d3b1637d5a39ff5f7d075
Patch0:		%{name}-includes.patch
Patch1:		%{name}-desktop.patch
URL:		http://apps.intra-links.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.5.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	subversion-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A new client for KDE that looks like tortoiseSVN. It can be used from
Konqueror context menu. It replace the standard KDE SubVersion menu.

%description -l de.UTF-8
Ein neuer SVN Klient für KDE der wie tortoiseSVN aussieht. Es kann
durch das Konqueror Kontextmenu benutzt werden.

%description -l pl.UTF-8
Nowy klient SVN dla KDE, który wygląda jak tortoiseSVN. Może być
używany z menu kontekstowego Konquerora. Zastępuje standardowe menu
KDE SubVersion.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f Makefile.cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	shelldesktopdir=%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_datadir}/apps/konqueror/servicemenus/subversion.desktop
%{_datadir}/apps/konqueror/servicemenus/subversion_toplevel.desktop
%{_desktopdir}/kde/ksvn.desktop
%{_iconsdir}/*/*/apps/%{name}.png
