$Revision: 1.2 $
Summary:	Arachne - web browser
Summary(es):	Navegador de Internet Arachne
Summary(pl):	Arachne - przegl±darka WWW
Summary(pt_BR):	Navegador Arachne
Name:		arachne
Version:	1.66b
Release:	1
License:	distributable
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://storage.prog.cz/xchaos/arachne-1.66b.tar.gz
URL:		http://browser.arachne.cz
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveOS:    Linux
ExclusiveArch:	%{ix86}


%description
Small and fast web browser.

%description -l pl
Szybka, ma³a, nie¼le siê prezentuj±ca przegl±darka www.

%package common
Summary:	Configuration files for Arachne
Summary(pl):	Pliki konfiguracyjne u¿ywane przez Arachne
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Requires:	glibc >= 2.1

%description common
Files shared between svgalib and ggi versions of Arachne.

%description common -l pl
Pliki konfiguracyjne u¿ywane przez obie wersje Arachne.

%package svga
Summary:	Arachne web browser for svgalib
Summary(pl):	Wersja przegl±darki Arachne korzystaj±ca z svgalib
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Requires:	arachne-common

%description svga
Arachne is web browser. This is beta release for svgalib.
Arachne uses external programs to convert JPEGs (djpeg) and PNGs(convert)
to BMPs, because BMP are faster to display. Few interesting ideas are
introduced by Arachne.

Information on the license may be found in the
file %{_docdir}/%{name}-common-%{version}/LICENSE.

%descripion svga -l pl
To jest wersja beta przegl±darki www - Arachne, która korzysta z biblioteki
svgalib. Arachne jest szybka i ma³a, niestety nie obs³uguje jeszcze
protoko³u https ani JavaScriptu, ani CSS.

Informacje na temat licencji mo¿na znale¼æ w pliku
%{_docdir}/%{name}-common-%{version}/LICENSE.

%package ggi
Summary:	Arachne web browser for ggi
Summary(pl):	Wersja przegl±darki Arachne korzystaj±ca z biblioteki ggi
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Requires:	arachne-common

%description ggi
Arachne is web browser. This is beta release for ggi.
Arachne uses external programs to convert JPEGs (djpeg) and PNGs(convert)
to BMPs, because BMP are faster to display. Few interesting ideas are
introduced by Arachne.

Information on the license may be found in the
file %{_docdir}/%{name}-common-%{version}/LICENSE.

%descripion ggi -l pl
To jest wersja beta przegl±darki www - Arachne, która korzysta z biblioteki
ggi. Arachne jest szybka i ma³a, niestety nie obs³uguje jeszcze
protoko³u https ani JavaScriptu, ani CSS.

Informacje na temat licencji mo¿na znale¼æ w pliku
%{_docdir}/%{name}-common-%{version}/LICENSE.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,\
%{_datadir}/arachne/{templates,iso-8859-1/codepage,iso-8859-2/codepage,\
gui,ikons},/usr/doc}

install bin/* $RPM_BUILD_ROOT%{_bindir}
install share/arachne/arachne-install $RPM_BUILD_ROOT%{_bindir}
install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
cp -r share/arachne/* $RPM_BUILD_ROOT%{_datadir}/arachne

ln -sf %{_docdir}/arachne-%{version} $RPM_BUILD_ROOT/usr/doc/arachne


cat > $RPM_BUILD_ROOT%{_bindir}/arachne << EOF
#!/bin/sh
if [ "\$TERM" = "linux" ]
then
/usr/bin/arachne-svgalib $@
else
/usr/bin/arachne-ggi $@
fi
EOF

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arachne
%{_mandir}/man1/*
/usr/doc/arachne
%doc doc/arachne/*
%dir %{_datadir}/arachne
%{_datadir}/arachne/*

%files ggi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arachne-ggi

%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arachne-svgalib

%clean
rm -rf $RPM_BUILD_ROOT
