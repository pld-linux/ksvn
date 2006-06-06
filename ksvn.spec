%bcond_with	debug	# enable debugging

Summary:	ksvn - SVN client for KDE
Summary(de):	ksvn - ein SVN Klient für KDE
Summary(pl):	ksvn - Klient SVN dla KDE
Name:		ksvn
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	dc005d97ba8d3b1637d5a39ff5f7d075
Patch0:		%{name}-includes.patch
URL:		http://apps.intra-links.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.5.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	subversion-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A new client for KDE that looks like tortoiseSVN. It can be used from
konqueror context menu. It replace the standard KDE SubVersion menu.

%description -l de
Ein neuer SVN Klient für KDE der wie tortoiseSVN aussieht. Es kann
durch das Konqueror Kontextmenu benutzt werden.

%description -l pl
Nowy klient SVN dla KDE, który wygl±da jak tortoiseSVN. Mo¿e byæ
u¿ywany z menu kontekstowego konquerora. Zastêpuje standardowe menu
KDE SubVersion.

%prep
%setup -q
%patch0 -p0

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
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/apps/%{name}
%{_datadir}/applnk/Utilities/ksvn.desktop
%{_datadir}/apps/konqueror/servicemenus/subversion.desktop
%{_datadir}/apps/konqueror/servicemenus/subversion_toplevel.desktop
